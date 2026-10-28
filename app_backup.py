
import streamlit as st

# ---------------- PAGE SETUP ----------------

st.set_page_config(
    page_title="Password Guard",
    page_icon="🔐",
    layout="centered"
)

# ---------------- PASSWORD DATA ----------------

COMMON_PASSWORDS = [
    "password", "password123", "123456",
    "12345678", "qwerty", "admin",
    "letmein", "welcome", "abc123",
    "iloveyou", "111111"
]

SEQUENCES = [
    "12345", "23456", "34567", "45678",
    "98765", "87654", "abcdef", "qwerty", "asdf"
]


# ---------------- ANALYSIS FUNCTION ----------------

def analyze_password(password):
    score = 0
    suggestions = []
    lower_password = password.lower()

    # Password length
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
        suggestions.append(
            "Try using at least 12 characters."
        )
    else:
        score += 1
        suggestions.append(
            "Use a longer password or passphrase."
        )

    # Character variety
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Consider adding numbers.")

    if any(not c.isalnum() for c in password):
        score += 1
    else:
        suggestions.append(
            "Consider adding special characters."
        )

    # Common password check
    is_common = lower_password in COMMON_PASSWORDS

    if is_common:
        score -= 4
        suggestions.append(
            "This is a common password. Choose a unique one."
        )

    # Predictable sequence check
    if any(seq in lower_password for seq in SEQUENCES):
        score -= 2
        suggestions.append(
            "Avoid predictable sequences such as 12345."
        )

    # Repeated character check
    if len(password) >= 3 and len(set(password)) == 1:
        score -= 3
        suggestions.append(
            "Avoid repeating the same character."
        )
    elif any(
        password[i] == password[i + 1] == password[i + 2]
        for i in range(len(password) - 2)
    ):
        score -= 1
        suggestions.append(
            "Avoid long runs of repeated characters."
        )

    # Keep score within 0–10
    score = max(0, min(score, 10))

    # Strength category
    if is_common or score <= 3:
        strength = "Weak"
    elif score <= 6:
        strength = "Moderate"
    elif score <= 8:
        strength = "Strong"
    else:
        strength = "Very Strong"

    return score, strength, suggestions


# ---------------- WEBSITE HEADER ----------------

st.title("🔐 Password Guard")
st.write("### Understand your password strength.")
st.write(
    "Check a sample password and get practical suggestions "
    "for making it harder to guess."
)

st.info(
    "Privacy tip: use a fictional sample, not a password "
    "you use for a real account."
)

# ---------------- MAIN PASSWORD CHECKER ----------------

st.subheader("Check your password")

password = st.text_input(
    "Enter a sample password",
    type="password",
    placeholder="Type a fictional password here",
    help="The password is analyzed by this app and is not saved to a file."
)

show_password = st.checkbox("Show password while typing")

if show_password:
    # This checkbox explains visibility; use the masked field above
    # for the analysis workflow.
    st.caption(
        "The password field remains masked in this version."
    )

analyze_clicked = st.button(
    "🔎 Check Password Strength",
    type="primary",
    use_container_width=True
)

if analyze_clicked:
    if not password:
        st.warning("Please enter a sample password first.")
    else:
        score, strength, suggestions = analyze_password(password)

        st.divider()
        st.subheader("Your results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Strength score", f"{score}/10")

        with col2:
            st.metric("Strength level", strength)

        st.progress(score / 10)

        if strength == "Weak":
            st.error(
                "This password has weaknesses that should be improved."
            )
        elif strength == "Moderate":
            st.warning(
                "This password could be stronger."
            )
        else:
            st.success(
                "This sample scored well in the basic checks."
            )

        st.subheader("How to improve it")

        if suggestions:
            for suggestion in suggestions:
                st.write(f"- {suggestion}")
        else:
            st.write(
                "No issues were found by these basic checks."
            )

        st.caption(
            "This score is an educational estimate, not a "
            "guarantee of real-world password security."
        )

# ---------------- EXTRA INFORMATION ----------------

st.divider()

tips_tab, about_tab = st.tabs(
    ["💡 Password Safety Tips", "ℹ️ About This Project"]
)

with tips_tab:
    st.subheader("Stay safer online")

    st.write("**1. Use long passwords.**")
    st.write("Long passphrases can be easier to remember and harder to guess.")

    st.write("**2. Avoid predictable choices.**")
    st.write("Names, birthdays, and simple sequences are poor choices.")

    st.write("**3. Use unique passwords.**")
    st.write("Do not reuse the same password across important accounts.")

    st.write("**4. Consider a password manager.**")
    st.write("A reputable password manager can help you create and store unique passwords.")

    st.write("**5. Enable two-factor authentication.**")
    st.write("This adds another layer of protection where available.")

with about_tab:
    st.subheader("About Password Guard")

    st.write(
        "Password Guard is a Python-based educational project "
        "that teaches users about password strength."
    )

    st.write("**Technology:** Python and Streamlit")
    st.write(
        "**Python concepts:** functions, variables, lists, "
        "loops, strings, and conditional statements."
    )

    st.write(
        "**Method:** the program checks length, character variety, "
        "selected common passwords, and predictable patterns."
    )

    st.write(
        "**Limitation:** the scoring method is basic and does not "
        "guarantee that a password is secure."
    )

# ---------------- FOOTER ----------------

st.divider()

st.caption(
    "Password Guard | A password safety awareness project"
)
