import bcrypt

def hashPassword(password):

    # Adding the salt to password
    salt = bcrypt.gensalt()
    # Hashing the password
    hashed = bcrypt.hashpw(password.encode(), salt)
    hashedPassword=[]
    hashedPassword.append(salt)
    hashedPassword.append(hashed)
    return hashedPassword
