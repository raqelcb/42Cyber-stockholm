from cryptography.fernet import Fernet
import key_generator

def encrypt(file_name, key):
	fernet = Fernet(key)
	with open(file_name, 'rb') as encrypted_file:
		file_info = encrypted_file.read()
	encrypted_data = fernet.encrypt(file_info)
	with open(file_name, 'wb') as encrypted_file:
		encrypted_file.write(encrypted_data)

key_generator.generate_key()
key = key_generator.load_key()
print(key)
file_name = 'test.txt'
encrypt(file_name, key)
