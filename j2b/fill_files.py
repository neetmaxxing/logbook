import uuid
import os


def generate_random_uuid():
	return uuid.uuid4()


def fill_files():
	i = 0
	for i in range(100):
		random_uuid = generate_random_uuid()
		with open(f"{i}.txt", "w") as f:
			f.write(str(random_uuid))
			f.close()

fill_files()
