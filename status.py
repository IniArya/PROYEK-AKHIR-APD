current_user = {
    "username": None,
    "is_logged_in": False
}

def login_user(username):
    current_user["username"] = username
    current_user["is_logged_in"] = True

def logout_user():
    current_user["username"] = None
    current_user["is_logged_in"] = False

def get_current_user():
    return current_user.copy()

def is_user_logged_in():
    return current_user["is_logged_in"]