import bcrypt

def hash_password(password):
    # Adding the salt to password
    salt = bcrypt.gensalt()
    # Hashing the password
    hashed = bcrypt.hashpw(password.encode(), salt)
    hashed_password = []
    hashed_password.append(salt)
    hashed_password.append(hashed)
    return hashed_password


def verify_hash(hashs, password, password_input):
    hashed_password = bcrypt.hashpw(password_input.encode(),hashs)
    if password == hashed_password:
        return True
    else:
        return False
