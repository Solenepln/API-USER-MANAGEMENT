import secrets


#secret key for session
def secret_key():
    return secrets.token_hex()
