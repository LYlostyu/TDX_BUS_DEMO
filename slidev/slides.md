---
theme: default
title: Git 教學
info: |
  本課程：Git 基礎概念與核心指令（本地工作流）
author: Luoyu
version: 2.2
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
      <div class="text-xl font-semibold mt-1">Git + GitHub（2 小時）</div>
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
    講師：洛魚　|　版本：v2.2
  </div>
</div>

<!--
各位同學好，今天這一堂課的目標：學會git

在資訊工程、軟體開發、甚至大學專題與公司實務中都**一定會用到的工具**

今天我們要學習業界最標準的解決方案——Git。
建立專案資料夾、保存版本、查看歷史、以及在出錯時能夠復原。
-->

---
layout: default
---

# Git 是什麼？
<img
  src="/images/comandos-git.jpg"
  class="w-40 max-w-xl ml-0 rounded-lg"
  style="object-fit: contain; filter: brightness(1.) invert(0.1);"
/>
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
 官方說明：<a class="underline" href="https://git-scm.com/book/en/v2/Getting-Started-What-is-Git%3F" target="_blank">What is Git?</a>
</div>

<!--
我們先來看這張圖。在沒有 Git 的情況下，大家通常是用手動複製檔案來做備份，檔名可能會變成『final』、『final(1)』甚至『final-真的最後一版』。這種方式不僅佔空間，最痛苦的是當多人合作時，你很難知道誰改了哪一部分，甚至會發生覆蓋掉別人程式碼的慘劇。

有了 Git 之後，你可以隨時追溯歷史、回溯到特定時間點，且每一筆紀錄都清楚標示了『誰、在什麼時間、改了什麼內容』。這就是版本控制的核心意義。

 Git 不是用來寫程式的工具，Git 是用來**管理專案歷史的系統工具**。是一套 **版本控制工具**
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
Git 的運作核心有三個區域

工作區 (Working Directory)：也就是你現在電腦看到的資料夾，實際寫程式、打報告、改檔案的地方。

暫存區 (Staging Area / Index)：在這裡你可以挑選哪些修改，準備要存成一個版本

版本庫 (Repository / Commit)：這是真正存放歷史版本的地方，每一次 commit，都會被永久記錄在這裡。

流程：
改檔案 → 放進暫存區 → 存成一個版本。
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
第一，Git 本身。
安裝完之後，只要在終端機輸入 `git --version`，能顯示版本號，代表安裝成功。

第二，編輯器。
今天示範會用 VS Code，它可以幫助我們查看檔案與 Git 狀態。

第三，專案資料夾。
建議之後所有 Git 專案都放在固定資料夾，例如 D:\projects。

這一步完成後，我們就可以開始真正操作 Git 了。
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
今天只會學最基本、最重要的五個指令。

`git init`：把資料夾變成 Git 專案
`git status`：查看目前狀態
`git add`：把檔案放進暫存區
`git commit`：建立一個版本
`git log`：查看版本歷史

如果你今天只記得一條流程，也完全夠用：

init → status → add → commit → log
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

<!--
Commit 是寫給未來自己與隊友看的紀錄。

基本原則三個：
一個 commit 做一件事
說清楚做了什麼
用簡短動詞開頭

常見格式例如：
feat: 新功能
fix: 修 bug
docs: 文件修改

例如：
docs: update README

commit 訊息，等於專案的歷史說明書。
-->

---
layout: two-cols-header
---

# Git config：設定你的身份
<div class="text-sm opacity-75 mt-1">
提交（commit）需要作者資訊！
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">為什麼要設定？</div>
    <ul class="space-y-3 text-lg">
      <li><b>每一筆 commit</b> 都會記錄作者（name / email）</li>
      <li>避免出現 <code>Author identity unknown</code> 之類錯誤</li>
      <li><b>global</b>：整台電腦通用</li>
      <li><b>local</b>：只套用在某個專案</li>
    </ul>
    <div class="mt-6 text-sm opacity-70">先設 global，若同一台電腦有不同身份，再用 local 覆蓋
    </div>
  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">使用指令</div>

```bash
# 查看目前設定
git config --list

# 設定（global=整台電腦通用）
git config --global user.name  "你的名字"
git config --global user.email "你的信箱"

# 只針對目前專案設定（local=當前專案資料夾下）
git config user.name  "專案用名字"
git config user.email "專案用信箱"
```


  </div>

</div>

<!--
Git 在你每次 commit 的時候，都會把「作者名稱」和「作者信箱」寫進歷史紀錄，所以如果沒有設定，第一次 commit 常會直接失敗。
global 的意思是這台電腦所有專案都用同一套設定；local 是只在目前專案生效，用來覆蓋 global。

投影片也提到 global 和 local 的差異：
global 是整台電腦通用。
local 是只針對某個專案。
一般教室環境通常用 global 比較方便，但如果是共用電腦，則要注意帳號不要混用。

設定完成後，你可以用 `git log -1` 看最新 commit 的作者資訊是否正確。
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
Git 可以復原的情況有三種。

第一，改了檔案，但還沒 add。
可以用 `git restore 檔名` 還原。

第二，已經 add，但還沒 commit。
用 `git restore --staged 檔名`，把檔案退回修改狀態。

第三，已經 commit，想取消一個版本。
使用 `git revert 版本號`，Git 會自動產生一個『反向版本』。

重點：Git 不會刪歷史，它是用新版本來修正舊版本。
-->

---
layout: two-cols-header
---

# 練習：完成兩次 Commit
### 任務 A : 初次提交
<div class="text-sm opacity-80">
目標：做出 <b>2 個 commit</b>，最後用 <code>git log --oneline</code> 看到兩筆紀錄
</div>   

::left::
<div class="pr-5 mt-2"> 
1. 設定作者名稱與信箱
<div class="text-sm">雙引號內請填入自己的資訊
</div>
```bash
git config --global user.name  "你的名字"
git config --global user.email "你的信箱"
```
</div>


<div class="pr-5 mt-5">    
2. 確認你在專案資料夾

<div class="text-sm">建立資料夾 + 初始化</div>

```bash
git init

```

<div class="text-sm opacity-70 mt-3">
  <code>git init</code> 會建立 <code>.git</code>版本庫
</div>
</div>


::right::

<div class="pr-5 mt-2">

3. 建立 README.md
<div class="text-sm">用 VS Code 新增檔案，並做編輯</div>

```md
- git init 用於初始化倉庫
- git status 查看狀態
- git log 查看歷史紀錄
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

4. 檢查狀態
```bash
git status
```

你會看到類似：
```powershell
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include...
        README.md
#看到 README.md 未追蹤
nothing added to commit but untracked files...
```

5. 加入暫存區（stage）
```bash
git add README.md
```
</div>

::right::

<div class="pr-5">  

6. 再檢查一次（應該看到 README.md 在 staged）
```bash
git status
```

你會看到類似：

```powershell
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   README.md
```

7. 提交（第一次 commit）
```bash
git commit -m "docs: add README.md"
```
你會看到類似：
```powershell
[master (root-commit) 1338eb8] docs: add README.md
 1 file changed, 3 insertions(+)
 create mode 100644 README.md
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

### 任務 B：修改檔案並再次提交

<div class="text-sm opacity-80">
目標：在 <code>README.md</code> 再加 2 行 → 用 <code>git diff</code> 看差異 → add → commit
</div>

::left::
<div class="pr-10">

1. 修改 `README.md` 

```md
- git add 將檔案加入暫存區
- git commit 寫入歷史版本
```

2. 看看差異（改了哪些內容）

```bash
git diff
```
結果類似：
```powershell
diff --git a/README.md b/README.md
index be2aa87..bbf9a92 100644
--- a/README.md
+++ b/README.md
@@ -1,3 +1,5 @@
 - git init 用於初始化倉庫
 - git status 查看狀態
 - git log 查看歷史紀錄
+- git add 將檔案加入暫存區
+- git commit 寫入歷史版本
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

# 檢查

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
##### - `untracked files`：檔案還沒 `git add`

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
      <li><code>git config</code>設定身分</li>
      <li><code>git init</code>初始化</li>
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
    <li>主要在你的電腦上運作</li>
  </ul>

  <div class="mt-5 text-sm opacity-70">
    常用：<code>git add、git commit、git log</code>
</div>

</div>


<div class="p-6 rounded-2xl bg-white/5 border border-white/10">
  <div class="text-2xl font-semibold mb-4"><a class="underline underline-offset-4" href="https://github.com/" target="_blank" rel="noopener">GitHub</a>（遠端）</div>

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
各位同學好，前一段我們學的是 **Git**，它是安裝在你電腦上的版本控制工具。
接下來我們要學 **GitHub**，它是一個放在網路上的平台，用來讓你把 Git 專案放到雲端，並和別人一起合作。

**Git 是本地端的版本控制工具；GitHub 是遠端的協作平台。**

先看 Git。
Git 的核心工作是：記錄每次修改、保存版本、能回到過去。
而且就算沒有網路，你也能在自己的電腦上做 commit、看 log。

再看 GitHub。
GitHub 是把專案放上網路，讓你可以：
第一，幫專案做雲端備份。
第二，讓多人協作更容易，例如討論、PR、Review、Issues。
第三，能把作品公開，變成履歷的一部分。

等一下我們會學：怎麼把本地端的 Git，接到 GitHub 這個遠端平台。
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
要讓本地端 Git 和 GitHub 連起來，最常用的四件事是：clone、remote、push、pull。

第一個，**clone**。
clone 的意思是：把 GitHub 上的專案整份『複製到你的電腦』。
指令通常是 `git clone <repository_url>`。
第一次拿到別人的專案，最常做的就是 clone。

第二個，**remote**。
remote 是『遠端地址的設定』。
你可以把 GitHub 的網址當作一個遠端倉庫，並取名叫 origin。
用 `git remote -v` 可以查看目前連到哪裡。

第三個，**push**。
push 是把你本地端已經 commit 的版本，上傳到 GitHub。
也就是把資料從你電腦推到雲端。
常見形式是 `git push -u origin <branch-name>`，之後就可以用 `git push`。

第四個，**pull**。
pull 則相反，是把 GitHub 上最新的版本拉回你電腦。
當別人改了專案、或你換電腦時，你就需要 pull。

請記住方向：
push 是『往外推到 GitHub』；pull 是『從 GitHub 拉回來』。
-->

---
layout:default
---

# Git vs GitHub

<div class="text-sm opacity-85 mt-2">
add / commit / push / pull</div>

<img
      src="/images/Git-push-pull.png"
      class="w-120 max-w-xl mx-auto rounded-lg shadow-md"
      style="object-fit: contain;"
    />

---
layout:default
---

# 練習：複製範例專案


<div class="mt-2 p-5 rounded-2xl bg-white/5 border border-white/10">
<div class="pr-2">
1.打開 VScode 終端機

2.使用 git clone 複製範例專案

```bash
git clone https://github.com/LYlostyu/TDX_BUS_DEMO.git
```

3.確認資料夾中是否出現了 TDX_BUS_DEMO 資料夾。

4.查看專案歷史

```bash
git log --oneline
```

5. 可自行探索
</div>

</div>

<!--
回到可用狀態。
-->

---
layout: two-cols-header
---

# 為什麼要用分支（Branch）？

<div class="grid grid-cols-2 gap-4 mt-4">


<div class="p-6 rounded-2xl bg-white/5 border border-white/10">
  <div class="text-2xl font-semibold mb-3">分支的重點</div>
  <ul class="space-y-3 text-lg leading-relaxed">
    <li><b>main</b> 主線保持穩定可運作</li>
    <li>開發／修 bug 在 <b>branch</b> 做</li>
    <li>做完再合併回 <b>main</b> 主線</li>
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
      <code class="px-2 py-1 rounded bg-white/5">feature/login-page</code>
    </div>

  <div class="flex items-center gap-2">
    <code class="px-2 py-1 rounded bg-white/5">bugfix/header-display</code>
  </div>

  <div class="flex items-center gap-2">
    <code class="px-2 py-1 rounded bg-white/5">docs/update-readme</code>
  </div>

  <div class="mt-5 text-sm opacity-70">
    <code>類型/任務描述</code>
  </div>
</div>

</div>

</div>

<style>
code { padding: .1rem .35rem; border-radius: .45rem; background: rgba(255,255,255,.06); }
</style>

<!--
接下來是多人協作最重要的概念：**分支 Branch**。

分支存在的原因是：我們不希望大家直接在 main 上亂改。
main 通常代表『穩定、可以運行、可以交付』的版本。

所以一般做法是：
要新增功能，就開一條 feature 分支。
要修 bug，就開一條 bugfix 分支。
文件更新可以用 docs 分支。

好處有三個：
第一，你可以在分支上放心實驗，不會影響 main。
第二，大家可以同時開不同分支，各做各的。
第三，最後要合併回 main 時，可以經過獨立清楚的檢查與審核。

分支名稱也要清楚
feature/login-page
bugfix/header-display
docs/update-readme
這些名稱一看就知道它在做什麼，方便合作與管理。
-->

---
layout: two-cols-header
---

# 分支

<div class="grid grid-cols-2 gap-4 mt-4">
  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">1. 查看分支</div>
    <div class="text-sm opacity-70 mb-3">確認你現在在哪個分支（符號 * 提示）</div>
```bash
git branch
```
  </div>

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">2. 建立並切換分支</div>
    <div class="text-sm opacity-70 mb-3">建立新分支並立刻切過去</div>

```bash
git switch -c <分支名稱>
```
<div class="text-sm opacity-70 mb-3">例：git switch -c feature/ui</div>
  </div>

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">3. 切回主支</div>
    <div class="text-sm opacity-70 mb-3">準備把分支成果合回主支</div>
```bash
git switch master
```
  </div>

  <div class="p-6 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-3">4. 合併分支</div>
    <div class="text-sm opacity-70 mb-3">把 feature/ui 的提交合進當前分支</div>
```bash
git merge feature/ui
```
  </div>

</div>

<div class="mt-5 text-sm opacity-70">
補充：<code>git checkout -b <分支></code>（等同 <code>switch -c</code>）
</div>

<style>
pre { margin: .4rem 0 !important; }
</style>

<!--
這一頁我們把分支操作拆成四步，讓你有一個標準流程。

第一步，建立並切換到新分支。
使用 `git switch -c feature/ui`。
意思是：建立一條叫 feature/ui 的分支，並立刻切過去。

第二步，查看分支。
用 `git branch`，你會看到目前有哪些分支，並且會標出你現在在哪一條。

第三步，切回 main。
當你分支的工作做完，準備要合併，就用 `git switch main` 回到 main。

第四步，合併分支。
站在 main 上，輸入 `git merge feature/ui`，把分支的修改合進 main。

補充：有些同學會看到 `git checkout -b`，它是舊式寫法。
現在建議用 `git switch`，語意更清楚。
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
hide: true
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

2. 建 branch-B 並改<span class="font-semibold text-xl">同一行
</span>
```bash
git switch -c branch-B
# edit README.md
git add .
git commit -m "feat: README header version B"
```
3. 在 branch-B 合併 branch-A（衝突）

```bash
git merge branch-A
```
</div>
</div>

<div class="mt-2 p-5 rounded-2xl bg-white/5 border border-white/10">
<div class="pl-2">



4. 手動解衝突：在 README 中把標記刪掉，只保留你要的內容

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

# Pull Request（PR）是什麼？

<div class="text-sm opacity-75 mt-1">PR = 我做完了，請你檢查後再合併
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">PR 的目的</div>

  <ul class="space-y-3 text-lg">
    <li>讓變更先被看過（review）</li>
    <li>提早抓 bug，減少事故</li>
    <li>讓審查者理解你做了什麼</li>
  </ul>

  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-2xl font-semibold mb-4">PR 不是刁難人</div>

  <ul class="space-y-3 text-lg">
    <li>不追求一次完美</li>
    <li>可討論、可追蹤、可安全合併</li>
  </ul>

  
  </div>
開 PR 的目的，是大家一起提升專案的品質。
</div>

<style>
ul { margin: 0 !important; padding-left: 1.1rem; }
</style>

<!--
接下來是 GitHub 協作的核心功能：**Pull Request，簡稱 PR**。

PR 可以理解成：
我完成一個分支的工作後，向團隊提出『我想把這些修改合併回 main』的申請。

PR 的目的有三個：
第一，讓別人可以 review 你的改動，避免錯誤直接進入 main。
第二，把討論集中在同一個地方，大家可以留言、建議、補充。
第三，留下紀錄，未來回看時會知道這次合併做了什麼。

PR 的目的不是為了刁難人， 而是讓變更先被看過，提早抓 bug，讓團隊理解你做了什麼
另外，投影片右邊也提醒：PR 不是測驗。
PR 不是一次就要做對。
你可以改、可以補、可以修，最後再合併。
它的本質是『可追蹤、可討論、可控制風險的合併流程』。
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
PR 不只是按一個按鈕，它也需要寫清楚內容。
這一頁提供一個很實用的格式：What、Why、How tested。

第一，What：我改了什麼？
請用最具體的句子描述，例如：
新增登入頁面、調整 CSS 排版、更新 README 說明。

第二，Why：為什麼要改？
例如：修正某個 bug 的原因、或原本設計不清楚、或需求新增。

第三，How tested：怎麼測過？
請說明你如何確認它可以運作，例如：
在本地端啟動專案、點過哪些功能、截圖或附上操作結果。

這樣寫的好處是：
別人不用猜你的目的，也能快速知道如何驗證，review 的效率會大幅提升。
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
這一頁是一個完整協作流程，我希望大家把它當成之後的標準做法。

左邊是本地端，也就是你電腦上要做的事：
第一，main 不直接改。
第二，每個任務都開新分支。
第三，在分支上完成修改並 commit。

右邊是 GitHub 上做的事：
第四，把分支 push 到 GitHub。
第五，開 PR 並請別人 review。
第六，review 通過後，再 merge 回 main。

請注意：這個繁瑣的的流程不是單純為了形式。
它的目的是讓 main 永遠保持穩定，並且讓每一次合併都有紀錄、能被檢查。
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
      <li><b>Clone</b>：把 repo 下載到你的電腦（本地）</li>
      <li><b>Branch</b>：在同一個 repo 裡開分支做功能（要有寫入權限）</li>
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
接下來是 GitHub 上另一個常見動作：**Fork**。

Fork 的意思是：
在 GitHub 上，把別人的 repo 複製一份到你自己的帳號底下。
這樣你就擁有一份自己的版本，可以自由修改、push、開分支，不會影響原作者的 repo。

什麼時候需要 fork？
通常是你沒有原 repo 的寫入權限，或你在參與開源專案。
你先 fork 到自己帳號，改完後再用 Pull Request 把修改送回原 repo，讓原作者決定要不要合併。

右側也幫你做了比較：
Clone：把 repo 下載到本地端。
Branch：在同一個 repo 裡切出工作線。
Fork：在 GitHub 上先複製出『你的版本』，通常用在你不是原 repo 成員的情境。
-->

---
layout: two-cols-header
---

# Fork 工作流程

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">在 GitHub 上</div>
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
    <div class="text-xl font-semibold">在本地端開發</div>

```bash
# 1. clone 你自己的 fork（origin 會指向你的 fork）
git clone <your_fork_url>

# 2. 加 upstream（指向原 repo）
git remote add upstream <original_repo_url>
git remote -v

# 3. 從 main 開一個功能分支
git switch -c feature/my-change

# 4. 改檔 → add → commit
git add .
git commit -m "feat: ..."

# 5. push 到你的 fork（origin）
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
最後一頁，我們把 fork 的標準流程走一遍，讓你可以在任何開源專案都套用。

在 GitHub 上做：
第一，到原 repo 按 Fork，得到你自己的 fork repo。
第二，在你自己的 fork repo 複製網址。
第三，之後開 Pull Request 時，目標是原 repo 的 main。

在本地端做：
第一，clone 你自己的 fork repo。
第二，新增 upstream，指向原 repo。
這一步很重要，因為原 repo 才是『真正的最新版本來源』。
第三，在本地端開新分支，完成修改並 commit。
第四，把分支 push 到你自己的 fork repo。
第五，在 GitHub 開 PR，送回原 repo。

補充一個維持同步的習慣：
當原 repo 更新時，你要 fetch upstream，再把更新合併回你的分支或 main，避免你的 fork 長期落後。

到這裡，你就具備參與開源專案、做多人協作的基本流程。
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
      <li>打開提供的 <a class="underline underline-offset-4" href="https://github.com/LYlostyu/TDX_BUS_DEMO" target="_blank" rel="noopener">repo</a> 頁面</li>
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
cd TDX_BUS_DEMO
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
git branch
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
    <div class="text-xl font-semibold mb-4">檢查</div>

```bash
git diff
git status
```

<div class="mt-4 text-sm opacity-70">
  確認只有 README.md 被修改
</div>

  </div>

  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">提交並推送</div>

```bash
git add README.md
git commit -m "docs: improve README"
git push -u origin docs/readme-update
```

<div class="mt-4 text-sm opacity-70">
  <code>-u</code>把本地分支和遠端分支綁定，之後就可只<code>git push</code> 
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
layout: two-cols-header
---

# 小示範：用 VSCode 側欄 AI 做一個簡單貪吃蛇

<div class="text-sm opacity-75 mt-1">
目標：與 AI 協作，開發專案
</div>

<div class="grid grid-cols-2 gap-4 mt-4">

  <div class="p-5 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-2">在 VSCode 側欄 AI 下指令</div>
    <ol class="space-y-1 text-sm list-decimal pl-6">
      <li>在 VSCode 打開一個新資料夾（例如 <code>snake-demo</code>）</li>
      <li>建立檔案 <code>index.html</code></li>
      <li>打開側欄 AI（Copilot Chat / Gemini / ChatGPT 擴充都可）</li>
      <li>貼上下面這段需求，請 AI 直接產生程式碼</li>
    </ol>
    <pre class="mt-1 text-sm p-4 leading-6 rounded-xl bg-black/30 border border-white/10 whitespace-pre-wrap"><code>請幫我做一個最小可玩的貪吃蛇遊戲：
- 一個 20x20 格子的 canvas 或方格
- 方向鍵控制移動
- 蛇吃到食物會變長 +1
- 撞牆或自己就 Game Over，顯示分數並可按 R 重來
- 我直接用瀏覽器打開就能玩
- 建立README說明如何操作</code></pre>
  </div>

  <div class="p-5 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold mb-4">實際運行 + 小幅修正</div>
    <ul class="space-y-1 text-sm">
      <li>把 AI 產生的內容存檔</li>
      <li>用瀏覽器開啟</li>
      <li>按方向鍵開始玩，確認遊戲功能齊全</li>
      <li>如果速度太快或太慢：嘗試與 AI 溝同闡明需求</li>
      <li>如果產生bug：嘗試與 AI 溝同解決</li>
    </ul>
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
    <div class="mt-2 text-sm font-semibold opacity-90">功能</div>
    <ul class="mt-2 text-base opacity-90">
      <li>影像 → 灰階 → 點陣映射</li>
      <li>輸入圖就能顯示文字</li>
      <li>適合做小功能擴充：尺寸、對比、字元密度</li>
    </ul>
    <div class="mt-2 text-sm font-semibold opacity-90">Repo</div>
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
    <div class="mt-2 text-sm font-semibold opacity-90">功能</div>
    <ul class="mt-2 text-base opacity-90">
      <li>桌面 App 的 UI/動畫與渲染</li>
      <li>偏完整產品：設定、體驗、工程結構</li>
      <li>適合觀察如何拆模組、如何做可擴充功能</li>
    </ul>
    <div class="mt-2 text-sm font-semibold opacity-90">Repo</div>
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
    <div class="mt-2 text-sm font-semibold opacity-90">功能</div>
    <ul class="mt-2 text-base opacity-90">
      <li>前端大型專案結構（UI/狀態/資料）</li>
      <li>協作功能：即時同步、分享流程</li>
      <li>適合理解如何把產品做成可維護的工程</li>
    </ul>
    <div class="mt-2 text-sm font-semibold opacity-90">Repo</div>
    <div class="mt-2 text-sm">
      <a class="underline underline-offset-4" href="https://github.com/excalidraw/excalidraw" target="_blank" rel="noopener">
        excalidraw/excalidraw
      </a>
    </div>
  </div>

</div>

---
layout: default
---

# 有趣的 GitHub 專案（靈感牆）

<div class="text-sm opacity-75 mt-1">
GitHub上有許多開源的專案，社群中創作者已經發表了許多好用的工具，可以多多探索！
</div>

<div class="grid grid-cols-3 gap-3 mt-4">

  <!-- 1) invofe -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold">invofe</div>
    <div class="text-sm opacity-75 mt-1">
      Windows 終端機檔案總管（Terminal-based File Explorer）
    </div>
    <div class="mt-2 text-sm font-semibold opacity-90">專案亮點</div>
    <ul class="mt-2 text-base opacity-90">
      <li>從零打造工具型專案</li>
      <li>具完整 build / run 流程，接近真實工程專案</li>
      <li>仍在開發中，可持續擴充新功能</li>
    </ul>
    <div class="mt-2 text-sm font-semibold opacity-90">Repo</div>
    <div class="mt-2 text-sm">
      <a class="underline underline-offset-4"
        href="https://github.com/casperchen1/invofe"
        target="_blank" rel="noopener">
        casperchen1/invofe
      </a>
    </div>
  </div>


  <!-- 2) you-get -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold">you-get</div>
    <div class="text-sm opacity-75 mt-1">命令列下載器：</div>
<div class="text-sm opacity-75 mt-1">抓影音/音訊/圖片等媒體
    </div>
    <div class="mt-2 text-sm font-semibold opacity-90">功能</div>
    <ul class="mt-2 text-base opacity-90">
      <li>CLI 工具：參數設計、使用說明、錯誤處理</li>
      <li>解析網站內容：把網頁「抽」出可下載的資源</li>
      <li>適合看：如何把工具做成可發佈套件</li>
    </ul>
    <div class="mt-2 text-sm font-semibold opacity-90">Repo</div>
    <div class="mt-2 text-sm">
      <a class="underline underline-offset-4" href="https://github.com/soimort/you-get" target="_blank" rel="noopener">
        soimort/you-get
      </a>
    </div>
  </div>

  <!-- 3) Kazumi -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold">Kazumi</div>
    <div class="text-sm opacity-75 mt-1">Flutter：</div><div class="text-sm opacity-75 mt-1">自訂規則採集番劇 + 線上觀看</div>
    <div class="mt-2 text-sm font-semibold opacity-90">功能</div>
    <ul class="mt-2 text-base opacity-90">
      <li>規則系統：用 Xpath 選擇器快速做資料來源</li>
      <li>跨平台：Android/Windows/ macOS/Linux/iOS</li>
      <li>影像處理：支援 Anime4K 即時超解析</li>
    </ul>
    <div class="mt-2 text-sm font-semibold opacity-90">Repo</div>
    <div class="mt-2 text-sm">
      <a class="underline underline-offset-4" href="https://github.com/Predidit/Kazumi" target="_blank" rel="noopener">
        Predidit/Kazumi
      </a>
    </div>
  </div>

</div>

---
layout: default
---

# 有趣的 GitHub 專案（靈感牆）

<div class="text-sm opacity-75 mt-1">
建議看點：README 的「如何安裝 / 如何用」寫得好不好？貢獻者怎麼協作？版本怎麼控？
</div>

<div class="grid grid-cols-3 gap-3 mt-4">

  <!-- 1) stable-diffusion-webui -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold">stable-diffusion-webui</div>
    <div class="text-sm opacity-75 mt-1">用 Gradio 打包的 Stable Diffusion Web 介面</div>
    <div class="mt-2 text-sm font-semibold opacity-90">功能</div>
    <ul class="mt-2 text-base opacity-90">
      <li>模型產品化：把 AI 模型做成一般人可用的工具</li>
      <li>高度擴充：外掛、腳本、模型管理</li>
      <li>工程觀察：設定檔、啟動流程、社群維護</li>
    </ul>
    <div class="mt-2 text-sm font-semibold opacity-90">Repo</div>
    <div class="mt-2 text-sm">
      <a class="underline underline-offset-4"
         href="https://github.com/AUTOMATIC1111/stable-diffusion-webui"
         target="_blank" rel="noopener">
        AUTOMATIC1111/stable-diffusion-webui
      </a>
    </div>
  </div>

  <!-- 2) gemini-cli -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold">gemini-cli</div>
    <div class="text-sm opacity-75 mt-1">在終端機中使用 Gemini 的開源 AI CLI</div>
    <div class="mt-2 text-sm font-semibold opacity-90">功能</div>
    <ul class="mt-2 text-base opacity-90">
      <li>CLI UX：指令設計、互動流程、錯誤提示</li>
      <li>Agent 思維：工具串接、工作流程設計</li>
      <li>專案文件：新手 onboarding 寫法</li>
    </ul>
    <div class="mt-2 text-sm font-semibold opacity-90">Repo</div>
    <div class="mt-2 text-sm">
      <a class="underline underline-offset-4"
         href="https://github.com/google-gemini/gemini-cli"
         target="_blank" rel="noopener">
        google-gemini/gemini-cli
      </a>
    </div>
  </div>

  <!-- 3) so-vits-svc -->
  <div class="p-7 rounded-2xl bg-white/5 border border-white/10">
    <div class="text-xl font-semibold">so-vits-svc</div>
    <div class="text-sm opacity-75 mt-1">SVC：歌聲 / 音色轉換系統（非單純 TTS）</div>
    <div class="mt-2 text-sm font-semibold opacity-90">功能</div>
    <ul class="mt-2 text-base opacity-90">
      <li>深度學習應用：聲音模型訓練與推論</li>
      <li>工程現實面：資料集、效能、品質控管</li>
      <li>適合觀察：研究到產品的專案結構</li>
    </ul>
    <div class="mt-2 text-sm font-semibold opacity-90">Repo</div>
    <div class="mt-2 text-sm">
      <a class="underline underline-offset-4"
         href="https://github.com/svc-develop-team/so-vits-svc"
         target="_blank" rel="noopener">
        svc-develop-team/so-vits-svc
      </a>
    </div>
  </div>

</div>

---
layout: default
---

# 5 小時競賽規則
<div class="text-sm opacity-75">
  個人專案為主（可協作，但需明確分工與分支規範）。
</div>

<script setup>
import { ref } from 'vue'

const showTeamModal = ref(false)

const rules = [
  "總時長 5 小時，開放無限制使用 AI 工具",
  "以個人開發為主（開放協作，但必須符合協作規則）",
  "每人需建立 GitHub Repo，繳交時提供 Repo 連結",
  "README.md 為必要文件（專案說明 / 功能）",
  "需使用 Git 進行版本管理（commit 紀錄視為成果的一部分）",
  "加分項：若使用 TDX API + 專案範例後端可額外加分（加分不多）",
]

const deliverables = [
  { title: "可運作 Demo", desc: "能跑的原型：功能少也可以，但要可操作、可展示流程。" },
  { title: "半成品 + 說明 / 計畫", desc: "核心功能完成一部分，附上限制、目前進度與下一步規劃。" },
  { title: "Repo + README", desc: "必須提供 Repo 連結，並確保 README 讓評審能快速理解與操作。" },
]

const teamChecklist = [
  "協作限制：允許協作，但必須有明確分工",
  "分支規範：組內每人至少一個分支（不要全部在 main）",
  "合併方式：以 PR 方式合併回 main",
  "提交方式：繳交 Repo 連結時，請確認 main 分支能正常執行 / 展示",
]
</script>

<div class="h-full w-full py-4">
  <div class="grid grid-cols-2 gap-4">
    <!-- Left -->
    <div class="space-y-2">
      <div class="rounded-2xl border border-white/10 bg-white/5 p-5">
        <div class="text-xl font-semibold mb-2">基本規則</div>
        <li v-for="(r, i) in rules" :key="i" class="flex gap-2">
          <span class="opacity-70">-</span>
          <span class="text-[15px] leading-8">{{ r }}</span>
        </li>
      </div>
      <div class="mt-2 pt-2 border-t border-white/10 flex items-center gap-4">
        <button
          class="px-12 py-4 rounded-xl border border-white/20 bg-black/30 hover:bg-white/10 transition font-semibold whitespace-nowrap"
          @click="showTeamModal = true"
        >多人組隊協作規則</button>
        <div class="text-xs opacity-70 leading-5">
          若要多人協作，請務必遵守分支與分工規範
        </div>
      </div>
    </div>
    <!-- Right -->
    <div class="space-y-4">
      <div class="rounded-2xl border border-white/10 bg-white/5 p-5">
        <div class="text-xl font-semibold mb-3">提交成果（擇一即可）</div>
        <div class="space-y-3">
          <div
            v-for="(d, i) in deliverables"
            :key="i"
            class="rounded-xl border border-white/10 bg-black/20 p-4"
          >
            <div class="font-semibold">{{ d.title }}</div>
            <div class="text-[14px] opacity-80 mt-1 leading-5">{{ d.desc }}</div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Modal 遮罩 -->
  <div
    v-if="showTeamModal"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm"
    @click.self="showTeamModal = false"
  >
    <!-- Modal 本體 -->
    <div class="w-[720px] max-w-[92vw] rounded-3xl border border-white/15 bg-[#0f0f0f] p-8 shadow-2xl">
      <div class="flex items-start justify-between mb-4">
        <div class="text-2xl font-bold">多人組隊協作規則</div>
        <button class="text-white/60 hover:text-white text-xl" @click="showTeamModal = false">✕</button>
      </div>
      <ul class="space-y-3">
        <li v-for="(p, i) in teamChecklist" :key="i" class="flex gap-3 items-start">
          <span class="mt-1 text-white/40">-</span>
          <span class="text-[16px] leading-10">{{ p }}</span>
        </li>
      </ul>
      <div class="mt-6 flex items-center justify-between">
      </div>
    </div>
  </div>
</div>

---
layout: default
---

<script setup>
import { reactive, ref } from 'vue'

const showBonus = ref(false)

const criteria = [
  "有在時限內完成交付（ repo 連結）",
  "主題清楚（你做了什麼？）",
  "完成基本功能（至少做出一個可用功能）",
  "可操作 Demo（能運行、能操作、能展示）",
  "Git 使用正確（有意義的 commit 訊息）",
  "分支使用（至少一個分支以上）",
  "Repo 連結可打開、 main 可跑",
  "介面/輸出清楚（畫面或輸出能夠被理解）",
  "README 清楚（如何使用 / 功能介紹）",
  "展示說明完整（限制 + 下一步規劃）",
]

const mark = reactive(Array(criteria.length).fill(0))

function toggle(i) {
  mark[i] = (mark[i] + 1) % 2
}

function symbol(i) {
  return mark[i] === 1 ? '☒' : '☐'
}

function pillClass(i) {
  return mark[i] === 1
    ? 'bg-green-500/15 border-green-400/30'
    : 'bg-black/20 border-white/15'
}
</script>

<div class="h-full w-full flex flex-col py-4">
  <div class="grid grid-cols-2 gap-4">
    <!-- Left: 評分項目 -->
    <div class="rounded-3xl border border-white/10 bg-white/5 p-5">
      <div class="flex items-center justify-between mb-2">
        <div class="text-2xl font-semibold">評分標準（10 項，每項 1 分）</div>
      </div>
      <div class="flex flex-wrap gap-1">
        <span
          v-for="(c, i) in criteria"
          :key="i"
          class="px-3 py-1 rounded-full border border-white/15 bg-black/20 text-[12px]"
        >
          {{ i + 1 }}. {{ c }}
        </span>
      </div>
      <div class="mt-1">
        <button
          class="px-3 py-1 rounded-xl border border-white/20 bg-black/30 hover:bg-white/10 transition text-sm font-semibold whitespace-nowrap"
          @click="showBonus = true"
          type="button"
        >
          Bonus 加分（點擊查看）
        </button>
      </div>
      <div class="mt-1 text-sm opacity-75 leading-5">
        重點：你是否能透過與 AI 的協作，理解一個專案如何從「想法」到「可運作成果」，包含問題定義、功能取捨，以及如何在有限時間內令專案「可理解、可展示、可追蹤」。
      </div>
    </div>
    <div class="rounded-3xl border border-white/10 bg-white/5 p-5">
      <div class="text-2xl font-semibold mb-3">自我檢核表</div>

<ul class="grid grid-cols-2 gap-2">
  <div v-for="(t, i) in criteria" :key="i">
    <button
      class="w-full text-left flex items-start gap-2 rounded-xl border px-3 py-2 hover:bg-white/5 transition"
      :class="pillClass(i)"
      @click="toggle(i)"
      type="button"
    >
      <span class="mt-0.5 text-base w-6 text-center select-none">
        {{ symbol(i) }}
      </span>
      <span class="text-[13px] leading-6 opacity-90">
        <span class="opacity-70">{{ i + 1 }}.</span> {{ t }}
      </span>
    </button>
  </div>
</ul>
    </div>
  </div>

  <div
    v-if="showBonus"
    class="fixed inset-0 z-50 flex items-center justify-center bg-black/70 backdrop-blur-sm"
    @click.self="showBonus = false"
  >
    <div class="w-[720px] max-w-[92vw] rounded-3xl border border-white/15 bg-[#0f0f0f] p-8 shadow-2xl">
      <div class="flex items-start justify-between mb-3">
        <div class="text-2xl font-bold">Bonus</div>
        <button class="text-white/60 hover:text-white text-xl" @click="showBonus = false" type="button">✕</button>
      </div>
      <div class="text-[16px] opacity-90 leading-8">
        若你是 <span class="font-semibold">fork 我原本的 TDX_BUS_DEMO 範例專案</span> 後繼續開發（並保留開發紀錄），可獲得額外加分。
        <div class="text-sm opacity-70 mt-3">
          建議：保留 fork 關係、在你自己的 repo 上 commit，並在 README 寫明你新增 / 修改了哪些功能。
        </div>
      </div>
      <div class="mt-6 flex items-center justify-end">
      </div>
    </div>
  </div>

</div>

---
layout: default
---

<div class="text-center">

# 成果上傳區
</div>

<SubmitRepo />
