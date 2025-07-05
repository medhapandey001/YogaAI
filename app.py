from flask import Flask, request, render_template, jsonify, send_from_directory, redirect, url_for, session, flash
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import pickle
import numpy as np
import traceback
import os
#import pymysql
#pymysql.install_as_MySQLdb()
#def get_db_connection():
 #   return pymysql.connect(
 #       host='localhost',
 #       user='root',
 #       password='',
 #       database='yogaai',
  #      cursorclass=pymysql.cursors.DictCursor
 #   )

app = Flask(__name__)
app.secret_key = 'medha_yogaai_secret_123'


from flask_sqlalchemy import SQLAlchemy

# MySQL database configuration
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/users'
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'yogaai.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database connection

db = SQLAlchemy(app)
# User model for signup/login

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.email}>"


CORS(app)

# Load model and encoders
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('label_encoders.pkl', 'rb') as f:
    label_encoders = pickle.load(f)

with open('target_encoder.pkl', 'rb') as f:
    target_encoder = pickle.load(f)

print("Model and encoders loaded successfully!")
print("Target classes:", target_encoder.classes_)

@app.route('/')
def home():
    if not session.get('loggedin'):
        return redirect(url_for('login'))
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.form.to_dict()
        print("🔍 Received form data:", data)

        # Process input
        categorical_cols = ['gender', 'fitness_level', 'pain_area', 'goal',
                            'stress_level', 'age_group', 'BMI_category', 'stress_category']
        numerical_cols = ['age', 'BMI']

        processed = []
    
        # Encode categorical
        for col in categorical_cols:
            le = label_encoders[col]
            val = data.get(col)
            if val is None:
                return jsonify({'error': f'Missing value for {col}'}), 400
            processed.append(le.transform([val])[0])

        # Add numerical values
        for col in numerical_cols:
            val = float(data.get(col, 0))
            processed.append(val)

        # Convert to numpy array and reshape for prediction
        X_input = np.array(processed).reshape(1, -1)

        # Make prediction
        predicted_class = model.predict(X_input)[0]
        try:
            predicted_label = target_encoder.inverse_transform([predicted_class])[0]
        except ValueError as e:
            print("Prediction error:", e)
            predicted_label = f"Unknown routine (label={predicted_class})"

        # print(f" Predicted class: {predicted_class} => {predicted_label}")
        return render_template('results.html', prediction=predicted_label)
          
        # return f"<p>Recommended Yoga: {predicted_class}</p>"
        

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['loggedin'] = True
            session['email'] = email
            return redirect(url_for('welcome'))
        else:
            error = 'Invalid email or password.'

    return render_template('login.html', error=error)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')
@app.route('/logout')
def logout():
    session.clear()
    return render_template('logout.html')

   
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    show_alert = False
    show_error = None

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cpassword = request.form['cpassword']

        if password != cpassword:
            show_error = "Passwords do not match"
        else:
            existing_user = User.query.filter_by(email=email).first()

            if existing_user:
                show_error = "An account with this email already exists"
            else:
                hashed_pw = generate_password_hash(password)
                new_user = User(email=email, password=hashed_pw)
                db.session.add(new_user)
                db.session.commit()
                show_alert = True

    return render_template('signup.html', show_alert=show_alert, show_error=show_error)






 
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        # ✅ TEMP: Add a sample user inside app context
        if not User.query.filter_by(email='test@example.com').first():
            sample_user = User(
                email='test@example.com',
                password=generate_password_hash('test123')
            )
            db.session.add(sample_user)
            db.session.commit()
            print("✅ Sample user added to yogaai.db")

        import os
        port = int(os.environ.get("PORT", 5000))
        app.run(host='0.0.0.0', port=port)


