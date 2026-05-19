---
created: 2026-05-19
tags: [topics, skills, ai-agents, architecture, research]
source: notes directory
---

# skill.sh Research: AI Agent Skills Distribution

## Summary

**skill.sh domain is parked** (not operational). However, extensive research reveals the **actual skills distribution ecosystem** currently used by Claude Code and compatible AI agents (Gemini CLI, Cursor, Windsurf, Pi, etc.).

---

## Current Skills Architecture (Real Implementation)

### 1. Installation Mechanism

**CLI Command:**
```bash
npx skills add <OWNER>/<REPO> --all
npx skills add <OWNER>/<REPO> --skill <skill-name>
npx skills add <OWNER>/<REPO> --all -a claude-code -a cursor
```

**Storage Locations:**
- **Primary:** `~/.agents/skills/<skill-name>/`
- **Symlinks:** `~/.claude/skills/<skill-name>/` (alias)
- **CLI Access:** `~/.local/bin/<script-name>` (auto-linked executables)

**Installation Flow:**
1. CLI clones/downloads from GitHub (public or private repos)
2. Runs `npm install` to fetch dependencies
3. Creates symlinks for executable scripts → `~/.local/bin/`
4. Makes scripts globally available (no `npm install -g` needed)

---

### 2. File Structure & Format

#### Root Directory Layout
```
skill-repo/
├── SKILL.md              # Metadata + documentation (YAML frontmatter + markdown)
├── package.json          # Standard npm package definition
├── tsconfig.json         # TypeScript config (if used)
├── scripts/              # Executable entry points
│   ├── main-script       # Bash/shell wrapper
│   └── main-script.ts    # TypeScript implementation
├── lib/                  # Helper utilities
├── README.md             # Full documentation
└── .env.example          # Configuration template
```

#### SKILL.md Metadata Format (Frontmatter)
```yaml
---
name: taskhub                          # Unique skill identifier
description: |
  Central task management for AI agents. 
  Use when: creating tasks, listing tasks, updating status
license: MIT
metadata:
  author: skill-creator
  version: 1.0.0
  category: task-management            # Category for discovery
  triggers:                             # Natural language triggers
    - task
    - taskhub
    - add task
    - create task
    - list tasks
---
```

#### package.json Entry Points
```json
{
  "name": "taskhub",
  "version": "1.0.0",
  "type": "module",
  "bin": {
    "taskhub": "./scripts/taskhub"      # Maps command → script path
  },
  "devDependencies": {
    "@types/bun": "latest"
  }
}
```

---

### 3. Multi-Agent Compatibility Strategy

**Supported Agents:**
- Claude Code
- Gemini CLI
- Cursor
- Windsurf
- OpenCode
- Pi

**Compatibility Mechanisms:**

#### A. CLI-Centric Design
- All skills are **command-line executables** (shell or compiled binary)
- Works universally with any agent that has terminal access
- No agent-specific SDK dependencies
- Output formats: `--json`, `--jq` filtering, semantic exit codes

#### B. MCP Server Mode
```bash
muapi mcp serve  # Expose all tools to any MCP-compatible agent
```
- Runs as Model Context Protocol server
- Claude Desktop, Cursor, and MCP agents access tools directly
- Structured JSON Schema input/output definitions

#### C. Shell Script Wrappers
```bash
#!/usr/bin/env bun

// TypeScript script that can be executed directly
// No compilation step needed
```

---

### 4. Custom/Private Skills

#### Creating a Skill

**Step 1: Repository Structure**
```bash
mkdir my-skill && cd my-skill
npm init -y
```

**Step 2: Add SKILL.md**
```yaml
---
name: my-skill
description: What this skill does
metadata:
  category: custom
  triggers:
    - keyword1
    - keyword2
---

# My Skill Documentation
```

**Step 3: Implement CLI**
```bash
# scripts/my-skill (executable wrapper)
#!/usr/bin/env bun
import { main } from './my-skill.ts';
await main(process.argv.slice(2));
```

**Step 4: Update package.json**
```json
{
  "bin": {
    "my-skill": "./scripts/my-skill"
  }
}
```

**Step 5: Push to GitHub (Public or Private)**
```bash
git init
git add .
git commit -m "Initial skill"
git push origin main
```

**Step 6: Install**
```bash
# For public repos
npx skills add username/my-skill --all

# For private repos (requires GitHub auth)
npx skills add username/my-skill --all
```

#### Private Skills Distribution

**GitHub-Based (Recommended):**
- Create private GitHub repo
- Users authenticate with `gh auth login`
- `npx skills add` works seamlessly with private repos
- No central registry needed — GitHub IS the registry

**NPM Package Option:**
```bash
npm publish --access private
# Then install as: npx skills add @scope/my-skill
```

---

### 5. Project Context Detection

**Auto-Configuration File (`.taskhub` pattern)**
```json
{
  "project": "ProjectName",
  "source": "claude-code"
}
```

**How It Works:**
1. CLI walks up directory tree looking for `.taskhub`
2. Automatically inherits settings from root to all subdirectories
3. Explicit `--project` flags override auto-detected values
4. Enables agents to work without repeating context flags

**Implementation for Custom Skills:**
```bash
# Initialize skill context in project
my-skill init --config "my-config.json"

# CLI auto-loads from parent directory
my-skill list  # Uses stored config
```

---

### 6. Real-World Example: Generative-Media-Skills

**Repository:** `SamurAIGPT/Generative-Media-Skills`

**Installation:**
```bash
npx skills add SamurAIGPT/Generative-Media-Skills --all
```

**Structure:**
- **core/**: Primitive CLI tools (muapi wrappers)
- **library/**: Expert skills (cinematography, atomic design, branding)
- **scripts/**: Bash/shell entry points
- **schema_data.json**: Tool definitions and schemas

**Multi-Agent Support:**
- CLI primitives → works everywhere
- MCP server → Claude Desktop + Cursor
- Direct scripts → Gemini CLI, Windsurf

**Features:**
- 100+ AI models accessible via CLI
- Structured JSON output for agentic pipelines
- `--view` flag to auto-display results
- `--output-json` for CI/CD and scripting

---

## Architecture Comparison

| Aspect | Implementation |
|--------|----------------|
| **Domain** | skill.sh (parked); actual system is GitHub-based |
| **Installation** | `npx skills add <owner>/<repo>` |
| **Storage** | `~/.agents/skills/<name>/` + `~/.local/bin/` symlinks |
| **Format** | YAML frontmatter in SKILL.md + standard npm package |
| **Compatibility** | CLI-first; optional MCP server for modern agents |
| **Private Skills** | GitHub private repos (auth required) |
| **Distribution** | GitHub repos (public/private) or npm packages |
| **Config** | `.{skillname}` files in project root (auto-detected) |
| **Scripting** | Bash, TypeScript, or any compiled binary |

---

## Key Insights

### Design Philosophy
1. **CLI-centric** — maximize compatibility across all agents
2. **No central registry** — GitHub IS the distribution channel
3. **Composable** — skills are independent CLI tools chained together
4. **Self-documenting** — SKILL.md metadata drives discovery and triggers

### Multi-Agent Strategy
- **Common layer:** Shell scripts + JSON I/O
- **Modern layer:** MCP server for direct tool access
- **Legacy layer:** Exit codes + STDOUT for any CLI-capable agent

### Extensibility
- Custom skills follow same pattern as official skills
- No special privileges or signing required
- Private repo support built-in via GitHub auth
- Each skill is independently versioned and deployed

---

## How to Create Compatible Skills

1. **Create GitHub repo** (public or private)
2. **Add SKILL.md** with metadata frontmatter
3. **Implement scripts/** with CLI tools
4. **Add package.json** with `"bin"` entry points
5. **Push to GitHub**
6. **Users install:** `npx skills add <owner>/<repo>`

**That's it.** No central approval, no registry, no complex tooling.

---

## Sources

- **Generative-Media-Skills:** https://github.com/SamurAIGPT/Generative-Media-Skills
- **TaskHub Skill:** `~/.agents/skills/taskhub/SKILL.md`
- **CodePilot (multi-agent client):** https://github.com/op7418/CodePilot
- **shaping-skills (example public skill):** https://github.com/rjs/shaping-skills
