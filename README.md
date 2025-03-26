# Digital Art Portfolio & Commission Website

## 🎨 Project Overview
This is a full-stack web application built for a digital artist to showcase their artwork and accept commission requests from clients. It features a clean and responsive design, portfolio display, secure admin access, and a validated form for receiving commission submissions.

## 🧩 Features
- Dynamic portfolio page that displays artworks pulled from a database
- Commission request form with field validation and CSRF protection
- Optional "questions" field in form submissions
- Password-protected admin interface to:
  - View incoming commission requests
  - Add new artwork entries to the portfolio
- Session-based login system using a secure passcode
- Clean UI built with Jinja2 templating and custom CSS
- Image serving directly from the database
- Secure handling of user input using Flask-WTF and `escape()`

## 🔧 Tech Stack
**Frontend:**
- HTML  
- CSS (with Flexbox/Grid)  
- Jinja2  

**Backend:**
- Python  
- Flask  
- Flask-WTF  
- Flask-SQLAlchemy  
- SQLAlchemy ORM  
- Email-validator  
- Python-dotenv  
- Poetry (for dependency and environment management)

## 🔐 Security Considerations
- CSRF protection using Flask-WTF
- Input sanitization with `escape()` to prevent XSS attacks
- Admin-only routes protected via session-based passcode authentication
- Sensitive values stored in `.env` file (not hardcoded)

## 📁 Structure (simplified)
```
/project-root
│
├── /templates        # Jinja2 HTML templates
├── /static           # CSS files, images, etc.
├── /instance         # SQLite database
├── /website
│   ├── __init__.py   # App factory
│   ├── views.py      # Routes and controllers
│   ├── models.py     # SQLAlchemy models
│   ├── forms.py      # Flask-WTF forms
│   └── ...
├── .env              # Environment variables
├── README.md
└── run.py            # App entry point
```

## 🚀 Setup Instructions
1. Clone the repo  
2. Create a virtual environment using Poetry  
3. Add a `.env` file with a secure password  
4. Run the app using `flask run` or `python run.py`

## 📌 Notes
- This project was built as part of the IB Computer Science Internal Assessment.
- Future enhancements include user accounts, improved admin tools, and mobile optimization.
