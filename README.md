# Deflect One

**v0.78 - AuthSentinel: Multi-Protocol Authentication Intelligence + Enhanced ServerCard UX + First-Run Onboarding**

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

### AuthSentinel - Multi-Protocol Authentication Intelligence
**Unified surveillance across SSH, sudo, databases, mail, FTP, and web panels.** Live auth event stream with anomaly detection (brute force, credential stuffing, impossible travel, privilege escalation chains). Session activity forensics: SSH command history, live SQL queries, SMTP envelope inspection. Per-host auth health scoring. sshd hardening auditor with auto-fix. One-click P1 containment workflow: block IP → kill session → disable account → rotate credentials.

![AuthSentinel - Live Event Feed](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-auth-sentinel-events-list.png)
![AuthSentinel - Fleet Statistics](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-auth-sentinel-stats.png)
![AuthSentinel - Activity Heatmap](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-auth-sentinel-heatmap.png)

---

### Enhanced Server Cards
Health score badges (0-100 with color gradient). Inline Docker container list with status navigation. Hostname pinned to card title. CPU/RAM trend arrows. Keyboard shortcuts and card reordering.

---

### First-Run Onboarding & Host Management
Welcome screen on cold launch: demo mode, add host, or import from `~/.ssh/config`. SSH config sync with credential write-back (backup included). Restore deleted hosts from 7-day archive.

### User & Group Administration
Full Linux user and group management over SSH — create, edit, lock accounts, manage SSH keys, view active sessions and audit details. Safety guards prevent accidental self-lockout.

![User & Group Administration](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-users-groups-administration.png)
![User Details](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-admin-user-details.png)
![User Edit](https://raw.githubusercontent.com/Frytskyy/deflect-one/main/screenshot-deflect-admin-user-edit.png)

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

## How Deflect One Compares

If you've used **btop** or **glances** to watch a single server in the terminal - Deflect One is that experience scaled to your entire fleet simultaneously, with management, security response, and deployments on top.

If you've evaluated **Zabbix**, **Checkmk**, or **Wazuh** and turned back because of agent rollout, a dedicated monitoring server, or a week of configuration - Deflect One is the open-source alternative that starts with `pip install deflect-one`.

| | **Deflect One** | Zabbix / Checkmk | Wazuh | Netdata | Cockpit / Webmin | Prometheus + Grafana | Termius | lazydocker | btop / glances |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **No agent to install** | ✅ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ✅ | ✅ | ✅ |
| **Terminal UI - no browser** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ✅ | ✅ | ✅ |
| **Open-source & free** | ✅ | ⚠️ | ✅ | ✅ | ✅ | ✅ | ❌ | ✅ | ✅ |
| **Multi-host fleet view** | ✅ | ✅ | ✅ | ⚠️ | ❌ | ✅ | ⚠️ | ❌ | ❌ |
| **Attack detection & security** | ✅ | ⚠️ | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **File manager (SFTP)** | ✅ | ❌ | ❌ | ❌ | ⚠️ | ❌ | ⚠️ | ❌ | ❌ |
| **Docker management** | ✅ | ❌ | ❌ | ⚠️ | ⚠️ | ❌ | ❌ | ✅ | ⚠️ |
| **Built-in AI assistant** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ |
| **`pip install` - up in 10s** | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ❌ | ⚠️ |

> ⚠️ = partial support or paid tier required

**Zabbix / Checkmk** - enterprise-grade monitoring, but requires an agent on every host, a dedicated server to run on, and days of setup before you see a single metric.  
**Wazuh** - serious security SIEM with strong detection, but it's an enterprise deployment project, not a tool you run from your laptop.  
**Netdata** - excellent real-time graphs on a single host, but can't manage, deploy to, or actively defend your servers.  
**Cockpit / Webmin** - web panels that manage one host at a time through a browser tab, and must be installed on each managed server.  
**Prometheus + Grafana** - the standard metrics stack, but a multi-component engineering project before you see your first dashboard; no management or security layer.  
**Termius** - polished SSH client with multi-host bookmarks, but it's a paid SaaS product with no monitoring, no security, and no management beyond the shell.  
**lazydocker** - great Docker TUI, but single-host only; exits the picture the moment you need anything beyond containers.  
**btop / glances** - the best single-host terminal monitors available. Deflect One brings that same instant terminal visibility across your entire fleet at once - and adds management, active security response, file transfers, deployments, and AI.

Deflect One is the only open-source tool that ships real-time monitoring, active attack defense, full system management, and AI in a single `pip install` - with no agents, no browser, and no separate infrastructure to maintain.

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

### Global Navigation

| Key | Action |
|-----|--------|
| `Tab` / `Shift+Tab` | Next / previous panel |
| `←` `→` | Switch between ServerCards |
| `↑` `↓` | Select row (Attack Radar or Services panel) |
| `q` / `F10` | Quit |

### Function Keys

| Key | Screen | Notes |
|-----|--------|-------|
| `F1` | Help | All shortcuts, version, donate link |
| `F2` | SSH Shell | Interactive paramiko shell · `F8` AI Hints · `F9` AI Command · `Ctrl+F` File Manager |
| `F3` | Log Tail | 8 sources: Journal · Auth · Nginx · Apache · Email · Fail2ban · UFW · Syslog · `Ctrl+←/→` switch source |
| `F4` | Disk Usage | Drill-down: top-10 dirs, ETA to full |
| `F5` | Port Forwards | SSH tunnel editor ⚠️ |
| `F6` | Settings | General · Notifications · Security · 🤖 AI ⚠️ |
| `F7` | Ban Last IP | Ban most recent attacker from any panel |
| `F8` | APT Upgrades | Upgradable packages per host, OS/kernel info |
| `F9` | Fleet Manager | All hosts, checkboxes, bulk ops, 🤖 AI Audit All |

> ⚠️ Windows Terminal intercepts `F5` and `F6` - disable its system shortcuts to use them.

### Infrastructure

| Keys | Screen | Notes |
|------|--------|-------|
| `Ctrl+B` | Network Connections | `ss -tnp`, state filters, anomaly summary |
| `Ctrl+D` | Docker | Containers, images, resource usage · RunWizard · PortEditor · RenameDialog |
| `Ctrl+E` | Env / Config Audit | `.env` diff between hosts, SSH key audit |
| `Ctrl+F` | File Manager | Dual-panel Local + SFTP (Midnight Commander style) - see below |
| `Ctrl+G` | Git / Deploy | Repos status, pull, restart service, rollback |
| `Ctrl+L` | Log Aggregation | Cross-host regex grep, 5 presets |
| `Ctrl+M` | Email Security | DKIM · SPF · DMARC · DNSBL · Greylist · SMTP TLS · **[v0.81]** |
| `Ctrl+P` | Process Monitor | Cross-host top, kill PID, OOM events |
| `Ctrl+R` | Network Recon | nmap/dig/whois/traceroute/curl, 11 presets |
| `Ctrl+S` | Script Runner | Library, inline editor, SFTP deploy, cron scheduling · 🤖 AI Generate |
| `Ctrl+T` | Cron & Timers | crontab + systemd timers, CRUD, bulk add |
| `Ctrl+U` | Backup Jobs | Native tar.gz scheduler · **[v0.79]** |
| `Ctrl+W` | Firewall | UFW/iptables rules, add/delete, toggle UFW · 🤖 AI Audit → hardening wizard |
| `Ctrl+Y` | Databases | PostgreSQL · MySQL · Redis · MongoDB |
| `Ctrl+N` | Add Host | New SSH host, per-host 🤖 AI instructions |
| `Ctrl+O` | Edit Host | Security config, all settings, 🤖 AI instructions |
| `Ctrl+Shift+D` | DNS Monitor | Service status, query logs, DNSSEC · DNSZoneEditor · **[v0.79]** |
| `Ctrl+Shift+S` | SpamAssassin | Status, rules lint, Bayes DB, sa-update · **[v0.79]** |
| `Ctrl+Shift+K` | DKIM Manager | Key list, generate, show public key, test · **[v0.81]** |
| `Ctrl+Shift+B` | DNSBL Check | Spamhaus · SpamCop · SORBS · CBL · Barracuda · PSBL per host · **[v0.81]** |

`Ctrl+M` tabs: `1` DKIM · `2` SPF · `3` DNSBL · `4` Greylist · `5` Relay · `6` SvcCtrl

`Ctrl+U` keys: `Enter`/`r` run now · `t` toggle · `d` delete · `Esc` close · `Ctrl+F` File Manager · `K` FM with backup panel

`Ctrl+Shift+D` sub-key: `z` DNS Zone Editor (BIND zones, records, `rndc reload`)

### Security & AI

| Keys | Screen | Notes |
|------|--------|-------|
| `Ctrl+A` | 🤖 AI Chat | Streaming conversation with full host context · **[v0.75]** |
| `Ctrl+H` | Auth Sentinel | Multi-protocol authentication intelligence · **[v0.78]** |
| `Ctrl+I` | 🤖 AI Stats | Token usage by tier/day, provider info, 7-day breakdown |
| `Ctrl+J` | User & Group Admin | Linux users, groups, SSH keys, active sessions · **[v0.78+]** |
| `Ctrl+K` | Secrets Vault | View/edit encrypted secrets, export/import with password |

### Auth Sentinel (`Ctrl+H`) - tabs & keys

| Tab | Content |
|-----|---------|
| Tab 1 | Live auth event feed · Active sessions · Threat summary |
| Tab 2 | Fleet auth stats · Protocol breakdown · 24h×7d heatmap |
| Tab 3 | sshd_config hardening auditor (CIS Benchmark) |
| Tab 4 | Mail abuse monitor (queue flood, bounce spike) |

`v` SessionActivityInspector · `c` ContainmentDialog · `t` IncidentTimeline · `b` ban IP fleet-wide · `a` 🤖 AI Auth Intel · `l` raw logs · `s`/`f` filter success/failed · `r` back to Attack Radar

### User & Group Admin (`Ctrl+J`) - tabs & keys

| Tab | Keys |
|-----|------|
| Users | `a` add · `e` edit · `l` lock/unlock · `K` SSH keys · `h` shell · `c` contain |
| Groups | `a` add · `e` edit · `Del` delete |
| Keys | `g` generate · `a` append · `o` full rotation · `Del` remove |

`←`/`→` switch host · Tabs: Users · Groups · Keys · Watched Sessions · Details

### File Manager (`Ctrl+F`) - keys

`Tab` switch panel · `Ctrl+U` swap panels · `Alt+C` quick CD · `Ins`/`Space` toggle select · `^A` select all · `\` deselect all  
`F2` rename · `F3` view · `F4` edit · `F5` copy · `F6` move · `F7` mkdir · `F8` delete  
`s` create/edit symlink · `Ctrl+Z` attributes (chmod/chown/touch) · `^1`/`^2`/`^3` sort by name/size/date (again to reverse)  
`Ctrl+D` favourite locations · `K` create backup job (left=src, right=dst)  
Transfer queue: `P` pause/resume · `C` cancel · `Del` clear done

### Server Card shortcuts (when a card is focused) - [v0.78]

`Click` focus · `Double-click` open Docker/Process · `o` edit host · `a` toggle AI-controlled · `m` toggle maintenance  
`p` Process monitor · `d` Docker navigation (↑↓ select · `Enter` open · `Esc` exit) · `F2` SSH shell · `f`/`Ctrl+F` File Manager  
`Ctrl+←/→/↑/↓` reposition card in grid

### Attack Radar (when focused)

`↑`/`↓` select IP row · `Enter`/`b` ban selected IP · `a` 🤖 AI analysis of selected event **[v0.75]**

### Services Panel (when focused)

`↑`/`↓` select service row · `r` restart selected service

### Top Menu & Layout (v0.79)

`Click` menu or `Alt+F`/`V`/`H`/`T`/`S` open dropdown · `←`/`→` walk menus · `Esc` close  
`Alt+←/→` resize vertical split (grid ⟷ radar) · `Alt+↑/↓` resize horizontal split (main ⟷ services) · drag splitter  
View menu: toggle Stats / F-Key / Radar / Services panels · force grid columns (1/2/3/Auto) · Compact mode  
All layout preferences saved in `deflect.json` under `"ui"`

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
