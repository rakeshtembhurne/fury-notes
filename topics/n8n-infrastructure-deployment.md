---
created: 2026-05-19
tags: [topics, automation, n8n, self-hosting, infrastructure]
source: YouTube transcripts
---

# n8n Infrastructure & Deployment

## Deployment Options

### 1. Cloud (n8n.io)
- 14-day free trial
- Managed hosting
- Quick start, no setup

### 2. Docker (Recommended)
```bash
docker run -d --name n8n -p 5678:5678 n8nio/n8n
```
- Lightweight, portable
- No messy installations
- Isolated environment
- Easy to manage

### 3. Coolify (Free Self-Hosted)
- One-click n8n deployment
- Free alternative to Render/Railway
- No server sleep issues
- Better than middleman platforms

### 4. AWS EC2 + Docker (Truly Free)
- **750 hours/month free tier** (12 months)
- = 31 days continuous runtime
- Direct AWS, no middleman
- No sleep on inactivity
- Full Docker capabilities
- Setup: EC2 instance → Docker → n8n container

## Why Self-Host?

| Benefit | Description |
|---------|-------------|
| Cost | Free vs $500/month Zapier |
| Privacy | Local, private data |
| Control | No limitations |
| Flexibility | Custom integrations |
| Open Source | Community support |

## n8n vs Alternatives

| Platform | n8n | Make.com | Zapier |
|----------|-----|----------|--------|
| Cost | Free/self-host | $$ | $$$ |
| Integrations | 500+ | 1000+ | 5000+ |
| AI Native | Yes | Some | Limited |
| Customization | High | Medium | Low |
| Learning Curve | Medium | Low | Low |

## MCP with n8n

Model Context Protocol enables:
- Standardized tool execution
- Direct AI-to-tool connectivity
- No HTTP request complexity
- Faster, smarter automation

### Docker + MCP Setup
1. Install Docker Desktop
2. Pull n8n image
3. Configure MCP
4. Enable dynamic tool execution

## n8n Architecture Basics

- **Trigger Nodes**: Start workflows (manual, schedule, webhook)
- **Action Nodes**: Process data
- **AI Nodes**: Agents, chat, embeddings
- **Integration Nodes**: Connect to external services
- **Code Nodes**: Custom logic

## Security Best Practices

1. Use environment variables for credentials
2. Enable HTTPS for cloud deployments
3. Regular backups of workflows
4. Access controls and permissions
5. VPN for remote access

## Homelab Integration

n8n can manage:
- UniFi (networking)
- Proxmox (VMs)
- Plex (media)
- NAS (storage)
- CLI/API accessible services

AI Agent ("Terry") can:
- Monitor services
- Troubleshoot issues
- With permission, auto-fix problems

## Resources

- n8n GitHub: Open source codebase
- n8n Templates: 3000+ pre-built workflows
- Community nodes: Extended functionality

---
**Sources**: NetworkChuck, Eric Tech, Josh Pocock, Zero2Launch, Fireship
