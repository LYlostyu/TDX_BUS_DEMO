export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST')
    return res.status(405).json({ error: 'Method not allowed' })
  }

  try {
    const { name, email, repoUrl, note } = req.body || {}

    if (!name || typeof name !== 'string') {
      return res.status(400).json({ error: 'name is required' })
    }
    if (!repoUrl || typeof repoUrl !== 'string') {
      return res.status(400).json({ error: 'repoUrl is required' })
    }
    if (!email || typeof email !== 'string') {
      return res.status(400).json({ error: 'email is required' })
    }

    if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
      return res.status(400).json({ error: 'Invalid email' })
    }
    if (name.length > 50) return res.status(400).json({ error: 'name too long' })
    if (repoUrl.length > 200) return res.status(400).json({ error: 'repoUrl too long' })

    let u
    try {
      u = new URL(repoUrl)
    } catch {
      return res.status(400).json({ error: 'Invalid URL' })
    }
    if (u.hostname !== 'github.com' && !u.hostname.endsWith('.github.com')) {
      return res.status(400).json({ error: 'Repo URL must be a GitHub link' })
    }

    const webhook = process.env.SUBMIT_WEBHOOK_URL
    if (!webhook) {
      return res.status(500).json({ error: 'Server not configured' })
    }

    // 轉送到 Google Apps Script（或你任何 webhook）
    const forwardRes = await fetch(webhook, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name,
        email,
        repoUrl,
        note: typeof note === 'string' ? note : '',
        submittedAt: new Date().toISOString(),
      }),
    })

    if (!forwardRes.ok) {
      const text = await forwardRes.text().catch(() => '')
      return res.status(502).json({ error: 'Upstream webhook failed', detail: text.slice(0, 200) })
    }

    return res.status(200).json({ ok: true })
  } catch (e) {
    return res.status(500).json({ error: 'Internal error' })
  }
}
