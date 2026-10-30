
import streamlit as st

login_page = st.Page(
    "pages/login_page.py",
    title="Login",
    icon="🔐"
)

dashboard = st.Page(
    "app.py",
    title="Dashboard",
    icon="📊"
)

live_ranking = st.Page(
    "live_customer_ranking.py",
    title="Live Customer Ranking",
    icon="🏆"
)


pg = st.navigation(
    [login_page, dashboard, live_ranking],
    position="sidebar"
)

pg.run()

