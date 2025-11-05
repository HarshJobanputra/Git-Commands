import streamlit as st
import pyperclip

# Page configuration
st.set_page_config(
    page_title="Git Commands Documentation",
    page_icon="🔧",
    layout="wide"
)

# Git commands data structure from README.md
git_commands = {
    "Basic Git Commands": [
        {"command": "git help", "description": "Prints Git help information and provides quick reference to basic usage and commonly used commands", "example": "git help"},
        {"command": "git help <command>", "description": "Display help information for any specific Git command", "example": "git help commit"},
        {"command": "git version", "description": "Displays the version of Git installed on your system", "example": "git version"},
        {"command": "git init", "description": "Initialize a new Git repository in the current directory, creating .git subdirectory", "example": "git init"},
        {"command": "git clone <repository_url>", "description": "Creates a copy of a remote Git repository on your local machine with all files, branches, and commit history", "example": "git clone https://github.com/user/repo.git"},
        {"command": "git clone --branch <branch-name> <repository-url>", "description": "Clone a specific Git branch from remote repository", "example": "git clone --branch develop https://github.com/user/repo.git"},
        {"command": "git clone -b <branch-name> --single-branch <repository-url>", "description": "Clone only a specific branch without full history of all branches", "example": "git clone -b develop --single-branch https://github.com/user/repo.git"},
        {"command": "git status", "description": "Shows the current state of the Git repository's working directory and staging area", "example": "git status"},
    ],
    "Working Directory and Staging Area": [
        {"command": "git checkout .", "description": "Discards all changes in the working directory, reverting files to their last committed state", "example": "git checkout ."},
        {"command": "git checkout -- <file>", "description": "Discard changes to a specific file", "example": "git checkout -- index.html"},
        {"command": "git reset -p", "description": "Allows you to interactively reset changes in the working directory with fine-grained control", "example": "git reset -p"},
        {"command": "git add <file>", "description": "Adds a specific file to the staging area, preparing it for inclusion in the next commit", "example": "git add index.html"},
        {"command": "git add -A", "description": "Add all new and changed files to the staging area", "example": "git add -A"},
        {"command": "git add .", "description": "Add all new and changed files to the staging area", "example": "git add ."},
        {"command": "git add -p", "description": "Interactively stage changes by breaking them into chunks (hunks) for selective adding", "example": "git add -p"},
        {"command": "git add -i", "description": "Enters interactive mode with text-based menu for staging individual changes, updating files, or viewing status", "example": "git add -i"},
        {"command": "git rm <file>", "description": "Removes a file from the working directory and stages the removal", "example": "git rm old-file.txt"},
        {"command": "git rm -r <file>", "description": "Remove a file or folder recursively", "example": "git rm -r folder"},
        {"command": "git rm --cached <file>", "description": "Stop a file being tracked (removes from staging area but keeps in working directory)", "example": "git rm --cached config.txt"},
        {"command": "git mv <old_path> <new_path>", "description": "Move or rename a file or directory within Git repository and automatically stages the change", "example": "git mv old-name.txt new-name.txt"},
        {"command": "git commit -m \"message\"", "description": "Creates a new commit with staged changes and a descriptive message", "example": "git commit -m \"Add new feature\""},
    ],
    "Working with Branches": [
        {"command": "git branch <branch_name>", "description": "Creates a new branch", "example": "git branch feature-branch"},
        {"command": "git checkout <branch_name>", "description": "Switches to the specified branch and updates the working directory", "example": "git checkout main"},
        {"command": "git checkout -", "description": "Switch to the branch last checked out", "example": "git checkout -"},
        {"command": "git checkout -b <branch_name> origin/<branch_name>", "description": "Clone a remote branch and switch to it", "example": "git checkout -b feature origin/feature"},
        {"command": "git branch", "description": "Lists all branches", "example": "git branch"},
        {"command": "git branch -d <branch_name>", "description": "Deletes a branch", "example": "git branch -d feature-branch"},
        {"command": "git push --delete <remote> <branch>", "description": "Deletes a remote branch", "example": "git push --delete origin feature-branch"},
        {"command": "git branch -m <old_name> <new_name>", "description": "Renames a branch", "example": "git branch -m old-feature new-feature"},
        {"command": "git checkout -b <new_branch>", "description": "Creates and switches to a new branch based on the current branch", "example": "git checkout -b new-feature"},
        {"command": "git switch <branch>", "description": "Switches the working directory to the specified branch", "example": "git switch main"},
        {"command": "git show-branch <branch>", "description": "Displays summary of commit history and branch relationships showing where each branch diverged", "example": "git show-branch feature"},
        {"command": "git show-branch --all", "description": "Shows commit history and relationships for all branches and their commits", "example": "git show-branch --all"},
        {"command": "git branch -r", "description": "Lists all remote branches that your local repository is aware of", "example": "git branch -r"},
        {"command": "git branch -a", "description": "Lists all branches including both local and remote branches", "example": "git branch -a"},
        {"command": "git branch --merged", "description": "Lists all branches that have been fully merged into current branch and can be safely deleted", "example": "git branch --merged"},
        {"command": "git branch --no-merged", "description": "Lists branches that have not been fully merged into current branch", "example": "git branch --no-merged"},
    ],
    "Merging in Git": [
        {"command": "git merge <branch>", "description": "Integrates changes from specified branch into current branch, combining their histories", "example": "git merge feature-branch"},
        {"command": "git merge --no-ff <branch>", "description": "Merges branch always creating a new merge commit even if fast-forward merge is possible", "example": "git merge --no-ff feature-branch"},
        {"command": "git merge --squash <branch>", "description": "Combines all changes from specified branch into single commit without merging branch history", "example": "git merge --squash feature-branch"},
        {"command": "git merge --abort", "description": "Cancels ongoing merge process and restores state before merge started", "example": "git merge --abort"},
        {"command": "git merge -s ours <branch>", "description": "Performs merge using 'ours' strategy, keeping current branch changes and discarding other branch changes", "example": "git merge -s ours feature-branch"},
        {"command": "git merge --strategy=ours <branch>", "description": "Same as above but expanded version - merges histories without integrating changes from other branch", "example": "git merge --strategy=ours feature-branch"},
        {"command": "git merge --strategy=theirs <branch>", "description": "Merges using 'theirs' strategy, resolving conflicts by favoring changes from branch being merged", "example": "git merge --strategy=theirs feature-branch"},
    ],
    "Git Remotes": [
        {"command": "git fetch", "description": "Fetches changes from remote repository but does not merge them into current branch", "example": "git fetch"},
        {"command": "git pull", "description": "Fetches changes from remote repository and immediately merges them into current branch", "example": "git pull"},
        {"command": "git push", "description": "Uploads your local branch's changes to a remote repository", "example": "git push"},
        {"command": "git push --all", "description": "Push changes to remote repository all branches", "example": "git push --all"},
        {"command": "git push -f", "description": "Push changes to remote repository (Force)", "example": "git push -f"},
        {"command": "git remote", "description": "Lists the names of remote repositories configured for your local repository", "example": "git remote"},
        {"command": "git remote -v", "description": "Displays URLs of remote repositories showing both fetch and push URLs", "example": "git remote -v"},
        {"command": "git remote add <name> <url>", "description": "Adds new remote repository with specified name and URL to local repository configuration", "example": "git remote add origin https://github.com/user/repo.git"},
        {"command": "git remote remove <name>", "description": "Deletes specified remote repository connection from local git configuration", "example": "git remote remove origin"},
        {"command": "git remote rm <name>", "description": "Shorthand version of git remote remove", "example": "git remote rm origin"},
        {"command": "git remote rename <old_name> <new_name>", "description": "Changes name of existing remote repository connection", "example": "git remote rename origin upstream"},
        {"command": "git remote set-url <name> <newurl>", "description": "Changes URL of existing remote repository connection", "example": "git remote set-url origin https://github.com/newuser/repo.git"},
        {"command": "git fetch <remote>", "description": "Retrieves latest changes from specified remote repository without merging", "example": "git fetch origin"},
        {"command": "git pull <remote>", "description": "Fetches changes from specified remote repository and merges them into current branch", "example": "git pull origin"},
        {"command": "git remote update", "description": "Fetches updates for all remotes tracked by the repository", "example": "git remote update"},
        {"command": "git push <remote> <branch>", "description": "Uploads specified branch from local repository to given remote repository", "example": "git push origin main"},
        {"command": "git push -u <remote> <branch>", "description": "Push changes to remote repository and remember the branch", "example": "git push -u origin main"},
        {"command": "git push <remote> --delete <branch>", "description": "Removes specified branch from remote repository", "example": "git push origin --delete feature-branch"},
        {"command": "git remote show <remote>", "description": "Displays detailed information about specified remote repository including URL and branch tracking", "example": "git remote show origin"},
        {"command": "git ls-remote <repository>", "description": "Lists references and commit IDs from specified remote repository without cloning", "example": "git ls-remote origin"},
        {"command": "git push origin <branch> --set-upstream", "description": "Pushes local branch to remote and sets up tracking for future push/pull commands", "example": "git push origin feature --set-upstream"},
        {"command": "git remote add upstream <repository>", "description": "Adds upstream remote to track original repository (commonly used with forks)", "example": "git remote add upstream https://github.com/original/repo.git"},
        {"command": "git fetch upstream", "description": "Retrieves updates from upstream remote repository", "example": "git fetch upstream"},
        {"command": "git pull upstream <branch>", "description": "Fetches and merges changes from upstream remote branch into current branch", "example": "git pull upstream main"},
    ],
    "Amending Commits": [
        {"command": "git commit --amend", "description": "Modifies the most recent commit, combining staged changes", "example": "git commit --amend"},
        {"command": "git commit --amend -m \"new message\"", "description": "Amends the commit message of the most recent commit", "example": "git commit --amend -m \"Updated commit message\""},
        {"command": "git commit --fixup=HEAD", "description": "Creates fixup commit intended to correct most recent commit, marked with fixup! prefix", "example": "git commit --fixup=HEAD"},
    ],
    "Stashing in Git": [
        {"command": "git stash", "description": "Stash changes in a dirty working directory - temporarily saves uncommitted changes", "example": "git stash"},
        {"command": "git stash -m \"message\"", "description": "Stashes changes with a custom message for easier identification", "example": "git stash -m \"Work in progress\""},
        {"command": "git stash show", "description": "Displays summary of changes in most recent stash entry showing modified files", "example": "git stash show"},
        {"command": "git stash list", "description": "Shows all stashed changes in repository in numbered list format", "example": "git stash list"},
        {"command": "git stash pop", "description": "Applies most recent stash and immediately removes it from stash list", "example": "git stash pop"},
        {"command": "git stash drop", "description": "Removes most recent stash entry without applying it to working directory", "example": "git stash drop"},
        {"command": "git stash apply", "description": "Reapplies most recently stashed changes without removing them from stash list", "example": "git stash apply"},
        {"command": "git stash clear", "description": "Remove all stashed entries - permanently deleting all saved changes", "example": "git stash clear"},
        {"command": "git stash branch <branch>", "description": "Creates new branch from commit where you stashed changes and applies stashed changes to it", "example": "git stash branch feature-stash"},
    ],
    "Git Tagging": [
        {"command": "git tag <tag_name>", "description": "Creates new lightweight tag pointing to current commit for marking releases or milestones", "example": "git tag v1.0"},
        {"command": "git tag -a <tag_name> -m \"message\"", "description": "Creates annotated tag with metadata like tagger name, email, date, and message", "example": "git tag -a v1.0 -m \"Version 1.0 release\""},
        {"command": "git tag -d <tag_name>", "description": "Deletes specified tag from local repository", "example": "git tag -d v1.0"},
        {"command": "git tag -f <tag> <commit>", "description": "Forces a tag to point to different commit", "example": "git tag -f v1.0 abc123"},
        {"command": "git show <tag_name>", "description": "Displays detailed information about specified tag including commit and annotations", "example": "git show v1.0"},
        {"command": "git push origin <tag_name>", "description": "Uploads specified tag to remote repository making it available to others", "example": "git push origin v1.0"},
        {"command": "git push origin --tags", "description": "Pushes all local tags to remote repository synchronizing all tags", "example": "git push origin --tags"},
        {"command": "git push --follow-tags", "description": "Pushes both commits and tags together", "example": "git push --follow-tags"},
        {"command": "git fetch --tags", "description": "Retrieves all tags from default remote repository without affecting current branches", "example": "git fetch --tags"},
    ],
    "Reverting Changes in Git": [
        {"command": "git checkout -- <file>", "description": "Discards changes in specified file from working directory, reverting to last commit state", "example": "git checkout -- index.html"},
        {"command": "git revert <commit>", "description": "Creates new commit that undoes changes in specified commit while preserving history", "example": "git revert abc123"},
        {"command": "git revert -n <commit>", "description": "Reverts a commit but does not automatically commit the result", "example": "git revert -n abc123"},
        {"command": "git reset", "description": "Resets current HEAD to specified state with options for staging area and working directory", "example": "git reset"},
        {"command": "git reset --soft <commit>", "description": "Moves HEAD to specified commit keeping index and working directory unchanged, changes remain staged", "example": "git reset --soft HEAD~1"},
        {"command": "git reset --mixed <commit>", "description": "Moves HEAD and updates index to match commit but leaves working directory unchanged", "example": "git reset --mixed HEAD~1"},
        {"command": "git reset --hard <commit>", "description": "Moves HEAD and updates both index and working directory to match commit, discarding all changes", "example": "git reset --hard HEAD~1"},
    ],
    "Inspection & Comparison": [
        {"command": "git log --summary", "description": "View changes with detailed information", "example": "git log --summary"},
        {"command": "git log --pretty=short", "description": "View changes in brief format", "example": "git log --pretty=short"},
        {"command": "git diff <source_branch> <target_branch>", "description": "Preview changes before merging between branches", "example": "git diff feature main"},
    ],
    "Undo Operations": [
        {"command": "git checkout <commit_id>", "description": "Return to previous commit (detached HEAD state)", "example": "git checkout abc123"},
        {"command": "git reset --soft HEAD^", "description": "Undo last commit, keep changes in staging area", "example": "git reset --soft HEAD^"},
        {"command": "git reset --hard HEAD^", "description": "Undo the last commit and remove the file from the staging area as well", "example": "git reset --hard HEAD^"},
        {"command": "git reset --hard HEAD^^", "description": "Undo the last 2 commits and all changes", "example": "git reset --hard HEAD^^"},
        {"command": "git checkout <file/to/restore>", "description": "Restore a file to a previous commit", "example": "git checkout README.md"},
    ],
    "Advanced Branch Operations": [
        {"command": "git reset --hard <branch_name>", "description": "Replace your current branch with specified branch completely", "example": "git reset --hard main"},
        {"command": "git merge <branch_name> --allow-unrelated-histories -X theirs", "description": "Merge and use their version for all conflicts", "example": "git merge feature --allow-unrelated-histories -X theirs"},
        {"command": "git fetch origin <branch_name>", "description": "Fetch specific branch from remote", "example": "git fetch origin main"},
        {"command": "git reset --hard origin/<branch_name>", "description": "Force sync current branch with remote branch", "example": "git reset --hard origin/main"},
        {"command": "git pull <remote_name> <branch_name>", "description": "Pull changes from a particular remote branch into your current local branch", "example": "git pull origin feature"},
    ],
    "Viewing History Logs": [
        {"command": "git log", "description": "Displays the commit history showing chronological sequence of commits", "example": "git log"},
        {"command": "git log --oneline", "description": "Displays summary of commits with one line each for condensed view", "example": "git log --oneline"},
        {"command": "git log --graph", "description": "Shows graphical representation of commit history with branch visualization", "example": "git log --graph"},
        {"command": "git log --stat", "description": "Displays file statistics along with commit history showing changed files", "example": "git log --stat"},
        {"command": "git log --pretty=format:\"%h %s\"", "description": "Formats log output according to specified format showing hash and subject", "example": "git log --pretty=format:\"%h %s\""},
        {"command": "git log --pretty=format:\"%h - %an, %ar : %s\"", "description": "Provides human-readable format showing hash, author, date, and subject", "example": "git log --pretty=format:\"%h - %an, %ar : %s\""},
        {"command": "git log --author=<author>", "description": "Shows commits made by specified author", "example": "git log --author=\"John Doe\""},
        {"command": "git log --before=<date>", "description": "Shows commits made before specified date", "example": "git log --before=\"2023-01-01\""},
        {"command": "git log --after=<date>", "description": "Shows commits made after specified date (same as --since)", "example": "git log --after=\"2023-01-01\""},
        {"command": "git log --cherry-pick", "description": "Omits commits that are equivalent between two branches", "example": "git log --cherry-pick"},
        {"command": "git log --follow <file>", "description": "Shows commits for a file including renames and moves", "example": "git log --follow README.md"},
        {"command": "git log --show-signature", "description": "Displays GPG signature information for commits", "example": "git log --show-signature"},
        {"command": "git shortlog", "description": "Summarizes git log output by author showing commit counts", "example": "git shortlog"},
        {"command": "git shortlog -sn", "description": "Summarizes git log output by author with commit counts in numerical format", "example": "git shortlog -sn"},
        {"command": "git log --simplify-by-decoration", "description": "Shows only commits that are referenced by tags or branches", "example": "git log --simplify-by-decoration"},
        {"command": "git log --no-merges", "description": "Omits merge commits from the log showing only regular commits", "example": "git log --no-merges"},
        {"command": "git whatchanged", "description": "Lists commit data in format similar to commit log with file changes", "example": "git whatchanged"},
        {"command": "git diff-tree --pretty --name-only --root <commit>", "description": "Shows detailed information for a commit tree including file names", "example": "git diff-tree --pretty --name-only --root abc123"},
        {"command": "git log --first-parent", "description": "Shows only commits of current branch excluding those merged from other branches", "example": "git log --first-parent"},
    ],
    "Git Diffs": [
        {"command": "git diff", "description": "Shows differences between working directory and index, or between commits/branches", "example": "git diff"},
        {"command": "git diff --stat", "description": "Shows summary of changes between working directory and index with file modification counts", "example": "git diff --stat"},
        {"command": "git diff --stat <commit>", "description": "Views changes between a commit and the working directory", "example": "git diff --stat HEAD~1"},
        {"command": "git diff --stat <commit1> <commit2>", "description": "Provides summary of changes between two commits showing altered files", "example": "git diff --stat abc123 def456"},
        {"command": "git diff --stat <branch1> <branch2>", "description": "Summarizes differences between two branches indicating changed files", "example": "git diff --stat main feature"},
        {"command": "git diff --name-only <commit>", "description": "Shows only names of files that changed in specified commit", "example": "git diff --name-only HEAD~1"},
        {"command": "git diff --cached", "description": "Shows differences between staged changes and last commit", "example": "git diff --cached"},
        {"command": "git diff HEAD", "description": "Shows differences between working directory and latest commit", "example": "git diff HEAD"},
        {"command": "git diff <branch1> <branch2>", "description": "Shows differences between tips of two branches", "example": "git diff main feature"},
        {"command": "git difftool", "description": "Launches external diff tool to compare changes", "example": "git difftool"},
        {"command": "git difftool <commit1> <commit2>", "description": "Uses diff tool to show differences between two specified commits", "example": "git difftool abc123 def456"},
        {"command": "git difftool <branch1> <branch2>", "description": "Opens diff tool to compare changes between two branches", "example": "git difftool main feature"},
        {"command": "git cherry <branch>", "description": "Compares commits in current branch against another branch showing unique commits", "example": "git cherry main"},
    ],
    "Git Flow": [
        {"command": "git flow init", "description": "Initializes repository for git-flow branching model with structured branch strategy", "example": "git flow init"},
        {"command": "git flow feature start <feature>", "description": "Starts new feature branch in git-flow model", "example": "git flow feature start user-auth"},
        {"command": "git flow feature finish <feature>", "description": "Finishes feature branch in git-flow merging back to develop", "example": "git flow feature finish user-auth"},
    ],
    "Exploring Git References": [
        {"command": "git show-ref --heads", "description": "Lists references to all heads (branches) showing commit hashes", "example": "git show-ref --heads"},
        {"command": "git show-ref --tags", "description": "Lists references to all tags showing commit hashes", "example": "git show-ref --tags"},
    ],
    "How to Configure Git": [
        {"command": "git config --global user.name \"Your Name\"", "description": "Sets the user name on a global level for all repositories", "example": "git config --global user.name \"John Doe\""},
        {"command": "git config --global user.email \"your_email@example.com\"", "description": "Sets the user email on a global level for all repositories", "example": "git config --global user.email \"john@example.com\""},
        {"command": "git config --global core.editor <editor>", "description": "Sets the default text editor for Git operations", "example": "git config --global core.editor nano"},
        {"command": "git config --global core.excludesfile <file>", "description": "Sets the global ignore file for all repositories", "example": "git config --global core.excludesfile ~/.gitignore_global"},
        {"command": "git config --list", "description": "Lists all the configuration settings currently active", "example": "git config --list"},
        {"command": "git config --list --show-origin", "description": "Lists all config variables showing their origins (global, local, system)", "example": "git config --list --show-origin"},
        {"command": "git config <key>", "description": "Retrieves the value for the specified configuration key", "example": "git config user.name"},
        {"command": "git config --get <key>", "description": "Retrieves the value for the specified configuration key (explicit version)", "example": "git config --get user.email"},
        {"command": "git config --unset <key>", "description": "Removes the specified configuration key from current scope", "example": "git config --unset user.name"},
        {"command": "git config --global --unset <key>", "description": "Removes the specified configuration key globally", "example": "git config --global --unset user.name"},
    ],
    "Git Security": [
        {"command": "git config --global user.signingKey <key>", "description": "Configures the GPG key for signing commits and tags ensuring authenticity", "example": "git config --global user.signingKey ABC123"},
        {"command": "git config --global commit.gpgSign true", "description": "Automatically signs all commits with GPG for enhanced security", "example": "git config --global commit.gpgSign true"},
    ],
    "How to Set Aliases in Git": [
        {"command": "git config --global alias.ci commit", "description": "Sets git ci as an alias for git commit command", "example": "git config --global alias.ci commit"},
        {"command": "git config --global alias.st status", "description": "Sets git st as an alias for git status command", "example": "git config --global alias.st status"},
        {"command": "git config --global alias.co checkout", "description": "Sets git co as an alias for git checkout command", "example": "git config --global alias.co checkout"},
        {"command": "git config --global alias.br branch", "description": "Sets git br as an alias for git branch command", "example": "git config --global alias.br branch"},
        {"command": "git config --global alias.graph \"log --graph --all --oneline --decorate\"", "description": "Creates alias for detailed graph of repository history", "example": "git config --global alias.graph \"log --graph --all --oneline --decorate\""},
    ],
    "Rebasing in Git": [
        {"command": "git rebase <branch>", "description": "Re-applies commits on top of another base tip for linear project history and smooth integration", "example": "git rebase main"},
        {"command": "git rebase --interactive <branch>", "description": "Starts interactive rebase allowing you to edit, reorder, squash, or drop commits", "example": "git rebase --interactive HEAD~3"},
    ]
}

# Problems data
git_problems = {
    "To take all code from one branch to another": [
        {"command": "git reset --hard <branch_name>", "description": "Replace your current branch with specified branch completely. Use this if you want to completely replace your current code with another branch's code.", "example": "git reset --hard main"},
        {"command": "git merge <branch_name> --allow-unrelated-histories -X theirs", "description": "Merge and use their version for all conflicts. Use this if you want to merge and automatically prefer the other branch's changes when conflicts occur.", "example": "git merge feature --allow-unrelated-histories -X theirs"},
        {"command": "git checkout <branch_name> && git checkout -b <new_branch>", "description": "Create a fresh branch from another branch. Use this if you want to start a new branch based on another branch.", "example": "git checkout main && git checkout -b feature-new"},
        {"command": "git fetch origin <branch_name> && git reset --hard origin/<branch_name>", "description": "Force push another branch to your branch. Use this if you want to pull the remote branch and forcefully sync it with your current branch.", "example": "git fetch origin main && git reset --hard origin/main"},
    ],
    "Undo last commit but keep changes": [
        {"command": "git reset --soft HEAD~1", "description": "Undo the last commit but keep all changes staged. Perfect when you want to modify the commit message or add more files.", "example": "git reset --soft HEAD~1"},
        {"command": "git commit --amend", "description": "Modify the last commit by adding new changes or changing the commit message. Use after staging additional files.", "example": "git commit --amend -m \"Updated commit message\""},
        {"command": "git reset HEAD~1", "description": "Undo the last commit and unstage changes, but keep files modified in working directory.", "example": "git reset HEAD~1"},
    ],
    "Remove file from Git but keep locally": [
        {"command": "git rm --cached <file>", "description": "Remove file from Git tracking but keep it in your local working directory. Useful for files that should not be tracked.", "example": "git rm --cached config.txt"},
        {"command": "echo '<file>' >> .gitignore && git add .gitignore", "description": "Add file to .gitignore to prevent future tracking and commit the ignore file.", "example": "echo 'config.txt' >> .gitignore && git add .gitignore"},
        {"command": "git update-index --skip-worktree <file>", "description": "Tell Git to ignore changes to a tracked file temporarily. Use when you need local modifications that shouldn't be committed.", "example": "git update-index --skip-worktree config.txt"},
    ],
    "Resolve merge conflicts": [
        {"command": "git status", "description": "Check which files have conflicts. Look for files marked as 'both modified' to identify conflict locations.", "example": "git status"},
        {"command": "git add <resolved-file> && git commit", "description": "After manually editing and resolving conflicts in files, stage the resolved files and commit the merge.", "example": "git add index.html && git commit"},
        {"command": "git merge --abort", "description": "Cancel the merge process and return to the state before the merge started. Use when conflicts are too complex.", "example": "git merge --abort"},
        {"command": "git checkout --theirs <file> && git add <file>", "description": "Accept their version of the conflicted file completely. Use when you want to keep the incoming changes.", "example": "git checkout --theirs index.html && git add index.html"},
        {"command": "git checkout --ours <file> && git add <file>", "description": "Accept your version of the conflicted file completely. Use when you want to keep your current changes.", "example": "git checkout --ours index.html && git add index.html"},
    ],
    "Accidentally committed to wrong branch": [
        {"command": "git log --oneline -n 5", "description": "First, identify the commit hash that you want to move to another branch.", "example": "git log --oneline -n 5"},
        {"command": "git checkout <target-branch> && git cherry-pick <commit-hash>", "description": "Switch to the correct branch and cherry-pick the commit from the wrong branch.", "example": "git checkout feature && git cherry-pick abc123"},
        {"command": "git checkout <wrong-branch> && git reset --hard HEAD~1", "description": "Go back to the wrong branch and remove the commit using hard reset.", "example": "git checkout main && git reset --hard HEAD~1"},
        {"command": "git branch <new-branch> && git reset --hard HEAD~1", "description": "Alternative: Create a new branch from current commit, then reset the current branch.", "example": "git branch feature-fix && git reset --hard HEAD~1"},
    ],
    "Sync fork with original repository": [
        {"command": "git remote add upstream <original-repo-url>", "description": "Add the original repository as upstream remote. Do this once when you first clone your fork.", "example": "git remote add upstream https://github.com/original/repo.git"},
        {"command": "git fetch upstream", "description": "Fetch all changes from the original repository without merging them into your local branches.", "example": "git fetch upstream"},
        {"command": "git checkout main && git merge upstream/main", "description": "Switch to your main branch and merge the latest changes from the original repository.", "example": "git checkout main && git merge upstream/main"},
        {"command": "git push origin main", "description": "Push the updated main branch to your fork on GitHub to keep it synchronized.", "example": "git push origin main"},
    ],
    "Recover deleted branch": [
        {"command": "git reflog", "description": "Show the reference log to find the commit hash where your deleted branch was pointing.", "example": "git reflog"},
        {"command": "git checkout -b <branch-name> <commit-hash>", "description": "Create a new branch from the commit hash found in reflog to recover the deleted branch.", "example": "git checkout -b feature-recovered abc123"},
        {"command": "git branch <branch-name> <commit-hash>", "description": "Alternative: Create the branch without switching to it immediately.", "example": "git branch feature-recovered abc123"},
    ],
    "Change commit message of last commit": [
        {"command": "git commit --amend -m \"New commit message\"", "description": "Change the message of the most recent commit. Only use this if you haven't pushed the commit yet.", "example": "git commit --amend -m \"Fix: Updated user authentication\""},
        {"command": "git commit --amend", "description": "Open the default editor to modify the last commit message interactively.", "example": "git commit --amend"},
        {"command": "git push --force-with-lease", "description": "If you already pushed the commit, use force push with lease to update the remote safely.", "example": "git push --force-with-lease"},
    ]
}

def copy_to_clipboard(text):
    """Copy text to clipboard"""
    try:
        pyperclip.copy(text)
        return True
    except:
        return False

# Custom CSS for larger code font and search input styling
st.markdown("""
<style>
div[data-testid="stCodeBlock"] code {
    font-size: 18px !important;
    line-height: 1.5 !important;
}
pre code {
    font-size: 18px !important;
    line-height: 1.5 !important;
}
.stCodeBlock pre {
    font-size: 18px !important;
}
div[data-testid="stTextInput"] input {
    font-size: 18px !important;
    line-height: 1.5 !important;
}
</style>
""", unsafe_allow_html=True)

# Main app
st.title("🔧 Git Commands Documentation")
st.markdown("Complete reference guide for Git commands from README.md with copy functionality")

# Sidebar for navigation
st.sidebar.title("📱 Navigation")

# Initialize session state
if 'section_type' not in st.session_state:
    st.session_state.section_type = "Git Commands"
if 'selected_category' not in st.session_state:
    st.session_state.selected_category = list(git_commands.keys())[0]
if 'selected_problem' not in st.session_state:
    st.session_state.selected_problem = list(git_problems.keys())[0]

# Section selection
section_type = st.sidebar.selectbox(
    "Select Section:",
    ["Git Commands", "Problems & Solutions"],
    key="section_selector"
)
st.session_state.section_type = section_type

if section_type == "Git Commands":
    st.sidebar.markdown("### 📚 Git Commands")
    for category in git_commands.keys():
        is_active = category == st.session_state.selected_category
        button_type = "primary" if is_active else "secondary"
        if st.sidebar.button(category, key=f"cat_{category}", use_container_width=True, type=button_type):
            st.session_state.selected_category = category
            st.rerun()
else:
    st.sidebar.markdown("### 🔧 Problems & Solutions")
    for problem in git_problems.keys():
        is_active = problem == st.session_state.selected_problem
        button_type = "primary" if is_active else "secondary"
        if st.sidebar.button(problem, key=f"prob_{problem}", use_container_width=True, type=button_type):
            st.session_state.selected_problem = problem
            st.rerun()

selected_category = st.session_state.selected_category

# Search functionality
search_term = st.text_input("🔍 Search commands:", placeholder="Type to search...")

if section_type == "Git Commands":
    selected_category = st.session_state.selected_category
    
    if search_term:
        filtered_commands = []
        for category, commands in git_commands.items():
            for cmd in commands:
                if (search_term.lower() in cmd["command"].lower() or 
                    search_term.lower() in cmd["description"].lower()):
                    filtered_commands.append({**cmd, "category": category})
        
        if filtered_commands:
            st.subheader(f"Search Results for '{search_term}'")
            
            for i in range(0, len(filtered_commands), 3):
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    cmd = filtered_commands[i]
                    st.code(cmd["command"], language="bash")
                    st.write(cmd["description"])
                    st.caption(f"*Category: {cmd['category']}*")
                    st.markdown("---")
                
                with col2:
                    if i + 1 < len(filtered_commands):
                        cmd = filtered_commands[i + 1]
                        st.code(cmd["command"], language="bash")
                        st.write(cmd["description"])
                        st.caption(f"*Category: {cmd['category']}*")
                        st.markdown("---")

                with col3:
                    if i + 2 < len(filtered_commands):
                        cmd = filtered_commands[i + 2]
                        st.code(cmd["command"], language="bash")
                        st.write(cmd["description"])
                        st.caption(f"*Category: {cmd['category']}*")
                        st.markdown("---")
        else:
            st.warning("No commands found matching your search.")
    else:
        st.subheader(f"📂 {selected_category}")
        
        commands_list = git_commands[selected_category]
        
        for i in range(0, len(commands_list), 3):
            col1, col2, col3 = st.columns(3)
            
            with col1:
                cmd = commands_list[i]
                st.code(cmd["command"], language="bash")
                st.write(cmd["description"])
                st.markdown("---")
            
            with col2:
                if i + 1 < len(commands_list):
                    cmd = commands_list[i + 1]
                    st.code(cmd["command"], language="bash")
                    st.write(cmd["description"])
                    st.markdown("---")
            
            with col3:
                if i + 2 < len(commands_list):
                    cmd = commands_list[i + 2]
                    st.code(cmd["command"], language="bash")
                    st.write(cmd["description"])
                    st.markdown("---")

else:
    selected_problem = st.session_state.selected_problem
    
    if search_term:
        filtered_solutions = []
        for problem, solutions in git_problems.items():
            for sol in solutions:
                if (search_term.lower() in sol["command"].lower() or 
                    search_term.lower() in sol["description"].lower() or
                    search_term.lower() in problem.lower()):
                    filtered_solutions.append({**sol, "problem": problem})
        
        if filtered_solutions:
            st.subheader(f"Search Results for '{search_term}'")
            
            for i in range(0, len(filtered_solutions), 2):
                col1, col2 = st.columns(2)
                
                with col1:
                    sol = filtered_solutions[i]
                    st.code(sol["command"], language="bash")
                    st.write(sol["description"])
                    st.caption(f"*Problem: {sol['problem']}*")
                    st.markdown("---")
                
                with col2:
                    if i + 1 < len(filtered_solutions):
                        sol = filtered_solutions[i + 1]
                        st.code(sol["command"], language="bash")
                        st.write(sol["description"])
                        st.caption(f"*Problem: {sol['problem']}*")
                        st.markdown("---")
        else:
            st.warning("No solutions found matching your search.")
    else:
        st.subheader(f"🔧 {selected_problem}")
        
        solutions_list = git_problems[selected_problem]
        
        for i, sol in enumerate(solutions_list, 1):
            st.markdown(f"### Option {i}:")
            st.code(sol["command"], language="bash")
            st.write(sol["description"])
            st.markdown("---")

# Footer
if section_type == "Git Commands":
    st.markdown(f"📊 **Total Commands:** {sum(len(commands) for commands in git_commands.values())} commands across {len(git_commands)} categories")
else:
    st.markdown(f"🔧 **Total Problems:** {len(git_problems)} common Git problems with solutions")