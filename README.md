# Home-Automation-Using-raspberry-Pi
# 🏠 Raspberry Pi Based Home Automation System with Web & Chatbot Control

## 📌 Project Overview
This project implements a **home automation system using Raspberry Pi**, where household appliances are emulated using LEDs and an RGB LED.  
The system can be controlled through:

- ✅ A **web-based dashboard** (buttons + slider)
- ✅ A **chatbot interface** (natural language commands)
- ✅ **PWM-based RGB color fading** to simulate fan speed
- ✅ **User authentication** using Firebase

The Raspberry Pi acts as both the **hardware controller** and **web server**, making the system fully self-contained.

---

## 🎯 Objectives
- Control lights and fan remotely via a web browser
- Simulate fan speed using RGB LED color transitions
- Accept natural language commands through a chatbot
- Maintain synchronization between chatbot commands and UI controls
- Implement secure user authentication
- Use software engineering best practices (process model & design patterns)

---

## 🧩 Features
### 🔹 Light Control
- Turn light **ON/OFF**
- Controlled via buttons and chatbot

### 🔹 Fan Control (RGB Simulation)
- Fan **ON/OFF**
- Speed control using a **slider (0–100%)**
- Smooth **PWM-based RGB color fading**
- Last fan speed is restored when fan is turned back ON

### 🔹 Chatbot Control
- Commands like:
  - `turn on fan`
  - `turn off light`
  - `set fan speed to 40`
  - `turn on fan and turn off light`
- Multiple actions handled in a single command
- UI updates automatically after chatbot actions

### 🔹 Authentication
- Firebase-based login/signup
- Dashboard accessible only after authentication

### 🔹 Network
- Raspberry Pi runs Flask server
- Static IP configuration for fixed dashboard URL

---

## 🛠 Hardware Components
- Raspberry Pi (any GPIO-capable model)
- Breadboard
- LEDs (for light simulation)
- RGB LED (common cathode recommended)
- 220Ω resistors
- Jumper wires

---

## 💻 Software & Technologies Used
- **Python 3**
- **Flask** – backend web framework
- **gpiozero** – GPIO and PWM control
- **HTML / CSS / JavaScript** – frontend
- **Firebase Authentication**
- **PWM (Pulse Width Modulation)** for RGB fading

---

## 🧠 Software Process Model
**Incremental Process Model (with Agile characteristics)**

The system was developed in multiple functional increments:
1. Basic GPIO control
2. Web-based control
3. PWM fan simulation
4. Chatbot integration
5. State synchronization
6. Authentication and UX improvements

---

## 🧩 Design Patterns Used
### ✅ Primary Pattern: **Adapter Pattern**
- Adapts high-level user commands (web/chatbot) into low-level GPIO operations

### Additional Patterns:
- **MVC (Model–View–Controller)** – system architecture
- **Command Pattern** – chatbot command execution
- **Facade Pattern** – Flask API hides hardware complexity
- **Observer-like behavior** – UI reacts to backend state changes

---

## 📂 Project Structure
home-automation/
│
├── app.py # Flask backend + GPIO logic
├── templates/
│ └── index.html # Web dashboard UI
├── static/ # (Optional) CSS/JS files
└── README.md

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies
```bash
sudo apt update
sudo apt install python3-flask
pip3 install gpiozero
```
2️⃣ Run the Application
```
sudo python3 app.py
```
3️⃣ Open Dashboard
```
http://<STATIC_PI_IP>:5000
```
🗣 Example Chatbot Commands
turn on light
turn off fan
set fan speed to 30
turn on fan and turn off light
🔐 Authentication
Login & signup handled using Firebase Authentication
Only authenticated users can access the dashboard
🚀 Future Improvements
Voice control integration
Real fan and relay module support
Mobile app version
MQTT-based IoT architecture
Database-based state persistence
HTTPS & remote access
👨‍💻 Author
[Mohammad Muaz & Pulok Kumar Shompod]
Department of Computer Science & Engineering, RUET
Raspberry Pi Home Automation Project
