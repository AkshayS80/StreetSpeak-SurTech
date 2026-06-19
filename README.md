# 🛣️ StreetSpeak

StreetSpeak is a gamified, citizen-powered web platform that empowers users to report civic issues — such as potholes, garbage, broken streetlights, or unsafe conditions — directly from their neighborhoods. Each report earns tokens and is analyzed using AI to assess urgency. The platform helps authorities act faster through transparent, community-driven insights.

---

## 🚀 Features

- 📸 **Report Civic Issues**  
  Users can submit descriptions and photos of local problems.

- 🤖 **AI-Powered Verification**  
  Reports are automatically verified using AI to detect issues like potholes or broken lights.

- 🎮 **Gamified Token System**  
  Verified reports earn tokens based on priority. High-priority issues earn more.

- 🎁 **Token Redemption**  
  Users can redeem tokens for rewards, recognition, or leaderboard status.

- 🏛️ **Government Collaboration Ready**  
  Designed to scale as a government-backed initiative for smart city management.

---

## 🧠 How It Works

1. **Sign Up / Log In**  
   Users create an account to start reporting.

2. **Submit a Report**  
   Describe the issue, upload a photo, and select priority.

3. **AI Verification**  
   The system uses AI to verify the issue and assign urgency.

4. **Earn Tokens**  
   Verified reports earn tokens based on priority level.

5. **Track & Redeem**  
   Users view their token history and redeem tokens for rewards.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Django (Python)  
- **Database:** SQLite  
- **Authentication:** Django’s built-in auth system  
- **AI Verification:** Image/text-based classification  
- **Styling:** Responsive CSS  
- **Hosting:** Localhost (deployment-ready)

---

## 📦 Installation

```bash
git clone https://github.com/AkshayS80/streetspeak.git
cd streetspeak
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
