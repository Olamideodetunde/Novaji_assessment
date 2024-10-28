from cryptography.fernet import Fernet
key = Fernet.generate_key()
f= Fernet(key)

sensitive_data=f.encrypt(b'Welcome to Lagos')
word=f.decrypt(sensitive_data)
print(sensitive_data,word)