import random
import string

def generate_key(length):
    characters = string.ascii_letters + string.digits
    key = ''.join(random.choice(characters) for i in range(length))
    return key

if __name__ == "__main__":
    try:
        key_length = int(input("Enter the desired key length: "))
        if key_length <= 0:
            raise ValueError("Key length must be a positive integer.")
        
        generated_key = generate_key(key_length)
        print("Generated Key:", generated_key)
    
    except ValueError as e:
        print("Error:", e)