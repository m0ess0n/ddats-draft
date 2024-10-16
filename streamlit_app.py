import streamlit as st

# App title
st.title("D-DATS: Dutch Device-Aided Therapy Screening tool")

# Response fluctuations
response_fluctuations = st.checkbox("Response fluctuations", value=False)
response_fluctuations_value = 1 if response_fluctuations else 0

# Troublesome dyskinesias
troublesome_dyskinesias = st.checkbox("Troublesome dyskinesias", value=False)
troublesome_dyskinesias_value = 1 if troublesome_dyskinesias else 0

# LEDD (levodopa equivalent daily dose)
ledd = st.slider("LEDD (levodopa equivalent daily dose)", 0, 3000, step=50)

# D-DATS score
d_dats_score = (2 * response_fluctuations_value) + (2 * troublesome_dyskinesias_value) + (0.003 * ledd)

# Showing D-DATS score
st.write(f"D-DATS score: {d_dats_score:.2f}")

# Implications D-DATS score
if d_dats_score < 5.8:
    st.write("Patient is not eligible for referral for DAT.")
else:
    st.write("Based on the D-DATS score, the patient is eligible for referral for DAT.")
