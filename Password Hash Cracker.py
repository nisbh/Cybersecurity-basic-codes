import hashlib

# The target hash we want to crack. This is SHA-256 hash for the password "password123".
target_hash = "ef92b778bafe771e89245b89ecbc08a44a4e166c06659911881f383d4473e94f"
wordlist_path = 'wordlist.txt'
print("Starting hash cracking...")
try:
    with open(wordlist_path, 'r') as wordlist_file:
        for line in wordlist_file:
            #.strip() function removes any whitespace/newline characters from beginning and end of line.
            password_candidate = line.strip()
            # encode the password string into bytes before hashing,hashing functions operate on bytes, not strings.
            password_bytes = password_candidate.encode('utf-8')
            # Create a new SHA-256 hash object.
            hash_object = hashlib.sha256()
            # Update the hash object with the password bytes.
            hash_object.update(password_bytes)
            # hexdigest() computes the final hash and returns it as string of hexadecimal characters,standard way to display hashes.
            generated_hash = hash_object.hexdigest()
            # Compare the hash generated from wordlist entry with target hash.
            if generated_hash == target_hash:
                print(f"[SUCCESS] Password found: {password_candidate}")
                exit(0)
    print("[FAILURE] Password not found in wordlist.")
except FileNotFoundError:
    print(f"Error: The file '{wordlist_path}' was not found.")
    print("Please create it and add some passwords to it.")