# 🧠 Django Quiz App
A dynamic and interactive quiz web application built using Django. Users can test their knowledge across various categories and difficulty levels with a smooth, timed quiz interface. The app includes **OTP-based email verification**, secure **user authentication with login/logout**, session-managed quiz flow, and personalized game history tracking.

## Features
- Category selection: History, Science, Sports, and Geography
- Difficulty levels: Easy, Medium, Hard
- Unique background themes for each category
- Timer: Each question must be answered within 60 seconds
- OTP-based email verification
- Score tracking and result history
- Only best results are stored and shown per user
- Filterable past results by category and difficulty
- Answer review: After each quiz, users can see their selected answers and the correct ones
- Admin panel to manage questions and categories

## Technologies Used
- **Backend:** Python (Django)
- **Frontend:** HTML, CSS, Bootstrap
- **Database:** SQLite
- **Email:** Django email backend (for OTP verification)
- **Session Management:** Django Sessions

## Screenshots
- **Login Page:**
![Login](/photos/login.jpeg)

- **Register:**
![Login](/photos/Register.jpeg)

- **Email Otp sent:**
![Login](/photos/email.png)

- **Otp verification:**
![Login](/photos/otppage.jpeg)

- **Home Page:**
![Login](/photos/home.png)

- **Choose a Category and Difficulty level:**
![Login](/photos/Category.png)

- **History Quiz:**
![Login](/photos/History.png)

- **Geography Quiz:**
![Login](/photos/Geography.png)

- **Sports Quiz:**
![Login](/photos/Sports.png)

- **Science Quiz:**
![Login](/photos/Science.png)

- **Result Page:**
![Login](/photos/output.png)

- **Check your answers:**
![Login](/photos/Results.png)

- **View your Record:**
![Login](/photos/record.png)

- **Verify email to change password:**
![Login](/photos/Resetpass.jpeg)

- **Change password:**
![Login](/photos/changepass.jpeg)

## How It Works
- User registers and verifies email via OTP.
- Selects quiz category and difficulty.
- One question is shown at a time with a 60-second timer.
- After quiz completion, the user:
    - Sees their total score
    - Reviews all their answers with correct answers highlighted
- Best scores are stored and shown in View Records, which can be filtered by category and difficulty.

## Run Locally

Clone the project
```bash
  git clone https://github.com/SalanKatuwal/django-quiz-app.git
```

Go to the project directory
```bash
  cd django-quiz-app
```

Set up virtual environment
```bash
  python -m venv env
  env\Scripts\activate
```
Apply migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
Create  a superuser
```bash
python manage.py createsuperuser
```
Start the server
```bash
python manage.py runserver
```
Open in browser: http://localhost:8000

## Email Setup for OTP
Update these settings in your settings.py to enable OTP email functionality:
```bash
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.yourprovider.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your_email@example.com'
EMAIL_HOST_PASSWORD = 'your_password'
```

## Contributing
Pull requests are welcome. For major changes, open an issue first to discuss ideas.

## Author
[@Salan Katuwal](https://www.linkedin.com/in/salan-katuwal-53b452342/)