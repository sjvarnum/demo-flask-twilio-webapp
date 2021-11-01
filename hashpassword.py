from werkzeug.security import generate_password_hash, check_password_hash


# If you need to generate a hashed password for manual entry into local database

password = '1234567'

hashed_password  = generate_password_hash(password, method='sha256')

print(hashed_password)