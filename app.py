import streamlit as st
import re

st.set_page_config(page_title="Password Strength Meter", page_icon="🔒")

st.title("🔒 Password Strength Meter")
st.markdown("""
### Let's test your password strength and make sure it's truly hacker-proof!🔥  
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.  
It will give you helpful tips to create a **Strong Password** 🔒
""")

# Create a form for password input
with st.form("password_form"):
    password = st.text_input("**Enter your password**", type="password")
    submitted = st.form_submit_button("Check Password Strength")

# Process the password after form submission
if submitted:
    feedback = []
    score = 0

    if len(password) < 8:
        feedback.append("Password should be at least 8 characters long.")
    else:
        score += 1

    if re.search("[a-z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter.")

    if re.search("[A-Z]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter.")

    if re.search("[0-9]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit.")

    if re.search("[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character.")

    # Determine password strength based on score
    if score == 5:
        st.success("✅ Your password is **very strong**! 🔒")
    elif 3 <= score < 5:
        st.warning("⚠️ Your password is **moderate**. Consider improving it!")
    else:
        st.error("❌ Your password is **weak**! 🔓")

    # Display suggestions if any
    if feedback:
        st.markdown("### Suggestions to strong your password:")
        for suggestion in feedback:
            st.write(f"- {suggestion}")
else:
    st.info("Enter a password and press **Enter** to check its strength.")

