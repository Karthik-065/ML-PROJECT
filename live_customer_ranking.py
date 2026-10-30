
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# =====================================================
# PAGE SETTINGS
# =====================================================

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="👥",
    layout="wide"
)

# ---------------------------------------------------
# LOAD CSS
# ---------------------------------------------------

def load_css():
    with open("style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()


# =====================================================
# HEADER
# =====================================================

st.title("👥 Customer Segmentation Analytics")

st.subheader(
    "Live Customer Ranking & Spending Analysis"
)

st.write(
    "Enter customer information below to identify "
    "the highest-ranked customer."
)

st.divider()

# =====================================================
# CUSTOMER INPUT
# =====================================================

st.header("📝 Customer Details")

num_customers = st.slider(
    "Select Number of Customers",
    5,
    7,
    5
)

# Create customer table
customer_data = pd.DataFrame({
    "Customer Name": [
        f"Customer {i}"
        for i in range(1, num_customers + 1)
    ],

    "Purchase Amount (₹)": [
        1000
    ] * num_customers,

    "Spending Score": [
        50
    ] * num_customers
})

# Editable table
edited_data = st.data_editor(
    customer_data,
    use_container_width=True,
    hide_index=True,
    num_rows="fixed",

    column_config={

        "Customer Name":
        st.column_config.TextColumn(
            "Customer Name"
        ),

        "Purchase Amount (₹)":
        st.column_config.NumberColumn(
            "Purchase Amount (₹)",
            min_value=0,
            step=100
        ),

        "Spending Score":
        st.column_config.NumberColumn(
            "Spending Score",
            min_value=0,
            max_value=100,
            step=1
        )
    }
)

st.write("")

# =====================================================
# ANALYZE BUTTON
# =====================================================

if st.button(
    "🚀 Analyze Customers",
    type="primary",
    use_container_width=True
):

    result = edited_data.copy()

    # Remove empty customer names
    result = result[
        result["Customer Name"]
        .astype(str)
        .str.strip() != ""
    ]

    if len(result) == 0:

        st.error(
            "Please enter at least one customer."
        )

        st.stop()

    # =================================================
    # CUSTOMER RATING
    # =================================================

    def get_rating(score):

        if score >= 80:
            return "🌟 Very High"

        elif score >= 60:
            return "🟢 High"

        elif score >= 40:
            return "🟡 Medium"

        elif score >= 20:
            return "🟠 Low"

        else:
            return "🔴 Very Low"

    result["Rating"] = (
        result["Spending Score"]
        .apply(get_rating)
    )

    # =================================================
    # CUSTOMER RANKING
    # =================================================

    result = result.sort_values(
        by=[
            "Spending Score",
            "Purchase Amount (₹)"
        ],
        ascending=[
            False,
            False
        ]
    ).reset_index(drop=True)

    result.insert(
        0,
        "Rank",
        range(1, len(result) + 1)
    )

    # =================================================
    # WINNER
    # =================================================

    winner = result.iloc[0]

    st.divider()

    st.header("🏆 Top Customer")

    st.success(
        f"**{winner['Customer Name']}** "
        f"is the highest-ranked customer!"
    )

    # =================================================
    # MAIN METRICS
    # =================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "🏆 Rank",
            f"#{int(winner['Rank'])}"
        )

    with col2:

        st.metric(
            "💰 Purchase",
            f"₹{winner['Purchase Amount (₹)']:,.0f}"
        )

    with col3:

        st.metric(
            "⭐ Spending Score",
            f"{winner['Spending Score']}/100"
        )

    with col4:

        st.metric(
            "📊 Rating",
            winner["Rating"]
        )

    # =================================================
    # TOP 3 CUSTOMERS
    # =================================================

    st.divider()

    st.header("🥇 Top 3 Customers")

    top3 = result.head(3)

    cols = st.columns(3)

    medals = [
        "🥇",
        "🥈",
        "🥉"
    ]

    for i, (_, customer) in enumerate(
        top3.iterrows()
    ):

        with cols[i]:

            st.subheader(
                f"{medals[i]} "
                f"{customer['Customer Name']}"
            )

            st.write(
                f"**Rank:** #{int(customer['Rank'])}"
            )

            st.write(
                f"**Purchase:** "
                f"₹{customer['Purchase Amount (₹)']:,.0f}"
            )

            st.write(
                f"**Spending Score:** "
                f"{customer['Spending Score']}/100"
            )

            st.write(
                f"**Rating:** "
                f"{customer['Rating']}"
            )

    # =================================================
    # RANKING TABLE
    # =================================================

    st.divider()

    st.header("📋 Complete Customer Ranking")

    st.dataframe(
        result,
        use_container_width=True,
        hide_index=True
    )

    # =================================================
    # CHARTS
    # =================================================

    st.divider()

    st.header("📊 Customer Comparison")

    chart1, chart2 = st.columns(2)

    # -------------------------------------------------
    # PURCHASE CHART
    # -------------------------------------------------

    with chart1:

        st.subheader(
            "💰 Purchase Amount"
        )

        fig1, ax1 = plt.subplots(
            figsize=(6, 4)
        )

        ax1.bar(
            result["Customer Name"],
            result["Purchase Amount (₹)"]
        )

        ax1.set_xlabel(
            "Customer"
        )

        ax1.set_ylabel(
            "Purchase Amount (₹)"
        )

        ax1.set_title(
            "Purchase Amount Comparison"
        )

        plt.xticks(
            rotation=30
        )

        st.pyplot(fig1)

    # -------------------------------------------------
    # SPENDING SCORE
    # -------------------------------------------------

    with chart2:

        st.subheader(
            "⭐ Spending Score"
        )

        fig2, ax2 = plt.subplots(
            figsize=(6, 4)
        )

        ax2.bar(
            result["Customer Name"],
            result["Spending Score"]
        )

        ax2.set_xlabel(
            "Customer"
        )

        ax2.set_ylabel(
            "Spending Score"
        )

        ax2.set_title(
            "Spending Score Comparison"
        )

        ax2.set_ylim(
            0,
            100
        )

        plt.xticks(
            rotation=30
        )

        st.pyplot(fig2)

    # =================================================
    # CUSTOMER INSIGHT
    # =================================================

    st.divider()

    st.header("💡 Customer Insight")

    st.info(
        f"**{winner['Customer Name']}** ranked first "
        f"because they achieved the highest Spending Score "
        f"of **{winner['Spending Score']}/100**."
    )

    st.write(
        "Ranking priority:"
    )

    st.write(
        "1️⃣ Spending Score — Main ranking factor"
    )

    st.write(
        "2️⃣ Purchase Amount — Used when scores are equal"
    )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "Customer Segmentation Analytics System | "
    "Live Customer Ranking Dashboard"
)

