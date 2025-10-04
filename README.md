# E-Learning Platform

## Setup
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the FastAPI server: `uvicorn backend.main:app --reload`
4. Open `http://localhost:8000/static/index.html` in your browser.

## Notes
- Uses SQLite (`elearning.db`) for simplicity. Update `DATABASE_URL` in `backend/database.py` for other databases.
- Mock authentication is implemented. Use JWT or OAuth for production.
- Replace mock answer response in `routes.py` with actual backend logic (e.g., AI processing).
- Ensure PDF/video URLs in the database point to valid resources.

project/
├── backend/
│   ├── __init__.py
│   ├── main.py          # FastAPI app setup, CORS, static file serving
│   ├── database.py      # SQLAlchemy setup (SQLite for simplicity)
│   ├── models.py        # SQLAlchemy models for User, Course, Lesson, Material, Book, Comment, Like
│   ├── schemas.py       # Pydantic schemas for API validation
│   └── routes.py        # API endpoints for auth, courses, lessons, materials, books, comments, likes, answers
├── frontend/
│   ├── index.html       # Login/registration page
│   ├── courses.html     # Displays 1st, 2nd, 3rd courses
│   ├── lesson.html      # Lesson page (1st course) with left nav, right content (PDF/video, title, transcripts, answer submission, comments, likes, next/prev buttons)
│   ├── material.html    # Material page (2nd course, PDF only)
│   ├── book.html        # Book page (3rd course, PDF only)
│   ├── styles.css       # Shared styling
│   └── scripts.js       # Shared JavaScript for API calls and dynamic UI
├── requirements.txt     # Dependencies
└── README.md            # Setup instructions