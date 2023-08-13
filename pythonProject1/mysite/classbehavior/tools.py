import re

def passwordstrength(password):
    """
    This function will return a score based on the strength of the password.
    The score is calculated based on the presence of lowercase, uppercase, digits and special characters.
    If the password has a length of at least 8 characters and includes at least one character from each category, it is considered strong.
    """

    # Score is initially 0
    score = 0

    # Test for presence of lowercase letters, increment score if present
    if re.search(r'[a-z]', password):
        score += 1

    # Test for presence of uppercase letters, increment score if present
    if re.search(r'[A-Z]', password):
        score += 1

    # Test for presence of digits, increment score if present
    if re.search(r'\d', password):
        score += 1

    # Test for presence of special characters, increment score if present
    if re.search(r'\W', password):
        score += 1

    # Test for length of at least 8, increment score if present
    if len(password) >= 8:
        score += 1

    return score
