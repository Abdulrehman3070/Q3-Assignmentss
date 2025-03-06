import streamlit as st
import re
import random

# List of common weak passwords
weak_passwords = ["password", "123456", "123456789", "qwerty", "abc123", "password1", "admin", "letmein"]

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    # Check if password is in the weak list
    if password.lower() in weak_passwords:
        return "❌ This password is too common! Choose a unique password.", "Weak", 20
    
    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")
    
    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")
    
    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")
    
    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password! Good job! 💪", "Strong", 100
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", "Moderate", 70
    else:
        return "\n".join(feedback), "Weak", 40

# Function to generate a strong password
def generate_strong_password():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    return "".join(random.choice(chars) for _ in range(12))

# Streamlit UI
st.title("🔐 Password Strength Meter")
st.write("Enter your password below to check its strength:")

password = st.text_input("🔑 Enter Password", type="password")

if password:
    feedback, strength, progress = check_password_strength(password)
    st.subheader("🔎 Password Analysis:")
    st.write(feedback)

    # Add progress bar for visual strength representation
    st.progress(progress / 100)

    if strength == "Weak":
        st.warning("⚠️ Your password is weak! Consider using a stronger password.")
        st.write("💡 Suggested Strong Password: ")
        st.code(generate_strong_password(), language="bash")
    elif strength == "Moderate":
        st.info("🔵 Your password is moderate. Here’s how to make it stronger:")
        st.write(feedback)  # Display specific improvement suggestions
        st.write("💡 Suggested Strong Password (if you want a better one):")
        st.code(generate_strong_password(), language="bash")
    else:
        st.success("✅ Your password is strong! Keep it safe. 🔒")
