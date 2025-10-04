'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zip_cracker import bruteforce_zipfile

def get_passwords(passwordlist='rockyou.txt', encoding="utf-8"):
    with open(passwordlist, 'r', encoding=encoding, errors='replace') as f:
        return [ line.rstrip('\n\r') for line in f ]

def main():
    print("[+] Beginning bruteforce ")

    try: 
        passwords = get_passwords('rockyou.txt')
    except FileNotFoundError:
        print("Wordlist missing!")
    else: 
        result = bruteforce_zipfile('enc.zip', passwords)

        if result.get('error'): 
            print(f"ERROR: {result.get('error')}")
            return 

        if result.get('success'): 
            print("SUCCESS: Password found!")
            print(f"Password: {result.get('password')}")
            print(f"Tries: {result.get('tries')}")
        else: 
            print("Password not found")
            print(f"Tries: {result.get('tries')}")

if __name__ == "__main__":
    main()