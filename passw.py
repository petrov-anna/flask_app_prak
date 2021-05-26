from werkzeug.security import generate_password_hash, check_password_hash, gen_salt


# генерация паролей
def enc_password(password):
    return generate_password_hash(password)
