# ╔══════════════════════════════════════════════════════════════════╗
# ║      AUTOHUB v3.5 — Abdullah's Ultimate Command Center         ║
# ║  8 Themes | 3-AI Fallback | Fixed Cards | Full Settings        ║
# ╚══════════════════════════════════════════════════════════════════╝

import subprocess, tkinter as tk, json, os, math, random, threading
import urllib.request, urllib.error
from tkinter import ttk, messagebox
from datetime import datetime, date, timedelta
import ctypes, sys, time

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(2)
except:
    pass

# ══════════════════════════════════════════════════════════════════
#  DATA PATHS
# ══════════════════════════════════════════════════════════════════
DATA_DIR  = r"C:\Abdullah\Abdullah\My-Drive\Personal-Hub-(Data)"

TASKS_DIR = os.path.join(DATA_DIR, "tasks")
LOGS_DIR  = os.path.join(DATA_DIR, "logs")
CFG_FILE  = os.path.join(DATA_DIR, "config.json")
for d in [DATA_DIR, TASKS_DIR, LOGS_DIR]:
    os.makedirs(d, exist_ok=True)

CHROME  = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROFILE = "Default"

# ══════════════════════════════════════════════════════════════════
#  8 THEMES
# ══════════════════════════════════════════════════════════════════
THEMES = {
    "Cyberpunk": {
        "bg":"#0a0c14","bg2":"#111420","bg3":"#181c2c",
        "card":"#1a1f30","card2":"#222840","border":"#2a3060",
        "accent":"#00e5ff","accent2":"#b44dff","green":"#00ff88",
        "amber":"#ffd700","red":"#ff3366","text":"#e8f0ff","text2":"#6e7aaa",
        "btn_hover":"#1e2845","particle":"#00e5ff","particle2":"#b44dff",
        "name":"⚡ Cyberpunk","particle_style":"matrix","icon":"⚡",
        "description":"Neon-lit dystopian future",
    },
    "Matrix": {
        "bg":"#000900","bg2":"#001100","bg3":"#001800",
        "card":"#001d00","card2":"#002800","border":"#003800",
        "accent":"#00ff41","accent2":"#00cc33","green":"#00ff41",
        "amber":"#88ff00","red":"#ff4400","text":"#ccffcc","text2":"#336633",
        "btn_hover":"#003300","particle":"#00ff41","particle2":"#00aa22",
        "name":"🟩 Matrix","particle_style":"matrix","icon":"🟩",
        "description":"Follow the white rabbit",
    },
    "Dracula": {
        "bg":"#1a1b26","bg2":"#24253a","bg3":"#2a2b40",
        "card":"#2d2e44","card2":"#363750","border":"#44465e",
        "accent":"#bd93f9","accent2":"#ff79c6","green":"#50fa7b",
        "amber":"#f1fa8c","red":"#ff5555","text":"#f8f8f2","text2":"#6272a4",
        "btn_hover":"#383950","particle":"#bd93f9","particle2":"#ff79c6",
        "name":"🧛 Dracula","particle_style":"bubbles","icon":"🧛",
        "description":"Dark & elegant vampire theme",
    },
    "Nord": {
        "bg":"#242933","bg2":"#2e3440","bg3":"#353c4a",
        "card":"#3b4252","card2":"#434c5e","border":"#4c566a",
        "accent":"#88c0d0","accent2":"#81a1c1","green":"#a3be8c",
        "amber":"#ebcb8b","red":"#bf616a","text":"#eceff4","text2":"#7b88a0",
        "btn_hover":"#434c5e","particle":"#88c0d0","particle2":"#81a1c1",
        "name":"❄️ Nord","particle_style":"stars","icon":"❄️",
        "description":"Arctic, clean & minimal",
    },
    "Sunset": {
        "bg":"#16071e","bg2":"#1e0d2a","bg3":"#261234",
        "card":"#2a1438","card2":"#341a46","border":"#4a2060",
        "accent":"#ff6b9d","accent2":"#ffcc44","green":"#44e5a0",
        "amber":"#ffcc44","red":"#ff4466","text":"#fff0f8","text2":"#aa6688",
        "btn_hover":"#3a1a4a","particle":"#ff6b9d","particle2":"#ffcc44",
        "name":"🌅 Sunset","particle_style":"bubbles","icon":"🌅",
        "description":"Warm dusk gradient vibes",
    },
    "Anime": {
        "bg":"#0d001a","bg2":"#150025","bg3":"#1c0030",
        "card":"#200035","card2":"#2a0048","border":"#5500aa",
        "accent":"#ff44cc","accent2":"#44aaff","green":"#44ffaa",
        "amber":"#ffee44","red":"#ff2266","text":"#fff0ff","text2":"#9966cc",
        "btn_hover":"#330055","particle":"#ff44cc","particle2":"#44aaff",
        "name":"🌸 Anime","particle_style":"sakura","icon":"🌸",
        "description":"Sakura petals & magic vibes",
    },
    "Ocean": {
        "bg":"#010d1a","bg2":"#011525","bg3":"#021c30",
        "card":"#042240","card2":"#062c50","border":"#0a4070",
        "accent":"#00cfff","accent2":"#00ffcc","green":"#00ffcc",
        "amber":"#ffe566","red":"#ff4455","text":"#e0f8ff","text2":"#4488aa",
        "btn_hover":"#0a3a60","particle":"#00cfff","particle2":"#00ffcc",
        "name":"🌊 Ocean","particle_style":"bubbles","icon":"🌊",
        "description":"Deep sea bioluminescence",
    },
    "Education": {
        "bg":"#f5f0e8","bg2":"#ece6d8","bg3":"#e0d8c8",
        "card":"#faf6ee","card2":"#ede6d6","border":"#c8b898",
        "accent":"#2244aa","accent2":"#aa2244","green":"#228844",
        "amber":"#cc7722","red":"#cc2233","text":"#1a1a2e","text2":"#5a5a7a",
        "btn_hover":"#d8d0bc","particle":"#2244aa","particle2":"#aa2244",
        "name":"📚 Education","particle_style":"stars","icon":"📚",
        "description":"Clean scholarly notebook",
    },
}

# ══════════════════════════════════════════════════════════════════
#  DEFAULT CONFIG
# ══════════════════════════════════════════════════════════════════
DEFAULT_CFG = {
    "theme":              "Cyberpunk",
    "gemini_api_key":     "",
    "groq_api_key":       "",
    "openrouter_api_key": "",
    "active_ai":          "auto",
    "particle_count":     55,
    "particle_style_override": "",
    "sites": {
        "LeetCode":    ["https://leetcode.com",                   "⚡"],
        "LinkedIn":    ["https://www.linkedin.com/feed/",         "💼"],
        "Kaggle":      ["https://www.kaggle.com/",                "📊"],
        "GitHub":      ["https://github.com/",                    "🐙"],
        "Hugging Face":["https://huggingface.co/",                "🤗"],
        "ChatGPT":     ["https://chatgpt.com/",                   "🤖"],
        "YouTube":     ["https://youtube.com",                    "▶️"],
        "Discord":     ["https://discord.com/app",                "💬"],
        "MS Teams":    ["https://teams.microsoft.com/",           "🟦"],
        "WhatsApp":    ["https://web.whatsapp.com/",              "📱"],
        "Drive":       ["https://drive.google.com/",              "☁️"],
    },
    "apps": {
        "Chrome":   [r"C:\Program Files\Google\Chrome\Application\chrome.exe",             "🌐"],
        "Notepad":  ["notepad.exe",                                                          "📝"],
        "VS Code":  [r"C:\Users\abdul\AppData\Local\Programs\Microsoft VS Code\Code.exe",  "💻"],
        "Discord":  [r"C:\Users\abdul\AppData\Local\Discord\Update.exe --processStart Discord.exe", "💬"],
        "Teams":    [r"C:\Users\abdul\AppData\Local\Microsoft\Teams\Update.exe --processStart Teams.exe", "🟦"],
        "WhatsApp": [r"C:\Users\abdul\AppData\Local\WhatsApp\WhatsApp.exe",                "📱"],
    },
    "folders": {
        "Abdullah":    [r"C:\Abdullah\Abdullah",              "📁"],
        "DataScience": [r"C:\Abdullah\Abdullah\DataScience",  "🔬"],
        "Personal Hub":[DATA_DIR,                             "🏠"],
    },
    "scripts": {
        "Auto TempClean":[r"C:\Users\abdul\Desktop\Automation-HUB\scripts\Auto_TempClean.bat","🧹"],
    },
}

def load_cfg():
    if os.path.exists(CFG_FILE):
        try:
            with open(CFG_FILE,"r",encoding="utf-8") as f: d=json.load(f)
            for k,v in DEFAULT_CFG.items():
                if k not in d: d[k]=v
            if "api_key" in d and not d.get("gemini_api_key"):
                d["gemini_api_key"]=d.pop("api_key","")
            return d
        except: pass
    return dict(DEFAULT_CFG)

def save_cfg(cfg):
    with open(CFG_FILE,"w",encoding="utf-8") as f:
        json.dump(cfg,f,indent=2,ensure_ascii=False)

CFG = load_cfg()

# ══════════════════════════════════════════════════════════════════
#  LOGGING + TASKS
# ══════════════════════════════════════════════════════════════════
def log(msg):
    try:
        with open(os.path.join(LOGS_DIR,f"log_{date.today().isoformat()}.txt"),
                  "a",encoding="utf-8") as f:
            f.write(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}\n")
    except: pass

log("AutoHub v3.5 started")

def today_str():  return date.today().isoformat()
def yest_str():   return (date.today()-timedelta(days=1)).isoformat()
def task_file(d): return os.path.join(TASKS_DIR,f"tasks_{d}.json")

def load_tasks(day):
    p=task_file(day)
    if os.path.exists(p):
        try:
            with open(p,"r",encoding="utf-8") as f: return json.load(f)
        except: pass
    return []

def save_tasks(day,tasks):
    with open(task_file(day),"w",encoding="utf-8") as f:
        json.dump(tasks,f,indent=2,ensure_ascii=False)

def migrate():
    if not os.path.exists(task_file(today_str())):
        carry=[dict(t,carried=True) for t in load_tasks(yest_str()) if not t.get("done")]
        save_tasks(today_str(),carry)
migrate()

# ══════════════════════════════════════════════════════════════════
#  LAUNCH HELPERS
# ══════════════════════════════════════════════════════════════════
def open_site(url):
    try: subprocess.Popen([CHROME,f"--profile-directory={PROFILE}",url]); log(f"Site:{url}")
    except Exception as e: log(f"SiteErr:{e}")

def open_app(path):
    try: subprocess.Popen(path,shell=True); log(f"App:{path}")
    except Exception as e: log(f"AppErr:{e}")

def open_folder(path):
    try: subprocess.Popen(["explorer",path]); log(f"Folder:{path}")
    except Exception as e: log(f"FolderErr:{e}")

def run_script(path):
    try:
        if os.path.splitext(path)[1].lower()==".bat": subprocess.Popen([path],shell=True)
        else: subprocess.Popen([sys.executable,path])
        log(f"Script:{path}")
    except Exception as e: log(f"ScriptErr:{e}")

# ══════════════════════════════════════════════════════════════════
#  ROOT WINDOW
# ══════════════════════════════════════════════════════════════════
root = tk.Tk()
root.title("⚡ AutoHub v3.5 — Abdullah's Command Center")
root.geometry("1340x840")
root.minsize(1100,700)

T = THEMES[CFG.get("theme","Cyberpunk")]
root.configure(bg=T["bg"])

F_LOGO  = ("Consolas",20,"bold")
F_SEC   = ("Consolas",10,"bold")
F_BTN   = ("Segoe UI",9,"bold")
F_SMALL = ("Segoe UI",8)
F_LABEL = ("Segoe UI",9)
F_CHAT  = ("Segoe UI",9)
F_CHATB = ("Segoe UI",9,"bold")
F_CLOCK = ("Consolas",9)

def hex2rgb(h):
    h=h.lstrip("#"); return tuple(int(h[i:i+2],16) for i in (0,2,4))

def blend(c1,c2,t=0.5):
    r1,g1,b1=hex2rgb(c1); r2,g2,b2=hex2rgb(c2)
    return "#{:02x}{:02x}{:02x}".format(
        int(r1+(r2-r1)*t),int(g1+(g2-g1)*t),int(b1+(b2-b1)*t))

# ══════════════════════════════════════════════════════════════════
#  ANIMATED CANVAS
# ══════════════════════════════════════════════════════════════════
bg_canvas = tk.Canvas(root, highlightthickness=0, bd=0)
bg_canvas.place(x=0,y=0,relwidth=1,relheight=1)

particles=[]
_anim_running=True

class Particle:
    def __init__(self,w,h,style):
        self.w=w; self.h=h; self.style=style; self.reset(init=True)
    def reset(self,init=False):
        s=self.style
        if s=="matrix":
            self.x=random.randint(0,self.w)
            self.y=random.randint(-self.h,0) if not init else random.randint(0,self.h)
            self.speed=random.uniform(2,5)
            self.char=random.choice("アイウエオカキクケコ0123456789ABCDEF@#")
            self.size=random.randint(9,14)
        elif s=="bubbles":
            self.x=random.randint(0,self.w)
            self.y=self.h+20 if not init else random.randint(0,self.h)
            self.r=random.randint(2,10); self.speed=random.uniform(0.3,1.2)
            self.dx=random.uniform(-0.4,0.4)
        elif s=="stars":
            self.x=random.randint(0,self.w); self.y=random.randint(0,self.h)
            self.r=random.uniform(0.5,2.5); self.tw=random.uniform(0,math.pi*2)
            self.tws=random.uniform(0.02,0.07)
        elif s=="sakura":
            self.x=random.randint(0,self.w)
            self.y=random.randint(-50,0) if not init else random.randint(0,self.h)
            self.size=random.randint(5,12); self.speed=random.uniform(0.8,2.2)
            self.dx=random.uniform(-1.0,1.0)
        self.id=None

def _get_particle_style():
    override=CFG.get("particle_style_override","")
    if override: return override
    return THEMES[CFG.get("theme","Cyberpunk")].get("particle_style","matrix")

def init_particles():
    global particles
    for p in particles:
        try: bg_canvas.delete(p.id)
        except: pass
    particles.clear()
    w=root.winfo_width() or 1340; h=root.winfo_height() or 840
    n=CFG.get("particle_count",55)
    style=_get_particle_style()
    for _ in range(n): particles.append(Particle(w,h,style))

def animate_bg():
    if not _anim_running: return
    try:
        bg_canvas.delete("particle")
        T2=THEMES[CFG.get("theme","Cyberpunk")]
        bg_canvas.configure(bg=T2["bg"])
        w=bg_canvas.winfo_width(); h=bg_canvas.winfo_height()
        style=_get_particle_style()
        c1,c2=T2["particle"],T2["particle2"]
        for p in particles:
            p.w=w; p.h=h
            if style=="matrix":
                p.y+=p.speed
                if p.y>h: p.x=random.randint(0,w); p.y=-20; p.char=random.choice("アイウエオ0123456789AB")
                bg_canvas.create_text(p.x,p.y,text=p.char,fill=c1,
                    font=("Consolas",p.size,"bold"),tags="particle")
                bg_canvas.create_text(p.x,p.y-p.size*1.2,text=p.char,fill=c2,
                    font=("Consolas",max(7,p.size-2)),tags="particle")
            elif style=="bubbles":
                p.y-=p.speed; p.x+=p.dx
                if p.y<-20: p.reset()
                x,y,r=p.x,p.y,p.r
                bg_canvas.create_oval(x-r,y-r,x+r,y+r,outline=c1,width=1,tags="particle")
                bg_canvas.create_oval(x-r*.35,y-r*.45,x-r*.1,y-r*.2,outline=c2,width=1,tags="particle")
            elif style=="stars":
                p.tw+=p.tws; af=(math.sin(p.tw)+1)/2
                r=p.r*(0.5+af*0.5); c=c1 if af>0.5 else c2
                bg_canvas.create_oval(p.x-r,p.y-r,p.x+r,p.y+r,fill=c,outline="",tags="particle")
            elif style=="sakura":
                p.y+=p.speed; p.x+=p.dx
                if p.y>h+20: p.x=random.randint(0,w); p.y=-15; p.dx=random.uniform(-1,1)
                s=p.size
                bg_canvas.create_oval(p.x-s*.8,p.y-s*.5,p.x+s*.8,p.y+s*.5,
                    fill=c1,outline=c2,width=1,tags="particle")
                bg_canvas.create_oval(p.x-s*.4,p.y-s*.8,p.x+s*.4,p.y,
                    fill=c2,outline="",tags="particle")
        root.after(50,animate_bg)
    except: pass

# ══════════════════════════════════════════════════════════════════
#  HEADER
# ══════════════════════════════════════════════════════════════════
header_frame=tk.Frame(bg_canvas, bg=T["bg2"],
                      highlightbackground=T["border"], highlightthickness=1)
header_frame.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.075)

logo_lbl=tk.Label(header_frame, text=f"{T['icon']} AUTOHUB", font=F_LOGO,
                  bg=T["bg2"], fg=T["accent"])
logo_lbl.pack(side="left", padx=14)

sub_lbl=tk.Label(header_frame, text="Abdullah's Command Center",
                 font=("Segoe UI",10), bg=T["bg2"], fg=T["text2"])
sub_lbl.pack(side="left")

clock_lbl=tk.Label(header_frame, text="", font=F_CLOCK, bg=T["bg2"], fg=T["text2"])
clock_lbl.pack(side="right", padx=14)

def tick():
    clock_lbl.config(text=datetime.now().strftime("%A  %d %b %Y   %H:%M:%S"))
    root.after(1000, tick)
tick()

theme_pill=tk.Label(header_frame, text=T["name"], font=("Consolas",8,"bold"),
                    bg=T["accent2"], fg=T["bg"], padx=8, pady=3)
theme_pill.pack(side="right", padx=6)

def open_settings(): SettingsWindow(root)

settings_btn=tk.Button(header_frame, text="⚙  Settings", command=open_settings,
                        bg=T["bg3"], fg=T["text2"],
                        activebackground=T["card2"], activeforeground=T["accent"],
                        relief="flat", bd=0, cursor="hand2", font=F_BTN, padx=10, pady=4)
settings_btn.pack(side="right", padx=4)

chat_panel_visible=tk.BooleanVar(value=False)

def toggle_chat_panel():
    if chat_panel_visible.get(): hide_chat_panel()
    else: show_chat_panel()

ai_chat_btn=tk.Button(header_frame, text="⚡  AI Chat", command=toggle_chat_panel,
                       bg=T["accent"], fg=T["bg"],
                       activebackground=T["accent2"], activeforeground=T["bg"],
                       relief="flat", bd=0, cursor="hand2",
                       font=("Consolas",9,"bold"), padx=12, pady=4)
ai_chat_btn.pack(side="right", padx=(4,6))

# ══════════════════════════════════════════════════════════════════
#  MAIN CONTENT
# ══════════════════════════════════════════════════════════════════
content=tk.Frame(bg_canvas, bg=T["bg"])
content.place(relx=0.005, rely=0.085, relwidth=0.99, relheight=0.88)

col_left  = tk.Frame(content, bg=T["bg"])
col_mid   = tk.Frame(content, bg=T["bg"])
col_right = tk.Frame(content, bg=T["bg"])
col_left.pack(side="left",  fill="both", expand=True, padx=(0,4))
col_mid.pack(side="left",   fill="both", expand=True, padx=4)
col_right.pack(side="left", fill="both", expand=True, padx=(4,0))

chat_side_panel=tk.Frame(content, bg=T["bg2"],
                          highlightbackground=T["accent"], highlightthickness=2)

# ══════════════════════════════════════════════════════════════════
#  PLAIN CARD HELPER  (v3.1 style — no scroll anywhere)
# ══════════════════════════════════════════════════════════════════
def mk_card(parent, title, title_color=None):
    """Plain non-scrollable card — same as v3.1."""
    T2=THEMES[CFG.get("theme","Cyberpunk")]
    tc=title_color or T2["accent"]
    outer=tk.Frame(parent, bg=T2["card"],
                   highlightbackground=T2["border"], highlightthickness=1)
    outer.pack(fill="x", pady=3)
    hdr=tk.Frame(outer, bg=T2["card2"]); hdr.pack(fill="x")
    tk.Label(hdr, text=title, bg=T2["card2"], fg=tc,
             font=F_SEC, padx=8, pady=5).pack(side="left")
    body=tk.Frame(outer, bg=T2["card"], padx=6, pady=4)
    body.pack(fill="x")
    outer._body=body; outer._hdr=hdr
    return body, outer

# ══════════════════════════════════════════════════════════════════
#  BUTTON BUILDERS
# ══════════════════════════════════════════════════════════════════
site_body=app_body=folder_body=script_body=None
_so=_ao=_fo=_sco=None

def _make_btn(parent, text, cmd, hover_fg):
    T2=THEMES[CFG.get("theme","Cyberpunk")]
    b=tk.Button(parent, text=text, command=cmd,
                bg=T2["bg3"], fg=T2["text"],
                activebackground=T2["btn_hover"], activeforeground=hover_fg,
                relief="flat", bd=0, cursor="hand2",
                font=F_BTN, anchor="w", padx=8, pady=5)
    b.pack(fill="x", pady=1)
    b.bind("<Enter>", lambda e,btn=b: btn.config(bg=T2["btn_hover"], fg=hover_fg))
    b.bind("<Leave>", lambda e,btn=b: btn.config(bg=T2["bg3"], fg=T2["text"]))

def rebuild_sites():
    for w in site_body.winfo_children(): w.destroy()
    T2=THEMES[CFG.get("theme","Cyberpunk")]
    for name,(url,ico) in CFG["sites"].items():
        _make_btn(site_body, f"{ico}  {name}", lambda u=url: open_site(u), T2["accent"])

def rebuild_apps():
    for w in app_body.winfo_children(): w.destroy()
    T2=THEMES[CFG.get("theme","Cyberpunk")]
    for name,(path,ico) in CFG["apps"].items():
        _make_btn(app_body, f"{ico}  {name}", lambda p=path: open_app(p), T2["accent2"])

def rebuild_folders():
    for w in folder_body.winfo_children(): w.destroy()
    T2=THEMES[CFG.get("theme","Cyberpunk")]
    for name,(path,ico) in CFG["folders"].items():
        _make_btn(folder_body, f"{ico}  {name}", lambda p=path: open_folder(p), T2["green"])

def rebuild_scripts():
    for w in script_body.winfo_children(): w.destroy()
    T2=THEMES[CFG.get("theme","Cyberpunk")]
    for name,(path,ico) in CFG["scripts"].items():
        _make_btn(script_body, f"{ico}  {name}", lambda p=path: run_script(p), T2["amber"])

# ── Build all columns using plain mk_card (no scroll) ──
site_body,   _so  = mk_card(col_left, "🌐  SITES",   T["accent"])
rebuild_sites()

app_body,    _ao  = mk_card(col_mid,  "💻  APPS",    T["accent2"])
rebuild_apps()
folder_body, _fo  = mk_card(col_mid,  "📁  FOLDERS", T["green"])
rebuild_folders()
script_body, _sco = mk_card(col_mid,  "⚙️  SCRIPTS", T["amber"])
rebuild_scripts()

# ══════════════════════════════════════════════════════════════════
#  TO-DO LIST (right col) — PLAIN FRAME, NO CANVAS SCROLL
# ══════════════════════════════════════════════════════════════════
todo_outer=tk.Frame(col_right, bg=T["bg"])
todo_outer.pack(fill="both", expand=True)

# ── Header row ──
todo_hdr=tk.Frame(todo_outer, bg=T["bg"])
todo_hdr.pack(fill="x", pady=(0,2))
tk.Label(todo_hdr, text="✅  TO-DO LIST", bg=T["bg"],
         fg=T["green"], font=F_SEC).pack(side="left")
prog_lbl=tk.Label(todo_hdr, text="0/0 done", bg=T["bg"], fg=T["text2"], font=F_SMALL)
prog_lbl.pack(side="right")

# ── Day selector ──
day_bar=tk.Frame(todo_outer, bg=T["bg"])
day_bar.pack(fill="x", pady=(0,3))
_day_btns={}
for label,dv in [("📅 Today",today_str()),("⏮ Yesterday",yest_str())]:
    b=tk.Button(day_bar, text=label, bg=T["bg3"], fg=T["text2"],
                activebackground=T["card2"], activeforeground=T["accent"],
                relief="flat", bd=0, cursor="hand2", font=F_SMALL, padx=8, pady=3)
    b.pack(side="left", padx=(0,4))
    _day_btns[dv]=b

# ── Task input ──
todo_entry_frame=tk.Frame(todo_outer, bg=T["bg"])
todo_entry_frame.pack(fill="x", pady=(0,2))
todo_var=tk.StringVar()
todo_entry=tk.Entry(todo_entry_frame, textvariable=todo_var,
                    bg=T["card"], fg=T["text"], insertbackground=T["accent"],
                    relief="flat", bd=0, font=F_LABEL,
                    highlightbackground=T["border"], highlightthickness=1)
todo_entry.pack(side="left", fill="x", expand=True, ipady=5, padx=(0,4))

def add_task(e=None):
    txt=todo_var.get().strip()
    if not txt: return
    day=viewing_day.get(); tasks=load_tasks(day)
    tasks.append({"text":txt,"done":False,"created":datetime.now().isoformat()})
    save_tasks(day,tasks); todo_var.set(""); refresh_todo()
    log(f"Task:{txt}")

todo_entry.bind("<Return>", add_task)
tk.Button(todo_entry_frame, text="＋ Add", command=add_task,
          bg=T["accent"], fg=T["bg"],
          activebackground=T["accent2"], activeforeground=T["bg"],
          relief="flat", bd=0, font=F_BTN,
          cursor="hand2", padx=10, pady=5).pack(side="left")

# ── Action buttons ──
todo_act=tk.Frame(todo_outer, bg=T["bg"])
todo_act.pack(fill="x", pady=(0,3))

def clear_done():
    day=viewing_day.get()
    save_tasks(day,[t for t in load_tasks(day) if not t.get("done")]); refresh_todo()

def new_day():
    tom=(date.today()+timedelta(days=1)).isoformat()
    if os.path.exists(task_file(tom)):
        messagebox.showinfo("AutoHub","Tomorrow already exists!"); return
    carry=[dict(t,carried=True) for t in load_tasks(today_str()) if not t.get("done")]
    save_tasks(tom,carry)
    messagebox.showinfo("AutoHub",f"✅ {len(carry)} task(s) carried forward!")

for txt_b,cmd_b,fc_b in [
    ("🗑 Clear Done",  clear_done,                    T["red"]),
    ("🌅 New Day →",   new_day,                        T["amber"]),
    ("📂 Folder",      lambda: open_folder(DATA_DIR),  T["text2"]),
]:
    b=tk.Button(todo_act, text=txt_b, command=cmd_b,
                bg=T["bg3"], fg=fc_b,
                activebackground=T["card2"], activeforeground=fc_b,
                relief="flat", bd=0, font=F_SMALL, cursor="hand2", padx=6, pady=3)
    b.pack(side="left", padx=(0,4))

# ── Plain task list frame (no canvas, no scrollbar) ──
viewing_day=tk.StringVar(value=today_str())

todo_list_frame=tk.Frame(todo_outer, bg=T["card"],
                          highlightbackground=T["border"], highlightthickness=1)
todo_list_frame.pack(fill="both", expand=True)

def refresh_todo():
    for w in todo_list_frame.winfo_children(): w.destroy()
    T2=THEMES[CFG.get("theme","Cyberpunk")]
    day=viewing_day.get(); tasks=load_tasks(day); is_today=(day==today_str())
    done_n=sum(1 for t in tasks if t.get("done"))
    prog_lbl.config(text=f"{done_n}/{len(tasks)} done",
                    fg=T2["green"] if (done_n==len(tasks) and tasks) else T2["text2"])
    for i,task in enumerate(tasks):
        done=task.get("done",False); carried=task.get("carried",False)
        row_bg=T2["card"] if not done else T2["bg3"]
        row=tk.Frame(todo_list_frame, bg=row_bg,
                     highlightbackground=T2["border"], highlightthickness=1)
        row.pack(fill="x", pady=1, padx=2)
        var=tk.BooleanVar(value=done)
        def toggle(v=var,t=task,ts=tasks,d=day):
            t["done"]=v.get(); save_tasks(d,ts); refresh_todo()
        tk.Checkbutton(row, variable=var, command=toggle,
                       bg=row_bg, activebackground=row_bg,
                       selectcolor=T2["bg3"], fg=T2["green"],
                       relief="flat", bd=0, cursor="hand2").pack(side="left", padx=(4,1))
        txt=task["text"]+("  📌" if carried else "")
        fc=T2["text2"] if done else T2["text"]
        fn=("Segoe UI",9,"overstrike") if done else F_CHAT
        tk.Label(row, text=txt, bg=row_bg, fg=fc, font=fn,
                 anchor="w", wraplength=220).pack(side="left", fill="x", expand=True, padx=2)
        if is_today:
            tk.Button(row, text="✕",
                      command=lambda ts=tasks,idx=i,d=day: (ts.pop(idx),save_tasks(d,ts),refresh_todo()),
                      bg=row_bg, fg=T2["red"],
                      activebackground=T2["bg3"], activeforeground=T2["red"],
                      relief="flat", bd=0, cursor="hand2",
                      font=("Segoe UI",9,"bold"), padx=4).pack(side="right", padx=2)

def set_day(d): viewing_day.set(d); refresh_todo()
for dv,b in _day_btns.items(): b.config(command=lambda d=dv: set_day(d))

refresh_todo()

# ══════════════════════════════════════════════════════════════════
#  AI CHAT PANEL
# ══════════════════════════════════════════════════════════════════
chat_history=[]
_cw={}
_chat_built=False
_ai_status={"current":"auto","gemini":"unknown","groq":"unknown","openrouter":"unknown"}

def ai_status_text():
    ico={"ok":"🟢","limit":"🟡","error":"🔴","no_key":"⚫","unknown":"⚪"}
    g=ico.get(_ai_status["gemini"],"⚪")
    gr=ico.get(_ai_status["groq"],"⚪")
    o=ico.get(_ai_status["openrouter"],"⚪")
    cur=_ai_status["current"].upper()
    return f"G{g} Groq{gr} OR{o}  [{cur}]"

def build_chat_panel():
    global _chat_built
    if _chat_built: return
    _chat_built=True
    T2=THEMES[CFG.get("theme","Cyberpunk")]

    ch=tk.Frame(chat_side_panel, bg=T2["bg2"]); ch.pack(fill="x")
    tk.Label(ch, text="⚡  AI CHAT", font=("Consolas",10,"bold"),
             bg=T2["bg2"], fg=T2["accent"]).pack(side="left", padx=10, pady=6)
    sl=tk.Label(ch, text=ai_status_text(), bg=T2["bg2"], fg=T2["text2"], font=("Consolas",7))
    sl.pack(side="left", padx=4)
    _cw["status"]=sl
    tk.Button(ch, text="✕", command=hide_chat_panel,
              bg=T2["bg2"], fg=T2["text2"],
              activebackground=T2["bg3"], activeforeground=T2["red"],
              relief="flat", bd=0, cursor="hand2",
              font=("Segoe UI",10,"bold"), padx=8, pady=3).pack(side="right", padx=4)

    pb=tk.Frame(chat_side_panel, bg=T2["bg2"]); pb.pack(fill="x", padx=6, pady=(0,2))
    tk.Label(pb, text="AI:", bg=T2["bg2"], fg=T2["text2"], font=F_SMALL).pack(side="left")
    pv=tk.StringVar(value=CFG.get("active_ai","auto")); _cw["prov"]=pv
    for val,lbl in [("auto","🔄 Auto"),("gemini","✨ Gemini"),("groq","⚡ Groq"),("openrouter","🌐 OR")]:
        tk.Radiobutton(pb, text=lbl, variable=pv, value=val,
                       bg=T2["bg2"], fg=T2["text2"], selectcolor=T2["bg3"],
                       activebackground=T2["bg2"], font=("Segoe UI",7),
                       relief="flat", cursor="hand2").pack(side="left", padx=(2,0))

    tk.Label(chat_side_panel,
             text="open youtube  •  add task ...  •  ask anything",
             bg=T2["bg2"], fg=T2["text2"], font=("Segoe UI",7)).pack(fill="x", padx=8, pady=(0,2))

    dsp=tk.Frame(chat_side_panel, bg=T2["bg3"],
                 highlightbackground=T2["border"], highlightthickness=1)
    dsp.pack(fill="both", expand=True, padx=6, pady=(0,2))
    _cw["dsp"]=dsp
    cv=tk.Canvas(dsp, bg=T2["bg3"], bd=0, highlightthickness=0)
    csb=tk.Scrollbar(dsp, orient="vertical", command=cv.yview, width=5)
    cv.configure(yscrollcommand=csb.set)
    csb.pack(side="right", fill="y"); cv.pack(side="left", fill="both", expand=True)
    _cw["cv"]=cv
    ci=tk.Frame(cv, bg=T2["bg3"])
    cw_id=cv.create_window((0,0), window=ci, anchor="nw")
    _cw["ci"]=ci; _cw["cw_id"]=cw_id

    ci.bind("<Configure>",lambda e:(
        cv.configure(scrollregion=cv.bbox("all")),
        cv.itemconfig(cw_id,width=cv.winfo_width())))
    cv.bind("<Configure>",lambda e: cv.itemconfig(cw_id,width=e.width))
    cv.bind("<Enter>",lambda e: cv.bind_all("<MouseWheel>",
            lambda ev: cv.yview_scroll(int(-1*(ev.delta/120)),"units")))
    cv.bind("<Leave>",lambda e: cv.unbind_all("<MouseWheel>"))

    inf=tk.Frame(chat_side_panel, bg=T2["bg2"], pady=4)
    inf.pack(fill="x", padx=6, pady=(0,4))
    _cw["inf"]=inf
    cv2=tk.StringVar()
    ce=tk.Entry(inf, textvariable=cv2, bg=T2["card"], fg=T2["text"],
                insertbackground=T2["accent"], relief="flat", bd=0, font=F_CHAT,
                highlightbackground=T2["border"], highlightthickness=1)
    ce.pack(side="left", fill="x", expand=True, ipady=5, padx=(0,3))
    _cw["entry"]=ce; _cw["var"]=cv2

    def send(e=None):
        msg=cv2.get().strip()
        if not msg: return
        cv2.set(""); add_bubble(msg,"user")
        chat_history.append({"role":"user","content":msg})
        local=interpret_cmd(msg)
        if local:
            add_bubble(local,"bot"); chat_history.append({"role":"assistant","content":local}); return
        add_bubble("Thinking... ⚡","bot")
        pref=pv.get()
        def on_r(reply,prov):
            try:
                for w in ci.winfo_children():
                    try:
                        lbs=w.winfo_children()
                        if lbs and lbs[-1].cget("text")=="Thinking... ⚡": w.destroy()
                    except: pass
            except: pass
            root.after(0,lambda: process_reply(reply,prov))
            root.after(0,lambda: chat_history.append({"role":"assistant","content":reply}))
        threading.Thread(target=call_ai_fallback,args=(msg,on_r,pref),daemon=True).start()

    ce.bind("<Return>",send)
    tk.Button(inf, text="Send ↗", command=send,
              bg=T2["accent"], fg=T2["bg"],
              activebackground=T2["accent2"], activeforeground=T2["bg"],
              relief="flat", bd=0, font=F_BTN, cursor="hand2", padx=9, pady=4).pack(side="left")
    tk.Button(inf, text="🗑 Clear",
              command=lambda: [w.destroy() for w in ci.winfo_children()],
              bg=T2["bg3"], fg=T2["text2"],
              activebackground=T2["card2"], activeforeground=T2["text"],
              relief="flat", bd=0, font=F_SMALL, cursor="hand2", padx=6, pady=4).pack(side="left", padx=(2,0))

    add_bubble(
        "Salam Abdullah! 👋 AutoHub AI v3.5 ready!\n"
        "3-AI auto-fallback: Gemini → Groq → OpenRouter 🔄\n"
        "Commands: open youtube | add task ... | change theme",
        "bot"
    )
    update_ai_status()

def add_bubble(text, role="user", prov=None):
    if "ci" not in _cw: return
    T2=THEMES[CFG.get("theme","Cyberpunk")]
    ci=_cw["ci"]; cv=_cw["cv"]
    is_user=(role=="user")
    picons={"gemini":"✨","groq":"⚡","openrouter":"🌐"}
    ptag=f" [{picons.get(prov,'')}]" if prov and not is_user else ""
    prefix="You: " if is_user else f"⚡ AI{ptag}: "
    pcol=T2["accent2"] if is_user else T2["accent"]
    row=tk.Frame(ci, bg=T2["bg3"]); row.pack(fill="x", padx=4, pady=2)
    tk.Label(row, text=prefix, bg=T2["bg3"], fg=pcol, font=F_CHATB).pack(side="left", anchor="n")
    tk.Label(row, text=text, bg=T2["bg3"], fg=T2["text"],
             font=F_CHAT, wraplength=260, justify="left").pack(side="left", fill="x", expand=True)
    cv.update_idletasks(); cv.yview_moveto(1.0)

def show_chat_panel():
    chat_panel_visible.set(True)
    T2=THEMES[CFG.get("theme","Cyberpunk")]
    ai_chat_btn.config(bg=T2["accent2"], fg=T2["bg"], text="✕  Close AI")
    chat_side_panel.config(bg=T2["bg2"], highlightbackground=T2["accent"])
    chat_side_panel.pack(side="left", fill="both", expand=True, padx=(4,0))
    build_chat_panel(); update_ai_status()

def hide_chat_panel():
    chat_panel_visible.set(False)
    T2=THEMES[CFG.get("theme","Cyberpunk")]
    ai_chat_btn.config(bg=T2["accent"], fg=T2["bg"], text="⚡  AI Chat")
    chat_side_panel.pack_forget()

def update_ai_status():
    if "status" not in _cw: return
    T2=THEMES[CFG.get("theme","Cyberpunk")]
    for k,ck in [("gemini","gemini_api_key"),("groq","groq_api_key"),("openrouter","openrouter_api_key")]:
        if not CFG.get(ck): _ai_status[k]="no_key"
    has=any(CFG.get(k) for k in ["gemini_api_key","groq_api_key","openrouter_api_key"])
    _cw["status"].config(text=ai_status_text(),
                          fg=T2["green"] if has else T2["red"], bg=T2["bg2"])

# ══════════════════════════════════════════════════════════════════
#  3-AI ENGINE
# ══════════════════════════════════════════════════════════════════
GEMINI_MODEL  = "gemini-2.0-flash"
GROQ_MODEL    = "llama-3.3-70b-versatile"
OR_MODEL      = "mistralai/mistral-7b-instruct:free"

SYSTEM_PROMPT = (
    "You are AutoHub AI in Abdullah's desktop launcher. "
    "Be friendly, concise (≤3 sentences). Mix Urdu/English if user does. "
    "Commands: CMD:SITE:<name> | CMD:APP:<name> | CMD:TASK:<text> | CMD:THEME:<name>\n"
    "Sites: LeetCode,LinkedIn,Kaggle,GitHub,Hugging Face,ChatGPT,YouTube,Discord,MS Teams,WhatsApp,Drive.\n"
    "Apps: Chrome,Notepad,VS Code,Discord,Teams,WhatsApp.\n"
    "Themes: Cyberpunk,Matrix,Dracula,Nord,Sunset,Anime,Ocean,Education."
)

def _sync_call(fn, msg):
    ev=threading.Event(); out=[None,None]
    def cb(r,p): out[0]=r; out[1]=p; ev.set()
    fn(msg, chat_history, cb); ev.wait(30); return out[0],out[1]

def _gemini(msg, history, cb):
    key=CFG.get("gemini_api_key","")
    if not key: cb(None,"no_key"); return
    contents=[]
    for m in history[-12:]:
        contents.append({"role":"user" if m["role"]=="user" else "model",
                          "parts":[{"text":m["content"]}]})
    payload=json.dumps({
        "system_instruction":{"parts":[{"text":SYSTEM_PROMPT}]},
        "contents":contents+[{"role":"user","parts":[{"text":msg}]}],
        "generationConfig":{"maxOutputTokens":400,"temperature":0.7}
    }).encode()
    url=f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL}:generateContent?key={key}"
    for attempt in range(2):
        req=urllib.request.Request(url,data=payload,
            headers={"Content-Type":"application/json"},method="POST")
        try:
            with urllib.request.urlopen(req,timeout=22) as r: data=json.loads(r.read())
            cands=data.get("candidates",[])
            if cands:
                parts=cands[0].get("content",{}).get("parts",[])
                reply="".join(p.get("text","") for p in parts).strip()
                _ai_status["gemini"]="ok"; cb(reply or None,"gemini"); return
            _ai_status["gemini"]="error"; cb(None,"gemini"); return
        except urllib.error.HTTPError as e:
            if e.code==429:
                _ai_status["gemini"]="limit"
                if attempt==0: time.sleep(3); continue
            else: _ai_status["gemini"]="error"
            cb(None,"gemini"); return
        except: _ai_status["gemini"]="error"; cb(None,"gemini"); return

def _groq(msg, history, cb):
    key=CFG.get("groq_api_key","")
    if not key: cb(None,"no_key"); return
    msgs=[{"role":"system","content":SYSTEM_PROMPT}]
    for m in history[-10:]: msgs.append({"role":m["role"],"content":m["content"]})
    msgs.append({"role":"user","content":msg})
    payload=json.dumps({"model":GROQ_MODEL,"messages":msgs,"max_tokens":400,"temperature":0.7}).encode()
    req=urllib.request.Request("https://api.groq.com/openai/v1/chat/completions",
        data=payload,headers={"Content-Type":"application/json","Authorization":f"Bearer {key}"},
        method="POST")
    try:
        with urllib.request.urlopen(req,timeout=22) as r: data=json.loads(r.read())
        reply=data["choices"][0]["message"]["content"].strip()
        _ai_status["groq"]="ok"; cb(reply or None,"groq")
    except urllib.error.HTTPError as e:
        _ai_status["groq"]="limit" if e.code==429 else "error"; cb(None,"groq")
    except: _ai_status["groq"]="error"; cb(None,"groq")

def _openrouter(msg, history, cb):
    key=CFG.get("openrouter_api_key","")
    if not key: cb(None,"no_key"); return
    msgs=[{"role":"system","content":SYSTEM_PROMPT}]
    for m in history[-10:]: msgs.append({"role":m["role"],"content":m["content"]})
    msgs.append({"role":"user","content":msg})
    payload=json.dumps({"model":OR_MODEL,"messages":msgs,"max_tokens":400}).encode()
    req=urllib.request.Request("https://openrouter.ai/api/v1/chat/completions",
        data=payload,headers={"Content-Type":"application/json",
        "Authorization":f"Bearer {key}","HTTP-Referer":"https://autohub.local","X-Title":"AutoHub"},
        method="POST")
    try:
        with urllib.request.urlopen(req,timeout=28) as r: data=json.loads(r.read())
        reply=data["choices"][0]["message"]["content"].strip()
        _ai_status["openrouter"]="ok"; cb(reply or None,"openrouter")
    except: _ai_status["openrouter"]="error"; cb(None,"openrouter")

def call_ai_fallback(msg, callback, preferred="auto"):
    if preferred=="auto":
        r,p=_sync_call(_gemini,msg)
        if r: _ai_status["current"]="gemini"; root.after(0,update_ai_status); callback(r,"gemini"); return
        if CFG.get("groq_api_key"):
            root.after(0,lambda: add_bubble("⚡ Switching to Groq...","bot"))
        r,p=_sync_call(_groq,msg)
        if r: _ai_status["current"]="groq"; root.after(0,update_ai_status); callback(r,"groq"); return
        if CFG.get("openrouter_api_key"):
            root.after(0,lambda: add_bubble("🌐 Trying OpenRouter...","bot"))
        r,p=_sync_call(_openrouter,msg)
        if r: _ai_status["current"]="openrouter"; root.after(0,update_ai_status); callback(r,"openrouter"); return
        missing=[k for k,ck in [("Gemini","gemini_api_key"),("Groq","groq_api_key"),
                                  ("OpenRouter","openrouter_api_key")] if not CFG.get(ck)]
        callback("⚠️ All AI failed!\n"+(f"Missing keys: {', '.join(missing)}" if missing else
                 "Rate limits hit. Try again in a minute."),"none")
    else:
        fn={"gemini":_gemini,"groq":_groq,"openrouter":_openrouter}.get(preferred)
        if not fn: callback("Unknown provider.","none"); return
        r,p=_sync_call(fn,msg)
        callback(r or f"⚠️ {preferred.title()} failed. Check key in Settings.",p or preferred)
    root.after(0,update_ai_status)

# ══════════════════════════════════════════════════════════════════
#  LOCAL COMMAND INTERPRETER
# ══════════════════════════════════════════════════════════════════
SITE_ALIASES={
    "youtube":"YouTube","yt":"YouTube","discord":"Discord","dicord":"Discord",
    "github":"GitHub","leetcode":"LeetCode","linkedin":"LinkedIn","kaggle":"Kaggle",
    "huggingface":"Hugging Face","hf":"Hugging Face","chatgpt":"ChatGPT","gpt":"ChatGPT",
    "teams":"MS Teams","whatsapp":"WhatsApp","wa":"WhatsApp","drive":"Drive",
}
APP_ALIASES={
    "chrome":"Chrome","browser":"Chrome","notepad":"Notepad",
    "vscode":"VS Code","code":"VS Code","vs":"VS Code",
    "discord":"Discord","dicord":"Discord","teams":"Teams",
    "whatsapp":"WhatsApp","wa":"WhatsApp",
}
LOCAL_REPLIES=[
    (["hello","hi","hey","salam","aoa"],         "Hey Abdullah! 👋 Kya haal hai? Koi kaam batao!"),
    (["kasa ho","kaisa ho","how are you","sup"],  "Bilkul theek hoon! ⚡ Aap ka hukum?"),
    (["thanks","shukriya","thank you","thx"],     "Koi baat nahi! 😊 Aur kuch?"),
    (["bye","alvida","exit","band"],              "Allah hafiz! 👋"),
    (["time","waqt","date","aaj"],                lambda: f"⏰ {datetime.now().strftime('%A, %d %b %Y — %H:%M:%S')}"),
    (["tasks","todo","kya karna"],                lambda: f"✅ Aaj {len(load_tasks(today_str()))} tasks hain!"),
    (["ai status","which ai","provider","status"],lambda: f"AI Status: {ai_status_text()}"),
    (["theme","theem"],                           "Themes: Cyberpunk⚡ Matrix🟩 Dracula🧛 Nord❄️ Sunset🌅 Anime🌸 Ocean🌊 Education📚"),
]

def _fm(ml, kw):
    if kw in ml: return True
    if kw.replace(" ","") in ml.replace(" ",""): return True
    return any(kw[:i]+kw[i+1:] in ml for i in range(len(kw)) if len(kw)-1>=3)

def interpret_cmd(msg):
    ml=msg.lower().strip()
    for triggers,reply in LOCAL_REPLIES:
        for t in triggers:
            if _fm(ml,t): return reply() if callable(reply) else reply
    ow=["open","launch","jao","chalo","start","kholo","go","chalao","run"]
    for alias,can in SITE_ALIASES.items():
        if _fm(ml,alias):
            if any(w in ml for w in ow) or len(ml.split())<=3:
                if can in CFG["sites"]: open_site(CFG["sites"][can][0]); return f"Opening {can} ✅"
    for name,(url,_) in CFG["sites"].items():
        if _fm(ml,name.lower()):
            if any(w in ml for w in ow) or len(ml.split())<=3:
                open_site(url); return f"Opening {name} ✅"
    for alias,can in APP_ALIASES.items():
        if _fm(ml,alias):
            if any(w in ml for w in ow) or len(ml.split())<=3:
                if can in CFG["apps"]: open_app(CFG["apps"][can][0]); return f"Launching {can} ✅"
    for name,(path,_) in CFG["apps"].items():
        if _fm(ml,name.lower()):
            if any(w in ml for w in ow) or len(ml.split())<=3:
                open_app(path); return f"Launching {name} ✅"
    for name,(path,_) in CFG["folders"].items():
        if _fm(ml,name.lower()): open_folder(path); return f"Folder: {name} ✅"
    if any(ml.startswith(p) for p in ["add task ","task ","add todo ","todo "]):
        txt=msg.split(" ",2)[-1].strip()
        if txt:
            t=load_tasks(today_str())
            t.append({"text":txt,"done":False,"created":datetime.now().isoformat()})
            save_tasks(today_str(),t); refresh_todo(); return f"Task: '{txt}' ✅"
    for tname in THEMES:
        if _fm(ml,tname.lower()):
            if any(w in ml for w in ["theme","set","change","apply","lagao"]) or len(ml.split())<=2:
                apply_theme(tname); return f"Theme → {tname} ✅"
    return None

def process_reply(reply, prov=None):
    if not reply: add_bubble("⚠️ No response.", "bot", prov); return
    if reply.startswith("CMD:SITE:"):
        n=reply[9:].strip()
        for nm,(url,_) in CFG["sites"].items():
            if nm.lower()==n.lower(): open_site(url); add_bubble(f"Opening {nm}! ✅","bot",prov); return
    elif reply.startswith("CMD:APP:"):
        n=reply[8:].strip()
        for nm,(path,_) in CFG["apps"].items():
            if nm.lower()==n.lower(): open_app(path); add_bubble(f"Launching {nm}! ✅","bot",prov); return
    elif reply.startswith("CMD:TASK:"):
        txt=reply[9:].strip()
        t=load_tasks(today_str())
        t.append({"text":txt,"done":False,"created":datetime.now().isoformat()})
        save_tasks(today_str(),t); refresh_todo(); add_bubble(f"Task: '{txt}' ✅","bot",prov); return
    elif reply.startswith("CMD:THEME:"):
        tn=reply[10:].strip()
        if tn in THEMES: apply_theme(tn); add_bubble(f"Theme → {tn} ✅","bot",prov); return
    add_bubble(reply,"bot",prov)

# ══════════════════════════════════════════════════════════════════
#  THEME APPLY
# ══════════════════════════════════════════════════════════════════
def apply_theme(tname):
    if tname not in THEMES: return
    CFG["theme"]=tname; save_cfg(CFG)
    T2=THEMES[tname]
    root.configure(bg=T2["bg"])
    header_frame.configure(bg=T2["bg2"], highlightbackground=T2["border"])
    logo_lbl.config(bg=T2["bg2"], fg=T2["accent"], text=f"{T2['icon']} AUTOHUB")
    sub_lbl.config(bg=T2["bg2"], fg=T2["text2"])
    clock_lbl.config(bg=T2["bg2"], fg=T2["text2"])
    theme_pill.config(bg=T2["accent2"], fg=T2["bg"], text=T2["name"])
    settings_btn.config(bg=T2["bg3"], fg=T2["text2"])
    ai_chat_btn.config(
        bg=T2["accent2"] if chat_panel_visible.get() else T2["accent"], fg=T2["bg"])
    content.configure(bg=T2["bg"])
    for w in [col_left,col_mid,col_right,todo_outer,todo_hdr,
               day_bar,todo_entry_frame,todo_act]:
        try: w.configure(bg=T2["bg"])
        except: pass
    # To-Do list frame (plain, no canvas)
    todo_list_frame.configure(bg=T2["card"], highlightbackground=T2["border"])
    todo_entry.configure(bg=T2["card"], fg=T2["text"], insertbackground=T2["accent"])
    prog_lbl.configure(bg=T2["bg"], fg=T2["text2"])
    # All plain cards (sites, apps, folders, scripts)
    for outer in [_so, _ao, _fo, _sco]:
        try:
            outer._body.configure(bg=T2["card"])
            outer.configure(bg=T2["card"], highlightbackground=T2["border"])
            outer._hdr.configure(bg=T2["card2"])
        except: pass
    if chat_panel_visible.get() and _chat_built:
        chat_side_panel.config(bg=T2["bg2"], highlightbackground=T2["accent"])
        for k,bgk in [("cv","bg3"),("ci","bg3"),("dsp","bg3"),("inf","bg2")]:
            if k in _cw:
                try: _cw[k].config(bg=T2[bgk])
                except: pass
        if "entry" in _cw:
            _cw["entry"].config(bg=T2["card"],fg=T2["text"],insertbackground=T2["accent"])
        update_ai_status()
    rebuild_sites(); rebuild_apps(); rebuild_folders(); rebuild_scripts()
    refresh_todo()
    init_particles()
    log(f"Theme:{tname}")

# ══════════════════════════════════════════════════════════════════
#  SETTINGS WINDOW
# ══════════════════════════════════════════════════════════════════
class SettingsWindow:
    def __init__(self, parent):
        T2=THEMES[CFG.get("theme","Cyberpunk")]
        self.win=tk.Toplevel(parent)
        self.win.title("⚙️  AutoHub v3.5 — Settings")
        self.win.geometry("900x700")
        self.win.configure(bg=T2["bg"])
        self.win.grab_set()
        self.T2=T2
        self._build()

    def _build(self):
        T2=self.T2
        nb=ttk.Notebook(self.win)
        st=ttk.Style(); st.theme_use("clam")
        st.configure("TNotebook",       background=T2["bg"],  borderwidth=0)
        st.configure("TNotebook.Tab",   background=T2["bg3"], foreground=T2["text"],
                     padding=[12,5],    font=F_BTN)
        st.map("TNotebook.Tab",
               background=[("selected",T2["accent2"])],
               foreground=[("selected",T2["bg"])])
        nb.pack(fill="both", expand=True, padx=10, pady=10)

        self._tab_themes(nb, T2)
        self._tab_ai_keys(nb, T2)
        self._tab_effects(nb, T2)
        self._tab_add(nb, T2)
        self._tab_manage(nb, T2)
        self._tab_paths(nb, T2)

    def _tab_themes(self, nb, T2):
        t=tk.Frame(nb, bg=T2["bg"]); nb.add(t, text="🎨 Themes")
        tk.Label(t, text="Choose your theme — colors, particles & vibe all change!",
                 bg=T2["bg"], fg=T2["text2"], font=F_LABEL).pack(anchor="w", padx=12, pady=(10,6))

        sc_outer=tk.Frame(t, bg=T2["bg"]); sc_outer.pack(fill="both", expand=True, padx=8, pady=4)
        sc_cv=tk.Canvas(sc_outer, bg=T2["bg"], bd=0, highlightthickness=0)
        sc_sb=tk.Scrollbar(sc_outer, orient="vertical", command=sc_cv.yview, width=5)
        sc_cv.configure(yscrollcommand=sc_sb.set)
        sc_sb.pack(side="right", fill="y"); sc_cv.pack(side="left", fill="both", expand=True)
        sc_inner=tk.Frame(sc_cv, bg=T2["bg"])
        sc_win=sc_cv.create_window((0,0), window=sc_inner, anchor="nw")
        sc_inner.bind("<Configure>", lambda e:(
            sc_cv.configure(scrollregion=sc_cv.bbox("all")),
            sc_cv.itemconfig(sc_win, width=sc_cv.winfo_width())))
        sc_cv.bind("<Configure>", lambda e: sc_cv.itemconfig(sc_win, width=e.width))
        sc_cv.bind("<Enter>", lambda e: sc_cv.bind_all("<MouseWheel>",
                   lambda ev: sc_cv.yview_scroll(int(-1*(ev.delta/120)),"units")))
        sc_cv.bind("<Leave>", lambda e: sc_cv.unbind_all("<MouseWheel>"))

        for tname,td in THEMES.items():
            is_active=(tname==CFG.get("theme","Cyberpunk"))
            row=tk.Frame(sc_inner, bg=td["card"],
                         highlightbackground=td["accent"] if is_active else T2["border"],
                         highlightthickness=2 if is_active else 1)
            row.pack(fill="x", padx=4, pady=3)
            top=tk.Frame(row, bg=td["card2"]); top.pack(fill="x")
            tk.Label(top, text=f"{td['icon']}  {td['name']}",
                     bg=td["card2"], fg=td["accent"], font=F_BTN, padx=10, pady=6).pack(side="left")
            if is_active:
                tk.Label(top, text="✓ ACTIVE", bg=td["accent"], fg=td["bg"],
                         font=("Consolas",7,"bold"), padx=6, pady=2).pack(side="right", padx=6, pady=4)
            body=tk.Frame(row, bg=td["card"]); body.pack(fill="x", padx=8, pady=4)
            tk.Label(body, text=td.get("description",""), bg=td["card"],
                     fg=td["text2"], font=F_SMALL).pack(side="left")
            sw=tk.Frame(body, bg=td["card"]); sw.pack(side="right")
            for ck in ["accent","accent2","green","amber","red"]:
                tk.Frame(sw, bg=td[ck], width=18, height=18).pack(side="left", padx=2)
            if not is_active:
                tk.Button(row, text="Apply Theme",
                          command=lambda tn=tname: (apply_theme(tn), self.win.destroy()),
                          bg=td["bg3"], fg=td["text"],
                          activebackground=td["btn_hover"], activeforeground=td["accent"],
                          relief="flat", bd=0, cursor="hand2", font=F_BTN,
                          padx=12, pady=4).pack(anchor="e", padx=8, pady=(0,6))

    def _tab_ai_keys(self, nb, T2):
        t=tk.Frame(nb, bg=T2["bg"]); nb.add(t, text="🔑 AI Keys")

        hf=tk.Frame(t, bg=T2["card2"], highlightbackground=T2["accent"], highlightthickness=1)
        hf.pack(fill="x", padx=12, pady=(12,8))
        tk.Label(hf, text="  3-Tier Auto-Fallback System",
                 bg=T2["card2"], fg=T2["accent"], font=("Consolas",10,"bold"),
                 padx=6, pady=8).pack(side="left")
        tk.Label(hf, text="Gemini limit → Groq auto-switch → OpenRouter backup",
                 bg=T2["card2"], fg=T2["text2"], font=F_SMALL,
                 padx=6, pady=8).pack(side="left")

        df=tk.Frame(t, bg=T2["bg"]); df.pack(fill="x", padx=12, pady=(0,8))
        tk.Label(df, text="Default AI Mode:", bg=T2["bg"], fg=T2["text2"], font=F_LABEL).pack(side="left")
        ai_pref_var=tk.StringVar(value=CFG.get("active_ai","auto"))
        for val,lbl in [("auto","🔄 Auto-Fallback"),("gemini","✨ Gemini Only"),
                        ("groq","⚡ Groq Only"),("openrouter","🌐 OpenRouter Only")]:
            tk.Radiobutton(df, text=lbl, variable=ai_pref_var, value=val,
                           bg=T2["bg"], fg=T2["text"], selectcolor=T2["bg3"],
                           activebackground=T2["bg"], font=F_SMALL,
                           relief="flat", cursor="hand2").pack(side="left", padx=6)

        api_fields=[
            ("gemini_api_key",  "✨ Gemini (Primary)",   "aistudio.google.com → Get API Key",  "gemini-2.0-flash",         T2["accent"]),
            ("groq_api_key",    "⚡ Groq (Backup)",      "console.groq.com → API Keys",         "llama-3.3-70b-versatile",  T2["green"]),
            ("openrouter_api_key","🌐 OpenRouter (Exp)","openrouter.ai → Keys",                "mistral-7b-instruct:free", T2["amber"]),
        ]
        api_vars={}
        for cfg_key,label,hint,model,color in api_fields:
            cf=tk.Frame(t, bg=T2["card"],
                        highlightbackground=color, highlightthickness=1)
            cf.pack(fill="x", padx=12, pady=3)
            tf=tk.Frame(cf, bg=T2["card2"]); tf.pack(fill="x")
            tk.Label(tf, text=label, bg=T2["card2"], fg=color,
                     font=F_BTN, padx=10, pady=5).pack(side="left")
            has_key=bool(CFG.get(cfg_key))
            dot=tk.Label(tf, text="✅ Key set" if has_key else "❌ Not set",
                         bg=T2["card2"], fg=T2["green"] if has_key else T2["red"],
                         font=F_SMALL, padx=8)
            dot.pack(side="right", padx=6)
            tk.Label(cf, text=f"🔗 {hint}  |  Model: {model}",
                     bg=T2["card"], fg=T2["text2"], font=F_SMALL, padx=10).pack(anchor="w", pady=(4,0))
            v=tk.StringVar(value=CFG.get(cfg_key,""))
            api_vars[cfg_key]=(v, dot)
            ef=tk.Frame(cf, bg=T2["card"]); ef.pack(fill="x", padx=10, pady=4)
            ent=tk.Entry(ef, textvariable=v, show="*",
                         bg=T2["bg3"], fg=T2["text"], insertbackground=T2["accent"],
                         relief="flat", bd=0, font=F_LABEL,
                         highlightbackground=T2["border"], highlightthickness=1)
            ent.pack(side="left", fill="x", expand=True, ipady=5)
            sv=tk.BooleanVar()
            def _tog(e=ent, s=sv): e.config(show="" if s.get() else "*")
            tk.Checkbutton(ef, text="👁", variable=sv, command=_tog,
                           bg=T2["card"], fg=T2["text2"], selectcolor=T2["bg3"],
                           activebackground=T2["card"], font=F_SMALL,
                           relief="flat", cursor="hand2").pack(side="left", padx=4)
            def _clear(var=v, d=dot):
                var.set("")
                d.config(text="❌ Not set", fg=T2["red"])
            tk.Button(ef, text="✕ Clear", command=_clear,
                      bg=T2["bg3"], fg=T2["red"],
                      activebackground=T2["btn_hover"], activeforeground=T2["red"],
                      relief="flat", bd=0, cursor="hand2", font=F_SMALL, padx=6).pack(side="left", padx=2)

        def save_keys():
            for k,(v,dot) in api_vars.items():
                CFG[k]=v.get().strip()
                dot.config(text="✅ Key set" if CFG[k] else "❌ Not set",
                           fg=T2["green"] if CFG[k] else T2["red"])
            CFG["active_ai"]=ai_pref_var.get()
            if _chat_built and "prov" in _cw:
                _cw["prov"].set(CFG["active_ai"])
            save_cfg(CFG); update_ai_status()
            g="✅" if CFG.get("gemini_api_key") else "❌"
            gr="✅" if CFG.get("groq_api_key") else "❌"
            o="✅" if CFG.get("openrouter_api_key") else "❌"
            messagebox.showinfo("Saved!",
                f"Keys saved!\nGemini {g}   Groq {gr}   OpenRouter {o}\n"
                f"Default AI: {CFG['active_ai'].upper()}")

        tk.Button(t, text="💾  Save All Keys & Settings", command=save_keys,
                  bg=T2["accent"], fg=T2["bg"], relief="flat", bd=0, cursor="hand2",
                  font=F_BTN, padx=14, pady=7).pack(anchor="w", padx=12, pady=8)

    def _tab_effects(self, nb, T2):
        t=tk.Frame(nb, bg=T2["bg"]); nb.add(t, text="✨ Effects")

        tk.Label(t, text="Particle / Animation Settings",
                 bg=T2["bg"], fg=T2["accent"], font=("Consolas",10,"bold")).pack(anchor="w", padx=12, pady=(12,4))

        tk.Label(t, text="Particle Style Override  (empty = use theme default):",
                 bg=T2["bg"], fg=T2["text2"], font=F_LABEL).pack(anchor="w", padx=12, pady=(8,2))
        ps_var=tk.StringVar(value=CFG.get("particle_style_override",""))

        sf=tk.Frame(t, bg=T2["bg"]); sf.pack(anchor="w", padx=20, pady=4)
        for val,lbl,desc in [
            ("",       "🎨 Theme Default", "Each theme picks its own style"),
            ("matrix", "🟩 Matrix Rain",   "Falling Japanese chars"),
            ("bubbles","🫧 Bubbles",        "Floating circles rising up"),
            ("stars",  "⭐ Stars",          "Twinkling star field"),
            ("sakura", "🌸 Sakura",         "Falling flower petals"),
        ]:
            rf=tk.Frame(sf, bg=T2["bg"]); rf.pack(anchor="w", pady=2)
            tk.Radiobutton(rf, text=lbl, variable=ps_var, value=val,
                           bg=T2["bg"], fg=T2["text"], selectcolor=T2["bg3"],
                           activebackground=T2["bg"], font=F_LABEL,
                           relief="flat", cursor="hand2").pack(side="left")
            tk.Label(rf, text=f"  — {desc}", bg=T2["bg"], fg=T2["text2"], font=F_SMALL).pack(side="left")

        tk.Label(t, text="Particle Count:",
                 bg=T2["bg"], fg=T2["text2"], font=F_LABEL).pack(anchor="w", padx=12, pady=(12,2))
        pc_v=tk.IntVar(value=CFG.get("particle_count",55))
        scf=tk.Frame(t, bg=T2["bg"]); scf.pack(anchor="w", padx=20)
        tk.Scale(scf, from_=5, to=150, orient="horizontal", variable=pc_v,
                 bg=T2["bg"], fg=T2["text"], troughcolor=T2["bg3"],
                 highlightthickness=0, font=F_SMALL, length=280).pack(side="left")
        tk.Label(scf, textvariable=pc_v, bg=T2["bg"], fg=T2["accent"],
                 font=("Consolas",10,"bold"), width=4).pack(side="left", padx=8)

        prev_lbl=tk.Label(t, text="", bg=T2["bg"], fg=T2["text2"], font=F_SMALL)
        prev_lbl.pack(anchor="w", padx=12)

        def _preview():
            s=ps_var.get() or THEMES[CFG.get("theme","Cyberpunk")].get("particle_style","matrix")
            prev_lbl.config(text=f"Preview: {s.upper()} style with {pc_v.get()} particles")

        def save_effects():
            CFG["particle_style_override"]=ps_var.get()
            CFG["particle_count"]=pc_v.get()
            save_cfg(CFG); init_particles()
            _preview()
            messagebox.showinfo("AutoHub","✅ Effects saved & applied!")

        bf=tk.Frame(t, bg=T2["bg"]); bf.pack(anchor="w", padx=12, pady=10)
        tk.Button(bf, text="👁 Preview", command=_preview,
                  bg=T2["bg3"], fg=T2["text2"], activebackground=T2["card"],
                  relief="flat", bd=0, cursor="hand2", font=F_BTN, padx=10, pady=6).pack(side="left", padx=(0,6))
        tk.Button(bf, text="💾  Save & Apply", command=save_effects,
                  bg=T2["accent"], fg=T2["bg"], activebackground=T2["accent2"],
                  relief="flat", bd=0, cursor="hand2", font=F_BTN, padx=12, pady=6).pack(side="left")

    def _tab_add(self, nb, T2):
        t=tk.Frame(nb, bg=T2["bg"]); nb.add(t, text="➕ Add New")
        nb2=ttk.Notebook(t); nb2.pack(fill="both", expand=True, padx=6, pady=6)
        cats=[
            ("🌐 Site",   "sites",   ["Name","URL","Icon (emoji)"]),
            ("💻 App",    "apps",    ["Name","Path / .exe","Icon (emoji)"]),
            ("📁 Folder", "folders", ["Name","Folder Path","Icon (emoji)"]),
            ("⚙️ Script", "scripts", ["Name","Script Path","Icon (emoji)"]),
        ]
        for cat_label,cfg_key,fields in cats:
            tab=tk.Frame(nb2, bg=T2["bg"]); nb2.add(tab, text=cat_label)
            tk.Label(tab, text=f"Add a new entry to {cat_label} panel:",
                     bg=T2["bg"], fg=T2["text2"], font=F_SMALL).grid(
                row=0, column=0, columnspan=2, sticky="w", padx=10, pady=(8,4))
            evars={}
            for fi,fname in enumerate(fields):
                tk.Label(tab, text=fname+":", bg=T2["bg"], fg=T2["text2"],
                         font=F_LABEL).grid(row=fi+1, column=0, sticky="w", padx=(10,4), pady=5)
                ev=tk.StringVar()
                tk.Entry(tab, textvariable=ev, bg=T2["card"], fg=T2["text"],
                         insertbackground=T2["accent"], relief="flat", bd=0, font=F_LABEL,
                         highlightbackground=T2["border"], highlightthickness=1).grid(
                    row=fi+1, column=1, sticky="ew", padx=(0,10), pady=5, ipady=5)
                tab.columnconfigure(1, weight=1); evars[fname]=ev
            tk.Label(tab, text="💡 Icon: paste any emoji  e.g. 🎮 📊 🔥 🌍",
                     bg=T2["bg"], fg=T2["text2"], font=F_SMALL).grid(
                row=len(fields)+1, column=0, columnspan=2, sticky="w", padx=10, pady=(0,4))
            def do_add(ck=cfg_key, ev=evars, fl=fields):
                n=ev[fl[0]].get().strip(); v1=ev[fl[1]].get().strip()
                ic=ev[fl[2]].get().strip() or "▶"
                if not n or not v1:
                    messagebox.showwarning("AutoHub","Name and path/URL are required!"); return
                CFG[ck][n]=[v1,ic]; save_cfg(CFG)
                {"sites":rebuild_sites,"apps":rebuild_apps,
                 "folders":rebuild_folders,"scripts":rebuild_scripts}[ck]()
                for key in ev: ev[key].set("")
                messagebox.showinfo("AutoHub",f"✅ '{n}' added to {ck}!")
            tk.Button(tab, text=f"➕  Add to {cat_label}", command=do_add,
                      bg=T2["accent"], fg=T2["bg"], activebackground=T2["accent2"],
                      relief="flat", bd=0, cursor="hand2", font=F_BTN,
                      padx=12, pady=5).grid(row=len(fields)+2, column=0, columnspan=2,
                                            sticky="w", padx=10, pady=8)

    def _tab_manage(self, nb, T2):
        t=tk.Frame(nb, bg=T2["bg"]); nb.add(t, text="🗂 Manage")
        nb2=ttk.Notebook(t); nb2.pack(fill="both", expand=True, padx=6, pady=6)
        cats=[("🌐 Sites","sites"),("💻 Apps","apps"),
               ("📁 Folders","folders"),("⚙️ Scripts","scripts")]

        for cat_label,cfg_key in cats:
            tab=tk.Frame(nb2, bg=T2["bg"]); nb2.add(tab, text=cat_label)
            tk.Label(tab, text=f"Click ✕ to remove an entry from {cat_label}:",
                     bg=T2["bg"], fg=T2["text2"], font=F_SMALL).pack(
                anchor="w", padx=10, pady=(8,4))

            list_frame=tk.Frame(tab, bg=T2["bg"])
            list_frame.pack(fill="both", expand=True, padx=6)

            def refresh_list(lf=list_frame, ck=cfg_key):
                for w in lf.winfo_children(): w.destroy()
                items=CFG.get(ck,{})
                if not items:
                    tk.Label(lf, text="(No entries)", bg=T2["bg"],
                             fg=T2["text2"], font=F_SMALL).pack(anchor="w", padx=6)
                    return
                for name,(val,ico) in list(items.items()):
                    row=tk.Frame(lf, bg=T2["card"],
                                 highlightbackground=T2["border"], highlightthickness=1)
                    row.pack(fill="x", pady=2, padx=2)
                    tk.Label(row, text=f"{ico}  {name}", bg=T2["card"],
                             fg=T2["text"], font=F_BTN, padx=8, pady=5).pack(side="left")
                    tk.Label(row, text=val[:55]+"…" if len(val)>55 else val,
                             bg=T2["card"], fg=T2["text2"],
                             font=F_SMALL).pack(side="left", padx=4)
                    def do_del(n=name, ck2=ck, rf=refresh_list, lf2=lf):
                        if messagebox.askyesno("Delete",f"Delete '{n}' from {ck2}?"):
                            CFG[ck2].pop(n, None); save_cfg(CFG)
                            {"sites":rebuild_sites,"apps":rebuild_apps,
                             "folders":rebuild_folders,"scripts":rebuild_scripts}[ck2]()
                            rf(lf2, ck2)
                    tk.Button(row, text="✕", command=do_del,
                              bg=T2["card"], fg=T2["red"],
                              activebackground=T2["bg3"], activeforeground=T2["red"],
                              relief="flat", bd=0, cursor="hand2",
                              font=("Segoe UI",9,"bold"), padx=8, pady=4).pack(side="right", padx=4)

            refresh_list()

    def _tab_paths(self, nb, T2):
        t=tk.Frame(nb, bg=T2["bg"]); nb.add(t, text="📂 Paths")
        tk.Label(t, text="AutoHub Data Locations",
                 bg=T2["bg"], fg=T2["accent"], font=("Consolas",10,"bold")).pack(
            anchor="w", padx=12, pady=(12,6))
        for lbl,val,ico in [
            ("Data Directory",   DATA_DIR,  "📁"),
            ("Tasks Directory",  TASKS_DIR, "✅"),
            ("Logs Directory",   LOGS_DIR,  "📋"),
            ("Config File",      CFG_FILE,  "⚙️"),
        ]:
            r=tk.Frame(t, bg=T2["card"],
                       highlightbackground=T2["border"], highlightthickness=1)
            r.pack(fill="x", padx=12, pady=3)
            tk.Label(r, text=f"{ico}  {lbl}", bg=T2["card"],
                     fg=T2["accent"], font=F_BTN, padx=10, pady=5).pack(anchor="w")
            tk.Label(r, text=val, bg=T2["card"],
                     fg=T2["text2"], font=F_SMALL, padx=12, pady=(0,6)).pack(anchor="w")

        bf=tk.Frame(t, bg=T2["bg"]); bf.pack(anchor="w", padx=12, pady=8)
        tk.Button(bf, text="📂  Open Data Folder", command=lambda: open_folder(DATA_DIR),
                  bg=T2["accent"], fg=T2["bg"], activebackground=T2["accent2"],
                  relief="flat", bd=0, cursor="hand2", font=F_BTN,
                  padx=12, pady=6).pack(side="left")
        tk.Button(bf, text="📋  Open Logs Folder", command=lambda: open_folder(LOGS_DIR),
                  bg=T2["bg3"], fg=T2["text2"], activebackground=T2["card"],
                  relief="flat", bd=0, cursor="hand2", font=F_BTN,
                  padx=12, pady=6).pack(side="left", padx=(6,0))

        vi=tk.Frame(t, bg=T2["card2"],
                    highlightbackground=T2["border"], highlightthickness=1)
        vi.pack(fill="x", padx=12, pady=(12,4))
        for line in [
            "AutoHub v3.5  —  Abdullah's Personal Command Center",
            "8 Themes  •  3-AI Auto-Fallback  •  Plain Cards (v3.1 style)",
            "AI: Gemini 2.0 Flash → Groq LLaMA 3.3 70B → OpenRouter Mistral",
        ]:
            tk.Label(vi, text=line, bg=T2["card2"], fg=T2["text2"],
                     font=F_SMALL).pack(anchor="w", padx=10, pady=2)

# ══════════════════════════════════════════════════════════════════
#  STATUS BAR
# ══════════════════════════════════════════════════════════════════
status_bar=tk.Frame(bg_canvas, bg=T["bg2"],
                    highlightbackground=T["border"], highlightthickness=1)
status_bar.place(relx=0.005, rely=0.966, relwidth=0.99, relheight=0.032)
tk.Label(status_bar, text=f"  📁 {DATA_DIR}",
         bg=T["bg2"], fg=T["text2"], font=F_CLOCK).pack(side="left")
tk.Label(status_bar,
         text="AutoHub v3.5  •  8 Themes  •  Gemini→Groq→OpenRouter  •  +100000% ⚡  ",
         bg=T["bg2"], fg=T["text2"], font=F_CLOCK).pack(side="right")

# ══════════════════════════════════════════════════════════════════
#  START
# ══════════════════════════════════════════════════════════════════
def start_anim(): init_particles(); animate_bg()
root.after(200, start_anim)

def on_close():
    global _anim_running
    _anim_running=False; log("AutoHub v3.5 closed"); root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)
root.mainloop()
