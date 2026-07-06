# TechNova Solutions Pvt. Ltd.

# Git and GitHub Training Manual

**Training Version:** 1.0
**Department:** Learning & Development (L&D) and Engineering
**Duration:** 2 Weeks
**Target Audience:** Software Engineers, Data Engineers, DevOps Engineers, Data Scientists, Interns, and Freshers

---

# 1. Introduction

Git is a distributed version control system used to track changes in source code and facilitate collaboration among developers.

GitHub is a cloud-based platform that hosts Git repositories and provides collaboration, automation, and project management features.

---

# 2. Why Version Control?

Version control helps teams:

* Track changes
* Collaborate effectively
* Maintain history
* Revert changes
* Manage releases
* Improve software quality

Benefits include:

* Backup and recovery
* Team collaboration
* Auditability
* Branch management
* Continuous integration

---

# 3. Installing Git

Verify installation:

```bash id="n8v3kp"
git --version
```

Example output:

```text id="g2wr7j"
git version 2.48.1
```

Configure Git:

```bash id="v9x2dc"
git config --global user.name "Aditi More"
git config --global user.email "aditi@example.com"
```

---

# 4. Git Architecture

Git consists of:

* Working Directory
* Staging Area
* Local Repository
* Remote Repository

Workflow:

```text id="f1pq7n"
Working Directory
        ↓
   Staging Area
        ↓
 Local Repository
        ↓
Remote Repository
```

---

# 5. Creating a Repository

Initialize a repository:

```bash id="w7cm4e"
git init
```

Example:

```bash id="b3xy6n"
mkdir project
cd project
git init
```

---

# 6. Checking Repository Status

Command:

```bash id="h5tr8m"
git status
```

Displays:

* Modified files
* Staged files
* Untracked files
* Branch information

---

# 7. Adding Files

Add a single file:

```bash id="m8dy1q"
git add app.py
```

Add all files:

```bash id="c9pw2r"
git add .
```

---

# 8. Committing Changes

Create a commit:

```bash id="u3vz5k"
git commit -m "Add login feature"
```

Commit messages should be:

* Short
* Descriptive
* Meaningful

Examples:

```bash id="y7lx9a"
feat: add authentication API
fix: resolve login issue
docs: update README
```

---

# 9. Viewing Commit History

Display history:

```bash id="r4mh1v"
git log
```

Compact history:

```bash id="k6pt7s"
git log --oneline
```

Graph view:

```bash id="z1cb5x"
git log --graph --oneline
```

---

# 10. Git Branching

View branches:

```bash id="s8qy2m"
git branch
```

Create branch:

```bash id="o5je7t"
git branch feature-login
```

Switch branch:

```bash id="a2nm4w"
git checkout feature-login
```

Create and switch:

```bash id="l9wk3q"
git checkout -b feature-login
```

---

# 11. Branching Strategy

TechNova follows GitFlow.

Permanent branches:

```text id="p4tz7d"
main
develop
```

Temporary branches:

```text id="q7va5k"
feature/*
bugfix/*
release/*
hotfix/*
```

Examples:

```text id="j8fn2y"
feature/payment-api
bugfix/login-error
release/v1.0
hotfix/security-patch
```

---

# 12. Merging Branches

Merge a branch:

```bash id="d5ru9n"
git checkout develop
git merge feature-login
```

Benefits:

* Preserve history
* Integrate features
* Support collaboration

---

# 13. Merge Conflicts

Example conflict:

```text id="x6vp4r"
<<<<<<< HEAD
Current changes
=======
Incoming changes
>>>>>>> branch
```

Resolution steps:

1. Open conflicting file.
2. Resolve conflicts.
3. Save file.
4. Add changes.
5. Commit merge.

---

# 14. Rebasing

Rebase command:

```bash id="e1my8q"
git rebase develop
```

Benefits:

* Cleaner history
* Linear commits
* Easier debugging

---

# 15. Stashing Changes

Save temporary changes:

```bash id="b7hk3v"
git stash
```

View stash:

```bash id="y4qc8n"
git stash list
```

Restore stash:

```bash id="g2re5k"
git stash pop
```

---

# 16. Remote Repositories

Add remote:

```bash id="w9fa6m"
git remote add origin https://github.com/company/project.git
```

View remotes:

```bash id="f3mn7x"
git remote -v
```

---

# 17. Pushing Changes

Push branch:

```bash id="t6qv4j"
git push origin main
```

Push feature branch:

```bash id="h7rd2s"
git push origin feature-login
```

---

# 18. Pulling Changes

Fetch and merge:

```bash id="m4sx8z"
git pull origin main
```

Fetch only:

```bash id="v8dy1f"
git fetch
```

---

# 19. Cloning Repositories

Clone repository:

```bash id="u5kn9m"
git clone https://github.com/company/project.git
```

Example:

```bash id="z3xc6a"
git clone https://github.com/Aditimore11/project.git
```

---

# 20. Undoing Changes

Restore file:

```bash id="p9fh2q"
git restore app.py
```

Undo commit:

```bash id="n1vj7w"
git revert HEAD
```

Reset:

```bash id="c6tm5x"
git reset --hard HEAD~1
```

---

# 21. Tags

Create tag:

```bash id="k8ru1p"
git tag v1.0.0
```

Push tag:

```bash id="y2ws4d"
git push origin v1.0.0
```

List tags:

```bash id="a5pm8r"
git tag
```

---

# 22. Pull Requests

Pull requests require:

* Description
* Reviewer assignment
* Test results
* Screenshots
* Documentation updates

Review criteria:

* Code quality
* Security
* Performance
* Maintainability

---

# 23. GitHub Features

GitHub provides:

* Repositories
* Pull requests
* Issues
* Projects
* Discussions
* Actions
* Wiki
* Releases

---

# 24. GitHub Actions

Example workflow:

```yaml id="f4bz9n"
name: CI

on: [push]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4
```

Benefits:

* Automation
* Testing
* Deployment
* Security scanning

---

# 25. Repository Protection Rules

Protected branches:

```text id="q3jh7p"
main
develop
```

Protection rules:

* Pull requests required
* Approval required
* Status checks required
* No force push

---

# 26. Git Best Practices

Developers should:

* Commit frequently
* Write meaningful messages
* Pull before pushing
* Create feature branches
* Avoid force pushes
* Review code carefully
* Use tags for releases

---

# 27. Common Git Commands

| Command    | Purpose             |
| ---------- | ------------------- |
| git init   | Create repository   |
| git add    | Stage files         |
| git commit | Save changes        |
| git push   | Upload changes      |
| git pull   | Download changes    |
| git clone  | Copy repository     |
| git branch | Manage branches     |
| git merge  | Merge branches      |
| git rebase | Rebase changes      |
| git stash  | Save temporary work |

---

# 28. Common Mistakes

Avoid:

* Direct commits to main
* Force pushing
* Large commits
* Hardcoded secrets
* Ignoring merge conflicts
* Poor commit messages

---

# 29. Practical Exercises

Students must complete:

* Create repository
* Create branches
* Resolve conflicts
* Create pull requests
* Merge branches
* Tag releases
* Configure GitHub Actions

---

# 30. Assessment

Evaluation criteria:

| Component      | Weightage |
| -------------- | --------- |
| Assignments    | 20%       |
| Practical Labs | 40%       |
| Final Project  | 30%       |
| Viva           | 10%       |

Minimum passing score:

```text id="m7dw2v"
70%
```

---

# 31. Frequently Asked Questions

### Q1. Can developers commit directly to main?

No.

### Q2. Is GitHub Actions mandatory?

Yes, for CI/CD projects.

### Q3. Are pull requests required?

Yes.

### Q4. Should developers use feature branches?

Yes.

### Q5. Is force push allowed?

No, on protected branches.

---

# 32. Training Ownership

This Git and GitHub Training Manual is maintained jointly by the Learning & Development Department, Engineering Department, and DevOps Team of TechNova Solutions Pvt. Ltd.
