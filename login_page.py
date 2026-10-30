
import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(
    page_title="Customer Segmentation | Login",
    page_icon="📊",
    layout="centered"
)


# -------------------------------------------------
# CSS
# -------------------------------------------------

st.markdown("""
<style>

/* ===============================
   MAIN BACKGROUND
   =============================== */

.stApp {
    background:
        radial-gradient(circle at 10% 20%, rgba(59,130,246,0.35), transparent 30%),
        radial-gradient(circle at 90% 80%, rgba(14,165,233,0.30), transparent 30%),
        linear-gradient(135deg, #020617, #0f172a, #1e3a8a);

    min-height: 100vh;
}


/* ===============================
   REMOVE DEFAULT STREAMLIT SPACE
   =============================== */

.block-container {
    padding-top: 3rem;
    padding-bottom: 2rem;
    max-width: 650px;
}


/* ===============================
   PROJECT LOGO
   =============================== */

.logo {
    width: 90px;
    height: 90px;

    margin: auto;

    border-radius: 50%;

    background: linear-gradient(
        135deg,
        #2563eb,
        #38bdf8
    );

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 45px;

    box-shadow:
        0 10px 30px rgba(37,99,235,0.45);
}


/* ===============================
   TITLE
   =============================== */

.project-title {
    text-align: center;

    color: white;

    font-size: 34px;

    font-weight: 800;

    margin-top: 18px;

    letter-spacing: 0.5px;
}


/* ===============================
   SUBTITLE
   =============================== */

.project-subtitle {
    text-align: center;

    color: #cbd5e1;

    font-size: 15px;

    margin-top: 5px;

    margin-bottom: 28px;
}


/* ===============================
   LOGIN CARD
   =============================== */

.login-card {
    background: rgba(255,255,255,0.96);

    padding: 35px;

    border-radius: 22px;

    box-shadow:
        0 25px 60px rgba(0,0,0,0.45);

    border: 1px solid rgba(255,255,255,0.5);
}


/* ===============================
   INPUT LABELS
   =============================== */

label {
    color: #1e293b !important;

    font-weight: 600 !important;
}


/* ===============================
   INPUT BOX
   =============================== */

.stTextInput input {
    border-radius: 10px;

    border: 1px solid #cbd5e1;

    padding: 12px;

    font-size: 15px;
}


/* ===============================
   LOGIN BUTTON
   =============================== */

.stButton > button {

    width: 100%;

    height: 50px;

    border-radius: 12px;

    border: none;

    background: linear-gradient(
        135deg,
        #2563eb,
        #0284c7
    );

    color: white;

    font-size: 17px;

    font-weight: 700;

    transition: 0.3s;

    box-shadow:
        0 8px 20px rgba(37,99,235,0.30);
}


/* BUTTON HOVER */

.stButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 12px 25px rgba(37,99,235,0.45);

    background: linear-gradient(
        135deg,
        #1d4ed8,
        #0369a1
    );
}


/* ===============================
   INFORMATION BOX
   =============================== */

.info-box {

    background: #eff6ff;

    border-left: 4px solid #2563eb;

    padding: 12px 15px;

    border-radius: 8px;

    color: #1e3a8a;

    font-size: 13px;

    margin-top: 18px;
}


/* ===============================
   FOOTER
   =============================== */

.footer {

    text-align: center;

    color: #cbd5e1;

    font-size: 13px;

    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# -------------------------------------------------
# HEADER
# -------------------------------------------------

st.markdown("""
<div class="logo">
📊
</div>

<div class="project-title">
Customer Segmentation
</div>

<div class="project-subtitle">
AI-Based Customer Analysis & Classification System
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------
# LOGIN CARD START
# -------------------------------------------------

st.markdown("""
<div class="login-card">
<h3 style="text-align:center;color:#1e293b;margin-bottom:5px;">
Welcome Back
</h3>

<p style="text-align:center;color:#64748b;font-size:14px;">
Login to access the customer analytics dashboard
</p>
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------
# LOGIN INPUTS
# -------------------------------------------------

username = st.text_input(
    "Username",
    placeholder="Enter your username"
)

password = st.text_input(
    "Password",
    type="password",
    placeholder="Enter your password"
)

st.write("")

login = st.button("🔐  Login to Dashboard")


# -------------------------------------------------
# LOGIN CHECK
# -------------------------------------------------

if login:

    if username == "" or password == "":
        st.warning("⚠️ Please enter username and password.")

    elif username == "admin" and password == "admin123":

        st.session_state["logged_in"] = True

        st.success("✅ Login successful!")

        st.switch_page("app.py")

    else:

        st.error("❌ Invalid username or password.")


# -------------------------------------------------
# DEMO INFORMATION
# -------------------------------------------------

st.markdown("""
<div class="info-box">
<b>Demo Access</b><br>
Use the project administrator credentials to access the dashboard.
</div>
""", unsafe_allow_html=True)


# -------------------------------------------------
# FOOTER
# -------------------------------------------------

st.markdown("""
<div class="footer">
Customer Segmentation System
<br>
Machine Learning • Data Analytics • Customer Insights
</div>
""", unsafe_allow_html=True)

