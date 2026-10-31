

import requests

# Backend API URL
API_URL = "https://ai-skill-gap-analyzer-backend-1.onrender.com"

def register_user(name, email, password, education, branch, target_role):
    """Register a new user through the Flask backend."""

    url = f"{API_URL}/api/register"

    payload = {
        "name": name,
        "email": email,
        "password": password,
        "education": education,
        "branch": branch,
        "target_role": target_role
    }

    try:
        response = requests.post(
            url,
            json=payload,
            timeout=30
        )

        try:
            result = response.json()
        except ValueError:
            result = {"message": response.text}

        return response.status_code, result

    except requests.RequestException as error:
        return None, {"message": str(error)}


def upload_resume(token, user_id, uploaded_file):
    """Upload a resume to the backend for skill analysis."""

    url = f"{API_URL}/api/upload-resume"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    files = {
        "resume": (
            uploaded_file.name,
            uploaded_file.getvalue(),
            uploaded_file.type
        )
    }

    data = {
        "user_id": str(user_id)
    }

    try:
        response = requests.post(
            url,
            headers=headers,
            files=files,
            data=data,
            timeout=120
        )

        try:
            result = response.json()
        except ValueError:
            result = {"message": response.text}

        return response.status_code, result

    except requests.RequestException as error:
        return None, {"message": str(error)}

def get_user_skills(token, user_id):
    """Fetch the logged-in user's saved skills."""
    url = f"{API_URL}/api/user-skills/{user_id}"
    headers = {"Authorization": f"Bearer {token}"}

    try:
        response = requests.get(
            url, headers=headers, timeout=30
        )
        try:
            result = response.json()
        except ValueError:
            result = {"message": response.text}

        return response.status_code, result

    except requests.RequestException as error:
        return None, {"message": str(error)}


def get_job_roles():
    """Fetch available target job roles."""
    try:
        response = requests.get(
            f"{API_URL}/api/job-roles", timeout=30
        )
        try:
            result = response.json()
        except ValueError:
            result = {"message": response.text}

        return response.status_code, result

    except requests.RequestException as error:
        return None, {"message": str(error)}


def get_skill_gap(token, user_id, role_id):
    """Analyze the user's skills against a target role."""
    headers = {"Authorization": f"Bearer {token}"}
    params = {
        "user_id": user_id,
        "role_id": role_id
    }

    try:
        response = requests.get(
            f"{API_URL}/api/skill-gap",
            headers=headers,
            params=params,
            timeout=30
        )
        try:
            result = response.json()
        except ValueError:
            result = {"message": response.text}

        return response.status_code, result

    except requests.RequestException as error:
        return None, {"message": str(error)}

def get_ai_recommendation(token, user_id, role_id):
    """Fetch AI-powered career recommendations from Flask backend."""

    headers = {
        "Authorization": f"Bearer {token}"
    }

    params = {
        "user_id": user_id,
        "role_id": role_id
    }

    try:
        response = requests.get(
            f"{API_URL}/api/ai-recommendation",
            headers=headers,
            params=params,
            timeout=120
        )

        try:
            result = response.json()
        except ValueError:
            result = {"message": response.text}

        return response.status_code, result

    except requests.RequestException as error:
        return None, {"message": str(error)}
