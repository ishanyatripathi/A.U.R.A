from flask import Flask, render_template, Response
import os
import time
import pyttsx3
import sys
import winreg
import json

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True
import os
os.environ.pop('WERKZEUG_SERVER_FD', None)
os.environ.pop('WERKZEUG_RUN_MAIN', None)

def add_to_startup():
    try:
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_SET_VALUE)
        script_path = os.path.abspath(__file__)
        pythonw_exe = sys.executable.replace("python.exe", "pythonw.exe")
        cmd = f'"{pythonw_exe}" "{script_path}"'
        winreg.SetValueEx(key, 'NFC_Environment', 0, winreg.REG_SZ, cmd)
        winreg.CloseKey(key)
    except Exception:
        pass

add_to_startup()

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 170)
    engine.say(text)
    engine.runAndWait()

def startup_stream():
    yield f"data: {json.dumps({'step': 0, 'status': 'Waking up system core...'})}\n\n"
    time.sleep(1)

    # 1. ChatGPT
    os.system("start chatgpt:")
    yield f"data: {json.dumps({'step': 1, 'status': 'ChatGPT interface launched'})}\n\n"
    time.sleep(3)

    # 2. Claude
    os.system('start chrome "https://claude.ai"')
    yield f"data: {json.dumps({'step': 2, 'status': 'Claude AI connected'})}\n\n"
    time.sleep(3)

    # 3. GitHub
    os.system('start chrome "https://github.com/ishanyatripathi"')
    yield f"data: {json.dumps({'step': 3, 'status': 'GitHub repository accessed'})}\n\n"
    time.sleep(3)

    # 4. Google
    os.system('start chrome "https://www.google.com"')
    yield f"data: {json.dumps({'step': 4, 'status': 'Google Search initialized'})}\n\n"
    time.sleep(3)

    # 5. Spotify
    os.system('start /min "" "C:\\Users\\ishan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Spotify.lnk"')
    yield f"data: {json.dumps({'step': 5, 'status': 'Spotify ambient audio started'})}\n\n"
    time.sleep(3)

    # 6. Antigravity
    try:
        os.startfile(r"C:\Users\ishan\AppData\Local\Programs\Antigravity\Antigravity.exe")
        time.sleep(2)
        # Use robust PowerShell to force it to foreground, bypassing Windows focus-stealing prevention
        os.system('powershell -command "$wshell = New-Object -ComObject wscript.shell; $wshell.AppActivate(\'Antigravity\')"')
    except Exception:
        pass
    yield f"data: {json.dumps({'step': 6, 'status': 'Antigravity workspace active'})}\n\n"
    time.sleep(2)

    # 7. Voice
    speak("Welcome back. Shall we begin?")
    yield f"data: {json.dumps({'step': 7, 'status': 'Voice synthesis & ready sequence complete'})}\n\n"
    
    # Close stream
    yield "event: close\ndata: {}\n\n"

@app.route('/stream')
def stream():
    return Response(startup_stream(), mimetype='text/event-stream')

@app.route('/start')
def start():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)