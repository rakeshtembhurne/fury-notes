---
created: 2026-05-19
tags: [topics, skills, claude-code, tutorial, implementation]
source: notes directory
---

# Creating AI Agent Skills — Implementation Guide

> Related: [[claude-code-skills]] · [[vibe-coding]] · [[skills-sh-research]] · [[claude-code-self-improving-skills]]

Quick start for building skills that work with Claude Code, Gemini CLI, Cursor, and other AI agents.

---

## Minimal Skill Template

```bash
mkdir my-skill && cd my-skill
```

### 1. SKILL.md
```yaml
---
name: my-skill
description: |
  Brief description of what this skill does.
  Use when: specific use cases
license: MIT
metadata:
  author: your-name
  version: 1.0.0
  category: utility
  triggers:
    - my-skill
    - skill-keyword
---

# My Skill

Full documentation goes here.

## Usage

\`\`\`bash
my-skill command --arg value
\`\`\`
```

### 2. package.json
```json
{
  "name": "my-skill",
  "version": "1.0.0",
  "type": "module",
  "bin": {
    "my-skill": "./scripts/my-skill"
  }
}
```

### 3. scripts/my-skill
```bash
#!/usr/bin/env bun
import { handler } from './my-skill.ts';
await handler(process.argv.slice(2));
```

### 4. scripts/my-skill.ts
```typescript
export async function handler(args: string[]) {
  const command = args[0];
  const rest = args.slice(1);
  
  switch (command) {
    case 'list':
      console.log(JSON.stringify({ items: [] }, null, 2));
      break;
    case 'help':
      console.log('Usage: my-skill <command> [options]');
      break;
    default:
      console.error(`Unknown command: ${command}`);
      process.exit(1);
  }
}
```

### 5. Make Scripts Executable
```bash
chmod +x scripts/my-skill
```

---

## Installation & Testing

```bash
# Test locally
npx scripts/my-skill list

# Install globally (for testing)
npm link

# Now available as: my-skill list
```

---

## GitHub Distribution

```bash
git init
git add .
git commit -m "Initial skill"
git remote add origin https://github.com/username/my-skill
git push -u origin main
```

**Public install:**
```bash
npx skills add username/my-skill --all
```

**Private install (requires GitHub auth):**
1. Create private repo
2. Users run: `gh auth login` (if not already authenticated)
3. Then: `npx skills add username/my-skill --all`

---

## Key Patterns

### CLI Design Rules
1. **Expect JSON output** — agents will parse it
2. **Use `--json` flag** — for structured machine output
3. **Always exit with codes** — 0 for success, 1+ for errors
4. **Use stdout for data** — stderr for errors/logs
5. **Single responsibility** — one command = one task

### Example: Task Management Skill
```bash
my-task add "Fix bug" --priority=high --project=MyApp
# Outputs JSON

my-task list --json
# Outputs: [ { id: "...", name: "...", status: "..." } ]

my-task update abc123 --status=done
# Exits: 0 (success)
```

### Auto-Config Pattern (.myskill)
```json
{
  "default_project": "MyApp",
  "api_key": "***"
}
```

**Code:**
```typescript
import * as fs from 'fs';
import * as path from 'path';

function loadConfig() {
  let cwd = process.cwd();
  while (cwd !== '/') {
    const configPath = path.join(cwd, '.myskill');
    if (fs.existsSync(configPath)) {
      return JSON.parse(fs.readFileSync(configPath, 'utf-8'));
    }
    cwd = path.dirname(cwd);
  }
  return {};
}
```

---

## MCP Server (Optional)

For modern agents (Claude Desktop, Cursor) that support Model Context Protocol:

```typescript
// scripts/my-skill-mcp.ts
import Anthropic from '@anthropic-ai/sdk';

const client = new Anthropic();

const tools = [
  {
    name: 'my_skill_list',
    description: 'List items',
    input_schema: {
      type: 'object',
      properties: {
        status: {
          type: 'string',
          enum: ['all', 'pending', 'done'],
          description: 'Filter by status'
        }
      }
    }
  }
];

export { tools };
```

---

## Multi-Agent Compatibility Checklist

- [ ] Works as CLI tool (executable script)
- [ ] Accepts standard arguments (`--json`, `--help`, etc.)
- [ ] Returns structured output (JSON preferred)
- [ ] Uses exit codes (0 = success, 1+ = error)
- [ ] Works with any shell (bash, zsh, etc.)
- [ ] No GUI, no interactive prompts
- [ ] Documented in SKILL.md with examples
- [ ] package.json defines entry points
- [ ] GitHub repo (public or private)

---

## Real Examples

**Well-designed skills:**
- `taskhub` — CLI + JSON, auto-config file support
- `muapi-cli` — 19 structured tools, MCP + CLI both work
- `find-skills` — Discovers other skills

**Pattern to follow:**
```bash
# Simple interface
skill-name <command> [options]

# Clear output
--json           # Machine-readable
--help           # Documentation
--version        # Version info

# Exit codes matter
0 = success
1 = general error
2 = usage error
```

---

## Publishing Checklist

Before pushing to GitHub:

1. **Documentation**
   - [ ] SKILL.md with clear triggers
   - [ ] README.md with usage examples
   - [ ] Example commands with output

2. **Quality**
   - [ ] All scripts executable (`chmod +x`)
   - [ ] No hardcoded secrets
   - [ ] package.json is valid
   - [ ] Dependencies listed

3. **Testing**
   - [ ] Run `npm link` and test commands
   - [ ] Test `--json` output format
   - [ ] Test error cases
   - [ ] Verify exit codes

4. **License**
   - [ ] LICENSE file included
   - [ ] Listed in package.json

---

## Example: Simple Data Skill

```typescript
// scripts/data-skill.ts
import * as fs from 'fs';

export async function handler(args: string[]) {
  const cmd = args[0];
  
  if (cmd === 'list') {
    const data = [
      { id: '1', name: 'Item 1', status: 'active' },
      { id: '2', name: 'Item 2', status: 'inactive' }
    ];
    console.log(JSON.stringify(data, null, 2));
    process.exit(0);
  }
  
  if (cmd === 'add') {
    const name = args[1];
    console.log(JSON.stringify({ success: true, added: name }, null, 2));
    process.exit(0);
  }
  
  console.error(`Unknown command: ${cmd}`);
  process.exit(1);
}

handler(process.argv.slice(2));
```

That's the complete pattern. Keep it simple. Make it composable. Let agents use it.
