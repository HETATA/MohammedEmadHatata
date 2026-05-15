import streamlit as st

st.set_page_config(
    page_title="Plastic Injection Factory",
    layout="wide"
)

# ===== Header Logos =====
col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.image("logo_left.png", width=180)

with col3:
    st.image("logo_right.png", width=180)

# ===== Main Title =====
st.markdown(
    "<h1 style='text-align: center;'>🏭 Plastic Injection Factory Dashboard</h1>",
    unsafe_allow_html=True
)

st.divider()

# ===== Main Sections =====
st.markdown("## Main Sections")

c1, c2, c3 = st.columns(3)

# Human Factor
with c1:
    with st.expander("👷 Human Factor"):
        st.markdown("""
        - 👷 Worker
        - 🧑‍🏭 Operator / مشغل ماكينة
        - ⏱️ Shift Time
        - 🧠 Skill Level
        """)

# Safety
with c2:
    with st.expander("🦺 Safety"):
        st.markdown("""
        - ⛑️ PPE
        - ⚠️ Risk
        - 🚨 Accident Prevention
        """)

# Work Management
with c3:
    with st.expander("📋 Work Management"):
        st.markdown("""
        - 📋 Work Instruction
        - 📊 Performance
        - 🎯 Productivity
        """)

st.divider()

st.success("Factory System Ready ✅")