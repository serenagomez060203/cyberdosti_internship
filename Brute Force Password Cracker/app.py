import itertools
import string

def brute_force_password_cracker(target_password, max_length=8):
    characters = string.ascii_lowercase  # Define the character set
    attempts = 0

    for length in range(1, max_length + 1):
        for guess in itertools.product(characters, repeat=length):
            attempts += 1
            guess_password = ''.join(guess)
            if guess_password == target_password:
                return guess_password, attempts

    return None, attempts

# Example usage
target_password = "abc"  # Change this to the password you want to crack
max_length = 8  # Maximum length of the password to try
cracked_password, attempts = brute_force_password_cracker(target_password, max_length)

if cracked_password:
    print(f"Password cracked: {cracked_password} in {attempts} attempts.")
else:
    print(f"Password not cracked within length {max_length}.")
