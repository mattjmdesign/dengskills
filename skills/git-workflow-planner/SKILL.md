---
name: git-workflow-planner
description: Use this skill when planning Git collaboration for designers, developers, and AI agents in one repository. Defines branch model, dev/main flow, feature and fix branches, agent branch rules, commit conventions, PR slicing, visual-vs-behavior review separation, worktrees, lock files, feature flags, and merge policy.
---

# Git Workflow Planner

Use this skill when multiple contributors or agents may touch the same product surface. The goal is to keep the app deployable while features, redesigns, and refactors happen in parallel.

## Process

1. Identify team shape: solo, designer+agent, small team, client team, or multi-agent workflow.
2. Recommend branch model: production, integration, short-lived feature/fix branches, and agent branch prefix.
3. Define PR slicing rules: visual, behavior, content, infrastructure, data, and intentional vertical slices.
4. Recommend worktrees when old and new UI must be compared side by side.
5. Define commit convention and merge policy.
6. Define agent-safe rules: allowed files, do-not-edit lock file, human review, and feature-flag expectations.
7. Produce a workflow checklist.

## Output format

```markdown
## Git workflow plan

**Branch model:**
**Branch naming:**
**Commit convention:**

### PR slicing rules
- Visual:
- Behavior/data:
- Content:
- Infrastructure:
- Vertical slice exception:

### Agent policy
- Branch prefix:
- Human review:
- Lock file:
- Allowed scope:

### Worktree recommendation

### Review and merge policy

### Coordination artifacts
- [item]

### Workflow checklist
- [ ] [criterion]
```

## Common mistakes to prevent

- Do not let redesigns live as one long branch.
- Do not mix visual changes and business logic unless it is an intentional, reviewable vertical slice.
- Do not let agents edit files without explicit scope and human review.

## Validate before final

- The branch model keeps `main` production-safe and the integration branch deployable.
- The PR rules explain how to split visual, behavioral, content, and infrastructure changes.
