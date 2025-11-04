# Anti-Idle Script

This Python script prevents system idling by **pressing keys and moving the mouse** at regular intervals.

##❓ Why Use This Script?

Many systems automatically go into sleep or lock mode after a period of inactivity, which can be disruptive during long-running remote sessions, unattended downloads, or background processing tasks. This script ensures your system stays active without requiring third-party tools like Caffeine or other system tray applications that may consume additional resources or clutter your workflow. It provides a lightweight, customizable, and scriptable alternative for keeping your system awake.

## 📌 Features

✅ Runs **until a specified time** or **indefinitely**\
✅ Accepts **command-line arguments** (`python script.py 17:30`)\
✅ **Moves the mouse & presses keys** to simulate activity\
✅ **Logs execution time** using `icecream`\
✅ **Handles invalid inputs gracefully**

---

## 🚀 Installation & Setup

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/petervirtech/anti-idle-script.git
cd anti-idle-script
```

### **2️⃣ Create a Virtual Environment & Install Dependencies**

`uv` can create a virtual environment and install dependencies in one step.

```bash
uv venv
uv pip install -r requirements.txt
```

💡 **Note:** When using `uv run`, the virtual environment is automatically activated. If you need to activate it manually (e.g., for other `pip` commands), use `source venv/bin/activate` (Mac/Linux) or `venv\Scripts\activate` (Windows).

---

## 📝 Usage

### **1️⃣ Run via Command Line**

```bash
uv run python main.py 17:30
```

- Runs until **17:30** today (or tomorrow if 17:30 has passed).

### **2️⃣ Run Interactively**

```bash
uv run python main.py
```

- Prompts:
  ```
  Enter end time (HH:MM) or press Enter to run indefinitely:
  ```
  - Enter `17:30` → Runs until **17:30**.
  - Press **Enter** → Runs **indefinitely**.

### **3️⃣ Stop the Script**

- Use **CTRL + C** in the terminal.

---

## 🛠 Troubleshooting

- If you see an **invalid time format error**, ensure you're entering the time as **HH****:MM** (24-hour format).
- If `pyautogui` doesn't work, ensure your system allows **keyboard and mouse control**.
- If you need to reinstall dependencies, run:
  ```bash
  uv pip install --upgrade --force-reinstall -r requirements.txt
  ```

---

## 🏗 Future Improvements

- Logging to a file instead of only using icecream
- Custom keypress and delay options
- Desktop notification on exit
---

📜 **License:** MIT\
✉ **Maintainer:** Peter

