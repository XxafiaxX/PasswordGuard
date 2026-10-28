
COMMON_PASSWORDS = [
    "password",
    "password123",
    "123456",
    "12345678",
    "qwerty",
    "admin",
    "letmein",
    "welcome",
    "abc123",
    "iloveyou",
    "111111"
]

SEQUENCES = [
    "12345",
    "23456",
    "34567",
    "45678",
    "98765",
    "87654",
    "abcdef",
    "qwerty",
    "asdf"
]


def analyze_password(password):
    score = 0
    suggestions = []

    # 1. Check password length
    if len(password) >= 12:
        score += 3
    elif len(password) >= 8:
        score += 2
        suggestions.append(
            "Use at least 12 characters for better protection."
        )
    else:
        score += 1
        suggestions.append(
            "Make your password longer."
        )

    # 2. Check lowercase letters
    if any(char.islower() for char in password):
        score += 1
    else:
        suggestions.append(
            "Add lowercase letters."
        )

    # 3. Check uppercase letters
    if any(char.isupper() for char in password):
        score += 1
    else:
        suggestions.append(
            "Add uppercase letters."
        )

    # 4. Check numbers
    if any(char.isdigit() for char in password):
        score += 1
    else:
        suggestions.append(
            "Add numbers."
        )

    # 5. Check special characters
    if any(not char.isalnum() for char in password):
        score += 1
    else:
        suggestions.append(
            "Consider adding special characters like ! or #."
        )

    # 6. Check common passwords
    lower_password = password.lower()

    if lower_password in COMMON_PASSWORDS:
        score -= 4
        suggestions.append(
            "Avoid common passwords. Choose a unique one."
        )

    # 7. Check predictable sequences
    for sequence in SEQUENCES:
        if sequence in lower_password:
            score -= 2
            suggestions.append(
                "Avoid predictable sequences like 12345 or qwerty."
            )
            break

    # 8. Check repeated characters
    if len(password) >= 3 and len(set(password)) == 1:
        score -= 3
        suggestions.append(
            "Avoid using the same character repeatedly."
        )
    elif any(
        password[i] == password[i + 1] == password[i + 2]
        for i in range(len(password) - 2)
    ):
        score -= 1
        suggestions.append(
            "Avoid long runs of repeated characters."
        )

    # Keep score within the range 0 to 10
    score = max(0, min(score, 10))

    # Decide strength level
    if lower_password in COMMON_PASSWORDS or score <= 3:
        strength = "WEAK"
    elif score <= 6:
        strength = "MODERATE"
    elif score <= 8:
        strength = "STRONG"
    else:
        strength = "VERY STRONG"

    return score, strength, suggestions


def analyze_option():
    print("\n--- PASSWORD STRENGTH ANALYZER ---")
    print("Use a sample password, not your real password.")

    password = input("Enter a sample password: ")

    if password == "":
        print("Password cannot be empty.")
        return

    score, strength, suggestions = analyze_password(password)

    print("\n========== RESULTS ==========")
    print("Password length:", len(password))
    print("Strength score:", str(score) + "/10")
    print("Strength level:", strength)

    if suggestions:
        print("\nSuggestions to improve:")
        for suggestion in suggestions:
            print("-", suggestion)
    else:
        print("\nGood job! No basic issues were detected.")

    print("\nNote: This is an educational estimate,")
    print("not a guarantee of password security.")


def compare_passwords():
    print("\n--- COMPARE SAMPLE PASSWORDS ---")
    print("Use fictional examples only.")

    first = input("Enter sample password 1: ")
    second = input("Enter sample password 2: ")

    if first == "" or second == "":
        print("Neither password can be empty.")
        return

    score1, strength1, _ = analyze_password(first)
    score2, strength2, _ = analyze_password(second)

    print("\nPassword 1")
    print("Length:", len(first))
    print("Score:", str(score1) + "/10")
    print("Strength:", strength1)

    print("\nPassword 2")
    print("Length:", len(second))
    print("Score:", str(score2) + "/10")
    print("Strength:", strength2)

    if score1 > score2:
        print("\nSample password 1 scored higher.")
    elif score2 > score1:
        print("\nSample password 2 scored higher.")
    else:
        print("\nBoth passwords received the same score.")

    print("Scores are estimates, not security guarantees.")


def show_tips():
    print("\n--- PASSWORD SAFETY TIPS ---")

    tips = [
        "Use long passwords or passphrases.",
        "Use a different password for every account.",
        "Avoid names, birthdays, and common sequences.",
        "Never share passwords with other people.",
        "Consider using a reputable password manager.",
        "Enable two-factor authentication when possible.",
        "Change passwords if they may have been exposed."
    ]

    for number, tip in enumerate(tips, start=1):
        print(str(number) + ".", tip)


def show_about():
    print("\n--- ABOUT PASSWORD GUARD ---")
    print("Project: Password Guard")
    print("Purpose: Password safety awareness")
    print("Programming language: Python")
    print("\nPython concepts used:")
    print("1. Variables and data types")
    print("2. Strings and lists")
    print("3. If-else conditions")
    print("4. Loops")
    print("5. Functions")
    print("6. String methods")
    print("7. Basic scoring and analysis")


def main():
    while True:
        print("\n================================")
        print("        PASSWORD GUARD")
        print("  PASSWORD STRENGTH ANALYZER")
        print("================================")
        print("1. Analyze password strength")
        print("2. Compare two sample passwords")
        print("3. View password safety tips")
        print("4. About this project")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ").strip()

        if choice == "1":
            analyze_option()
        elif choice == "2":
            compare_passwords()
        elif choice == "3":
            show_tips()
        elif choice == "4":
            show_about()
        elif choice == "5":
            print("\nThank you for using Password Guard!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.")



if __name__ == "__main__":
    main()
