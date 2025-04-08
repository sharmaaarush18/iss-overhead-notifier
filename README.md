# 🛰️ ISS Overhead Notifier

A Python project that uses real-time data from the ISS and your local sunrise/sunset time to notify you when the ISS is flying overhead and visible from your location.

---

## 🌟 Features

- **Tracks the International Space Station (ISS)** in real-time  
- **Fetches your local sunrise and sunset times**  
- **Sends an email notification** if the ISS is overhead and visible (i.e., it's night-time at your location)  
- Utilizes **multiple APIs**: [Open Notify API](http://open-notify.org/Open-Notify-API/ISS-Location-Now/) and [Sunrise Sunset API](https://sunrise-sunset.org/api)

---

## 🛠️ Tech Stack

- **Python 3**  
- **SMTP (for sending emails)**  
- **`requests` module**  
- **`datetime` module**  
- **Open Notify API** (for ISS location)  
- **Sunrise-Sunset API** (for daylight hours)

---

## ▶️ How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/iss-overhead-notifier.git
   cd iss-overhead-notifier
   ```

2. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Your Settings**
   - Open `main.py`
   - Replace placeholders with:
     - Your **latitude** and **longitude**
     - Your **email credentials** (email, password, SMTP server info)

4. **Run the Script**
   ```bash
   python main.py
   ```

   - The script checks every 60 seconds:
     - Is the ISS overhead?
     - Is it dark outside?
     - If **yes** to both: you'll get an email notification to go look up 👀

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤓 Fun Fact

The ISS travels at about 28,000 km/h — meaning it orbits Earth roughly every 90 minutes! 🚀

---

### ❤️ Made with love by Aarush Sharma
