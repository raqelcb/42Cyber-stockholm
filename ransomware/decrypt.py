from cryptography.fernet import Fernet
import key_generator

def decrypt(file_name, key):
	fernet = Fernet(key)
	with open(file_name, 'rb') as encrypted_file:
		encrypted_data = encrypted_file.read()
	decrypted_data = fernet.decrypt(encrypted_data)
	with open(file_name, 'wb') as encrypted_file:
		encrypted_file.write(decrypted_data)

key = key_generator.load_key()
print(key)
file_name = 'test.txt'
decrypt(file_name, key)