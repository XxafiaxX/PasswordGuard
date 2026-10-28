
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
def check_phishing(message):
    warning_signs = [
        "urgent",
        "verify your account",
        "click here",
        "password",
        "otp",
        "bank account",
        "won a prize",
        "claim your reward",
    ]

    found = [
        sign for sign in warning_signs
        if sign in message.lower()
    ]

    return found
st.divider()
st.header("🔎 Phishing Message Checker")
st.write("Check a suspicious message for common warning signs.")

message = st.text_area(
    "Paste a sample message",
    placeholder="Example: Urgent! Verify your account now..."
)

if st.button("Analyze Message"):
    if not message.strip():
        st.warning("Please enter a message first.")
    else:
        warnings = check_phishing(message)

        if warnings:
            st.warning("Potential warning signs detected:")
            for warning in warnings:
                st.write(f"⚠️ {warning}")
            st.info("This is a basic checker, not a definitive scam detector.")
        else:
            st.success("No listed warning signs detected.")
            st.info("This does not guarantee the message is safe.")
st.divider()
st.header("🛡️ Security Risk Assessment")
st.write("Check your everyday cybersecurity habits.")

unique_passwords = st.radio(
    "Do you use different passwords for different accounts?",
    ["Yes", "No"]
)

two_factor = st.radio(
    "Do you enable two-factor authentication (2FA)?",
    ["Yes", "No"]
)

updates = st.radio(
    "Do you regularly update your devices and apps?",
    ["Yes", "No"]
)

link_safety = st.radio(
    "Do you check links before opening them?",
    ["Yes", "No"]
)

if st.button("Assess My Security"):
    score = sum([
        unique_passwords == "Yes",
        two_factor == "Yes",
        updates == "Yes",
        link_safety == "Yes"
    ])

    st.subheader(f"Your security habits score: {score}/4")

    if score == 4:
        st.success("Great! You're following these four security practices.")
    else:
        st.warning("Here are some ways to improve:")

        if unique_passwords == "No":
            st.write("🔐 Use unique passwords for each account.")
        if two_factor == "No":
            st.write("🛡️ Enable two-factor authentication where possible.")
        if updates == "No":
            st.write("🔄 Keep your devices and apps updated.")
        if link_safety == "No":
            st.write("🔗 Check suspicious links before opening them.")  
st.divider()
st.header("🚨 Cyber Incident Guide")

incident = st.selectbox(
    "What happened?",
    [
        "My account may be hacked",
        "I clicked a suspicious link",
        "I shared an OTP or password",
        "I suspect an online scam",
    ],
)

guidance = {
    "My account may be hacked": [
        "Change your password from a trusted device.",
        "Sign out of other active sessions.",
        "Enable two-factor authentication.",
        "Contact the service's official support if needed.",
    ],
    "I clicked a suspicious link": [
        "Don't enter any more information on that page.",
        "Close the page and check your device for unusual activity.",
        "If you downloaded a file, don't open it.",
        "If you entered credentials, change them from a trusted device.",
    ],
    "I shared an OTP or password": [
        "Contact the relevant bank or service immediately.",
        "Change your password from a trusted device.",
        "Revoke active sessions and enable two-factor authentication.",
        "If money is involved, contact your bank immediately.",
    ],
    "I suspect an online scam": [
        "Stop communicating with the suspected scammer.",
        "Don't send money or share additional information.",
        "Save relevant messages and transaction details.",
        "Report the incident to the relevant service or local authorities.",
    ],
}

if st.button("Show Safety Steps"):
    for step in guidance[incident]:
        st.write(f"✅ {step}")          
          