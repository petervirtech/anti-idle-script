# Anti-Idle Script

This Python script prevents system idling by **pressing keys and moving the mouse** at regular intervals.

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
git clone https://github.com/yourusername/anti-idle-script.git
cd anti-idle-script
```

### **2️⃣ Create a Virtual Environment**

Creating a virtual environment ensures dependencies don't interfere with other Python projects.

#### **Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

#### **Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

💡 **Note:** Each time you work on this project, remember to **activate the virtual environment** (`source venv/bin/activate` or `venv\Scripts\activate`).

---

## 📝 Usage

### **1️⃣ Run via Command Line**

```bash
python script.py 17:30
```

- Runs until **17:30** today (or tomorrow if 17:30 has passed).

### **2️⃣ Run Interactively**

```bash
python script.py
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
- If you installed dependencies outside the virtual environment, run:
  ```bash
  pip install --upgrade --force-reinstall -r requirements.txt
  ```

---

## 🏗 Future Improvements

- Logging to a file instead of only using icecream
- Custom keypress and delay options
- Desktop notification on exit
---

📜 **License:** MIT\
✉ **Maintainer:** Peter

