import re

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add uppercase letter")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add lowercase letter")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add a number")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("Add special character (!@#$%)")

    if score == 5:
        return "Strong Password - Good!"
    elif score >= 3:
        return f"Medium Strength - {', '.join(feedback)}"
    else:
        return f"Weak Password - {', '.join(feedback)}"

pwd = input("Enter password: ")
print(check_password_strength(pwd))
