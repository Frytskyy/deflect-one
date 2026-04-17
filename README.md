# Deflect One

**Agentless DevOps command center for your entire Linux infrastructure - from one terminal.
No agents. No cloud. No SaaS. Just SSH access - and Deflect One turns that into a complete operations platform: server monitoring, active attack detection, file management, deployments, and more. AI support is available as an optional add-on.**

No agents to install on servers. No cloud. No SaaS. Just SSH access - and Deflect One turns that into a complete operations platform.

From server health monitoring to active attack detection, from deployment orchestration to natural-language command execution via built-in AI - Deflect One combines DevOps observability, cybersecurity response, and LLM-powered decision support into a single, self-contained Python file.

> **Beta** - actively developed.

---

## Main Dashboard

![Main Dashboard](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-main.png)

---

## Features

### Real-Time Infrastructure Monitoring
CPU, RAM, disk, network I/O, Docker containers, MySQL/PostgreSQL/Redis - across unlimited servers simultaneously. Async-native coroutine pool, near-zero overhead.

![Cross-Host Process Monitor](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-cross-host-process-monitor.png)
![DB Monitor](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-db-monitor.png)
![Connections Viewer](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-connections-viewer.png)

---

### Active Attack Detection & Defense
Live attack radar: malicious IPs, geo-location, timeline. Manages UFW/iptables rules. Defense mode executes bans, restarts, and rate limits autonomously within your policy.

![Firewall Manager](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-host-firewall-manager.png)
![Firewall Manager - Rules](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-host-firewall-manager2.png)
![Ban IP](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-ban-ip.png)

---

### Package & System Management
Full apt integration: view available updates, security patches, and install packages - across all hosts from one screen.

![APT Update Manager](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-apt-upd-manager.png)
![APT Package Installer](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-apt-package-installer.png)

---

### Docker & Services
Manage containers, images, and systemd services without leaving the terminal.

![Docker Manager](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-docker-mgr.png)
![Services Manager](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-services-manager.png)

---

### File Manager
Dual-panel SFTP/SSH file manager - browse, upload, download, edit, copy files between hosts. Midnight Commander style.

![File Manager](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-file-manager.png)

---

### Log Aggregation & Journal Viewer
Cross-host regex log search and live journalctl tailing with 8 preset tabs.

![Cross-Host Log Filtering](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-cross-hosts-logs-filtering.png)
![Journal Viewer](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-host-journal-viewer.png)

---

### Email Monitor
MTA queue monitoring, account overview, error rates - across all hosts.

![Email Monitor](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-email-monitor.png)
![Email Queue Manager](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-email-maanger-queue.png)

---

### Fleet & Bulk Operations
Manage your entire server fleet: bulk DevOps commands, SSH key rotation, host management.

![Host Fleet Manager](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-host-fleet-mgr.png)
![Bulk Commands - Select](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-bulk-devops-commands-select.png)
![Bulk Commands - Result](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-bulk-devops-commands-result.png)
![Batch Rotate Keys](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-batch-rotate-keys.png)

---

### 🔧 More Tools
Cron & systemd timer management, network reconnaissance, script runner, config export.

![Cron Manager](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-cron-mgr.png)
![Network Recon](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-hosts-network-recon.png)
![Script Runner](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-scripts-runner.png)
![Tools](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-tools.png)
![Config Export](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-config-export.png)

---

### AI-Enhanced Autonomous Operations (experimental, optional)
Unified AI engine: Claude, GPT-4, Gemini, Mistral, Groq, LM Studio. Per-host LLM instructions enable background governance loops - *"restart /home/bot1/BotService if /home/bot1/tests.log file is older than one day"* - running 24/7 without you watching.

![AI-Driven Operations](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-ai-driven2.png)
![AI SSH Session](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-ssh-ai-driven.png)
![AI SSH Sample](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-ssh-ai-sample.png)
![Host AI Settings](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-host-ai-settigns.png)
![AI Settings](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-settings-ai.png)
![AI Stats](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-ai-stats.png)

---

### 💬 Natural-Language Command Terminal
`Ctrl+A` → describe what you want in plain English → Deflect One translates to CLI/SSH/Bash and executes it.

---

### Some fun
But why not?

![Deflect key](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/deflect-key.jpg)

---

## Installation

```bash
# Install via pip
pip install deflect-one
deflect --demo    # demo mode, no SSH required
deflect           # real mode
```

```bash
# Or run directly without installing
pip install textual paramiko cryptography
python deflect.py --demo
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
Linux · macOS (Intel + Apple Silicon) · Windows (Windows Terminal and Cmd) · WSL2  
*Any OS that runs Python 3.10+*

**Manages (remote servers):**  
Debian · Ubuntu - primary targets, fully tested  
Fedora · CentOS · Arch · Alpine - works via SSH, not all features tested yet

---

## Tech Stack

- **Python 3.10+** · **Textual 8.x** (TUI) · **asyncio** · **paramiko** (SSH)
- **cryptography** - Fernet + PBKDF2 for HardwareVault
- **AI backends:** `anthropic` · `openai` · `google-generativeai` · `mistralai` *(all optional, experimental)*

---

## License

MIT License with Attribution Requirement.  
Free for personal and commercial use. Attribution to [vladonai.com/deflect](https://vladonai.com/deflect-one) required.

---

*Created by [Volodymyr Frytskyy (WhitemanV)](https://vladonai.com/deflect)*
