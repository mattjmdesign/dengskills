---
name: git-workflow-planner
description: Plan a safe Git workflow for product teams, design engineers, and AI agents working in the same repository. Use when deciding branch strategy, PR slicing, commit conventions, dev/main flow, redesign coordination, git worktrees, feature branches, agent branches, locks, review rules, or merge policy.
---

# Git Workflow Planner

Use this skill when multiple contributors or agents may touch the same product surface. The goal is to keep the app deployable while features, redesigns, and refactors happen in parallel.

## Process

1. Identify team shape: solo, designer+agent, small team, client team, or multi-agent workflow.
2. Recommend branch model: production branch, integration branch, short-lived feature/fix branches, and agent branch prefix.
3. Define PR slicing rules: visual, behavior, content, infrastructure, and data changes should be reviewable separately unless a vertical slice requires integration.
4. Recommend worktrees when old and new UI must be compared side by side.
5. Define commit message convention and merge policy.
6. Define agent-safe rules: allowed files, do-not-edit lock file, human review, and feature-flag expectations.
7. Produce a workflow checklist.

## Output format

```markdown
## Git workflow plan

**Recommended branch model:**

**Branch naming:**

**PR slicing rules:**

**Commit convention:**

**Agent branch policy:**

**Worktree recommendation:**

**Review and merge policy:**

**Coordination artifacts:**

**Workflow checklist:**
```

## Guardrails

- Keep branches short-lived; if a branch exceeds a few days, split the work.
- Never merge agent-generated code without human review.
- Separate visual-only changes from behavior/data changes unless the PR is an intentional vertical slice.
