import streamlit as st
from mpin_checker import check_pin_strength

st.set_page_config(page_title="MPIN Strength Checker", layout="centered")

st.title("🔐 MPIN Strength Checker")
st.write("Evaluate the strength of your 4 or 6-digit MPIN based on common patterns and personal data.")

# Input Fields
mpin = st.text_input("Enter your MPIN (4 or 6 digits)", max_chars=6)

dob_self = st.text_input("Your Date of Birth (DDMMYYYY)", max_chars=8)
dob_spouse = st.text_input("Spouse's Date of Birth (DDMMYYYY)", max_chars=8)
anniversary = st.text_input("Anniversary Date (DDMMYYYY)", max_chars=8)

# Validate inputs and run check
if st.button("Check Strength"):
    if len(mpin) not in [4, 6]:
        st.warning("MPIN must be either 4 or 6 digits long.")
    elif not (dob_self.isdigit() and dob_spouse.isdigit() and anniversary.isdigit()):
        st.warning("Please enter valid dates in DDMMYYYY format.")
    else:
        strength, reasons = check_pin_strength(mpin, dob_self, dob_spouse, anniversary)

        if strength == "STRONG":
            st.success("✅ MPIN is STRONG")
        else:
            st.error("❌ MPIN is WEAK")
            st.write("**Reasons:**")
            for reason in reasons:
                st.markdown(f"- {reason}")

