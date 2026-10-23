# AI Skill Gap Analyzer – V2 Frontend

An AI-Based Skill Gap Analyzer and Personalized Career Recommendation System that helps students identify missing skills, analyze their skill gaps, and explore personalized learning paths for their target careers.

## Features

- **User Authentication:** Register and log in to the application.
- **Dashboard:** View your career profile and skill assessment information.
- **Resume & Skills:** Upload your resume and review extracted skills.
- **Skill Gap Analysis:** Compare your current skills with the skills required for a target job role.
- **Learning Roadmap:** Explore learning recommendations to improve missing skills.
- **AI Career Recommendations:** Get personalized career guidance.
- **Interactive UI:** Built using Streamlit with custom styling.

## Tech Stack

- Python
- Streamlit
- Flask REST API
- CSS
- Git and GitHub

## Project Structure

```text
frontend/
├── app.py
├── api.py
├── requirements.txt
├── .gitignore
├── .streamlit/
│   └── config.toml
├── assets/
│   ├── dashboard-banner.png.png
│   ├── robot-person.png
│   └── style.css
└── robot-person (1).png
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/labhshetwarsakshi068-hash/AI-Skill-Gap-Analyzer-V2-Frontend.git
cd AI-Skill-Gap-Analyzer-V2-Frontend
```

### 2. Create and activate a virtual environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the backend

Make sure the Flask backend is running and configure the correct backend API URL in the frontend. Keep API keys, passwords, and other secrets in environment variables rather than committing them to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

The application will open in your browser, usually at `http://localhost:8501`.

## Repository

[AI-Skill-Gap-Analyzer-V2-Frontend](https://github.com/labhshetwarsakshi068-hash/AI-Skill-Gap-Analyzer-V2-Frontend)

## Project Purpose

This project aims to help students understand the skills required for their desired careers, identify skill gaps, and plan their learning journey more effectively.

---

**Note:** The frontend requires a compatible backend API for authentication, resume processing, skill gap analysis, and personalized recommendations.
