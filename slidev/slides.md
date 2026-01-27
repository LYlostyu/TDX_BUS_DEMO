---
theme: default
title: Git 教學
info: |
  本課程：Git 基礎概念與核心指令（本地工作流）
author: Luoyu
version: 1.7
layout: cover
class: text-left
---

<div class="max-w-3xl">
  <div class="text-6xl font-bold leading-tight">
    Git 入門
  </div>

  <div class="text-3xl opacity-80 mt-4">
    版本控制的第一堂課
  </div>

  <div class="mt-8 grid grid-cols-2 gap-4">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10">
      <div class="text-base opacity-70">Day 1</div>
      <div class="text-xl font-semibold mt-1">Git + GitHub（80分鐘）</div>
      <div class="text-sm opacity-70 mt-2">
        clone / commit / push<br>
        branch / PR / review
      </div>
    </div>
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10">
      <div class="text-base opacity-70">Day 2</div>
      <div class="text-xl font-semibold mt-1">專案競賽（5 小時）</div>
      <div class="text-sm opacity-70 mt-2">
        Issue 分工 / PR 合併<br>
        Demo + 成果展示
      </div>
    </div>
  </div>

  <div class="mt-8 text-base opacity-70">
    講師：洛魚　|　版本：v1.7
  </div>
</div>

<!--
【內容：Git 版本控制：從零開始的備份與協作藝術】

「各位同學大家好。歡迎參加今天的課程。在我們開始學習寫程式之後，大家一定遇過一個問題：當你改動了程式碼卻發現跑不動，想換回昨天的版本，卻發現已經忘記改了哪裡。今天，我們要學習業界最標準的解決方案——Git。這不只是一個工具，更是一種讓你的開發過程變得『有跡可循』的思維方式。」
-->

---
layout: default
---

# Git 是什麼？

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">沒有 Git </div>
    <ul class="space-y-3 text-lg leading-relaxed">
      <li>改壞了不知道哪裡壞</li>
      <li>檔名雜亂：final / final(1) / final(2)</li>
      <li>多人合作互相覆蓋，合併痛苦</li>
    </ul>
  </div>

  <div class="p-6 rounded-2xl  bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">有 Git</div>
    <ul class="space-y-3 text-lg leading-relaxed">
      <li>改動可追溯、可回溯</li>
      <li>協作流程更穩（分支 / PR）</li>
      <li>每個版本都有紀錄（時間、作者、內容）</li>
    </ul>
  </div>

</div>

<div class="mt-8 text-sm opacity-70">Git 是版本控制工具
  <span class="mx-2">|</span>
  詳細說明：<a class="underline" href="https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F" target="_blank">What is Git?</a>
</div>

<!--
【內容：Git 與非 Git 的對比】

「我們先來看這張圖。在沒有 Git 的情況下，大家通常是用手動複製檔案來做備份，檔名可能會變成『final』、『final(1)』甚至『final-真的最後一版』。這種方式不僅佔空間，最痛苦的是當多人合作時，你很難知道誰改了哪一部分，甚至會發生覆蓋掉別人程式碼的慘劇。

有了 Git 之後，每一筆改動都像是有了一台時光機。你可以隨時追溯歷史、回溯到特定時間點，且每一筆紀錄都清楚標示了『誰、在什麼時間、改了什麼內容』。這就是版本控制的核心意義。」
-->

---
layout: default
---

# Git 的架構

<div class="grid grid-cols-2 gap-10 items-center mt-6">

  <div>
    <img
      src="/images/git-flow.png"
      class="w-full max-w-xl mx-auto rounded-lg shadow-md"
      style="object-fit: contain;"
    />
    <p class="text-sm opacity-60 text-center mt-2">
      Working Directory → Staging Area → Repository
    </p>
  </div>

  <div class="space-y-5">
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10">
      <div class="text-lg font-semibold">工作區（Working Directory）</div>
      <div class="text-base opacity-80 mt-1">
        你正在編輯的檔案，改動還沒被記錄
      </div>
      <div class="text-sm opacity-60 mt-2">
        常見動作：編輯 / 儲存 / git status
      </div>
    </div>
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10">
      <div class="text-lg font-semibold">暫存區（Staging Area）</div>
      <div class="text-base opacity-80 mt-1">
        本次提交要包含哪些改動
      </div>
      <div class="text-sm opacity-60 mt-2">
        常見動作：git add（把改動放進來）
      </div>
    </div>
    <div class="p-5 rounded-2xl bg-white/5 border border-white/10">
      <div class="text-lg font-semibold">版本庫（Repository / .git）</div>
      <div class="text-base opacity-80 mt-1">
        提交後的歷史版本紀錄
      </div>
      <div class="text-sm opacity-60 mt-2">
        常見動作：git commit / git log
      </div>
    </div>

  </div>
</div>

<!--
【內容：工作區、暫存區、儲存庫】

「要學好 Git，必須理解這三個區域的運作。請大家想像你在整理書房：

工作區 (Working Directory)：就是你的書桌，你正在寫程式、修改檔案的地方。

暫存區 (Staging Area / Index)：這像是一個搬家紙箱。你覺得這幾個檔案改好了，就把它們放進箱子準備封箱。

儲存庫 (Repository / Commit)：當你下達 commit 指令，就像是把箱子封好並貼上標籤，正式存入倉庫。這就是一個永久的版本紀錄。」
-->

---
layout: default
---

# 準備工作

<div class="grid grid-cols-3 gap-6 mt-4">

  <!-- Card 1 -->
  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">安裝 Git</div>
    <div class="text-sm opacity-70 mb-2">Windows</div>
    <div class="text-base">
      Git for Windows
    </div>
    <div class="mt-4 text-sm opacity-70 mb-2">macOS</div>
    <div class="text-base">
      <code>git --version</code><br />
      <span class="text-sm opacity-70">沒有就安裝 Command Line Tools</span>
    </div>
    <div class="mt-4 text-sm opacity-70 mb-2">Linux</div>
    <div class="text-base">
      <code>sudo apt install git</code>
    </div>
  </div>

  <!-- Card 2 -->
  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">編輯器</div>
    <div class="text-base">
      VS Code（建議）
    </div>
    <div class="mt-4 text-sm opacity-70">
      方便看差異、操作 Git、整合終端機
    </div>
  </div>

  <!-- Card 3 -->
  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">專案資料夾建議</div>
    <ul class="space-y-3 text-base">
      <li>一個專案，一個資料夾</li>
      <li>路徑盡量簡短</li>
      <li>避免特殊符號與長路徑</li>
    </ul>
    <div class="mt-4 text-sm opacity-70">
      範例：<code>D:\Projects\my-app</code>
    </div>
  </div>

</div>

<div class="mt-8 text-sm opacity-70">
  檢查：<code>git --version</code> 有出現版本號就代表已經安裝了
</div>

<!--
「接下來我們進入實作環節。

git init：這是第一步，告訴 Git『請幫我監控這個資料夾』。執行後，你會發現資料夾多了一個隱藏的 .git 檔，那是它的資料庫。

git add：當你修改完檔案，使用 git add . 將所有變更放入剛剛提到的『暫存區紙箱』。

git commit：這是最重要的一步。記得加上 -m 後接訊息，例如『修正登入畫面標題』。這就是你為這個版本寫下的備忘錄。

git push：最後，將本地端的紀錄同步到雲端（如 GitHub），這確保了你的程式碼即使電腦壞了也不會消失。」
-->

---
layout: default
---

# Git常用指令

<div class="grid grid-cols-2 gap-3 items-center mt-6">

  <div>
    <img
      src="/images/git-flow.png"
      class="w-100 max-w-xl mx-auto rounded-lg shadow-md"
      style="object-fit: contain;"
    />
    <p class="text-sm opacity-60 text-center mt-2">
      Working Directory → Staging Area → Repository
    </p>
  </div>

<div class="space-y-5">

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">建立與檢查</div>
    <ul class="space-y-3 text-lg">
      <li><code>git init</code>：初始化倉庫</li>
      <li><code>git status</code>：現況報告</li>
      <li><code>git log --oneline</code>：看歷史版本</li>
    </ul>
  </div>

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">提交流程</div>
    <ul class="space-y-3 text-lg">
      <li><code>git add</code>：放入暫存區</li>
      <li><code>git commit</code>：提交成版本</li>
    </ul>
  </div>
  <div class=" text-sm opacity-70">記憶順序：<code>init → status → add → commit → log</code>
    </div>

  </div>
</div>

<!--
「接下來我們進入實作環節。

git init：這是第一步，告訴 Git『請幫我監控這個資料夾』。執行後，你會發現資料夾多了一個隱藏的 .git 檔，那是它的資料庫。

git add：當你修改完檔案，使用 git add . 將所有變更放入剛剛提到的『暫存區紙箱』。

git commit：這是最重要的一步。記得加上 -m 後接訊息，例如『修正登入畫面標題』。這就是你為這個版本寫下的備忘錄。
-->

---
layout: two-cols-header
---

# Demo：初始化新專案

::left::
<div class="pr-5">
  
<div class="text-xl font-semibold mb-3">建立資料夾 + 初始化</div>

```bash
mkdir my-first-git
cd my-first-git
git init
```

<div class="text-sm opacity-70 mt-3">
  <code>git init</code> 會建立 <code>.git</code>版本庫
</div>
</div>
::right::
<div class="pr-5">

<div class="text-xl font-semibold mb-3">建立 README 後第一次提交</div>

```bash
git status
git add README.md
git commit -m "init: add README"
git log
```

<div class="text-sm opacity-70 mt-3">
  <code>init → status → add → commit → log</code>
</div>

</div>

<!--
「接下來我們進入實作環節。

git init：這是第一步，告訴 Git『請幫我監控這個資料夾』。執行後，你會發現資料夾多了一個隱藏的 .git 檔，那是它的資料庫。

git add：當你修改完檔案，使用 git add . 將所有變更放入剛剛提到的『暫存區紙箱』。

git commit：這是最重要的一步。記得加上 -m 後接訊息，例如『修正登入畫面標題』。這就是你為這個版本寫下的備忘錄。

git push：最後，將本地端的紀錄同步到雲端（如 GitHub），這確保了你的程式碼即使電腦壞了也不會消失。」
-->

---
layout: default
---

# 版本復原

<div class="grid grid-cols-2 gap-4 mt-2">

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-2">情境 A：還沒 add</div>
    <div class="text-sm opacity-70 mb-4">
      取消工作區改動，回到上一個狀態
    </div>

```bash
git restore <file>
````

<div class="mt-3 text-sm opacity-70">
  例：<code>git restore README.md</code>
</div>

  </div>

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-2">情境 B：已 add 但還沒 commit</div>
    <div class="text-sm opacity-70 mb-4">
      把檔案從暫存區移除（保留工作區修改）
    </div>

```bash
git restore --staged <file>
```

  <div class="mt-3 text-sm opacity-70">
    例：<code>git restore --staged README.md</code>
  </div>

  </div>

</div>


<div class="mt-4 p-6 rounded-2xl bg-white/5 border border-white/10">
  <div class="text-xl font-semibold mb-2">情境 C：已 commit，想回復到之前版本</div>
  <div class="text-sm opacity-70 mb-4">
    用 <code>git revert</code> 產生一個「反向 commit」，保留歷史紀錄
  </div>


```bash
git log --oneline
git revert <commit>
# 只想撤銷上一筆：git revert HEAD
```

<div class="mt-3 text-sm opacity-70 leading-tight">
  <div>例：<code>git revert a1b2c3d</code>（會開編輯器讓你確認 commit 訊息，存檔後完成）</div>
  <div class="mt-1">只想「暫時」看看舊版本：<code>git switch --detach &lt;commit&gt;</code>，看完用 <code>git switch -</code> 回來</div>
</div>

</div>

<!--
誰都會手滑。這頁只教不恐怖、最安全的撤回方式。
情境一：還沒 add，就用 git restore <file> 回到上一個狀態。
情境二：已 add 但還沒 commit，用 git restore --staged <file> 把檔案從暫存區移除，但保留工作區修改。
commit 後才發現錯會更複雜，之後講分支與協作流程再深入。
-->

---
layout: default
---

# Commit 訊息怎麼寫？

<div class="grid grid-cols-2 gap-4 mt-4">

  <!-- Left: rules -->
  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">三個原則</div>
    <ul class="space-y-3 text-lg leading-relaxed">
      <li>小步提交：一次 commit 只做一件事</li>
      <li>動詞開頭、簡潔明瞭</li>
      <li>讓人清楚看懂改動</li>
    </ul>
    <div class="mt-6 text-sm opacity-70">
      推薦格式：<code>&lt;type&gt;: &lt;what&gt;</code>
    </div>
  </div>

<!-- Right: prefixes -->
<div class="p-6 rounded-2xl bg-white/5 border border-white/10">
  <div class="text-xl font-semibold mb-4">常見前綴（推薦）</div>
  
  <div class="grid grid-cols-2 gap-3 text-lg">
    <div class="flex items-center gap-2">
      <code class="px-2 py-1 rounded bg-white/5">feat:</code><span class="opacity-85">新功能</span>
    </div>
    <div class="flex items-center gap-2">
      <code class="px-2 py-1 rounded bg-white/5">fix:</code><span class="opacity-85">修 bug</span>
    </div>
    <div class="flex items-center gap-2">
      <code class="px-2 py-1 rounded bg-white/5">docs:</code><span class="opacity-85">文件</span>
    </div>
    <div class="flex items-center gap-2">
      <code class="px-2 py-1 rounded bg-white/5">chore:</code><span class="opacity-85">雜項/工具</span>
    </div>
    <div class="flex items-center gap-2">
      <code class="px-2 py-1 rounded bg-white/5">refactor:</code><span class="opacity-85">重構</span>
    </div>
    <div class="flex items-center gap-2">
      <code class="px-2 py-1 rounded bg-white/5">test:</code><span class="opacity-85">測試</span>
    </div>
</div>

  <div class="mt-4 text-sm opacity-70">
    commit沒有強制的規定，重點是要清楚描述改動內容
  </div>
</div>

</div>

<div class="mt-4 p-5 rounded-2xl bg-white/5 border border-white/10">
  <div class="text-lg font-semibold mb-3">範例</div>

```bash
git commit -m "docs: update README.md"
```

</div>

<style>
pre { margin-top: 0.4rem !important; margin-bottom: 0.4rem !important; }
</style>

---
layout: two-cols-header
---

# 練習：完成兩次 Commit

### 任務 A : 初次提交

<div class="text-sm opacity-80">
目標：做出 <b>2 個 commit</b>，最後用 <code>git log --oneline</code> 看到兩筆紀錄
</div>

::left::
<div class="pr-5">    

1. 確認你在專案資料夾

- 你應該能看到專案檔案，或看到 <code>.git</code> 資料夾  
- 如果不確定，先用下面指令確認目前路徑

```bash
# Windows (PowerShell)
pwd
# macOS / Linux
pwd
# 或用 dir 看目前資料夾內容
dir
````
</div>

::right::

<div class="pr-5">

2. 建立 README.md

用 VS Code 新增檔案，打三行文字並儲存

```md
- git init 用於初始化倉庫
- git status 查看狀態
- git add 將檔案加入暫存區
```


<style>
pre { margin: .35rem 0 !important; }
</style>

</div>

<!--
第一步：確認你在正確資料夾。 你打 pwd 或 dir，看一下你是不是在你要做 Git 的那個資料夾裡。 如果你等一下看到 .git 資料夾，代表你真的在 Git 專案裡。 沒有 .git 就表示你還沒初始化，或你在錯資料夾。

現在建立一個 README.md，寫三行字。內容隨便，你可以寫： line 1 line 2 line 3 重點不是內容，是讓 Git 有東西可以記錄。
-->

---
layout: two-cols-header
---

::left::
<div class="pr-5">  

3. 檢查狀態
```bash
git status
```

你會看到類似：
```powershell
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include...
        note.txt
#看到 README.md 未追蹤
nothing added to commit but untracked files...
```

4. 加入暫存區（stage）
```bash
git add README.md
```
</div>

::right::

<div class="pr-5">  

5. 再檢查一次（應該看到 README.md 在 staged）
```bash
git status
```

你會看到類似：

```powershell
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   note.txt
```

6. 提交（第一次 commit）
```bash
git commit -m "docs: add README.md"
```
你會看到類似：
```powershell
[master (root-commit) 1338eb8] docs: add README.md
 1 file changed, 3 insertions(+)
 create mode 100644 note.txt
```
</div>

<style>
pre { margin: .35rem 0 !important; }
</style>

<!--
現在打： git status 你應該會看到 untracked files，裡面有 notes.txt。 untracked 的意思是：Git 看到它了，但還沒開始追蹤它。 這時候你還不能 commit，因為你還沒把它加入暫存區。

把 notes.txt 加入暫存區： git add notes.txt 再看一次狀態： git status 你要看到 changes to be committed，裡面有 notes.txt，代表它已經在 stage 了。 最後做第一次 commit： git commit -m "docs: add notes.txt" 這句訊息是說：我新增了一個文件 notes.txt。 commit 訊息不是寫給 Git 的，是寫給未來的你跟隊友看的。
-->

---
layout: two-cols-header
---

### 任務 B：修改檔案並提交

<div class="text-sm opacity-80">
目標：在 <code>README.md</code> 再加 2 行 → 用 <code>git diff</code> 看差異 → add → commit
</div>

::left::
<div class="pr-10">

1. 修改 `README.md` 

```md
- git commit 寫入歷史版本
- git log 則查看歷史紀錄
```

2. 看看差異（改了哪些內容）

```bash
git diff
```
結果類似：
```powershell
diff --git a/note.txt b/note.txt
index be2aa87..bbf9a92 100644
--- a/note.txt
+++ b/note.txt
@@ -1,3 +1,5 @@
 - git init 用於初始化倉庫
 - git status 查看狀態
 - git add 將檔案加入暫存區
+- git commit 寫入歷史版本
+- git log 則查看歷史紀錄
\ No newline at end of file
```

</div>

::right::

<div class="pr-10">

3. 加入暫存區（stage）

```bash
git add README.md
```

4. 提交／第二次 commit

```bash
git commit -m "docs: update README.md"
```

結果類似：
```powershell
[master f1bcd00] docs: update README.md
 1 file changed, 2 insertions(+)
```

</div>

<!--
第二次 commit 會更像真實開發流程：先改、看差異、再提交。 第一步，打開 notes.txt，在最後再加兩行，例如： line 4 line 5 第二步，先不要急著 add。先看你改了什麼： git diff 你會看到紅色是被刪掉或被替換的，綠色是新增的。 這一步是讓你確認：我等一下 commit 的東西，真的是我想送出去的東西。 第三步，加入暫存區： git add notes.txt 第四步，第二次 commit： git commit -m "docs: update notes.txt" 最後檢查歷史： git log --oneline 你要看到兩行，代表你完成兩次 commit。
-->

---
layout: two-cols-header
---

# 最後檢查

::left::
<div class="pr-10">

列出歷史
```bash
git log --oneline
```

你應該看到兩筆 commit，像這樣：

```text
xxxxxxx (HEAD -> master) docs: update README.md
yyyyyyy docs: add README.md
```

</div>

::right::

<div class="pr-10">

常見錯誤

##### - `nothing to commit`：沒有改動 / 忘記存檔
##### - `changes not staged for commit`：有改檔，但忘了 `git add`
##### - `untracked files`：新檔案還沒 `git add`

補救流程

```bash
git status
```

</div>

<!--
我們用一句話收尾本機部分： git log --oneline 看到兩行就過關。 如果你只有一行，代表第二次沒有 commit 成功。 如果你看到 changes not staged for commit，代表你改了但忘記 git add。 如果你看到 nothing to commit，代表你根本沒改到，或改了但又改回去。 以後遇到任何 Git 問題，先 git status，八成就知道原因。
-->

---
layout: default
---

# 小結

<div class="text-lg opacity-85 mt-2">
你已經把 Git 的基本功學完了：能新增檔案、看狀態、提交紀錄，還知道怎麼安全撤回。
</div>

<div class="mt-4 grid grid-cols-2 gap-4">
  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-2">我們學了什麼</div>
    <ul class="text-base opacity-85 space-y-2 leading-relaxed">
      <li><code>git init</code>     　初始化</li>
      <li><code>git status</code> 看狀態</li>
      <li><code>git add</code> 暫存（stage）</li>
      <li><code>git commit</code> 提交</li>
      <li><code>git log</code>查看歷史</li>
    </ul>
  </div>

  

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-2">版本回溯</div>
    <ul class="text-base opacity-85 space-y-2 leading-relaxed">
      <li>還沒 add：<code>git restore</code></li>
      <li>已 add：<code>git restore --staged</code></li>
      <li>已 commit：<code>git revert</code></li>
    </ul>
  </div>
</div>

<div class="mt-4 text-lg">
下一章：GitHub 協作（<span class="opacity-90">branch / PR / review / merge</span>）
</div>

<!--
恭喜，你已經會了 Git 最核心的部分：把變更變成可追蹤的歷史。 接下來我們把「一個人在電腦上存檔」升級成「多人合作」。 這就要用到 GitHub。
-->

---
layout: section
---

# GitHub 協作入門
<div class="opacity-80 text-lg mt-2">
我們把「本地 Git」接上「遠端 GitHub」：branch / PR / review / merge / fork
</div>

<!--
一句話分清楚： Git 是你電腦上的版本控制工具。 GitHub 是放專案、做協作的線上平台。 左邊這個 Git，本地端： 它負責記錄每次變更、讓你回到任何版本。 右邊這個 GitHub，遠端： 它負責把專案放上去、讓別人看得到、可以一起 review、一起討論、一起合併。 所以 GitHub 不是 Git 的替代品，是把 Git 的協作能力放大。
-->

---
layout: two-cols-header
---

# GitHub 是什麼？（Git vs GitHub）

<div class="text-sm opacity-85 mt-2">
<b>Git</b> 是版本控制工具；<b>GitHub</b> 是把專案放到線上一起協作的平台
</div>

<div class="mt-4 grid grid-cols-2 gap-4">
  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
  <div class="text-2xl font-semibold mb-4">Git（本地）</div>
  
  <ul class="space-y-3 text-lg leading-relaxed">
    <li>版本控制：記錄每次變更</li>
    <li>可以回到任意版本</li>
    <li>主要在你的電腦上運作（不一定要網路）</li>
  </ul>

  <div class="mt-5 text-sm opacity-70">
    常用：<code>git add、git commit、git log</code>
</div>

</div>


<div class="p-6 rounded-2xl bg-white/5 border border-white/10">
  <div class="text-2xl font-semibold mb-4">GitHub（遠端）</div>

  <ul class="space-y-3 text-lg leading-relaxed">
    <li>線上倉庫：存放/備份專案</li>
    <li>團隊協作：PR / Review / Issues</li>
    <li>讓「分享、討論、合併」變成有流程、有紀錄</li>
  </ul>

  <div class="mt-5 text-sm opacity-70">
    常用：<code>git push、git pull</code>(把本地 Git 跟 GitHub 接起來)
  </div>
</div>

</div>

<!--
一句話分清楚： Git 是你電腦上的版本控制工具。 GitHub 是放專案、做協作的線上平台。 左邊這個 Git，本地端： 它負責記錄每次變更、讓你回到任何版本。 右邊這個 GitHub，遠端： 它負責把專案放上去、讓別人看得到、可以一起 review、一起討論、一起合併。 所以 GitHub 不是 Git 的替代品，是把 Git 的協作能力放大。
-->

---
layout: two-cols-header
---

# 遠端四件套：clone / remote / push / pull

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">clone</div>
    <div class="text-sm opacity-70 mb-3">第一次把遠端倉庫抓到本機</div>

```bash
git clone <repository_url>
```

  </div>

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">remote</div>
    <div class="text-sm opacity-70 mb-3">確認目前連到哪個遠端</div>
```bash
git remote -v
```
  </div>

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">push</div>
    <div class="text-sm opacity-70 mb-3">把本地 commit 上傳到遠端</div>
```bash
git push -u origin <branch-name>
```

<div class="text-sm opacity-70 mt-2">
  之後可簡化成：<code>git push</code>
</div>

  </div>

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">pull</div>
    <div class="text-sm opacity-70 mb-3">把遠端最新變更同步到本地</div>
```bash
git pull
```
  </div>

</div>


<style>
pre { margin: .4rem 0 !important; }
</style>

<!--
遠端互動你只要記四個字：看、下載、推、拉。 clone：把別人的專案下載到你電腦。 remote：看你現在連到哪個 GitHub 倉庫。 push：把你本機的 commit 推上 GitHub。 pull：把 GitHub 上新的 commit 拉回來。 你可以把 push/pull 當成同步： push 是你把更新送出去， pull 是你把別人的更新拿回來。


# Docker has specific installation instructions for each operating system.
# Please refer to the official documentation at https://docker.com/get-started/

# Pull the Node.js Docker image:
docker pull node:24-alpine

# Create a Node.js container and start a Shell session:
docker run -it --rm --entrypoint sh node:24-alpine

# Verify the Node.js version:
node -v # Should print "v24.13.0".

# Verify npm version:
npm -v # Should print "11.6.2".
-->

---
layout: two-cols-header
---

# 為什麼要用分支（Branch）？

<div class="grid grid-cols-2 gap-4 mt-4">


<div class="p-6 rounded-2xl bg-white/5 border border-white/10">
  <div class="text-2xl font-semibold mb-3">分支的重點</div>
  <ul class="space-y-3 text-lg leading-relaxed">
    <li><b>main</b> 保持穩定可運作</li>
    <li>開發／修 bug 在 <b>branch</b> 做</li>
    <li>做完再合併回 <b>main</b></li>
  </ul>

  <div class="mt-5 text-sm opacity-70">
    一個任務一個分支，清楚明瞭 
  </div>
<div class="text-sm opacity-75 mt-1">
分支像實驗室，你可以大膽修改，不會弄壞 main
</div>

</div>



<div class="p-6 rounded-2xl bg-white/5 border border-white/10">
  <div class="text-2xl font-semibold mb-3">分支命名建議</div>

  <div class="grid gap-3 text-lg">
    <div class="flex items-center gap-2">
      <code class="px-2 py-1 rounded bg-white/5">feature/</code>
      <span class="opacity-85">login-page</span>
    </div>

  <div class="flex items-center gap-2">
    <code class="px-2 py-1 rounded bg-white/5">bugfix/</code>
    <span class="opacity-85">header-display</span>
  </div>

  <div class="flex items-center gap-2">
    <code class="px-2 py-1 rounded bg-white/5">docs/</code>
    <span class="opacity-85">update-readme</span>
  </div>

  <div class="mt-5 text-sm opacity-70">
    <code>類型/任務描述</code>（全小寫、用 <code>-</code> 分隔）
  </div>
</div>

</div>

</div>

<style>
code { padding: .1rem .35rem; border-radius: .45rem; background: rgba(255,255,255,.06); }
</style>

<!--
分支就像「安全實驗室」。 main 是穩定版本，你不要直接在 main 亂改。 你想做新功能、修 bug、改 UI，都先開分支。 做完再合併回 main。 這樣你就算做壞了，也只是在自己的分支爆炸， main 還是乾淨、可用、可交付的狀態。
-->

---
layout: two-cols-header
---

# 分支

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">1. 建立並切換分支</div>
    <div class="text-sm opacity-70 mb-3">建立新分支並立刻切過去</div>

```bash
git switch -c feature/ui
```

  </div>

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">2. 查看分支</div>
    <div class="text-sm opacity-70 mb-3">確認你現在在哪個分支（有 * 的那個）</div>
```bash
git branch
```
  </div>

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">3. 切回 main</div>
    <div class="text-sm opacity-70 mb-3">準備把分支成果合回主線</div>
```bash
git switch main
```
  </div>

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">4. 合併分支</div>
    <div class="text-sm opacity-70 mb-3">把 feature/ui 的提交合進 main</div>
```bash
git merge feature/ui
```
  </div>

</div>

<div class="mt-5 text-sm opacity-70">
補充：<code>git checkout -b feature/ui</code>（等同 <code>switch -c</code>）
</div>

<style>
pre { margin: .4rem 0 !important; }
</style>

<!--
分支的最低配流程只要四步： 1 建立並切換分支： git switch -c feature/ui 2 看有哪些分支： git branch 3 切回 main： git switch main 4 合併分支： git merge feature/ui 你把它背起來，協作就能開始跑了。
-->

---
layout: two-cols-header
---

# Pull Request（PR）是什麼？

<div class="text-sm opacity-75 mt-1">PR = 我做完了，請你檢查後再合併
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">PR 的目的</div>

  <ul class="space-y-3 text-lg">
    <li>讓變更先被看過（review）</li>
    <li>提早抓 bug，減少事故</li>
    <li>讓團隊理解你做了什麼</li>
  </ul>

  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">PR 不是測驗</div>

  <ul class="space-y-3 text-lg">
    <li>不追求一次完美</li>
    <li>可討論、可追蹤、可安全合併</li>
  </ul>

  
  </div>
<div class="mt-5 text-sm opacity-70">開 PR 的目的，是大家一起提升專案的品質。
  </div>
</div>

<style>
ul { margin: 0 !important; padding-left: 1.1rem; }
</style>

<!--
PR 是一句話： 「我做完了，請你檢查後再合併。」 PR 的目的不是為了刁難人， 而是讓變更先被看過，提早抓 bug，讓團隊理解你做了什麼。 右邊這句話我很愛： PR 不是考試。 你不是追求一次完美，你追求的是可討論、可追蹤、可安全合併。
-->

---
layout: two-cols-header
---

# PR 內容

<div class="text-sm opacity-75 mt-1">
審查者會想知道：你改了什麼、為什麼改、怎麼確認功能正常
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <!-- Left card -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">1. 我改了什麼（What）</div>
    <ul class="space-y-3 text-lg">
      <li>具體做了哪些改動</li>
      <li>例：新增頁面、調整 CSS 排版</li>
    </ul>

  <div class="h-6"></div>

  <div class="text-2xl font-semibold mb-4">2. 為什麼要改（Why）</div>
  <ul class="space-y-3 text-lg">
    <li>需求來源 / 修 bug 的原因</li>
    <li>讓別人知道你不是亂改</li>
  </ul>
  </div>

  <!-- Right card -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">3. 怎麼測過（How tested）</div>
    <ul class="space-y-3 text-lg">
      <li>你怎麼確認功能能跑</li>
      <li>例：本地跑過、測試通過、附上截圖</li>
    </ul>

  <div class="mt-6 text-sm opacity-70">
    寫得越清楚，review 會更快，效率更高
  </div>
  </div>

</div>

<style>
ul { margin: 0 !important; padding-left: 1.1rem; }
</style>

<!--
你寫 PR 時，reviewer 其實只想知道三件事： 第一，我改了什麼（What）。 例如：新增登入頁、修排版、調 API 參數。 第二，為什麼要改（Why）。 需求來源是什麼？你在修哪個 bug？避免讓人以為你在亂改。 第三，怎麼測過（How tested）。 你用什麼方式確認它能跑？例如：本地跑過、哪些頁面點過、哪些 API 打過。 你把這三件事寫清楚，review 會快非常多，合併也更安心。
-->

---
layout: two-cols-header
---

# 協作流程


<div class="grid grid-cols-2 gap-4 mt-4">

  <!-- Left card -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">本地端（開發、上傳）</div>

  <ol class="space-y-3 text-lg list-decimal pl-6">
    <li><b>main 不直接改</b></li>
    <li><b>每個任務開新分支</b></li>
    <li><b>在分支上 commit</b></li>
  </ol>

  </div>

  <!-- Right card -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">GitHub（協作、合併）</div>

  <ol class="space-y-3 text-lg list-decimal pl-6" start="4">
    <li><b>push</b> 分支到 GitHub</li>
    <li><b>開 PR</b> 互相 review</li>
    <li><b>approve 後 merge</b> 回 main</li>
  </ol>

  </div>

</div>

<style>
ol { margin: 0 !important; }
</style>

<!--
這是一個很常用、也很安全的協作流程。 黃金法則：不要一次 PR 改太多。 流程是： 1 main 不直接改 2 每個任務開新分支 3 在分支上小步 commit 4 push 分支到 GitHub 5 開 PR，互相 review 6 approve 後 merge 回 main 你把它當作團隊的交通規則。 有規則，合作才不會撞車。
-->

---
layout: two-cols-header
---

# 衝突（Conflict）是什麼？

<div class="grid grid-cols-2 gap-4 mt-4">


<div class="mt-2 p-5 rounded-2xl bg-white/5 border border-white/10">
<div class="text-xl font-semibold mb-4">常見原因</div>
<ul class="space-y-2 text-lg">
  <li>兩個分支同時改到同一段</li>
  <li>Git 無法自動判斷要選誰</li>
</ul>

</div>


<div class="mt-2 p-5 rounded-2xl bg-white/5 border border-white/10">
<div class="text-xl font-semibold mb-4">你會看到的標記</div>
```bash
 <<<<<<< HEAD
 （你的版本）
 =======
 （別人的版本）
 >>>>>>> branch-A
```

<div class="text-sm opacity-70 mt-3">
看到這些符號＝需要你手動選擇/合併內容，再把符號刪掉。
</div>


</div>

</div>

<style>
/* 讓清單更舒服 */
ul { margin: 0 !important; padding-left: 1.1rem; }

/* code block 更緊湊，不要吃太多高度 */
pre { margin: .35rem 0 !important; }

/* 右邊卡片裡的 code 不要再額外留太多空 */
.slidev-code { font-size: 0.95em; line-height: 1.35; }
</style>

<!--
衝突不是壞事，它只是 Git 在說： 「你們兩個都改到同一段，我不知道要用哪個。」 常見原因就兩個： 兩個分支同時改到同一段， Git 無法自動判斷誰對。 你會看到的標記是這種： 　<<<<<<< HEAD ======= >>>>>>> branch-A 這時候你要做的事情也很單純： 打開檔案，決定要留哪個版本，或自己手動合成一個更好的版本， 然後把這些標記刪掉，存檔，再 add，再 commit。
-->

---
layout: two-cols-header
---

# 練習：刻意製造一次衝突

<div class="grid grid-cols-2 gap-4 mt-4">

<div class="mt-2 p-5 rounded-2xl bg-white/5 border border-white/10">
<div class="pr-10">

1. 建立 branch-A 並改 README 某一行

```bash
git switch -c branch-A
# edit README.md
git add .
git commit -m "feat: README header version A"
```

2. 切回 main 建 branch-B 並改同一行

```bash
git switch main
git switch -c branch-B
# edit README.md
git add .
git commit -m "feat: README header version B"
```
3. 在 branch-B 合併 branch-A（會衝突）

```bash
git switch main
git merge branch-A
```
</div>
</div>

<div class="mt-2 p-5 rounded-2xl bg-white/5 border border-white/10">
<div class="pl-2">



4. 手動解衝突：打開 README 把標記刪掉，保留你要的內容：

```bash
 <<<<<<< HEAD
 （branch-B 的版本）
 =======
 （branch-A 的版本）
 >>>>>>> branch-A
```
5. 完成後提交

```bash
git add .
git commit -m "fix: resolve conflict on README 
header"
```
</div>
</div>
</div>

<style>
pre { margin: .35rem 0 !important; }
</style>

<!--
我們來做一次「刻意撞車」。 因為你真的解過一次衝突，之後就不怕了。 第一步：從 main 開 branch-A，改 README 第一行，commit。 第二步：切回 main，再開 branch-B，也改 README 同一行，commit。 第三步：切回 main，merge branch-A，通常會成功。 第四步：再 merge branch-B，這次就會衝突。 衝突出現後： 你打開 README，你會看到剛剛那種 <<<<<<< ======= >>>>>>> 的標記。 你決定要保留 A、保留 B、或自己整合一個版本。 最後刪掉標記，存檔。 然後： git add . git commit -m "fix: resolve conflict on README header" 這筆 commit 的意義是：我解決衝突，讓歷史再次回到可用狀態。
-->

---
layout: two-cols-header
---

# Git config：設定你的身份
<div class="text-sm opacity-75 mt-1">
提交（commit）需要作者資訊；遠端協作時也常會用到一些基本設定
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">為什麼要設定？</div>
    <ul class="space-y-3 text-lg">
      <li><b>每一筆 commit</b> 都會記錄作者（name / email）</li>
      <li>避免出現 <code>Author identity unknown</code> 之類錯誤</li>
      <li><b>global</b>：整台電腦通用；<b>local</b>：只套用在某個專案</li>
    </ul>
    <div class="mt-6 text-sm opacity-70">先設 global，若同一台電腦有不同身份，再用 local 覆蓋
    </div>
  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">常用指令</div>

```bash
# 查看目前設定
git config --list

# 設定（整台電腦通用）
git config --global user.name  "你的名字"
git config --global user.email "你的信箱"

# 只針對目前專案設定（會覆蓋 global）
git config user.name  "專案用名字"
git config user.email "專案用信箱"

# 看某一項設定
git config user.name
git config --global user.email
```

<div class="mt-4 text-sm opacity-70">
  檢查 commit 作者是否正確：<code>git log -1</code>
</div>

  </div>

</div>

<style>
pre { margin: .35rem 0 !important; }
code { padding: .1rem .35rem; border-radius: .45rem; background: rgba(255,255,255,.06); }
</style>

<!--
講者稿（逐字稿，簡短版）：
這一頁我們要把 git config 釐清楚。Git 在你每次 commit 的時候，都會把「作者名稱」和「作者信箱」寫進歷史紀錄，所以如果沒有設定，第一次 commit 常會直接失敗。
global 的意思是這台電腦所有專案都用同一套設定；local 是只在目前專案生效，用來覆蓋 global。
我建議大家先把 global 設起來，之後如果你在同一台電腦需要不同身份，例如學校專案與個人專案，再用 local 去覆蓋。
最後提醒：設定完可以用 git log -1 看最新一筆 commit 的作者資訊是否正確。
-->

---
layout: two-cols-header
---

# Fork 是什麼？什麼時候需要 fork？

<div class="text-sm opacity-75 mt-1">
Fork 用於「沒有原專案寫入權限」或「想保留一份自己的副本」時的協作情境
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">Fork 的概念</div>
    <ul class="space-y-3 text-lg">
      <li>在 GitHub 上，把別人的 repo <b>複製一份</b>到你帳號底下</li>
      <li>你對自己的 fork 有完整權限（可 push、開分支）</li>
      <li>之後透過 <b>Pull Request</b> 把改動提交回原 repo</li>
    </ul>
    <div class="mt-6 text-sm opacity-70">
      常見用途：開源貢獻、課程作業模板、沒有權限但想修 bug / 加功能
    </div>
  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">Fork vs Branch vs Clone</div>
    <ul class="space-y-3 text-lg leading-relaxed">
      <li><b>Clone</b>：把某個 repo 下載到你的電腦（本機端）</li>
      <li><b>Branch</b>：在同一個 repo 裡開分支做功能（你通常要有寫入權限）</li>
      <li><b>Fork</b>：在 GitHub 上先做「一份你自己的遠端副本」再協作</li>
    </ul>
    <div class="mt-6 text-sm opacity-70">
      判斷方式：<br/>
      有寫入權限 → 用 branch + PR<br/>
      沒寫入權限 → fork → 再 PR 回去
    </div>
  </div>

</div>

<style>
code { padding: .1rem .35rem; border-radius: .45rem; background: rgba(255,255,255,.06); }
</style>

<!--
講者稿：
這一頁要讓大家清楚 fork 的用途。fork 是在 GitHub 上先把原專案複製到你的帳號底下，讓你擁有寫入權限，之後你可以在你的 fork 開分支、push，最後再用 PR 把變更提交回原專案。
fork 常見在兩種情境：你沒有原 repo 的寫入權限，或你想保留一份自己的副本。
如果你有權限，通常不需要 fork，直接在同一個 repo 開分支、開 PR 就可以。
-->

---
layout: two-cols-header
---

# Fork 工作流程（標準做法）

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">在 GitHub 上做</div>
    <ol class="space-y-3 text-lg list-decimal pl-6">
      <li>到原 repo，按 <b>Fork</b></li>
      <li>到你自己的 fork repo，複製 URL</li>
      <li>之後改完，用 <b>Pull Request</b> 送回原 repo</li>
    </ol>
    <div class="mt-6 text-sm opacity-70">
      PR 的目標（base）是原 repo 的 main，而不是你自己的 fork
    </div>
<br>
<div class="text-sm opacity-75 mt-1">
fork → clone → 加 upstream → 開分支改 → push → 開 PR → 同步 upstream
</div>
  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold">在本機端做</div>

```bash
# 1) clone 你自己的 fork（origin 會指向你的 fork）
git clone <your_fork_url>

# 2) 加 upstream（指向原 repo）
git remote add upstream <original_repo_url>
git remote -v

# 3) 從 main 開一個功能分支
git switch -c feature/my-change

# 4) 改檔 → add → commit
git add .
git commit -m "feat: ..."

# 5) push 到你的 fork（origin）
git push -u origin feature/my-change
```

<div class="mt-4 text-sm opacity-70">
  同步原 repo 更新（常用）：<code>git fetch upstream</code> 後再合併/重置
</div>

  </div>

</div>

<div class="mt-6 p-5 rounded-2xl bg-white/5 border border-white/10">
  <div class="text-lg font-semibold mb-2">同步 upstream（兩種常見方式）</div>

```bash
# 方法 A：merge（保留合併紀錄）
git switch main
git fetch upstream
git merge upstream/main

# 方法 B：rebase（線性歷史，進階用）
git switch feature/my-change
git fetch upstream
git rebase upstream/main
```

</div>

<style>
pre { margin: .35rem 0 !important; }
</style>

<!--
講者稿：
這頁是 fork 的標準流程。我會強調兩個 remote 名稱：origin 和 upstream。
origin 是你自己的 fork（你有權限，可以 push）；upstream 是原 repo（通常你沒權限，不能 push，只能用來同步更新）。
流程是：先 clone 自己的 fork，然後手動加 upstream 指向原 repo。接著從 main 開功能分支，在分支上改檔、commit，最後 push 到 origin，再到 GitHub 開 PR 回 upstream。
同步更新時常用 fetch upstream，再把 upstream/main 合進你的 main，或把你的分支 rebase 到 upstream/main。新手先用 merge 就好，rebase 之後再講。
-->

---
layout: center
class: text-center
---

# 完成 GitHub 協作入門
<br>
<br>
<br>
<br>

## 你已經可以用 branch + PR 做「安全協作」了

<br>
<br>
<br>

<!--
今天你已經把 Git 的核心技能拿到了： 本機：你會 status / diff / add / commit / log 協作：你會 branch / merge GitHub：你知道 push / pull，知道 PR 的意義與寫法 進階：你知道衝突是什麼、怎麼解 你下一步要做的是： 把這套流程用在你自己的專案上。 例如：你把 Slidev 加進你的 Git 專案，做一筆 docs commit， 然後 push 上 GitHub，練一次開 PR。我們會在明天做「真實協作演練」：
-->



---
layout: two-cols-header
---

# 實作任務：Fork → 改 README → 開 PR

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">任務流程</div>
    <ol class="space-y-3 text-lg list-decimal pl-6">
      <li>Fork 本專案到你的 GitHub</li>
      <li>Clone 你的 fork 到本機</li>
      <li>開分支修改 <code>README.md</code></li>
      <li>Commit + Push</li>
      <li>開 Pull Request 回到原專案</li>
    </ol>
    <div class="mt-6 text-sm opacity-70">
      只改 README，練協作流程
    </div>
  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">注意事項</div>
    <ul class="space-y-3 text-lg">
      <li><b>不要提交</b> <code>.env</code>、API key、token</li>
      <li>不要動 <code>node_modules</code>、不要貼大段 log</li>
      <li>Commit 訊息用 <code>docs:</code> 開頭</li>
      <li>PR 說明要寫清楚：What / Why / How tested</li>
    </ul>
  </div>

</div>

<style>
pre { margin: .35rem 0 !important; }
</style>

---
layout: two-cols-header
---

# Step 1：Fork 專案到你的帳號

<div class="text-sm opacity-75 mt-1">
Fork = 在 GitHub 上建立你自己的遠端副本
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">在 GitHub 上操作</div>
    <ol class="space-y-3 text-lg list-decimal pl-6">
      <li>打開提供的原 repo 頁面</li>
      <li>右上角按 <b>Fork</b></li>
      <li>Owner 選你的帳號，repo 名稱保留預設</li>
      <li>按 <b>Create fork</b></li>
    </ol>
    <div class="mt-6 text-sm opacity-70">網址應該變成 <code>github.com/你的帳號/TDX_BUS_DEMO</code>
    </div>
  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">常見錯誤</div>
    <ul class="space-y-3 text-lg">
      <li>把 Fork 當成 Clone（Fork 在 GitHub 上做，Clone 在本機做）</li>
      <li>仍然停留在原 repo 頁面，結果改不到自己的 fork</li>
    </ul>
  </div>

</div>

---
layout: two-cols-header
---

# Step 2：Clone 你的 fork + 設定 upstream

<div class="text-sm opacity-75 mt-1">
origin = 你的 fork（用於自己 push），upstream = 作者原 repo（用來同步更新）
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">Clone（下載你的 fork）</div>

```bash
git clone <你的_fork_URL>
cd tdx-bus-demo
git remote -v
````

<div class="mt-4 text-sm opacity-70">
  你會看到 <code>origin</code> 指向你的 GitHub repo
</div>

  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">加 upstream（連回原 repo）</div>

```bash
git remote add upstream <作者_原repo_URL>
git remote -v
```

<div class="mt-4 text-sm opacity-70">
  目的：作者更新原 repo 時，你可以同步最新版本
</div>

  </div>

</div>

<style>
pre { margin: .35rem 0 !important; }
</style>

---
layout: two-cols-header
---

# Step 3：開分支，修改 README.md

<div class="text-sm opacity-75 mt-1">
一個任務一個分支，這次任務就是文件更新
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">開分支</div>

```bash
git switch -c docs/readme-update
git status
```

<div class="mt-4 text-sm opacity-70">
  確認你現在在 <code>docs/readme-update</code> 分支
</div>

  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">README 要改什麼？（擇一）</div>

<ul class="space-y-3 text-lg">
  <li><b>新增 Troubleshooting</b>：例如 <code>npm install</code> 版本衝突、啟動常見錯誤</li>
  <li><b>補充啟動步驟</b>：把某一步寫更清楚（Windows 指令、路徑、常見漏做）</li>
  <li><b>改善可讀性</b>：加小標題、加 checklist、修錯字、排版 Markdown</li>
</ul>

<div class="mt-6 text-sm opacity-70">
  建議：只改 README 內容，不改程式碼
</div>

  </div>

</div>

---
layout: two-cols-header
---

# Step 4：Commit + Push（只提交 README）

<div class="text-sm opacity-75 mt-1">
提交前先檢查差異與狀態，避免把不該提交的檔案送上去
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">檢查差異</div>

```bash
git diff
git status
```

<div class="mt-4 text-sm opacity-70">
  確認只有 README.md 被修改
</div>

  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">提交並推上去</div>

```bash
git add README.md
git commit -m "docs: improve README"
git push -u origin docs/readme-update
```

<div class="mt-4 text-sm opacity-70">
  <code>-u</code>：把本地分支和遠端分支綁定，之後直接 <code>git push</code> 即可
</div>

  </div>

</div>

<style>
pre { margin: .35rem 0 !important; }
</style>

---
layout: two-cols-header
---

# Step 5：開 Pull Request 回到原專案

<div class="text-sm opacity-75 mt-1">
PR = 請求把你分支上的變更合併進原 repo 的 main
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">在 GitHub 上開 PR</div>
    <ol class="space-y-3 text-lg list-decimal pl-6">
      <li>到你的 fork repo 頁面</li>
      <li>點選提示 <b>Compare & pull request</b></li>
      <li>確認 <b>base repo</b> 是老師原 repo</li>
      <li>確認 <b>base branch</b> 是 <code>main</code></li>
      <li>compare 是你的 <code>docs/readme-update</code></li>
      <li>按 <b>Create pull request</b></li>
    </ol>
  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">PR 內容</div>
    <ul class="space-y-3 text-lg">
      <li><b>What</b>：我改了什麼（例如新增 Troubleshooting）</li>
      <li><b>Why</b>：為什麼要改（例如同學常卡 npm/vite）</li>
      <li><b>How tested</b>：我怎麼確認格式正確（預覽 README、照著步驟跑一次）</li>
    </ul>

<div class="mt-6 text-sm opacity-70">標題可以用 <code>docs:</code> 開頭，例如 <code>docs: add troubleshooting section</code>
</div>

  </div>

</div>

---
layout: default
---

# 有趣的 GitHub 專案（靈感牆）

<div class="text-sm opacity-75 mt-1">
挑 1 個你最有興趣的：先讀 README → 看 Issues → 看 PR → 看 commits（理解一個專案怎麼被維護）
</div>

<div class="grid grid-cols-3 gap-3 mt-4">

  <!-- 1) Image-to-Braille -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold">Image-to-Braille</div>
    <div class="text-sm opacity-75 mt-1">
      把圖片轉成 Unicode 盲文點陣（Braille art）
    </div>
    <div class="mt-5 text-sm font-semibold opacity-90">功能</div>
    <ul class="mt-2 space-y-2 text-base opacity-90">
      <li>影像 → 灰階/抖動 → 點陣映射</li>
      <li>輸入文字就能「顯示圖」</li>
      <li>適合做小功能擴充：尺寸、對比、字元密度</li>
    </ul>
    <div class="mt-5 text-sm font-semibold opacity-90">Repo</div>
    <div class="mt-2 text-sm">
      <a class="underline underline-offset-4" href="https://github.com/505e06b2/Image-to-Braille" target="_blank" rel="noopener">
        505e06b2/Image-to-Braille
      </a>
    </div>
  </div>

  <!-- 2) BetterLyrics -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold">BetterLyrics</div>
    <div class="text-sm opacity-75 mt-1">
      高度可自訂的歌詞視覺化 + 音樂播放器（WinUI3 / Win2D）
    </div>
    <div class="mt-5 text-sm font-semibold opacity-90">功能</div>
    <ul class="mt-2 space-y-2 text-base opacity-90">
      <li>桌面 App 的 UI/動畫與渲染</li>
      <li>偏完整產品：設定、體驗、工程結構</li>
      <li>適合觀察如何拆模組、如何做可擴充功能</li>
    </ul>
    <div class="mt-5 text-sm font-semibold opacity-90">Repo</div>
    <div class="mt-2 text-sm">
      <a class="underline underline-offset-4" href="https://github.com/jayfunc/BetterLyrics" target="_blank" rel="noopener">
        jayfunc/BetterLyrics
      </a>
    </div>
  </div>

  <!-- 3) Excalidraw -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold">Excalidraw</div>
    <div class="text-sm opacity-75 mt-1">
      手繪風白板工具（支援協作/分享）
    </div>
    <div class="mt-5 text-sm font-semibold opacity-90">功能</div>
    <ul class="mt-2 space-y-2 text-base opacity-90">
      <li>前端大型專案結構（UI/狀態/資料）</li>
      <li>協作功能：即時同步、分享流程</li>
      <li>適合理解如何把產品做成可維護的工程</li>
    </ul>
    <div class="mt-5 text-sm font-semibold opacity-90">Repo</div>
    <div class="mt-2 text-sm">
      <a class="underline underline-offset-4" href="https://github.com/excalidraw/excalidraw" target="_blank" rel="noopener">
        excalidraw/excalidraw
      </a>
    </div>
  </div>

</div>

<style>
pre { margin: .35rem 0 !important; }
</style>

---
layout: default
---

# 5 小時競賽規則與建議
<div class="text-sm opacity-75 mt-1">
  成果可以是「作品」或「專案計畫」，不一定要完成可展示系統
</div>

<script setup>
import { ref } from 'vue'

const showPlanModal = ref(false)

const rules = [
  "總時長 6 小時，小組合作",
  "每組需建立 GitHub Repo，並於繳交時提供 Repo 連結",
  "README.md 為必要文件（專案說明 / 計畫內容 / 操作方式）",
  "需使用 Git 進行版本管理（commit 紀錄視為成果的一部分）",
  "不可提交 .env / API key / token，不要上傳 node_modules 或大量 log",
  "活動結束後，每組有 8 分鐘成果報告時間",
]

const deliverables = [
  { title: "可運作 Demo", desc: "能跑的最小原型：功能少也可以，但要可操作。" },
  { title: "半成品 + 說明", desc: "核心功能完成，搭配架構、限制與下一步規劃。" },
  { title: "專案計畫書（可選）", desc: "不一定要做出作品。請用計畫呈現你的想法。" },
]

const planChecklist = [
  "問題定義：要解決什麼？誰會用？",
  "解決方案：功能範圍與取捨（MVP）",
  "系統架構 / 流程圖：前後端、資料流、頁面流程",
  "分工與時程：6 小時內怎麼切任務",
  "驗證方式：如何測試或展示成果",
]
</script>

<div class="h-full w-full px-10 py-6">
  <div class="grid grid-cols-2 gap-6">
    <!-- Left -->
    <div class="space-y-4">
      <div class="rounded-2xl border border-white/10 bg-white/5 p-5">
        <div class="text-xl font-semibold mb-3">基本規則（請務必完成）</div>
        <ul class="space-y-2">
          <li v-for="(r, i) in rules" :key="i" class="flex gap-2">
            <span class="opacity-70">•</span>
            <span class="text-[15px] leading-6">{{ r }}</span>
          </li>
        </ul>
      </div>
    </div>
    <!-- Right -->
    <div class="space-y-4">
      <div class="rounded-2xl border border-white/10 bg-white/5 p-5">
        <div class="text-xl font-semibold mb-3">可提交成果（擇一即可）</div>
        <div class="space-y-3">
          <div
            v-for="(d, i) in deliverables"
            :key="i"
            class="rounded-xl border border-white/10 bg-black/20 p-4"
          >
            <div class="font-semibold">{{ d.title }}</div>
            <div class="text-[14px] opacity-80 mt-1 leading-2">{{ d.desc }}</div>
          </div>
        </div>
        <div class="mt-4 pt-4 border-t border-white/10 flex items-center justify-between gap-4">
          <button
            class="px-4 py-2 rounded-xl border border-white/20 bg-black/30 hover:bg-white/10 transition font-semibold whitespace-nowrap"
            @click="showPlanModal = true"
          >
            計畫書建議內容
          </button>
          <div class="text-xs opacity-70 leading-5">
            選「專案計畫書」的組別<br />請點此查看 checklist
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal 遮罩 -->
  <div
    v-if="showPlanModal"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm"
    @click.self="showPlanModal = false"
  >
    <!-- Modal 本體 -->
    <div class="w-[720px] max-w-[92vw] rounded-3xl border border-white/15 bg-[#0f0f0f] p-8 shadow-2xl">
      <div class="flex items-start justify-between mb-4">
        <div class="text-2xl font-bold">計畫書建議內容（計畫組重點）</div>
        <button class="text-white/60 hover:text-white text-xl" @click="showPlanModal = false">✕</button>
      </div>
      <ul class="space-y-3">
        <li v-for="(p, i) in planChecklist" :key="i" class="flex gap-3 items-start">
          <span class="mt-1 text-white/40">●</span>
          <span class="text-[16px] leading-7">{{ p }}</span>
        </li>
      </ul>
      <div class="mt-6 flex items-center justify-between">
        <button
          class="px-5 py-2 rounded-xl border border-white/20 bg-white/10 hover:bg-white/20 transition"
          @click="showPlanModal = false"
        >
          關閉
        </button>
      </div>
    </div>
  </div>
</div>

---
layout: center
---

<div class="text-center">

# 成果評量與發表說明
</div>


<script setup>
const grading = ["問題清楚", "解法合理", "說明完整", "Git 使用正確", "README 品質", "分工與過程可追蹤"]
</script>

<div class="h-full w-full flex flex-col justify-center px-20">

  <div class="grid grid-cols-2 gap-10">
    <!-- 評量重點 -->
    <div class="rounded-3xl border border-white/10 bg-white/5 p-8">
      <div class="text-2xl font-semibold mb-5">評量重點</div>
      <div class="flex flex-wrap gap-3">
        <span
          v-for="(g, i) in grading"
          :key="i"
          class="px-4 py-2 rounded-full border border-white/15 bg-black/20 text-base"
        >
          {{ g }}
        </span>
      </div>
      <div class="mt-6 text-lg opacity-80 leading-5">
        評分會重視你們如何定義問題、如何設計解法、  
        以及你們在有限時間內做出的取捨與規劃能力。
      </div>
    </div>
    <!-- 提醒 -->
    <div class="rounded-3xl border border-white/10 bg-white/5 p-8 flex flex-col justify-between">
      <div>
        <div class="text-2xl font-semibold mb-5">提醒</div>
        <ul class="space-y-4 text-lg leading-8">
          <li>每組一定要繳交 <span class="font-semibold">GitHub Repo 連結</span></li>
          <li>Repo 內一定要有 <span class="font-semibold">README.md</span></li>
          <li>README 必須能看懂你們在做什麼、怎麼想、怎麼規劃</li>
          <li>🎤 活動結束後，每組有 <span class="font-semibold text-xl">8 分鐘成果報告</span></li>
        </ul>
      </div>
    </div>
  </div>
</div>
