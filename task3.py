import re

def password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) < 8:
        feedback.append("Password is too short (less than 8 characters).")
    else:
        strength += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password lacks uppercase letters.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback.append("Password lacks lowercase letters.")

    # Check for digits
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password lacks digits.")

    # Check for special characters
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Password lacks special characters.")

    # Determine the strength of the password
    if strength == 5:
        return "Strong password", feedback
    elif 3 <= strength < 5:
        return "Moderate password", feedback
    else:
        return "Weak password", feedback

def main():
    password = input("Enter a password to check its strength: ")
    strength, feedback = password_strength(password)
    
    print(f"Password strength: {strength}")
    if feedback:
        print("Feedback:")
        for comment in feedback:
            print(f"- {comment}")

if __name__ == "__main__":
    main()
