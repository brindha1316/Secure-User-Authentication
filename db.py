# Simulated DB using dictionary
users = {}

def save_user(username, email, otp):
    users[username] = {"email": email, "otp": otp}

def get_user(username):
    return users.get(username, None)
