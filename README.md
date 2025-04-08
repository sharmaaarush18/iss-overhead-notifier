# 🛰 ISS Overhead Notifier

A Python automation tool that sends you an email notification **only when the International Space Station (ISS) is overhead and it's dark outside**, so you can go outside and spot it in real time!

---

## ✨ Features

- **Live ISS Tracking**  
  Uses the Open Notify API to get real-time ISS coordinates.

- **Daylight Detection**  
  Checks if it's dark at your location using the Sunrise-Sunset API.

- **Email Alerts**  
  Automatically emails you when conditions are perfect to view the ISS.

- **Runs Forever**  
  Uses a simple loop to keep checking every 60 seconds.

---

## 🛠 Tech Stack

- Python 3
- `requests` module
- Open Notify API
- Sunrise-Sunset API
- SMTP (for email)

---

## 📦 Requirements

This project uses the `requests` module to interact with external APIs.  
Make sure to install it before running the project:

```bash
pip install requests
```

Alternatively, you can install everything listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/sharmaaarush18/iss-overhead-notifier.git
   cd iss-overhead-notifier
   ```

2. **Set Your Coordinates & Email Credentials**
   - Open `main.py`
   - Replace the latitude/longitude with your own location
   - Add your email address and app password (or enable less secure apps)

3. **Run the Project**
   ```bash
   python main.py
   ```

4. **Leave It Running**  
   It checks every minute whether:
   - The ISS is within +5 or -5 degrees of your location
   - It's currently dark outside  
   If both are true, you’ll get an email alert! 🛰📩

---

## 🔐 Environment Variables (Optional but Recommended)

To keep things secure, you can store your email credentials and location in a `.env` file and load them using `python-dotenv`.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

> ❤️ Made with love by Aarush Sharma
