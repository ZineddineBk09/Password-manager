import bcrypt

stri="jmsldf"
password=bytes(stri, encoding='utf-8')

hashed1=bcrypt.hashpw(password,bcrypt.gensalt())
hashed2=bcrypt.hashpw(password,bcrypt.gensalt(16))
print(hashed1)
#print(hashed2)
