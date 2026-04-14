# Deflect One

**Agentless DevOps command center for your entire Linux infrastructure - from one terminal.
No agents. No cloud. No SaaS. Just SSH access - and Deflect One turns that into a complete operations platform: server monitoring, active attack detection, file management, deployments, and more. AI support is available as an optional add-on.**

No agents to install on servers. No cloud. No SaaS. Just SSH access - and Deflect One turns that into a complete operations platform.

From server health monitoring to active attack detection, from deployment orchestration to natural-language command execution via built-in AI - Deflect One combines DevOps observability, cybersecurity response, and LLM-powered decision support into a single, self-contained Python file.

> ⚠️ **Beta** - actively developed. Core features are stable, new screens added regularly.

---

## Main Dashboard

![Main Dashboard](screenshot-deflect-main.png)

---

## Features

### 📈 Real-Time Infrastructure Monitoring
CPU, RAM, disk, network I/O, Docker containers, MySQL/PostgreSQL/Redis - across unlimited servers simultaneously. Async-native coroutine pool, near-zero overhead.

![Cross-Host Process Monitor](screenshot-deflect-cross-host-process-monitor.png)
![DB Monitor](screenshot-deflect-db-monitor.png)
![Connections Viewer](screenshot-deflect-connections-viewer.png)

---

### 🛡 Active Attack Detection & Defense
Live attack radar: malicious IPs, geo-location, timeline. Manages UFW/iptables rules. Defense mode executes bans, restarts, and rate limits autonomously within your policy.

![Firewall Manager](screenshot-deflect-host-firewall-manager.png)
![Firewall Manager - Rules](screenshot-deflect-host-firewall-manager2.png)
![Ban IP](screenshot-deflect-ban-ip.png)

---

### 📦 Package & System Management
Full apt integration: view available updates, security patches, and install packages - across all hosts from one screen.

![APT Update Manager](screenshot-deflect-apt-upd-manager.png)
![APT Package Installer](screenshot-deflect-apt-package-installer.png)

---

### 🐳 Docker & Services
Manage containers, images, and systemd services without leaving the terminal.

![Docker Manager](screenshot-deflect-docker-mgr.png)
![Services Manager](screenshot-deflect-services-manager.png)

---

### 📁 File Manager
Dual-panel SFTP file manager - browse, upload, download, edit, copy between hosts. Midnight Commander style.

![File Manager](screenshot-deflect-file-manager.png)

---

### 📋 Log Aggregation & Journal Viewer
Cross-host regex log search and live journalctl tailing with 8 preset tabs.

![Cross-Host Log Filtering](screenshot-deflect-cross-hosts-logs-filtering.png)
![Journal Viewer](screenshot-deflect-host-journal-viewer.png)

---

### ✉️ Email Monitor
MTA queue monitoring, account overview, error rates - across all hosts.

![Email Monitor](screenshot-deflect-email-monitor.png)
![Email Queue Manager](screenshot-deflect-email-maanger-queue.png)

---

### ⚙️ Fleet & Bulk Operations
Manage your entire server fleet: bulk DevOps commands, SSH key rotation, host management.

![Host Fleet Manager](screenshot-deflect-host-fleet-mgr.png)
![Bulk Commands - Select](screenshot-deflect-bulk-devops-commands-select.png)
![Bulk Commands - Result](screenshot-deflect-bulk-devops-commands-result.png)
![Batch Rotate Keys](screenshot-deflect-batch-rotate-keys.png)

---

### 🔧 More Tools
Cron & systemd timer management, network reconnaissance, script runner, config export.

![Cron Manager](screenshot-deflect-cron-mgr.png)
![Network Recon](screenshot-deflect-hosts-network-recon.png)
![Script Runner](screenshot-deflect-scripts-runner.png)
![Tools](screenshot-deflect-tools.png)
![Config Export](screenshot-deflect-config-export.png)

---

### 🤖 AI-Enhanced Autonomous Operations
Unified AI engine: Claude, GPT-4, Gemini, Mistral, Groq, LM Studio. Per-host LLM instructions enable background governance loops - *"restart MySQL if slow-query rate exceeds 10/min"* - running 24/7 without you watching.

![AI-Driven Operations](screenshot-deflect-ai-driven2.png)
![AI SSH Session](screenshot-deflect-ssh-ai-driven.png)
![AI SSH Sample](screenshot-deflect-ssh-ai-sample.png)
![Host AI Settings](screenshot-deflect-host-ai-settigns.png)
![AI Settings](screenshot-deflect-settings-ai.png)
![AI Stats](screenshot-deflect-ai-stats.png)

---

### 💬 Natural-Language Command Terminal
`Ctrl+A` → describe what you want in plain English → Deflect One translates to CLI/SSH/Bash and executes it.

---

### Some fun
But why not?

![Deflect key](deflect-key.jpg)
deflect-key.jpg

---

## Installation

```bash
# Minimal (no AI)
pip install textual paramiko cryptography

# Full (with AI support)
pip install textual paramiko cryptography anthropic openai

# Run
python deflect.py --demo    # demo mode, no SSH required
python deflect.py           # real mode, reads deflect.json next to the script
```

**Configure AI:** `F6` → 🤖 AI tab → choose provider → enter API key → Test Connection

---

## Keyboard Shortcuts

| Keys | Screen |
|------|--------|
| `Ctrl+D` | Docker |
| `Ctrl+W` | Firewall (UFW/iptables) |
| `Ctrl+F` | File Manager (SFTP, dual-panel) |
| `Ctrl+A` | AI Chat |
| `Ctrl+L` | Log Aggregation |
| `Ctrl+P` | Process Monitor |
| `Ctrl+Y` | Databases |
| `Ctrl+G` | Deployments |
| `Ctrl+X` | Email Monitor |
| `Ctrl+S` | Script Runner |
| `Ctrl+T` | Cron & Timers |
| `Ctrl+B` | Network Connections |
| `Ctrl+R` | Network Recon |
| `Ctrl+K` | Secrets Vault |
| `F2` | Interactive SSH Shell |
| `F3` | Log Tail (journalctl -f) |
| `F1` | Help (full shortcut list) |

---

## Compatibility

**Runs on (your machine):**  
✅ Linux · ✅ macOS (Intel + Apple Silicon) · ✅ Windows (Windows Terminal) · ✅ WSL2  
*Any OS that runs Python 3.10+*

**Manages (remote servers):**  
✅ Debian 10+ · ✅ Ubuntu 20.04+ - primary targets, fully tested  
🟨 Fedora · CentOS · Arch · Alpine - works via SSH, not all features tested yet

---

## Tech Stack

- **Python 3.10+** · **Textual 8.x** (TUI) · **asyncio** · **paramiko** (SSH)
- **cryptography** - Fernet + PBKDF2 for HardwareVault
- **AI backends:** `anthropic` · `openai` · `google-generativeai` · `mistralai` *(all optional)*

---

## License

MIT License with Attribution Requirement.  
Free for personal and commercial use. Attribution to [vladonai.com/deflect](https://vladonai.com/deflect) required.

---

*Created by [Volodymyr Frytskyy (WhitemanV)](https://vladonai.com/deflect)*
