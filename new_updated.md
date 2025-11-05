# Git Commands

## A list of Git commands

### Tell Git who you are

| Description                           | Command                                          |
| ------------------------------------- | ------------------------------------------------ |
| Configure the author name.            | git config --global user.name "`<username>`"     |
| Configure the author's email address. | git config --global user.email `<email address>` |

### Getting & Creating Projects

| Description                                                           | Command                                                                                                |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Initialize a local Git repository                                     | git init                                                                                               |
| Create a local copy of a remote repository                            | git clone ssh://git@github.com/`<username>`/`<repository-name>`.git                                    |
| To clone a specific Git branch                                        | git clone --branch `<branch-name>` `<repository-url>`orgit clone -b `<branch-name>` `<repository-url>` |
| If you only want that branch and not the full history of all branches | git clone -b develop --single-branch https://github.com/username/repo.git                              |

### Basic Snapshotting

| Description                                       | Command                            |
| ------------------------------------------------- | ---------------------------------- |
| Check status                                      | git status                         |
| Add a file to the staging area                    | git add <file-name.txt>            |
| Add all new and changed files to the staging area | git add -Aorgit add .              |
| Commit changes                                    | git commit -m "`<commit message>`" |
| Remove a file (or folder)                         | git rm -r <file-name.txt>          |

### Inspection & Comparison

| Description                        | Command                                                             |
| ---------------------------------- | ------------------------------------------------------------------- |
| View changes                       | git log                                                             |
| View changes (detailed)            | git log --summary                                                   |
| View changes in one line (briefly) | git log --onelineorgit log --pretty=onelineorgit log --pretty=short |

### Undo to previous file

| Description                                                 | Command                        |
| ----------------------------------------------------------- | ------------------------------ |
| List of all commit with commit id and commit message)       | git log --oneline              |
| Return to previous commit                                   | git checkout `<commit id>`     |
| Revert commit(undo one particular commit)                   | git revert `<commit id>`       |
| Reset to previous commit(remove history of all commit after | git reset --hard `<commit id>` |
| Stop a file being tracked                                   | git rm --cached <file/folder>  |
| Restore a file to a previous commit                         | git checkout <file/to/restore> |

### Branching & Merging

| Description                                                            | Command                                                |
| ---------------------------------------------------------------------- | ------------------------------------------------------ |
| List branches (the asterisk denotes the current branch)                | git branch                                             |
| List all branches (local and remote)                                   | git branch -a                                          |
| Create a new branch                                                    | git branch `<branch name>`                             |
| Create a new branch and switch to it                                   | git checkout -b `<branch name>`                        |
| Clone a remote branch and switch to it                                 | git checkout -b `<branch name>` origin/`<branch name>` |
| Rename a local branch                                                  | git branch -m `<old branch name>` `<new branch name>`  |
| Switch to a branch                                                     | git checkout `<branch name>`                           |
| Switch to the branch last checked out                                  | git checkout -                                         |
| Discard changes to a file                                              | git checkout -- <file-name.txt>                        |
| Delete a branch                                                        | git branch -d `<branch name>`                          |
| Delete a remote branch                                                 | git push origin --delete `<branch name>`               |
| Preview changes before merging                                         | git diff `<source branch>` `<target branch>`           |
| Merge a branch into the active branch                                  | git merge `<branch name>`                              |
| Merge a branch into a target branch                                    | git merge `<source branch>` `<target branch>`          |
| Stash changes in a dirty working directory                             | git stash                                              |
| Remove all stashed entries                                             | git stash clear                                        |
| Undo last commit, keep changes in staging area                         | git reset –soft HEAD^                                  |
| undo the last commit and remove the file from the staging area as well | git reset –hard HEAD^                                  |
| To undo the last 2 commits and all changes                             | git reset –hard HEAD^^                                 |

### Sharing & Updating Projects

| Description                                                                    | Command                                                                             |
| ------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------- |
| Push a branch to your remote repository                                        | git push origin `<branch name>`                                                     |
| Push changes to remote repository (and remember the branch)                    | git push -u origin `<branch name>`                                                  |
| Push changes to remote repository (remembered branch)                          | git push                                                                            |
| Push changes to remote repository all branch                                   | git push --all                                                                      |
| Push changes to remote repository (Force)                                      | git push -f                                                                         |
| Delete a remote branch                                                         | git push origin --delete `<branch name>`                                            |
| Update local repository to the newest commit                                   | git pull                                                                            |
| Pull changes from remote repository                                            | git pull origin `<branch name>`                                                     |
| Add a remote repository                                                        | git remote add origin ssh://git@github.com/`<username>`/`<repository-name>`.git     |
| Set a repository's origin branch to SSH                                        | git remote set-url origin ssh://git@github.com/`<username>`/`<repository-name>`.git |
| To pull changes from a particular remote branch into your current local branch | git pull <remote_name> <branch_name>                                                |

---

### To take all code from one branch to another, you have a few options:

| Description                                                                                                                                              | Command                                                   |
| -------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| Option 1: Replace your current branch with Branch_1 completely``Use this if you want to completely replace your current code with Branch_1's code.       | git reset --hard Branch_1                                 |
| Option 2: Merge and use their version for all conflicts``Use this if you want to merge and automatically prefer Branch_1's changes when conflicts occur. | git merge Branch_1 --allow-unrelated-histories -X theirs  |
| Option 3: Create a fresh branch from Branch_1``Use this if you want to start a new branch based on Branch_1.                                             | git checkout Branch_1git checkout -b Branch_2_new         |
| Option 4: Force push Branch_1 to your branch``Use this if you want to pull the remote Branch_1 branch and forcefully sync it with your current branch.   | git fetch origin Branch_1git reset --hard origin/Branch_1 |

\*\*
