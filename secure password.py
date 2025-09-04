# secure_password_generator.py
import string
import secrets

def generate_password(length, use_lower=True, use_upper=True,
                      use_digits=True, use_symbols=True):
    # Build character pools based on user choices
    pools = []
    if use_lower:
        pools.append(string.ascii_lowercase)
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.?/\\|~")

    if not pools:
        raise ValueError("At least one character type must be selected.")

    all_chars = "".join(pools)

    while True:
        # Generate random password
        password = "".join(secrets.choice(all_chars) for _ in range(length))

        # Validate: must contain at least one char from each chosen pool
        valid = True
        for pool in pools:
            if not any(ch in pool for ch in password):
                valid = False
                break

        if valid:
            return password

if __name__ == "__main__":
    print("==== Secure Password Generator ====")
    try:
        length = int(input("Enter password length (min 4): "))
        if length < 4:
            raise ValueError("Password length must be at least 4.")

        use_lower = input("Include lowercase letters? (y/n): ").lower() == "y"
        use_upper = input("Include uppercase letters? (y/n): ").lower() == "y"
        use_digits = input("Include digits? (y/n): ").lower() == "y"
        use_symbols = input("Include symbols? (y/n): ").lower() == "y"

        password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
        print("\nYour secure password:", password)

    except ValueError as e:
        print("Error:", e)
