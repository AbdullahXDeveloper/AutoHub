# ⚡ AutoHub v3.5
### Abdullah's Personal Command Center

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=flat-square)
![AI](https://img.shields.io/badge/AI-Gemini%20%7C%20Groq%20%7C%20OpenRouter-purple?style=flat-square)
![Themes](https://img.shields.io/badge/Themes-8-orange?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)

> A powerful, animated desktop launcher that puts everything one click away — with built-in AI chat, task management, and 8 gorgeous themes.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🎨 **8 Animated Themes** | Cyberpunk, Matrix, Dracula, Nord, Sunset, Anime, Ocean, Education |
| 🤖 **3-AI Fallback System** | Gemini 2.0 Flash → Groq LLaMA 3.3 70B → OpenRouter Mistral |
| ✅ **Task Manager** | Daily to-do list with carry-forward, progress tracking & logs |
| 🌐 **Site Launcher** | One-click access to YouTube, GitHub, LeetCode, LinkedIn & more |
| 💻 **App Launcher** | Instantly open Chrome, VS Code, Discord, WhatsApp, Teams |
| 📁 **Folder Shortcuts** | Jump to your most-used directories instantly |
| ⚡ **AI Chat Panel** | Integrated chat — open sites, add tasks, change themes via voice |
| 🎆 **Particle Animations** | Matrix rain, bubbles, sakura petals, twinkling stars |
| ⚙️ **Full Settings UI** | Add/remove entries, manage API keys, switch themes, tune effects |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- Windows OS (uses `ctypes`, `subprocess`, `explorer`)

### Installation

```bash
git clone https://github.com/YOUR_USERNAME/autohub.git
cd autohub
python autohub.py
```

No pip installs needed — uses Python standard library only!

---

## 🔑 AI Setup (Optional but Recommended)

AutoHub supports a **3-tier AI fallback** system. Add your API keys in ⚙️ Settings → AI Keys:

| Provider | Model | Get Key |
|---|---|---|
| ✨ Gemini (Primary) | gemini-2.0-flash | [aistudio.google.com](https://aistudio.google.com) |
| ⚡ Groq (Backup) | llama-3.3-70b-versatile | [console.groq.com](https://console.groq.com) |
| 🌐 OpenRouter (Extra) | mistral-7b-instruct:free | [openrouter.ai](https://openrouter.ai) |

All keys are stored **locally** in `config.json` — never sent anywhere except the respective AI API.

---

## 🎨 Themes

| Theme | Vibe | Particles |
|---|---|---|
| ⚡ Cyberpunk | Neon-lit dystopian | Matrix rain |
| 🟩 Matrix | Follow the white rabbit | Matrix rain |
| 🧛 Dracula | Dark & elegant | Bubbles |
| ❄️ Nord | Arctic, clean & minimal | Stars |
| 🌅 Sunset | Warm dusk gradient | Bubbles |
| 🌸 Anime | Sakura & magic vibes | Sakura petals |
| 🌊 Ocean | Deep sea bioluminescence | Bubbles |
| 📚 Education | Clean scholarly notebook | Stars |

---

## 🤖 AI Chat Commands

Talk to the AI panel naturally — it understands Urdu/English mix:

```
open youtube          → Opens YouTube in Chrome
add task study DSA    → Adds task to today's list
change theme Matrix   → Switches to Matrix theme
what time is it?      → Returns current time
```

---

## 📁 Project Structure

```
autohub/
├── autohub.py          # Main application
└── data/               # Auto-created on first run
    ├── config.json     # Your settings & API keys
    ├── tasks/          # Daily task files (JSON)
    └── logs/           # Activity logs
```

---

## 📸 Screenshots
UI
> <img width="669" height="442" alt="image" src="https://github.com/user-attachments/assets/3b195699-bb7f-4e0d-9ac8-c3fa8bda8336" />

Setting
> <img width="451" height="370" alt="image" src="https://github.com/user-attachments/assets/472df53e-eae7-4594-ab61-b8e967a36077" />

---

## 🛠️ Built With

- **Python** — Core language
- **Tkinter** — GUI framework (zero dependencies!)
- **Gemini API** — Primary AI
- **Groq API** — Backup AI (blazing fast)
- **OpenRouter** — Extra AI fallback

---

## 👤 Author

**Muhammad Abdullah**
- 🎓 CS Student @ MAJU University, Karachi

---

## 📄 License

This project is licensed under the MIT License — feel free to use and modify!

---

*Built with ⚡ by Abdullah — because why open 10 windows when one hub does it all?*
