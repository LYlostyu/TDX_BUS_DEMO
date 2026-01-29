<script setup>
import { ref, computed } from 'vue'

const name = ref('')
const repoUrl = ref('')
const note = ref('')
const loading = ref(false)
const message = ref('')
const ok = ref(false)
const email = ref('')
const isValidEmail = computed(() =>
  /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value.trim())
)
const isValidUrl = computed(() => {
  try {
    const u = new URL(repoUrl.value.trim())
    return u.hostname === 'github.com' || u.hostname.endsWith('.github.com')
  } catch {
    return false
  }
})

async function submit() {
  message.value = ''
  ok.value = false

  if (!name.value.trim()) {
    message.value = '請填名字'
    return
  }
  if (!isValidEmail.value) {
    message.value = '請輸入有效的電子信箱'
    return
  }
  if (!isValidUrl.value) {
    message.value = 'Repo 連結看起來不是 GitHub URL'
    return
  }
  loading.value = true
  try {
    const res = await fetch('/api/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        name: name.value.trim(),
        email: email.value.trim(),
        repoUrl: repoUrl.value.trim(),
        note: note.value.trim(),
        // passcode: passcode.value.trim(),通關碼，避免被濫用
      }),
    })

    const data = await res.json().catch(() => ({}))
    if (!res.ok) {
      message.value = data?.error || `送出失敗（${res.status}）`
      return
    }

    ok.value = true
    message.value = '已送出！你可以去找助教確認是否有收到'
  } catch (e) {
    message.value = '送出失敗：網路或伺服器錯誤'
  } finally {
    loading.value = false
  }
}
</script>

<template>
  <div class="p-5 rounded-3xl border border-white/10 bg-white/5 backdrop-blur">
    <div class="text-xl font-bold mb-3">Repo 繳交</div>

    <div class="grid gap-2">
      <label class="text-sm opacity-80">名字</label>
      <input v-model="name" class="p-1 rounded-lg bg-black/30 border border-white/10" placeholder="請填寫你的名字" />

      <label class="text-sm opacity-80">聯絡信箱</label>
      <input v-model="email" class="p-2 rounded-lg bg-black/30 border border-white/10" placeholder="example@gmail.com" />

      <label class="text-sm opacity-80">GitHub Repo 連結</label>
      <input v-model="repoUrl" class="p-1 rounded-lg bg-black/30 border border-white/10" placeholder="https://github.com/xxx/yyy" />

      <label class="text-sm opacity-80">備註（可選）</label>
      <input v-model="note" class="p-1 rounded-lg bg-black/30 border border-white/10" placeholder="例如：專案完成度/呈現方式/發表需求" />


      <button
        class="mt-2 px-4 py-2 rounded-lg bg-white/15 hover:bg-white/20 border border-white/10 disabled:opacity-50"
        :disabled="loading"
        @click="submit"
      >
        {{ loading ? '送出中…' : '送出' }}
      </button>

      <div v-if="message" class="text-sm" :class="ok ? 'text-green-300' : 'text-yellow-200'">
        {{ message }}
      </div>
    </div>
  </div>
</template>
