
import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# ---------------------------------------------------
# PAGE SETTINGS
# ---------------------------------------------------

st.set_page_config(
    page_title="Customer Segmentation System",
    page_icon="📊",
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



# ---------------------------------------------------
# LOAD MODEL AND DATASET
# ---------------------------------------------------

model = joblib.load("customer_segmentation_model.pkl")

df = pd.read_csv("Mall_Customers.csv")

# ---------------------------------------------------
# CREATE CLUSTERS
# ---------------------------------------------------

X = df[
    [
        "Annual Income (k$)",
        "Spending Score (1-100)"
    ]
]

df["Cluster"] = model.predict(X) + 1

# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📊 Customer Segmentation System")

st.write(
    "Analyze customer data and predict customer segments "
    "using Machine Learning."
)

# ===================================================
# DASHBOARD
# ===================================================

st.subheader("📈 Customer Dashboard")

total_customers = len(df)
average_age = df["Age"].mean()
average_income = df["Annual Income (k$)"].mean()
average_spending = df["Spending Score (1-100)"].mean()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👥 Total Customers", total_customers)

with col2:
    st.metric("🎂 Average Age", f"{average_age:.1f}")

with col3:
    st.metric("💰 Average Income", f"${average_income:.1f}k")

with col4:
    st.metric("🛍️ Avg Spending Score", f"{average_spending:.1f}")

# ---------------------------------------------------
# CLUSTER DISTRIBUTION
# ---------------------------------------------------

st.subheader("📊 Customer Distribution by Cluster")

cluster_counts = (
    df["Cluster"]
    .value_counts()
    .sort_index()
)

st.bar_chart(cluster_counts)

# ===================================================
# CUSTOMER PREDICTION
# ===================================================

st.divider()

st.subheader("🔍 Predict Customer Segment")

st.write(
    "Enter customer details to predict the customer segment."
)

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=1,
        max_value=100,
        value=25
    )

with col2:
    income = st.number_input(
        "Annual Income (k$)",
        min_value=1,
        max_value=200,
        value=50
    )

with col3:
    spending_score = st.number_input(
        "Spending Score (1-100)",
        min_value=1,
        max_value=100,
        value=50
    )

# ---------------------------------------------------
# PREDICTION
# ---------------------------------------------------

if st.button("🔍 Predict Customer Segment"):

    input_data = pd.DataFrame(
        [[income, spending_score]],
        columns=[
            "Annual Income (k$)",
            "Spending Score (1-100)"
        ]
    )

    prediction = model.predict(input_data)[0]

    cluster = prediction + 1

    cluster_names = {
        1: "Standard Customer",
        2: "High Value Customer",
        3: "Low Value Customer",
        4: "Careful Spender",
        5: "Target Customer"
    }

    segment = cluster_names.get(
        cluster,
        f"Customer Segment {cluster}"
    )

    st.success(
        f"🎯 Customer belongs to Cluster {cluster}"
    )

    st.subheader("🏷️ Customer Segment")

    st.info(
        f"Customer Type: **{segment}**"
    )

    # ------------------------------------------------
    # CUSTOMER INFORMATION
    # ------------------------------------------------

    st.subheader("📋 Customer Information")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Age", age)

    with col2:
        st.metric("Income", f"${income}k")

    with col3:
        st.metric("Spending Score", spending_score)

    with col4:
        st.metric("Cluster", cluster)

    # ------------------------------------------------
    # GRAPH
    # ------------------------------------------------

    st.subheader("📈 Customer Segmentation Graph")

    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df["Annual Income (k$)"],
        df["Spending Score (1-100)"],
        s=60,
        alpha=0.7,
        label="Existing Customers"
    )

    ax.scatter(
        income,
        spending_score,
        marker="*",
        s=400,
        edgecolors="black",
        linewidths=2,
        label="Your Customer"
    )

    ax.set_xlabel("Annual Income (k$)")
    ax.set_ylabel("Spending Score (1-100)")
    ax.set_title("Annual Income vs Spending Score")

    ax.legend()

    st.pyplot(fig)

    st.caption(
        "⭐ The star shows the position of the customer you entered."
    )

    # ------------------------------------------------
    # SUMMARY
    # ------------------------------------------------

    st.subheader("📝 Prediction Summary")

    customer_data = pd.DataFrame({
        "Details": [
            "Age",
            "Annual Income",
            "Spending Score",
            "Cluster",
            "Customer Type"
        ],
        "Value": [
            age,
            f"${income}k",
            spending_score,
            cluster,
            segment
        ]
    })

    st.table(customer_data)

# ===================================================
# DATASET FILTERS
# ===================================================

st.divider()

st.subheader("🔎 Filter Customer Dataset")

st.write(
    "Use the filters below to find specific customers."
)

# ---------------------------------------------------
# FILTER COLUMNS
# ---------------------------------------------------

filter_col1, filter_col2 = st.columns(2)

with filter_col1:

    gender_options = ["All"] + sorted(
        df["Gender"].unique().tolist()
    )

    selected_gender = st.selectbox(
        "Gender",
        gender_options
    )

with filter_col2:

    age_min = int(df["Age"].min())
    age_max = int(df["Age"].max())

    selected_age = st.slider(
        "Age Range",
        min_value=age_min,
        max_value=age_max,
        value=(age_min, age_max)
    )

# ---------------------------------------------------
# INCOME AND SPENDING FILTERS
# ---------------------------------------------------

filter_col3, filter_col4 = st.columns(2)

with filter_col3:

    income_min = int(
        df["Annual Income (k$)"].min()
    )

    income_max = int(
        df["Annual Income (k$)"].max()
    )

    selected_income = st.slider(
        "Annual Income (k$)",
        min_value=income_min,
        max_value=income_max,
        value=(income_min, income_max)
    )

with filter_col4:

    spending_min = int(
        df["Spending Score (1-100)"].min()
    )

    spending_max = int(
        df["Spending Score (1-100)"].max()
    )

    selected_spending = st.slider(
        "Spending Score",
        min_value=spending_min,
        max_value=spending_max,
        value=(spending_min, spending_max)
    )

# ---------------------------------------------------
# APPLY FILTERS
# ---------------------------------------------------

filtered_df = df.copy()

if selected_gender != "All":

    filtered_df = filtered_df[
        filtered_df["Gender"] == selected_gender
    ]

filtered_df = filtered_df[
    (filtered_df["Age"] >= selected_age[0]) &
    (filtered_df["Age"] <= selected_age[1])
]

filtered_df = filtered_df[
    (filtered_df["Annual Income (k$)"] >= selected_income[0]) &
    (filtered_df["Annual Income (k$)"] <= selected_income[1])
]

filtered_df = filtered_df[
    (filtered_df["Spending Score (1-100)"] >= selected_spending[0]) &
    (filtered_df["Spending Score (1-100)"] <= selected_spending[1])
]

# ---------------------------------------------------
# FILTER RESULT
# ---------------------------------------------------

st.write(
    f"**Showing {len(filtered_df)} customers**"
)

st.dataframe(
    filtered_df,
    use_container_width=True
)

# ---------------------------------------------------
# DOWNLOAD FILTERED DATA
# ---------------------------------------------------

csv = filtered_df.to_csv(index=False)

st.download_button(
    label="⬇️ Download Filtered Dataset",
    data=csv,
    file_name="filtered_customers.csv",
    mime="text/csv"
)

