# GitHub Setup Guide

Follow these steps to push the Portico RAG project to GitHub.

## Prerequisites

- GitHub account
- Git installed locally
- GitHub Personal Access Token (PAT) or SSH key configured

## Step 1: Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `portico-rag`
3. Description: "RAG-based Policy Q&A system for Portico communities"
4. Visibility: **Private** (unless approved to be public)
5. Click "Create repository"

## Step 2: Initialize Local Repository

From the project root:

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "feat: Initial RAG system with policy documents, FastAPI backend, and Streamlit UI"

# Rename branch to main (if needed)
git branch -M main

# Add remote
git remote add origin https://github.com/yourusername/portico-rag.git

# Push to GitHub
git push -u origin main
```

## Step 3: Protect Main Branch

1. Go to repository Settings → Branches
2. Click "Add rule"
3. Branch name pattern: `main`
4. Enable:
   - ✓ Require pull request reviews
   - ✓ Require status checks
   - ✓ Require branches to be up to date

## Step 4: Add Collaborators

1. Settings → Collaborators
2. Add team members with appropriate access:
   - Maintainers: Write access
   - Contributors: Pull request only
   - Reviewers: Read access

## Step 5: Setup CI/CD (Optional)

Create `.github/workflows/tests.yml`:

```yaml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - uses: actions/setup-python@v2
        with:
          python-version: "3.11"
      - run: pip install -r requirements.txt
      - run: python -m pytest tests/
```

## Step 6: Documentation Updates

After pushing, update:

1. `README.md` — Change repo URL
2. `GETTING_STARTED.md` — Add clone instructions
3. `CONTRIBUTING.md` — Add contribution guidelines

## Step 7: GitHub Actions Secrets

If using CI/CD, add secrets:

1. Settings → Secrets and variables → Actions
2. Add:
   - `ANTHROPIC_API_KEY`
   - `PINECONE_API_KEY`

## Step 8: Enable Discussions (Optional)

1. Settings → General → Features
2. Enable "Discussions"
3. For Q&A and feedback from team

## Useful Git Commands

```bash
# View commit history
git log --oneline

# Create a new branch for feature work
git checkout -b feature/new-feature-name

# Merge feature back to main
git push origin feature/new-feature-name
# Then create Pull Request on GitHub

# Keep fork in sync (if forked)
git fetch upstream
git merge upstream/main

# Tag releases
git tag -a v1.0.0 -m "Initial release"
git push origin v1.0.0
```

## Commit Message Format

Follow conventional commits:

```
feat: Add new feature
fix: Bug fix
docs: Documentation update
test: Test additions
refactor: Code refactoring
chore: Maintenance
```

Example:
```bash
git commit -m "feat: Add document filtering by policy category"
git commit -m "fix: Handle null responses from API"
git commit -m "docs: Update deployment guide"
```

## Code Review Checklist

Before merging, ensure:

- [ ] Code follows project style guide
- [ ] Tests pass (if applicable)
- [ ] Documentation is updated
- [ ] No sensitive data in commits
- [ ] Commit messages are clear
- [ ] PR description explains changes

## Future Enhancements

- [ ] Add automated testing
- [ ] Setup code coverage reporting
- [ ] Configure dependency scanning
- [ ] Add security vulnerability scanning
- [ ] Setup automated deployments

---

**Repository created!** 🎉

Next: Deploy to Hugging Face Spaces (see HUGGINGFACE_DEPLOY.md)
