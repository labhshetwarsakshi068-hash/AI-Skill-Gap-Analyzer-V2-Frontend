import streamlit as st
from pathlib import Path
from api import (
    get_ai_recommendation,
    get_progress,
    update_progress,
    login_user,
    get_job_roles,
    register_user
)

st.set_page_config(
    page_title="AI Skill Gap Analyzer",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Load CSS
css_path = Path(__file__).parent / "assets" / "style.css"
if css_path.exists():
    st.markdown(
        f"<style>{css_path.read_text(encoding='utf-8')}</style>",
        unsafe_allow_html=True
    )

# Session state
defaults = {
    "page": "Home",
    "logged_in": False,
    "user": None,
}

for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value


def go_to(page):
    st.session_state.page = page
    st.rerun()


# Navigation
if st.session_state.logged_in:
    pages = [
        "Dashboard",
        "Resume Skills",
        "Skill Gap Analysis",
        "Learning Roadmap",
        "AI Recommendations",
        "Progress Tracking",
        "Logout"
    ]
else:
    pages = ["Home", "Register", "Login", "Forgot Password"]

with st.sidebar:
    st.markdown(
        """
        <div style="padding:12px 0 22px">
            <div style="font-size:23px;font-weight:800;color:#50dcff">
                ◈ AI Skill Gap Analyzer
            </div>
            <div style="font-size:12px;color:#a9bbdf">
                Build Your Future
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()
 
with st.sidebar:
    for nav_page in pages:
        if nav_page == "Forgot Password":
            continue

        if st.button(
            nav_page,
            key=f"nav_{nav_page}",
            use_container_width=True
        ):
            st.session_state.page = nav_page
            st.rerun()

    page = st.session_state.page

    st.divider()
    st.caption("Small steps today,")
    st.caption("bigger opportunities tomorrow.")


# Top breadcrumb
st.markdown(
    """
    <div style="
        color:#91b7f4;
        font-size:28px;
        font-weight:900;
        line-height:1.6;
        padding:12px 0 24px;
        letter-spacing:0.5px;
    ">
        AI SKILL GAP ANALYZER / Personalized Career Platform
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()

# =========================================================
# HELPER FUNCTION
# =========================================================


def feature_card(number, title, description):
    st.markdown(
        f"""
        <div style="
            background:#0d1b36;
            border:1px solid #244a82;
            border-radius:12px;
            padding:18px;
            min-height:120px;
            margin-bottom:12px;
        ">
            <div style="color:#36d9ff;font-size:12px;font-weight:700">
                {number}
            </div>
            <h4 style="color:#f3f6ff;margin:10px 0">
                {title}
            </h4>
            <p style="color:#aabbd8;margin:0">
                {description}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

# =========================================================
# HOME
# =========================================================

if page == "Home":

    st.markdown(
        """
        <div class="home-nav"></div>
        <div class="home-kicker">YOUR CAREER JOURNEY STARTS HERE</div>
        """,
        unsafe_allow_html=True
    )

    hero_left, hero_right = st.columns([1.15, 0.85], gap="large")

    with hero_left:
        st.markdown(
            """
            <div class="home-hero">
                <div class="home-title">
                    AI-Based<br>
                    <span>Skill Gap Analyzer</span>
                </div>
                <div class="home-subtitle">
                    Personalized Career Recommendation System
                </div>
                <div class="home-description">
                    Analyze your current skills, identify skill gaps,
                    discover career opportunities, and get personalized
                    learning recommendations based on your target role.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        c1, c2 = st.columns(2)
        with c1:
            if st.button("Get Started →", use_container_width=True):
                go_to("Register")
        with c2:
            if st.button("Explore Dashboard", use_container_width=True):
                go_to("Dashboard")

                
    with hero_right:
        image_path = Path(__file__).parent / "assets" / "robot-person.png"

        if image_path.exists():
            st.image(
                str(image_path),
                width=420
            )
        else:
            st.error("Image not found in assets folder.")

            
    st.markdown("## What Our System Provides")

    features = [
        ("📄", "01", "Resume Analysis",
         "Upload your resume and identify your existing technical skills."),
        ("🎯", "02", "Skill Gap Analysis",
         "Compare your current skills with your target job role."),
        ("🗺️", "03", "Learning Roadmap",
         "Plan learning steps, topics, resources and practical projects."),
        ("🧠", "04", "AI Career Recommendations",
         "Explore career options aligned with your skills and interests.")
    ]

    cols = st.columns(4, gap="medium")
    for col, item in zip(cols, features):
        icon, number, title, description = item
        with col:
            st.markdown(
                f"""
                <div class="home-feature">
                    <div style="color:#50dcff;font-size:12px;font-weight:800">
                        {number}
                    </div>
                    <div class="home-feature-icon">{icon}</div>
                    <h3>{title}</h3>
                    <p>{description}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        """
        <div class="home-cta">
            <div style="font-size:20px;font-weight:800">
                🚀 Start Your Career Skill Analysis
            </div>
            <p style="color:#c6d7ff">
                Register or log in to begin your personalized career journey.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if st.button("Create Your Account →", key="home_register"):
        go_to("Register")

# REGISTER
elif page == "Register":
    left, right = st.columns([0.9, 1.1], gap="large")

    with left:
        st.markdown(
            """
            <div class="home-hero">
                <div class="home-kicker">YOUR FUTURE STARTS HERE</div>
                <div class="home-title">
                    Build Your<br><span>Career Profile</span>
                </div>
                <div class="home-description">
                    Create your account to analyze your skills and
                    discover your next career opportunities.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with right:
        st.markdown("## Create Your Account")
        st.caption("Join us and start your career journey.")

        with st.form("register_form"):
            name = st.text_input("Full Name")
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            confirm = st.text_input("Confirm Password", type="password")

            education = st.selectbox(
                "Education",
                [
                    "Select Education", "Diploma", "B.Tech", "B.E.",
                    "B.Sc", "M.Tech", "MCA", "Other"
                ]
            )

            branch = st.selectbox(
                "Branch",
                [
                    "Select Branch", "Computer Science",
                    "Information Technology", "AI & Data Science",
                    "Electronics", "Other"
                ]
            )

            role = st.selectbox(
                "Target Career Role",
                [
                    "Select Role", "Data Scientist", "Web Developer",
                    "Data Analyst", "Java Developer", "AI/ML Engineer"
                ]
            )

            submitted = st.form_submit_button(
                "Create Account →",
                use_container_width=True
            )

        if submitted:
            if not all([name.strip(), email.strip(), password, confirm]):
                st.error("Please fill in all fields.")

            elif password != confirm:
                st.error("Passwords do not match.")

            elif len(password) < 8:
                st.error("Password must contain at least 8 characters.")

            elif education == "Select Education":
                st.error("Please select your education.")

            elif branch == "Select Branch":
                st.error("Please select your branch.")

            elif role == "Select Role":
                st.error("Please select your target role.")

            else:
                with st.spinner("Creating your account..."):
                    status, result = register_user(
                        name.strip(),
                        email.strip(),
                        password,
                        education,
                        branch,
                        role
                    )

                if status == 201 and result.get("success"):
                    st.success(
                        "Registration successful! Please log in."
                    )

                elif status is None:
                    st.error("Could not connect to the backend.")
                    st.caption(result.get("message", ""))

                else:
                    st.error(
                        result.get("message", "Registration failed.")
                    )

        st.markdown("Already registered?")

        if st.button("Go to Login"):
            go_to("Login")
# =========================================================
# LOGIN
# =========================================================
elif page == "Login":

    _, form_col, _ = st.columns([1, 1.5, 1])

    with form_col:
        st.markdown(
            "<div style='text-align:center'><h1>Welcome Back!</h1>"
            "<p>Login to your career dashboard.</p></div>",
            unsafe_allow_html=True
        )

        with st.form("login_form"):
            email = st.text_input("Email Address")
            password = st.text_input("Password", type="password")
            submitted = st.form_submit_button(
                "Login →", use_container_width=True
            )

        if submitted:
            if not email.strip() or not password:
                st.error("Enter your email and password.")
            else:
                try:
                    login_user

                    with st.spinner("Logging in..."):
                        status, result = login_user(
                            email.strip(),
                            password
                        )

                    if status == 200:
                        st.session_state["token"] = result.get("token")
                        st.session_state["user"] = result.get("user", {})
                        st.session_state["logged_in"] = True

                        st.success("Login successful!")
                        st.rerun()

                    elif status is None:
                        st.error("Could not connect to the backend.")
                        st.caption(str(result.get("message", "")))

                    else:
                        st.error("Login failed.")
                

                except Exception as error:
                    st.error("Login error.")
                    st.caption(str(error))

        if st.button("Forgot Password?"):
            st.session_state["otp_sent"] = False
            st.session_state["otp_verified"] = False
            st.session_state.pop("reset_email", None)
            st.session_state.pop("reset_otp", None)
            go_to("Forgot Password")

        if st.button("Create an Account"):
            go_to("Register")


# =========================================================
# FORGOT PASSWORD
# =========================================================
elif page == "Forgot Password":

    import requests
    from api import API_URL

    st.title("Forgot Password")
    st.caption("Reset your password using the OTP sent to your email.")

    if not st.session_state.get("otp_sent", False):

        with st.form("forgot_password_form"):
            reset_email_input = st.text_input("Registered Email Address")
            send_otp = st.form_submit_button(
                "Send OTP", use_container_width=True
            )

        if send_otp:
            if not reset_email_input.strip():
                st.error("Please enter your registered email.")
            else:
                try:
                    with st.spinner("Sending OTP..."):
                        response = requests.post(
                            f"{API_URL}/api/forgot-password",
                            json={"email": reset_email_input.strip()},
                            timeout=30
                        )

                    try:
                        result = response.json()
                    except ValueError:
                        result = {}

                    if response.status_code == 200:
                        st.session_state["reset_email"] = (
                            reset_email_input.strip().lower()
                        )
                        st.session_state["otp_sent"] = True
                        st.session_state["otp_verified"] = False
                        st.success("OTP request submitted.")
                        st.rerun()
                    else:
                        st.error(
                            result.get("message", "Could not send OTP.")
                        )

                except Exception as error:
                    st.error("Could not connect to the backend.")
                    st.caption(str(error))

    if st.session_state.get("otp_sent", False):

        st.info(
            f"OTP sent to: {st.session_state.get('reset_email', '')}"
        )

        with st.form("verify_otp_form"):
            otp = st.text_input(
                "Enter 6-digit OTP",
                max_chars=6
            )
            verify_otp = st.form_submit_button(
                "Verify OTP", use_container_width=True
            )

        if verify_otp:
            if not otp.isdigit() or len(otp) != 6:
                st.error("Please enter a valid 6-digit OTP.")
            else:
                try:
                    email_to_reset = st.session_state.get(
                        "reset_email", ""
                    ).strip().lower()

                    with st.spinner("Verifying OTP..."):
                        response = requests.post(
                            f"{API_URL}/api/verify-reset-otp",
                            json={
                                "email": email_to_reset,
                                "otp": otp
                            },
                            timeout=30
                        )

                    try:
                        result = response.json()
                    except ValueError:
                        result = {}

                    if response.status_code == 200:
                        st.session_state["otp_verified"] = True
                        st.session_state["reset_otp"] = otp
                        st.success("OTP verified successfully!")
                        st.rerun()
                    else:
                        st.error(
                            result.get(
                                "message", "OTP verification failed."
                            )
                        )

                except Exception as error:
                    st.error("Could not connect to the backend.")
                    st.caption(str(error))

    if st.session_state.get("otp_verified", False):

        st.subheader("Set New Password")

        with st.form("reset_password_form"):
            new_password = st.text_input(
                "New Password", type="password"
            )
            confirm_password = st.text_input(
                "Confirm New Password", type="password"
            )
            reset_password = st.form_submit_button(
                "Reset Password", use_container_width=True
            )

        if reset_password:
            if len(new_password) < 8:
                st.error("Password must contain at least 8 characters.")
            elif new_password != confirm_password:
                st.error("Passwords do not match.")
            else:
                try:
                    email_to_reset = st.session_state.get(
                        "reset_email", ""
                    ).strip().lower()
                    saved_otp = st.session_state.get("reset_otp", "")

                    with st.spinner("Resetting password..."):
                        response = requests.post(
                            f"{API_URL}/api/reset-password",
                            json={
                                "email": email_to_reset,
                                "otp": saved_otp,
                                "new_password": new_password
                            },
                            timeout=30
                        )

                    try:
                        result = response.json()
                    except ValueError:
                        result = {}

                    if response.status_code == 200:
                        st.success(
                            "Password reset successfully! Please log in."
                        )

                        st.session_state["otp_sent"] = False
                        st.session_state["otp_verified"] = False
                        st.session_state.pop("reset_email", None)
                        st.session_state.pop("reset_otp", None)

                        go_to("Login")
                    else:
                        st.error(
                            result.get(
                                "message", "Password reset failed."
                            )
                        )

                except Exception as error:
                    st.error("Could not connect to the backend.")
                    st.caption(str(error))

    if st.button("← Back to Login"):
        st.session_state["otp_sent"] = False
        st.session_state["otp_verified"] = False
        st.session_state.pop("reset_email", None)
        st.session_state.pop("reset_otp", None)
        go_to("Login")



# =========================================================
# DASHBOARD
# =========================================================
elif page == "Dashboard":

    user = st.session_state.get("user") or {}

    user_name = user.get("name") or "Student"
    email = user.get("email") or "Email not available"
    education = user.get("education") or "Not provided"
    branch = user.get("branch") or "Not provided"

    target_role = (
        user.get("target_role")
        or user.get("target_role_name")
        or user.get("role")
        or "Not selected"
    )

    initials = "".join(
        part[0] for part in user_name.split()[:2] if part
    ).upper()

    
    banner_col1, banner_col2 = st.columns([1, 1.5], gap="medium")

    with banner_col1:
        st.markdown(
            f"""
            <div class="welcome-text">
                <div class="welcome-kicker">AI SKILL GAP ANALYZER</div>
                <div class="welcome-title">Welcome back,<br/>{user_name}! 👋</div>
                <div class="welcome-desc">
                    Let's continue building your dream career.<br/>
                    Check your progress and explore new opportunities.
                </div>
                <br/>
            </div>
            """,
            unsafe_allow_html=True
        )

        
    with banner_col2:
        st.empty()

    st.markdown(
        """
        <div class="dashboard-muted" style="text-align:center;">
            ✨ Better skills. Bigger dreams. Brighter future.
        </div>
        """,
        unsafe_allow_html=True
    )



    profile_col, info_col = st.columns([1, 2], gap="large")
    with profile_col:
        st.markdown(
            f"""
            <div class="dashboard-panel">
                <div class="dashboard-small-label">
                    YOUR PROFILE
                </div>
                <div style="
                    width:68px;height:68px;border-radius:50%;
                    background:linear-gradient(135deg,#50dcff,#8d48ff);
                    color:#07132b;display:flex;align-items:center;
                    justify-content:center;font-size:25px;
                    font-weight:800;margin:12px 0;
                ">{initials}</div>
                <div class="dashboard-profile-name">{user_name}</div>
                <div class="dashboard-muted">{email}</div>
                <br>
                <span class="dashboard-chip">Student Profile</span>
                <br><br>
                <div class="dashboard-small-label">TARGET CAREER</div>
                <div style="color:#50dcff;font-weight:700">
                    {target_role}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    
     
   
    with info_col:
        st.markdown("## 👤 Profile Information")

        with st.container(border=True):
            st.markdown("**Education**")
            st.write(education)

            st.divider()

            st.markdown("**Branch**")
            st.write(branch)

            st.divider()

            st.markdown("**Email Address**")
            st.write(email)

    c1, c2, c3 = st.columns(3, gap="large")

    with c1:
        st.markdown(
            """
            <div class="dashboard-panel">
                <div style="font-size:28px">📄</div>
                <div class="dashboard-panel-title">Resume Skills</div>
                <div class="dashboard-muted">
                    Upload your resume and review your extracted skills.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Upload Resume →", use_container_width=True):
            go_to("Resume Skills")

    with c2:
        st.markdown(
            """
            <div class="dashboard-panel">
                <div style="font-size:28px">🎯</div>
                <div class="dashboard-panel-title">Skill Gap Analysis</div>
                <div class="dashboard-muted">
                    Compare your current skills with your target career.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Analyze Skills →", use_container_width=True):
            go_to("Skill Gap Analysis")

    with c3:
        st.markdown(
            """
            <div class="dashboard-panel">
                <div style="font-size:28px">🗺️</div>
                <div class="dashboard-panel-title">Learning Roadmap</div>
                <div class="dashboard-muted">
                    Discover a step-by-step learning path for your goals.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("View Roadmap →", use_container_width=True):
            go_to("Learning Roadmap")

    c4, c5, c6 = st.columns(3, gap="large")

    with c4:
        st.markdown(
            """
            <div class="dashboard-panel">
                <div style="font-size:28px">🤖</div>
                <div class="dashboard-panel-title">AI Recommendations</div>
                <div class="dashboard-muted">
                    Get personalized career and skill suggestions.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
        if st.button("Get Recommendations →", use_container_width=True):
            go_to("AI Recommendations")


# =========================================================
# RESUME SKILLS
# =========================================================
elif page == "Resume Skills":

    st.title("📄 Resume Skills")
    st.caption("Upload your resume to begin your skill assessment.")

    with st.container(border=True):

        uploaded = st.file_uploader(
            "Upload your resume (PDF, DOCX or Image)",
            type=["pdf", "docx", "jpg", "jpeg", "png"]
        )

        if uploaded:

            st.success(f"Selected file: {uploaded.name}")

            if st.button("Analyze Resume", use_container_width=True):

                try:
                    from api import upload_resume

                    token = st.session_state.get("token")
                    user = st.session_state.get("user", {})

                    if not token:
                        st.warning("Please login first.")

                    elif not isinstance(user, dict) or not user.get("id"):
                        st.warning("User ID not found. Please login again.")

                    else:

                        with st.spinner("Analyzing your resume..."):

                            status, result = upload_resume(
                                token,
                                user["id"],
                                uploaded
                            )

                        if status == 200:

                            st.success("Resume uploaded successfully!")

                            detected = result.get("detected_skills", [])
                            saved = result.get("saved_skills", [])
                            not_found = result.get("not_found_skills", [])

                            total_detected = result.get(
                                "total_detected_skills",
                                len(detected)
                            )

                            total_saved = result.get(
                                "total_saved_skills",
                                len(saved)
                            )

                            # SUMMARY
                            st.divider()
                            st.subheader("📊 Resume Analysis Summary")

                            col1, col2, col3 = st.columns(3)

                            col1.metric(
                                "Detected Skills",
                                total_detected
                            )

                            col2.metric(
                                "Saved Skills",
                                total_saved
                            )

                            col3.metric(
                                "Not Found",
                                len(not_found)
                            )

                            # DETECTED SKILLS
                            st.divider()
                            st.subheader("✅ Detected Skills")

                            if detected:

                                categories = {
                                    "Programming Languages": [
                                        "Python", "Java", "C++", "C",
                                        "JavaScript", "PHP"
                                    ],
                                    "Web Technologies": [
                                        "HTML", "CSS", "React",
                                        "Angular", "Node.js"
                                    ],
                                    "Data Science": [
                                        "Pandas", "NumPy", "Matplotlib",
                                        "Machine Learning", "Deep Learning"
                                    ],
                                    "Database": [
                                        "SQL", "MySQL", "MongoDB",
                                        "PostgreSQL"
                                    ],
                                    "DevOps & Cloud": [
                                        "Docker", "Kubernetes", "AWS",
                                        "Azure", "Jenkins", "Git"
                                    ],
                                    "Tools & Platforms": [
                                        "GitHub", "Linux", "VS Code"
                                    ]
                                }

                                displayed_skills = set()

                                for category, category_skills in categories.items():

                                    matched = [
                                        skill for skill in detected
                                        if skill.lower() in [
                                            item.lower()
                                            for item in category_skills
                                        ]
                                    ]

                                    if matched:

                                        st.markdown(f"**{category}**")

                                        st.write(" · ".join(matched))

                                        displayed_skills.update(
                                            skill.lower()
                                            for skill in matched
                                        )

                                other_skills = [
                                    skill for skill in detected
                                    if skill.lower() not in displayed_skills
                                ]

                                if other_skills:

                                    st.markdown("**Other Skills**")
                                    st.write(" · ".join(other_skills))

                            else:

                                st.info("No skills detected in this resume.")

                            # SAVED SKILLS
                            st.divider()
                            st.subheader("💾 Skills Saved in Database")

                            if saved:
                                st.write(" · ".join(saved))
                                st.success(
                                    f"{total_saved} skills saved successfully."
                                )
                            else:
                                st.info("No skills were saved.")

                            # NOT FOUND SKILLS
                            st.divider()
                            st.subheader("⚠️ Skills Not Found")

                            if not_found:
                                st.write(" · ".join(not_found))
                            else:
                                st.success("All detected skills were saved!")

                            # FILE INFORMATION
                            with st.expander("📁 Resume File Details"):

                                st.write(
                                    "**Original Filename:**",
                                    result.get("filename", uploaded.name)
                                )

                                st.write(
                                    "**Saved Filename:**",
                                    result.get("saved_filename", "N/A")
                                )

                                st.write(
                                    "**User ID:**",
                                    result.get("user_id", "N/A")
                                )

                                st.write(
                                    "**Status:**",
                                    result.get("message", "Success")
                                )

                        elif status is None:

                            st.error("Could not connect to the backend.")

                            st.caption(
                                str(result.get("message", ""))
                            )

                        else:

                            st.error(f"Upload failed (HTTP {status}).")

                            st.write(
                                result.get("message", "Please try again.")
                            )

                except Exception as error:

                    st.error("Something went wrong.")
                    st.caption(str(error))

# SKILL GAP ANALYSIS
elif page == "Skill Gap Analysis":
    st.title("Skill Gap Analysis")
    st.caption("Compare your saved skills with your target job role.")

    from api import get_user_skills, get_job_roles, get_skill_gap

    token = st.session_state.get("token")
    user = st.session_state.get("user") or {}
    user_id = user.get("id")

    if not token or not user_id:
        st.warning("Please log in again to analyze your skills.")

    else:
        # Fetch saved skills
        with st.spinner("Loading your saved skills..."):
            skills_status, skills_result = get_user_skills(
                token, user_id
            )

        if skills_status != 200 or not skills_result.get("success"):
            st.error("Could not load your saved skills.")
            st.write(skills_result.get("message", "Please try again."))

        else:
            saved_skills = skills_result.get("skills", [])

            if saved_skills:
                st.markdown("### Your Saved Skills")
                st.write(
                    ", ".join(
                        item["skill_name"] for item in saved_skills
                    )
                )
            else:
                st.info("No saved skills found. Please upload your resume first.")

            
            # Fetch available job roles
            with st.spinner("Loading target job roles..."):
                roles_status, roles_result = get_job_roles()

            if roles_status != 200 or not roles_result.get("success"):
                st.error("Could not load job roles.")
                st.write(roles_result.get("message", "Please try again."))
            else:
                roles = roles_result.get("job_roles", [])

                # Hide Data Scientist from the dropdown
                roles = [
                    role for role in roles
                    if role["role_name"].strip().lower() != "data scientist"
                ]

                if not roles:
                    st.warning("No job roles found in the database.")
                else:
                    role_names = [item["role_name"] for item in roles]
                    current_role = user.get("target_role", "")
                    default_index = 0

                    for index, role_item in enumerate(roles):
                        if role_item["role_name"].strip().lower() == str(current_role).strip().lower():
                            default_index = index
                            break

                    selected_role = st.selectbox(
                        "Target Job Role",
                        role_names,
                        index=default_index
                    )

                    if st.button(
                        "Analyze Skill Gap →",
                        use_container_width=True
                    ):
                        selected_role_data = next(
                            item for item in roles
                            if item["role_name"] == selected_role
                        )

                        role_id = selected_role_data["id"]

                        if not saved_skills:
                            st.warning(
                                "Upload your resume first so your saved skills "
                                "can be compared with this role."
                            )
                        else:
                            with st.spinner("Analyzing your skill gap..."):
                                gap_status, gap_result = get_skill_gap(
                                    token, user_id, role_id
                                )

                            if (
                                gap_status == 200
                                and gap_result.get("success")
                            ):
                                matched = gap_result.get(
                                    "matched_skills", []
                                )
                                missing = gap_result.get(
                                    "missing_skills", []
                                )
                                percentage = gap_result.get(
                                    "match_percentage", 0
                                )
                                total_required = gap_result.get(
                                    "total_required_skills", 0
                                )

                                st.session_state["skill_gap_result"] = {
                                    "role": selected_role,
                                    "matched": matched,
                                    "missing": missing,
                                    "percentage": percentage,
                                    "total_required": total_required
                                }

                            else:
                                st.error(
                                    gap_result.get(
                                        "message",
                                        "Skill gap analysis failed."
                                    )
                                )

                    # Display last successful analysis
                    analysis = st.session_state.get("skill_gap_result")

                    if analysis and analysis.get("role") == selected_role:
                        st.divider()
                        st.subheader(
                            f"Results for {analysis['role']}"
                        )

                        col1, col2, col3 = st.columns(3)

                        with col1:
                            st.metric(
                                "Required Skills",
                                analysis["total_required"]
                            )

                        with col2:
                            st.metric(
                                "Matched Skills",
                                len(analysis["matched"])
                            )

                        with col3:
                            st.metric(
                                "Skill Match",
                                f"{analysis['percentage']}%"
                            )

                        st.progress(
                            min(
                                max(float(analysis["percentage"]) / 100, 0),
                                1
                            )
                        )

                        left, right = st.columns(2)

                        with left:
                            st.markdown("### ✅ Matched Skills")
                            if analysis["matched"]:
                                for skill in analysis["matched"]:
                                    st.write(f"• {skill}")
                            else:
                                st.info("No matching skills found yet.")

                        with right:
                            st.markdown("### 📚 Skills to Learn")
                            if analysis["missing"]:
                                for skill in analysis["missing"]:
                                    st.write(f"• {skill}")
                            else:
                                st.success(
                                    "Great! All required skills are matched."
                                )

#
# =========================================================
# LEARNING ROADMAP
# =========================================================
elif page == "Learning Roadmap":
    import requests
    from api import API_URL

    st.title("Your Learning Roadmap")
    st.caption("A personalized learning path based on your target role and skills.")

    token = st.session_state.get("token")
    user = st.session_state.get("user") or {}
    user_id = user.get("id")

    if not token or not user_id:
        st.warning("Please log in again to view your learning roadmap.")

    else:
        # Reuse the selected role from the Skill Gap Analysis page
        analysis = st.session_state.get("skill_gap_result") or {}
        selected_role_name = analysis.get("role") or (
            user.get("target_role")
            or user.get("target_role_name")
            or user.get("role")
        )

        try:
            from api import get_job_roles

            roles_status, roles_result = get_job_roles()

            if roles_status != 200 or not roles_result.get("success"):
                st.error("Could not load job roles.")
                st.write(roles_result.get("message", "Please try again."))

            else:
                roles = roles_result.get("job_roles", [])

                matching_role = next(
                    (
                        role for role in roles
                        if role.get("role_name", "").strip().lower()
                        == str(selected_role_name or "").strip().lower()
                    ),
                    None
                )

                if not matching_role:
                    st.warning(
                        "Target role could not be identified. "
                        "Open Skill Gap Analysis, select your target role, "
                        "and click Analyze Skill Gap first."
                    )

                else:
                    role_id = matching_role.get("id")

                    with st.spinner("Preparing your personalized roadmap..."):
                        response = requests.get(
                            f"{API_URL}/api/personalized-roadmap",
                            params={
                                "user_id": user_id,
                                "role_id": role_id
                            },
                            headers={
                                "Authorization": f"Bearer {token}"
                            },
                            timeout=30
                        )

                    try:
                        result = response.json()
                    except ValueError:
                        result = {}

                    if response.status_code != 200 or not result.get("success"):
                        st.error(
                            result.get(
                                "message",
                                "Could not load your personalized roadmap."
                            )
                        )

                    else:
                        st.subheader(
                            f"Target Role: {result.get('target_role', selected_role_name)}"
                        )

                        percentage = result.get("match_percentage", 0)
                        st.metric("Skill Match", f"{percentage}%")
                        st.progress(
                            min(max(float(percentage) / 100, 0), 1)
                        )

                        matched = result.get("matched_skills", [])
                        missing = result.get("missing_skills", [])
                        roadmap = result.get("personalized_roadmap", [])

                        with st.expander("Skills you already have"):
                            if matched:
                                st.write(", ".join(matched))
                            else:
                                st.info("No matched skills found yet.")

                        st.markdown("## Skills to Learn")

                        if not missing:
                            st.success(
                                "Great! You have matched all required skills "
                                "for this role."
                            )

                        elif not roadmap:
                            st.info(
                                "No learning resources are available yet "
                                "for your missing skills."
                            )

                        else:
                            for index, item in enumerate(roadmap, start=1):
                                skill_name = item.get(
                                    "skill_name", "Skill"
                                )
                                difficulty = item.get(
                                    "difficulty", "Not specified"
                                )

                                with st.container(border=True):
                                    st.markdown(
                                        f"### {index:02d}. {skill_name}"
                                    )
                                    st.caption(
                                        f"Difficulty: {difficulty}"
                                    )

                                    st.markdown("**Learning Topics**")
                                    topics = item.get("learning_topics")
                                    st.write(
                                        topics or "Topics will be added soon."
                                    )

                                    st.markdown("**Learning Resources**")
                                    resources = item.get("resources")
                                    st.write(
                                        resources or "No resources available yet."
                                    )

                                    st.markdown("**Project Ideas**")
                                    projects = item.get("project_ideas")
                                    st.write(
                                        projects or "Project ideas will be added soon."
                                    )

        except requests.RequestException as error:
            st.error("Could not connect to the backend.")
            st.caption(str(error))

        except Exception as error:
            st.error("Something went wrong while loading the roadmap.")
            st.caption(str(error))


#
# AI RECOMMENDATIONS
elif page == "AI Recommendations":
    st.title("AI Career Recommendations")
    st.caption(
        "Get personalized career guidance based on your target role and skills."
    )

    token = st.session_state.get("token")
    user = st.session_state.get("user") or {}
    user_id = user.get("id")

    if not token or not user_id:
        st.warning("Please log in again to view AI recommendations.")

    else:
        analysis = st.session_state.get("skill_gap_result") or {}

        selected_role_name = (
            analysis.get("role")
            or user.get("target_role")
            or user.get("target_role_name")
            or user.get("role")
        )

        if not selected_role_name:
            st.warning(
                "Please select your target role in Skill Gap Analysis first."
            )

        else:
            st.write(f"**Target Role:** {selected_role_name}")

            if st.button(
                "Generate AI Recommendation →",
                use_container_width=True
            ):
                with st.spinner("Generating your personalized recommendation..."):
                    try:
                        roles_status, roles_result = get_job_roles()

                        if roles_status != 200:
                            st.error("Could not load job roles.")
                            st.write(
                                roles_result.get("message", "Please try again.")
                            )

                        else:
                            roles = (
                                roles_result.get("job_roles")
                                or roles_result.get("roles")
                                or roles_result.get("data")
                                or []
                            )

                            selected_role_id = analysis.get("role_id")

                            if not selected_role_id:
                                for role in roles:
                                    role_name = (
                                        role.get("role_name")
                                        or role.get("name")
                                        or role.get("title")
                                    )

                                    if role_name == selected_role_name:
                                        selected_role_id = (
                                            role.get("id")
                                            or role.get("role_id")
                                        )
                                        break

                            if not selected_role_id:
                                st.error(
                                    "Could not identify the role ID. "
                                    "Open Skill Gap Analysis, select your target "
                                    "role, and try again."
                                )

                            else:
                                status, result = get_ai_recommendation(
                                    token,
                                    user_id,
                                    selected_role_id
                                )

                                if status == 200:
                                    recommendation = (
                                        result.get("ai_recommendation")
                                        or result.get("recommendation")
                                    )

                                    if recommendation:
                                        st.success(
                                            "Your recommendation is ready!"
                                        )
                                        st.markdown(recommendation)
                                    else:
                                        st.warning(
                                            "The API responded, but no "
                                            "recommendation was returned."
                                        )
                                        st.json(result)

                                else:
                                    st.error(
                                        "Could not generate AI recommendation."
                                    )
                                    st.write(
                                        result.get(
                                            "message",
                                            f"Request failed (status: {status})."
                                        )
                                    )

                    except Exception as error:
                        st.error(
                            f"Something went wrong: {error}"
                        )


# =========================================================
# PROGRESS TRACKING
# =========================================================

elif page == "Progress Tracking":

    st.title("📊 Learning Progress Tracking")
    st.caption(
        "Track your completed and pending skills for your target career role."
    )

    token = st.session_state.get("token")
    user = st.session_state.get("user") or {}
    user_id = user.get("id")

    if not token or not user_id:

        st.warning("Please log in again to view your progress.")

    else:

        analysis = st.session_state.get("skill_gap_result") or {}

        selected_role_name = (
            analysis.get("role")
            or user.get("target_role")
            or user.get("target_role_name")
            or user.get("role")
        )

        if not selected_role_name:

            st.warning(
                "Please select your target role in Skill Gap Analysis first."
            )

        else:

            # GET ROLE ID

            roles_status, roles_result = get_job_roles()

            if roles_status != 200:

                st.error("Could not load job roles.")

            else:

                roles = (
                    roles_result.get("job_roles")
                    or roles_result.get("roles")
                    or roles_result.get("data")
                    or []
                )

                selected_role_id = analysis.get("role_id")

                if not selected_role_id:

                    for role in roles:

                        role_name = (
                            role.get("role_name")
                            or role.get("name")
                            or role.get("title")
                        )

                        if role_name == selected_role_name:

                            selected_role_id = (
                                role.get("id")
                                or role.get("role_id")
                            )
                            break

                if not selected_role_id:

                    st.error("Could not identify your target role ID.")

                else:

                    st.write(f"**Target Role:** {selected_role_name}")

                    # FETCH SAVED PROGRESS

                    status, result = get_progress(
                        token,
                        user_id,
                        selected_role_id
                    )

                    if status == 200 and result.get("success"):

                        skills = result.get("skills", [])

                        total = result.get("total_skills", 0)
                        completed = result.get("completed_skills", 0)
                        pending = result.get("pending_skills", 0)
                        percentage = result.get("progress_percentage", 0)

                        # PROGRESS SUMMARY

                        col1, col2, col3 = st.columns(3)

                        col1.metric("Total Skills", total)
                        col2.metric("Completed", completed)
                        col3.metric("Pending", pending)

                        st.subheader("Overall Learning Progress")

                        st.progress(
                            min(max(float(percentage) / 100, 0.0), 1.0)
                        )

                        st.write(f"**{percentage}% Completed**")

                        st.divider()

                        st.subheader("Your Skills Checklist")

                        # SAVE STATUS WHEN CHECKBOX CHANGES

                        def save_skill_progress(
                            skill_id,
                            widget_key,
                            auth_token,
                            current_user_id,
                            current_role_id
                        ):

                            new_status = bool(
                                st.session_state[widget_key]
                            )

                            save_status, save_result = update_progress(
                                auth_token,
                                current_user_id,
                                current_role_id,
                                skill_id,
                                new_status
                            )

                            if save_status != 200:

                                st.session_state["progress_save_error"] = (
                                    save_result.get(
                                        "message",
                                        "Could not save progress."
                                    )
                                )

                            else:

                                st.session_state.pop(
                                    "progress_save_error",
                                    None
                                )

                        # DISPLAY SKILLS

                        for skill in skills:

                            skill_id = skill.get("skill_id")
                            skill_name = skill.get("skill_name")

                            if skill_id is None or not skill_name:
                                continue

                            widget_key = (
                                f"progress_{user_id}_"
                                f"{selected_role_id}_{skill_id}"
                            )

                            if widget_key not in st.session_state:

                                st.session_state[widget_key] = bool(
                                    skill.get("is_completed", False)
                                )

                            st.checkbox(
                                f"{skill_name}",
                                key=widget_key,
                                on_change=save_skill_progress,
                                args=(
                                    skill_id,
                                    widget_key,
                                    token,
                                    user_id,
                                    selected_role_id
                                )
                            )

                        save_error = st.session_state.get(
                            "progress_save_error"
                        )

                        if save_error:
                            st.error(save_error)

                        st.caption(
                            "Your progress is automatically saved when "
                            "you mark or unmark a skill."
                        )

                        if total > 0 and completed == total:

                            st.success(
                                "🎉 Congratulations! You have completed "
                                "all skills for this role."
                            )

                    else:

                        st.error("Could not load your learning progress.")

                        st.write(
                            result.get(
                                "message",
                                f"Request failed (status: {status})."
                            )
                        )

# LOGOUT
elif page == "Logout":
    st.session_state.logged_in = False
    st.session_state.user = None
    st.session_state.page = "Home"
    st.rerun()

# Footer
st.markdown(
    """
    <div class="app-footer">
        AI Skill Gap Analyzer · Personalized Career Recommendation System
    </div>
    """,
    unsafe_allow_html=True
)
