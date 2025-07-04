# 🧘‍♀️ YogaAI

*Your Personalized Yoga & Meditation Assistant – Powered by AI, Guided by Wellness*
![Python](https://img.shields.io/badge/python-3.10-blue)

<p align="center">
  <img src="logo.png" alt="YogaAI Logo" width="200"/>
</p>

---

## 🔍 Features

- 🤖 **AI-Powered Routine Suggestions**  
  Get personalized yoga and meditation routines based on your specific health concerns using trained ML models.

- 💬 **Smart Understanding via NLP**  
  Uses Natural Language Processing to interpret your inputs like "I feel anxious" or "I have back pain" and respond accordingly.

- 🧘‍♂️ **Curated Wellness Plans**  
  Suggests beginner-friendly yoga poses and guided meditations to match your comfort and needs.

- 💻 **Smooth User Interface**  
  Clean, responsive front-end built with HTML, CSS, and JavaScript.

- 🔒 **Secure Login System**  
  Flask-powered authentication system with secure SQLite-based storage using SQLAlchemy ORM
  , and separate login/signup pages for user data protection.

---
## 🛠️ Tech Stack

- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Python with Flask  
- **Database:** SQLite using SQLAlchemy ORM  
- **AI/ML:** scikit-learn, pandas, pickle  
- **NLP Techniques:** Label Encoding, Target Encoding
- ## 📁 Project Structure
- yogaai/
├── static/ # Static assets (CSS, images)
├── templates/ # HTML templates (login, signup, homepage, etc.)
├── app.py # Main Flask application
├── model.pkl # Trained ML model for yoga suggestions
├── label_encoders.pkl # Encoded input features
├── target_encoder.pkl # Encoded output labels
├── requirements.txt # Python dependencies
├── logo.png # Project logo
├── yogaai.db            # SQLite database containing registered users

  


## 🚀 Getting Started

Follow these steps to set up and run YogaAI locally:

### 1. Clone the Repository

```bash
git clone https://github.com/medhapandey001/YogaAI.git

//run these commands one by one in cmd//
cd yogaai
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python app.py

Note: On the first run, the app automatically creates a sample user:
Email: test@example.com  
Password: test123

//open browser and visit http://127.0.0.1:5000//

---

> ✅ Replace `yourusername` with your actual GitHub username in the clone link.
---

## 🤝 Contributing
---

## 🛣️ Roadmap

- [ ] Add more yoga categories (e.g., prenatal, senior-friendly)
- [ ] Improve NLP accuracy with better preprocessing
- [ ] Add voice input support for user concerns
- [ ] Deploy to a live server (Render/Heroku)
- [ ] Add user dashboard with history tracking


Want to contribute to YogaAI?

1. 🍴 Fork the repository  
2. 🌿 Create a new branch: `git checkout -b feature/your-feature`  
3. 💻 Make your changes  
4. ✅ Commit and push: `git push origin feature/your-feature`  
5. 📬 Open a pull request!

All kinds of contributions are welcome — from bug fixes and new features to design suggestions!
---

## ⚙️ Model Files

This project uses pre-trained machine learning models:

- `model.pkl` — core yoga routine prediction model  
- `label_encoders.pkl` and `target_encoder.pkl` — used for processing user input and mapping output

> If you ever need to regenerate these files, make sure to run the training script with the appropriate dataset. (Retraining code coming soon!)



✨ *YogaAI is more than just code — it's a small step toward mindful living through intelligent tech.*  
Feel free to explore, suggest improvements, or contribute!

// done










