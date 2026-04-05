# 🌌 A.U.R.A — Automated Unified Runtime Activation

A.U.R.A is a zero-touch, NFC-triggered environment activation system. By simply tapping an NFC tag with a mobile device, this system seamlessly boots up a predefined suite of productivity tools (ChatGPT, Claude AI, GitHub, Google, Spotify, and Antigravity IDE) while simultaneously serving a highly aesthetic, real-time glassmorphism dashboard to your phone.

---

## ✨ Features

* **NFC Triggered**: Designed to be activated by a physical NFC tag linked to the server's IP address (`/start` route).
* **Live Sync Dashboard**: Leverages Flask Server-Sent Events (SSE) to sync Python background execution precisely with mobile UI checkboxes.
* **Premium Aesthetics**: Fully responsive glassmorphism UI with dynamic CSS ambient orbs, grid textures, and fluid micro-animations—tailored specifically for mobile screens.
* **Zero-Touch Startup**: Automatically registers itself to the Windows Registry upon first run and boots 100% silently in the background via `pythonw.exe`.
* **Intelligent Foregrounding**: Uses a native PowerShell `AppActivate` bypass to guarantee that the final Antigravity IDE is forcefully brought to the center of your screen over all other apps.
* **Voice Feedback**: Integrated `pyttsx3` announces when the workspace has fully stabilized.

---

## 🚀 The Launch Sequence

Once triggered, the automation sequence spins up the following environments while feeding data back to the phone screen:

1. ChatGPT Web Interface
2. Claude AI
3. GitHub Repository
4. Google Search
5. Ambient Spotify Audio (Booted minimized to prevent distraction)
6. Antigravity IDE (Brought to absolute foreground)

---

## 🛠️ Installation & Setup

### 1. Prepare the Directory

Store this repository in a permanent location (e.g. `C:\Users\ishan\aura`). The directory must not be moved after the first run.

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Initialize the Hidden Server

To lock the server into your Windows Startup sequence and run it without any terminal showing:

```powershell
pythonw.exe aura_main.py
```

> Note: Using `python.exe` will run it visibly in a terminal. `pythonw.exe` ensures it runs silently in the background.

### 4. Program your NFC Tag

Write a web URI to your physical NFC tag pointing exactly to your machine's local IP address:

```
http://192.168.1.X:5000/start
```

---

## 📂 Project Structure

* `aura_main.py` — The core Flask backend, automation engine, SSE generator, and Windows registry logic
* `templates/index.html` — The frontend mobile UI with glassmorphism + live SSE updates
* `requirements.txt` — Project dependencies

---

## ⚠️ Troubleshooting

* **Server Already Running**
  Since the server runs in the background continuously, you may encounter conflicts if starting it manually. To stop it:

  ```powershell
  taskkill /f /im pythonw.exe
  ```

* **UI Hot-Reloading**
  Editing `index.html` does not require restarting the server. Flask’s `TEMPLATES_AUTO_RELOAD` ensures changes reflect instantly on the next trigger.
