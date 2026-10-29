# AI Skill Gap Analyzer – V2 Frontend

An AI-Based Skill Gap Analyzer and Personalized Career Recommendation System that helps students identify missing skills, analyze their skill gaps, and explore personalized learning paths for their target careers.

## Features

- **User Authentication:** Register and log in to the application.
- **Dashboard:** View career profile and skill assessment information.
- **Resume & Skills:** Upload a resume and review extracted skills.
- **Skill Gap Analysis:** Compare current skills with skills required for a target job role.
- **Learning Roadmap:** Explore learning topics, resources, and project ideas for missing skills.
- **AI Career Recommendations:** Get personalized career guidance.
- **Interactive UI:** Built using Streamlit with custom styling.

## Tech Stack

- Python
- Streamlit
- Flask REST API
- MySQL
- CSS
- Git and GitHub

## Project Structure

```text
AI-Skill-Gap-Analyzer-V2-Frontend/
├── .streamlit/
│   └── config.toml
├── assets/
├── .gitignore
├── README.md
├── api.py
├── app.py
├── requirements.txt
└── robot-person (1).png
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/labhshetwarsakshi068-hash/AI-Skill-Gap-Analyzer-V2-Frontend.git
cd AI-Skill-Gap-Analyzer-V2-Frontend
```

### 2. Create and Activate a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

### 4. Configure the Backend

Make sure the Flask backend is running and the frontend is configured with the correct backend API URL.

Keep API keys, database passwords, email credentials, and other secrets in environment variables. Do not commit secret files to GitHub.

### 5. Run the Application

```powershell
python -m streamlit run app.py
```

The application will usually open at:

`http://localhost:8501`

## Repository

[AI-Skill-Gap-Analyzer-V2-Frontend](https://github.com/labhshetwarsakshi068-hash/AI-Skill-Gap-Analyzer-V2-Frontend)

## Project Purpose

This project helps students understand the skills required for their desired careers, identify skill gaps, and plan their learning journey more effectively.

## Note

The frontend requires a compatible Flask backend API for authentication, resume processing, skill gap analysis, and personalized recommendations.

