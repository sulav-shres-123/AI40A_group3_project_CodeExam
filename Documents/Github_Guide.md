# CodeExam: GitHub Guide for the Team

**For:** every CodeExam team member, including anyone who has never used Git.
**Repository:** https://github.com/sulav-shres-123/AI40A_group3_project_CodeExam
**User stories (Google Sheet):** https://docs.google.com/spreadsheets/d/1tfZ5bA3O4vtW1Jed4QUYUkUNgUzSBHn_/edit?usp=sharing&ouid=114220969951788972793&rtpof=true&sd=true
**Task tracking (Trello):** *(board link to be added)*

Work through Parts 1–4 **once**. After that, Part 5 is what you do every day.

---

## Contents

1. [Install what you need](#part-1-install-what-you-need)
2. [Get access to the repository](#part-2-get-access-to-the-repository)
3. [Set up Git on your computer (once)](#part-3-set-up-git-on-your-computer-once)
4. [Clone the repository](#part-4-clone-the-repository)
5. [Daily workflow: from task to merged pull request](#part-5-daily-workflow)
6. [Pull requests and code review](#part-6-pull-requests-and-code-review)
7. [Keeping your branch up to date and fixing conflicts](#part-7-keeping-your-branch-up-to-date-and-fixing-conflicts)
8. [Fixing common mistakes](#part-8-fixing-common-mistakes)
9. [Team rules](#part-9-team-rules)
10. [Troubleshooting](#part-10-troubleshooting)
11. [Command cheat sheet](#part-11-command-cheat-sheet)
12. [Words you will hear](#part-12-words-you-will-hear)

---

## Part 1: Install what you need

| Tool | Why | Get it |
| --- | --- | --- |
| **A GitHub account** | To be added to the repo and open pull requests | https://github.com/signup |
| **Git** | Version control on your computer | **Windows:** https://git-scm.com/download/win (keep the default options; this also installs *Git Credential Manager*, which handles sign-in). **Mac:** run `xcode-select --install` in Terminal, or `brew install git` |
| **VS Code** | Editor with built-in Git support | https://code.visualstudio.com/ |
| VS Code extensions (recommended) | GitLens (who changed what), GitHub Pull Requests (review in the editor), Python | Extensions panel (Ctrl+Shift+X) |

**Check Git is installed.** Open a terminal (Windows: *PowerShell* or the VS Code terminal with Ctrl+\`; Mac: *Terminal*) and run:
```bash
git --version
```
You should see something like `git version 2.x`. If you get "not recognized", restart your computer and try again.

---

## Part 2: Get access to the repository

The repository is **public**, so anyone can *view* and *clone* it. **To push your work you must be a collaborator.**

1. **Send your GitHub username** (not your email) to Sulav, the repository owner, in the team chat.
2. Sulav adds you: *repo → Settings → Collaborators → Add people*.
3. **Accept the invitation.** It expires after 7 days. Accept it from either:
   - the email GitHub sends you, or
   - https://github.com/sulav-shres-123/AI40A_group3_project_CodeExam/invitations, or
   - https://github.com/notifications
4. **Check:** open the repo page. If you see the **Settings** tab, or can create a branch from the branch dropdown, you have access.

> ⚠ Because the repo is public, **anything you push can be seen by anyone.** Never push passwords, API keys or `.env` files.

---

## Part 3: Set up Git on your computer (once)

Run these in a terminal. Replace the name and email with yours.

```bash
# Who you are (shown on every commit)
git config --global user.name  "Your Full Name"
git config --global user.email "you@example.com"

# Sensible defaults
git config --global init.defaultBranch main
git config --global pull.rebase true      # cleaner history when you pull
git config --global fetch.prune true      # forget branches that were deleted on GitHub
```

**Line endings: pick ONE line for your computer:**
```bash
git config --global core.autocrlf true    # Windows
git config --global core.autocrlf input   # Mac / Linux
```

**Email privacy (recommended):** the repo is public, so your commit email is public too. To hide it, go to GitHub → *Settings → Emails*, tick **Keep my email addresses private**, copy the address that looks like `12345678+username@users.noreply.github.com`, and use it in `user.email` above.

**Check:**
```bash
git config --global --list
```

### How sign-in works

- **Windows:** the first time you `git push`, a browser window opens. Sign in to GitHub and click **Authorize**. Git Credential Manager remembers it.
- **Mac:** Git asks for a username and password. **GitHub does not accept your account password here.** Create a *Personal access token* (GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens, with access to this repository and **Contents: Read and write**), and paste the token as the password. The Mac keychain remembers it.
- **SSH keys** are optional. HTTPS (above) is enough for this project.

---

## Part 4: Clone the repository

"Cloning" downloads the repository and its full history, already connected to GitHub.

```bash
# 1. Go to the folder where you keep projects (example paths)
cd ~/Documents                       # Mac
cd $HOME\Documents                   # Windows PowerShell

# 2. Clone
git clone https://github.com/sulav-shres-123/AI40A_group3_project_CodeExam.git

# 3. Go into it and open it in VS Code
cd AI40A_group3_project_CodeExam
code .
```

**Alternative without the terminal:** VS Code → *Ctrl+Shift+P* → **Git: Clone** → paste the URL → choose a folder.

**Check it worked:**
```bash
git status          # "On branch main ... up to date with 'origin/main'"
git remote -v       # shows the GitHub URL twice (fetch and push)
```

### Where to start reading

| File / folder | Read it to… |
| --- | --- |
| `README.md` | Get an overview and folder guide |
| `plan.md` | See the goal, roles, sprint plan and team rules |
| `docs/requirements/required-apps.txt` | Check you've installed every app the project needs |
| `docs/proposal.pdf` | Read the project proposal and its requirements |
| `docs/DESIGN.md` | Understand *why* things are designed the way they are |

> **Only want the files, not Git?** On the GitHub page: **Code → Download ZIP**. You can't push from a ZIP, so developers should always clone.

---

## Part 5: Daily workflow

The golden rule: **never work directly on `main`.** Every task gets its own branch, and it reaches `main` only through a reviewed pull request.

### Step 1: Pick a task
Open the team's **Trello board** and choose a card in the current sprint that matches your role. Add yourself as a member of the card and move it to **In progress**. The story's acceptance criteria and Given/When/Then scenario are in the **Google Sheet** (search for its story ID, e.g. US1).

### Step 2: Get the latest `main`
```bash
git switch main
git pull
```

### Step 3: Create your branch
Name it after the story ID and a few words from the card title:
```bash
git switch -c feat/us1-teacher-registration-login
```
Branch name format: `type/usNN-short-description`

| Type | Use for |
| --- | --- |
| `feat/` | A new feature or story (`feat/us27-run-against-sample-tests`) |
| `fix/` | A bug fix (`fix/us24-deadline-timezone`) |
| `test/` | Only tests (`test/us10-hidden-tests-not-exposed`) |
| `docs/` | Documentation (`docs/api-routes`) |
| `chore/` | Setup or tooling (`chore/docker-compose`) |

### Step 4: Work and commit in small steps
```bash
git status                  # what changed?
git diff                    # see the exact changes
git add path/to/file.py     # stage specific files (or: git add -A for everything)
git commit -m "feat(auth): add teacher registration form"
```

**Commit message format:** `type(scope): what changed`, in the imperative ("add", not "added"):

| Example | Meaning |
| --- | --- |
| `feat(exams): add create exam form` | New feature in the exams area |
| `fix(sessions): reject saves after the deadline` | Bug fix |
| `test(grading): add partial credit unit tests` | Tests only |
| `docs(api): list exam routes` | Documentation |
| `chore(infra): add docker compose file` | Setup / tooling |

Scopes we use: `auth`, `exams`, `questions`, `sessions`, `grading`, `worker`, `infra`, `docs`, `backlog`.
Commit whenever one small piece works. Several small commits are better than one huge one.

### Step 5: Push your branch
```bash
git push -u origin feat/us1-teacher-registration-login     # first push of this branch
git push                                                    # every push after that
```
Push at least **once a day**, even if the work isn't finished. That way it's backed up and teammates can see progress.

### Step 6: Open a pull request (PR)
See Part 6.

### Step 7: After your PR is merged
```bash
git switch main
git pull
git branch -d feat/us1-teacher-registration-login    # delete your local copy of the branch
```
Then move your Trello card to **Done**.

---

## Part 6: Pull requests and code review

### Opening a PR
1. After pushing, open the repo on GitHub. A yellow banner says **"Compare & pull request"**. Click it.
   (Or: **Pull requests → New pull request** → base: `main`, compare: your branch.)
2. **Title:** the story and a summary, e.g. `US1: teacher registration and login`.
3. **Description:**
   - What you did and why
   - How to test it (steps a reviewer can follow)
   - Which acceptance criteria are done (copy them from the Google Sheet as a checklist)
   - A link to the Trello card. Also paste the PR link into the card and move the card to **In review**.
4. **Reviewers** (right side): pick the reviewer for your role (see `plan.md` section 6).
5. Click **Create pull request**.

Tip: if the work isn't ready yet, choose **Create draft pull request**. Teammates can see it, but it can't be merged.

### When you get review comments
Make the changes on the **same branch**, then commit and push again. The PR updates automatically:
```bash
git add -A
git commit -m "fix(auth): use generic login error message"
git push
```
Reply to each comment ("Done", or why you disagree), then click **Re-request review**.

### Merging
Once it's approved: **Squash and merge** → **Confirm** → **Delete branch**. Then do Step 7 above.

### Reviewing a teammate's PR
1. Open the PR → **Files changed** tab.
2. Click the **+** next to a line to comment. Be specific and kind ("This returns hidden tests to students. Can we filter `is_hidden`?").
3. To run their code locally:
   ```bash
   git fetch
   git switch feat/us5-add-question       # their branch name
   ```
   When you're done: `git switch main`.
4. **Review changes** → choose **Comment**, **Approve** or **Request changes**.
5. Try to review within **24 hours**. A waiting PR blocks a teammate.

**What to check:** the acceptance criteria are met · tests exist and pass · no passwords or `.env` · hidden tests never reach students · the code is readable.

---

## Part 7: Keeping your branch up to date and fixing conflicts

If `main` changed while you were working, bring those changes into your branch **before** opening the PR, or whenever GitHub says "This branch is out-of-date":

```bash
git switch your-branch-name
git fetch origin
git rebase origin/main
```

### If there's a conflict
Git stops and lists the conflicting files. Inside a conflicting file you'll see:
```
<<<<<<< HEAD
the version from main
=======
your version
>>>>>>> your commit
```
1. Open the file in VS Code. Click **Accept Current**, **Accept Incoming** or **Accept Both**, or open the **Merge Editor** and edit by hand. Make sure all the `<<<<<<<`, `=======` and `>>>>>>>` lines are gone.
2. Mark it fixed and continue:
   ```bash
   git add path/to/file
   git rebase --continue
   ```
3. Repeat until the rebase finishes, then run the app and tests to check everything still works.
4. Push. A rebase rewrites your branch, so you need:
   ```bash
   git push --force-with-lease
   ```
   ⚠ Only ever force-push **your own feature branch**, never `main`.

**Panic button:** `git rebase --abort` puts everything back to how it was before you started the rebase.

**Avoid conflicts in the first place:** pull `main` every morning, keep branches small (≤ 3 days), and tell the team before you edit shared files (`base.html`, models, migrations).

---

## Part 8: Fixing common mistakes

| Situation | What to run |
| --- | --- |
| I staged a file by mistake | `git restore --staged file` |
| I want to throw away my uncommitted changes to a file | `git restore file` ⚠ the changes are lost |
| I need to switch branches but I'm not ready to commit | `git stash`, then later `git stash pop` |
| Wrong message on my last commit (**not pushed yet**) | `git commit --amend -m "new message"` |
| I forgot a file in my last commit (**not pushed yet**) | `git add file` then `git commit --amend --no-edit` |
| I committed on `main` by mistake (**not pushed**) | `git branch feat/my-work` → `git reset --hard origin/main` → `git switch feat/my-work`. Your commits are now on the new branch. |
| I need to undo a commit that's already pushed | `git revert <commit-id>` (adds a new commit that undoes it, which is safe for shared branches) |
| I committed a password or `.env` file | **Tell the team immediately.** Change the password or key first. Deleting the file in a new commit is not enough, because it stays in the history. |
| I'm lost and want to see what happened | `git log --oneline --graph -15` and `git status` |

---

## Part 9: Team rules

1. **Never push to `main`.** Use a branch and a pull request, every time.
2. **One story or task per branch,** named after the backlog story (`feat/usNN-...`).
3. **Pull `main` before you start work** each day.
4. **Small commits, clear messages** in the `type(scope): summary` format.
5. **Every PR needs 1 approval** from someone other than the author before merging.
6. **Never commit secrets:** `.env`, passwords, API keys. The `.gitignore` blocks `.env`, so don't work around it.
7. **Only one person changes the database schema at a time.** One migration per PR, and pull before creating it.
8. **Keep your Trello card current:** move it the same day you start, open a PR, or finish.
9. **Push daily,** even unfinished work, on your branch.
10. **Ask early.** If you're stuck for more than an hour, post in the team chat.

---

## Part 10: Troubleshooting

| Message | Meaning and fix |
| --- | --- |
| `remote: Permission to ... denied` / `403` | You aren't a collaborator yet, or haven't accepted the invite. See Part 2. |
| `Updates were rejected because the remote contains work that you do not have` | Someone pushed first. Run `git pull` (or `git rebase origin/main` on your branch), then push again. |
| `fatal: not a git repository` | You're in the wrong folder. `cd` into `AI40A_group3_project_CodeExam`. |
| `Your branch is behind 'origin/main'` | Run `git pull`. |
| `Support for password authentication was removed` | Use the browser sign-in (Windows) or a personal access token (Mac). See Part 3. |
| `LF will be replaced by CRLF` | A harmless line-ending notice. The repo's `.gitattributes` handles it. |
| `error: pathspec 'xyz' did not match` | Check the branch or file name: `git branch -a` lists all branches. |
| Push to `main` rejected (`protected branch`) | Working as intended. Create a branch and open a PR. |
| VS Code shows hundreds of changed files | You may have opened the wrong folder (for example your whole user folder). Open the `AI40A_group3_project_CodeExam` folder itself. |

---

## Part 11: Command cheat sheet

| I want to… | Command |
| --- | --- |
| Download the repo (first time) | `git clone https://github.com/sulav-shres-123/AI40A_group3_project_CodeExam.git` |
| See what's changed | `git status` |
| See the exact line changes | `git diff` |
| Get the latest `main` | `git switch main` then `git pull` |
| Create a branch and switch to it | `git switch -c feat/usNN-description` |
| Switch to an existing branch | `git switch branch-name` |
| List branches | `git branch` (local) · `git branch -a` (all) |
| Stage changes | `git add file` · `git add -A` (everything) |
| Commit | `git commit -m "type(scope): summary"` |
| Push a new branch | `git push -u origin branch-name` |
| Push again | `git push` |
| Update my branch with `main` | `git fetch origin` then `git rebase origin/main` |
| See history | `git log --oneline --graph -20` |
| Who changed this line? | `git blame file` (or GitLens in VS Code) |
| Park unfinished work | `git stash` · bring it back: `git stash pop` |
| Delete a merged local branch | `git branch -d branch-name` |

---

## Part 12: Words you will hear

| Word | Meaning |
| --- | --- |
| **Repository (repo)** | The project folder plus its full history |
| **Clone** | Your own full copy of the repo, connected to GitHub |
| **Commit** | A saved snapshot of changes, with a message |
| **Branch** | A separate line of work, so you don't disturb `main` |
| **`main`** | The shared, always-working version of the project |
| **Push / Pull** | Send your commits to GitHub / get others' commits from GitHub |
| **Pull request (PR)** | A request to merge your branch into `main`, where teammates review it |
| **Merge / Squash** | Combine a branch into `main`. "Squash" turns all its commits into one tidy commit. |
| **Conflict** | Two people changed the same lines, so Git needs you to choose |
| **Rebase** | Replay your commits on top of the latest `main` |
| **Origin** | The name for the GitHub copy of the repo |
| **Collaborator** | A person with permission to push to the repo |
| **Story (USNN)** | One user story from the backlog, e.g. US1 = teacher registration and login |

---

*Questions about this guide: ask in the team chat. Questions about **what** to build: see `plan.md` in the repo, the Google Sheet (user stories) and the Trello board (tasks).*
