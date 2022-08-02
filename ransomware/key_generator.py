from cryptography.fernet import Fernet
import os
import sys

def generate_key():
	key = Fernet.generate_key()
	with open('key_generator.key', 'wb') as key_file:
		key_file.write(key)

def load_key():
	return open ('key_generator.key', 'rb').read()

