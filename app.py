import streamlit as st
import random
import string
import pyperclip

# Function to generate a password
def generate_password(length=12, use_digits=True, use_special=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    return "".join(random.choice(chars) for _ in range(length))

# Function to check password strength and provide detailed feedback
def check_strength(password):
    length_score = min(len(password) / 4, 4)
    digit_score = any(c.isdigit() for c in password)
    special_score = any(c in string.punctuation for c in password)
    upper_score = any(c.isupper() for c in password)
    lower_score = any(c.islower() for c in password)
    score = length_score + digit_score + special_score + upper_score + lower_score
    
    feedback = []
    if len(password) < 8:
        feedback.append("Increase length (8+ characters recommended)📏")
    if not digit_score:
        feedback.append("Add numbers for better security🔢")
    if not special_score:
        feedback.append("Include special characters for stronger security💠✔")
    if not upper_score:
        feedback.append("Use at least one uppercase letter⬆")
    if not lower_score:
        feedback.append("Use at least one lowercase letter⬇")
    
    if score >= 5:
        return "Strong", feedback
    elif score >= 3:
        return "Medium", feedback
    else:
        return "Weak", feedback

# Streamlit UI
st.title("🔐 Password Manager")

# Password Generation Section
st.header("Generate a Secure Password👀🔒")
length = st.slider("Password Length", 6, 32, 12)
use_digits = st.checkbox("Include Numbers🔢", True)
use_special = st.checkbox("Include Special Characters⚡", True)
if st.button("Generate Password"):
    generated_password = generate_password(length, use_digits, use_special)
    st.success(f"Generated Password: {generated_password}")
    if st.button("Copy to Clipboard"):
        pyperclip.copy(generated_password)
        st.success("Password copied to clipboard!")

# Password Strength Checker
st.header("Check Your Password Strength 💪🔑")
user_password = st.text_input("Enter a Password to Analyze✔", type="password")
if st.button("Check Strength"):
    if user_password:
        strength, feedback = check_strength(user_password)
        st.write(f"Password Strength: **{strength}**")
        if feedback:
            st.write("### Suggestions to Improve Password:")
            for tip in feedback:
                st.warning(tip)
    else:
        st.warning("Please enter a password to check↩.")


st.write("Made with ❤️ by [SARA ASIF]")