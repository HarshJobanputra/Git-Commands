# Git Commands Reference Guide

## Table of Contents
- [Repository Setup](#repository-setup)
- [Basic Commands](#basic-commands)
- [Branching and Merging](#branching-and-merging)
- [Remote Repositories](#remote-repositories)
- [Staging and Committing](#staging-and-committing)
- [History and Logs](#history-and-logs)
- [Undoing Changes](#undoing-changes)
- [Stashing](#stashing)
- [Tagging](#tagging)
- [Configuration](#configuration)
- [Advanced Commands](#advanced-commands)

## Repository Setup

| Command | Description | Example |
|---------|-------------|---------|
| `git init` | Initialize a new Git repository | `git init` |
| `git init <directory>` | Initialize repository in specific directory | `git init my-project` |
| `git clone <url>` | Clone a repository from remote URL | `git clone https://github.com/user/repo.git` |
| `git clone <url> <directory>` | Clone repository to specific directory | `git clone https://github.com/user/repo.git my-folder` |

## Basic Commands

| Command | Description | Example |
|---------|-------------|---------|
| `git status` | Show working directory status | `git status` |
| `git add <file>` | Add file to staging area | `git add index.html` |
| `git add .` | Add all files to staging area | `git add .` |
| `git add -A` | Add all files including deleted ones | `git add -A` |
| `git commit -m "<message>"` | Commit staged changes with message | `git commit -m "Add new feature"` |
| `git commit -am "<message>"` | Add and commit in one command | `git commit -am "Fix bug"` |
| `git diff` | Show unstaged changes | `git diff` |
| `git diff --staged` | Show staged changes | `git diff --staged` |
| `git rm <file>` | Remove file from repository | `git rm old-file.txt` |
| `git mv <old> <new>` | Rename/move file | `git mv old-name.txt new-name.txt` |

## Branching and Merging

| Command | Description | Example |
|---------|-------------|---------|
| `git branch` | List all branches | `git branch` |
| `git branch <name>` | Create new branch | `git branch feature-branch` |
| `git branch -d <name>` | Delete branch | `git branch -d feature-branch` |
| `git branch -D <name>` | Force delete branch | `git branch -D feature-branch` |
| `git checkout <branch>` | Switch to branch | `git checkout main` |
| `git checkout -b <name>` | Create and switch to new branch | `git checkout -b new-feature` |
| `git switch <branch>` | Switch to branch (newer syntax) | `git switch main` |
| `git switch -c <name>` | Create and switch to new branch | `git switch -c new-feature` |
| `git merge <branch>` | Merge branch into current branch | `git merge feature-branch` |
| `git merge --no-ff <branch>` | Merge with no fast-forward | `git merge --no-ff feature-branch` |
| `git rebase <branch>` | Rebase current branch onto another | `git rebase main` |
| `git rebase -i <commit>` | Interactive rebase | `git rebase -i HEAD~3` |

## Remote Repositories

| Command | Description | Example |
|---------|-------------|---------|
| `git remote` | List remote repositories | `git remote` |
| `git remote -v` | List remotes with URLs | `git remote -v` |
| `git remote add <name> <url>` | Add remote repository | `git remote add origin https://github.com/user/repo.git` |
| `git remote remove <name>` | Remove remote repository | `git remote remove origin` |
| `git fetch` | Fetch changes from remote | `git fetch` |
| `git fetch <remote>` | Fetch from specific remote | `git fetch origin` |
| `git pull` | Fetch and merge from remote | `git pull` |
| `git pull <remote> <branch>` | Pull from specific remote/branch | `git pull origin main` |
| `git push` | Push changes to remote | `git push` |
| `git push <remote> <branch>` | Push to specific remote/branch | `git push origin main` |
| `git push -u <remote> <branch>` | Push and set upstream | `git push -u origin main` |
| `git push --force` | Force push (dangerous) | `git push --force` |
| `git push --force-with-lease` | Safer force push | `git push --force-with-lease` |

## Staging and Committing

| Command | Description | Example |
|---------|-------------|---------|
| `git add -p` | Interactively stage changes | `git add -p` |
| `git reset <file>` | Unstage file | `git reset index.html` |
| `git reset` | Unstage all files | `git reset` |
| `git commit --amend` | Amend last commit | `git commit --amend` |
| `git commit --amend -m "<message>"` | Amend last commit with new message | `git commit --amend -m "Updated message"` |
| `git commit --no-edit` | Commit without opening editor | `git commit --no-edit` |

## History and Logs

| Command | Description | Example |
|---------|-------------|---------|
| `git log` | Show commit history | `git log` |
| `git log --oneline` | Show condensed log | `git log --oneline` |
| `git log --graph` | Show log with graph | `git log --graph` |
| `git log --all --graph --oneline` | Show all branches in graph | `git log --all --graph --oneline` |
| `git log -n <number>` | Show last n commits | `git log -n 5` |
| `git log --since="<date>"` | Show commits since date | `git log --since="2023-01-01"` |
| `git log --author="<name>"` | Show commits by author | `git log --author="John Doe"` |
| `git show <commit>` | Show commit details | `git show abc123` |
| `git blame <file>` | Show who changed each line | `git blame index.html` |
| `git shortlog` | Show commit summary by author | `git shortlog` |

## Undoing Changes

| Command | Description | Example |
|---------|-------------|---------|
| `git checkout -- <file>` | Discard changes in working directory | `git checkout -- index.html` |
| `git restore <file>` | Restore file (newer syntax) | `git restore index.html` |
| `git restore --staged <file>` | Unstage file | `git restore --staged index.html` |
| `git reset --soft <commit>` | Reset to commit, keep changes staged | `git reset --soft HEAD~1` |
| `git reset --mixed <commit>` | Reset to commit, unstage changes | `git reset --mixed HEAD~1` |
| `git reset --hard <commit>` | Reset to commit, discard all changes | `git reset --hard HEAD~1` |
| `git revert <commit>` | Create new commit that undoes changes | `git revert abc123` |
| `git clean -f` | Remove untracked files | `git clean -f` |
| `git clean -fd` | Remove untracked files and directories | `git clean -fd` |

## Stashing

| Command | Description | Example |
|---------|-------------|---------|
| `git stash` | Stash current changes | `git stash` |
| `git stash save "<message>"` | Stash with message | `git stash save "Work in progress"` |
| `git stash list` | List all stashes | `git stash list` |
| `git stash show` | Show stash contents | `git stash show` |
| `git stash apply` | Apply most recent stash | `git stash apply` |
| `git stash apply stash@{n}` | Apply specific stash | `git stash apply stash@{2}` |
| `git stash pop` | Apply and remove most recent stash | `git stash pop` |
| `git stash drop` | Delete most recent stash | `git stash drop` |
| `git stash clear` | Delete all stashes | `git stash clear` |

## Tagging

| Command | Description | Example |
|---------|-------------|---------|
| `git tag` | List all tags | `git tag` |
| `git tag <name>` | Create lightweight tag | `git tag v1.0` |
| `git tag -a <name> -m "<message>"` | Create annotated tag | `git tag -a v1.0 -m "Version 1.0"` |
| `git tag -d <name>` | Delete tag | `git tag -d v1.0` |
| `git push origin <tag>` | Push tag to remote | `git push origin v1.0` |
| `git push origin --tags` | Push all tags to remote | `git push origin --tags` |
| `git show <tag>` | Show tag information | `git show v1.0` |

## Configuration

| Command | Description | Example |
|---------|-------------|---------|
| `git config --global user.name "<name>"` | Set global username | `git config --global user.name "John Doe"` |
| `git config --global user.email "<email>"` | Set global email | `git config --global user.email "john@example.com"` |
| `git config --list` | Show all configuration | `git config --list` |
| `git config user.name` | Show username | `git config user.name` |
| `git config --global init.defaultBranch main` | Set default branch name | `git config --global init.defaultBranch main` |
| `git config --global core.editor "<editor>"` | Set default editor | `git config --global core.editor "code --wait"` |
| `git config --global alias.<alias> "<command>"` | Create command alias | `git config --global alias.st status` |

## Advanced Commands

| Command | Description | Example |
|---------|-------------|---------|
| `git cherry-pick <commit>` | Apply specific commit to current branch | `git cherry-pick abc123` |
| `git bisect start` | Start binary search for bug | `git bisect start` |
| `git bisect good <commit>` | Mark commit as good | `git bisect good abc123` |
| `git bisect bad <commit>` | Mark commit as bad | `git bisect bad def456` |
| `git reflog` | Show reference log | `git reflog` |
| `git fsck` | Check repository integrity | `git fsck` |
| `git gc` | Garbage collect unreferenced objects | `git gc` |
| `git archive --format=zip HEAD > archive.zip` | Create archive of repository | `git archive --format=zip HEAD > project.zip` |
| `git submodule add <url> <path>` | Add submodule | `git submodule add https://github.com/user/lib.git lib` |
| `git submodule update --init` | Initialize and update submodules | `git submodule update --init` |
| `git worktree add <path> <branch>` | Create new worktree | `git worktree add ../feature feature-branch` |
| `git grep "<pattern>"` | Search for pattern in repository | `git grep "TODO"` |

## Useful Combinations

| Command | Description | Example |
|---------|-------------|---------|
| `git log --oneline --graph --all` | Visual branch history | `git log --oneline --graph --all` |
| `git commit -am "<message>"` | Stage all and commit | `git commit -am "Quick fix"` |
| `git push -u origin HEAD` | Push current branch and set upstream | `git push -u origin HEAD` |
| `git reset --hard origin/main` | Reset to match remote main | `git reset --hard origin/main` |
| `git branch -vv` | Show branch tracking information | `git branch -vv` |
| `git log --stat` | Show commit history with file changes | `git log --stat` |

## Emergency Commands

| Command | Description | Example |
|---------|-------------|---------|
| `git reflog` | Find lost commits | `git reflog` |
| `git reset --hard HEAD@{1}` | Undo last reset using reflog | `git reset --hard HEAD@{1}` |
| `git fsck --lost-found` | Find dangling commits | `git fsck --lost-found` |
| `git stash` | Quickly save work in progress | `git stash` |
| `git checkout -` | Switch to previous branch | `git checkout -` |

---

*This reference guide covers the most commonly used Git commands. For more detailed information, use `git help <command>` or visit the official Git documentation.*