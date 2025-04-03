from cryptography.fernet import Fernet

key = Fernet.generate_key()

message = b'This is my secret message'

engine = Fernet(key)

encrypted_message = engine.encrypt(message)
decrypted_message = engine.decrypt(encrypted_message)

print(encrypted_message)
print(decrypted_message)

#print(engine.decrypt(encrypted_message))