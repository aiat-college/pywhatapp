# 💬 PyWhatApp

**PyWhatApp** is a Python-powered web application built with [Streamlit](https://streamlit.io/) that allows you to send **bulk WhatsApp messages** effortlessly 📢.  
Powered by the [pywhatkit](https://pypi.org/project/pywhatkit/) library, it’s perfect for **businesses**, **communities**, and **event organizers** who want to reach multiple contacts in just a few clicks.

---

## ✨ Features

- 📂 **Bulk Send** – Upload an Excel file with recipient details and send messages to all listed users.
- ⚡ **Quick Send** – Enter comma-separated WhatsApp numbers and send messages instantly.
- 📝 **Personalization** – Use `%name%` in your message to include each recipient’s name (Bulk Send).
- 👀 **Message Preview** – See exactly how your message will look before sending.
- 🌐 **Browser-based** – Works directly from your browser, no additional software required.
- 🔒 **Privacy First** – Messages are sent through your own WhatsApp Web session. No Data Stored or Shared. All processing happens locally on your device.

---

## 📋 Prerequisites

Before you start, make sure you have:

- 🐍 **Python 3.8+** installed
- ✅ **Google Chrome / Chromium** browser
- ✅ **WhatsApp Web** logged in with the sender's number on the same browser  
  👉 [https://web.whatsapp.com/](https://web.whatsapp.com/)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aiat-college/pywhatapp.git
   cd pywhatapp
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate     # On macOS/Linux
   venv\Scripts\activate        # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Running the App

Run the Streamlit app with:
```bash
streamlit run app.py
```

The app will open in your default web browser. If it doesn’t, visit:
```
http://localhost:8501
```

---

## 📂 Usage

### **1. Bulk Send**
- Upload an Excel file containing a **Phone Number** column (and optionally a **Name** column).
- Use `%name%` in your message to personalize each message.
- Click **Send** to deliver messages to all listed numbers.

### **2. Quick Send**
- Enter one or more comma-separated WhatsApp numbers in the format:
  ```
  +1234567890, +1987654321
  ```
- Type your message and click **Send**.

---

## ⚠️ Important Notes
- ✅ Make sure WhatsApp Web is **already logged in** on this browser with the sender's number.
- 🕒 The app uses **pywhatkit**, which schedules messages a few seconds ahead — keep your browser window active.
- 🚫 Do not use this app for spam or unsolicited messaging. Follow WhatsApp’s terms of service.

---

## 🛠️ Built With
- [Streamlit](https://streamlit.io/) – Web app framework for Python
- [PyWhatKit](https://pypi.org/project/pywhatkit/) – WhatsApp messaging automation
- [Pandas](https://pandas.pydata.org/) – Data processing
- Python Virtual Environment – For isolated dependency management

---

## 🤝 Contributing
Pull requests are welcome! If you’d like to contribute:
1. Fork the repo
2. Create your feature branch (`git checkout -b feature/NewFeature`)
3. Commit changes (`git commit -m 'Add new feature'`)
4. Push to branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

---

## 📜 License
This project is licensed under the **GPL-3.0 license** – see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact
- **Email**: tech@aiat.edu.in  
- **GitHub**: [PyWhatApp Repository](https://github.com/aiat-college/pywhatapp)
