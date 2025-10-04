'''
Forage AIG Cybersecurity Program
Bruteforce starter template
'''

from zipfile import ZipFile, BadZipFile

def get_passwords(passwordlist='rockyou.txt', encoding="utf-8"):
    with open(passwordlist, 'r', encoding=encoding, errors='replace') as f:
        return [ line.rstrip('\n\r') for line in f ]

def attempt_extract(zf_handle, file, password):
    try: 
        with zf_handle.open(file, pwd=password.encode('utf-8')) as f:
            # Since decryption happens when reading data, read at least one byte. 
            f.read(1)
        return True
    
    except RuntimeError as e: 
        if 'password required' in str(e).lower() or 'bad password' in str(e).lower():
            return False
        else: 
            raise

def bruteforce_zipfile(zipfile, passwords):
    result = {
        'success': False, 
        'password': None, 
        'tries': 0,
        'error': None
    }

    try: 
        with ZipFile(zipfile, 'r') as zf:
            files = zf.namelist()
            
            if not files:
                result['error'] = "ZIP is empty!"
                return result

            for password in passwords:
                result['tries'] += 1

                if attempt_extract(zf, files[0], password):
                    result['success'] = True
                    result['password'] = password
                    break
    except FileNotFoundError: 
        result['error'] = 'ZIP file not found!'
    except BadZipFile:
        result['error'] = 'Bad ZIP file!'
    except Exception: 
        raise
    
    return result

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