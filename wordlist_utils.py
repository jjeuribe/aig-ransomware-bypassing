def get_passwords(passwordlist='rockyou.txt', encoding="utf-8"):
    with open(passwordlist, 'r', encoding=encoding, errors='replace') as f:
        return [ line.rstrip('\n\r') for line in f ]
