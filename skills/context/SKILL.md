---
name: context
description: "Create or revise repository instructions using verified commands, paths, architecture constraints, and review expectations."
---

# Agent context

Record what an agent would otherwise guess incorrectly. Read existing context files and their scope before editing; keep one authoritative home for each rule.

## Work

- Verify project purpose, commands, runtime, paths, and architecture from the workspace. Never invent a test command or an existing component.
- Capture consequential boundaries: where secrets and authorization live, who owns cached data, token/component sources, and generated files.
- Include the actual checks and observable evidence expected for the work. Distinguish lint/build from rendered or behavioral verification.
- Separate durable conventions from task-specific plans. Link focused supporting docs instead of embedding complete manuals.
- Reconcile contradictions and stale instructions, including blanket lockfile bans, duplicate formatting stacks, and obsolete paths. Preserve explicit user policies unless asked to change them.
- Match the client and file format already in use. If adding client-specific discovery rules, verify current client documentation; do not claim every client loads every filename.

## Deliver

Update the requested file, or provide a ready-to-use draft when edits were not requested. Usually include purpose, commands, important paths, non-obvious constraints, and verification. Omit empty sections and generic coding advice.

Example: “Tokens live in app/globals.css. Docs styles consume them in app/docs-theme.css. Run pnpm build to validate MDX routes.” This is more useful than “write clean code.”

Check every referenced local command and path; label external or future dependencies. The file guides authorized work, not permission to publish or expand a task.
