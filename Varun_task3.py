import random
import string

# ==========================================
# TASK 3: PASSWORD GENERATOR (BEGINNER TIER)
# ==========================================

def get_password_length():
    """
    Prompts the user for password length and enforces:
    1. Numeric integer input
    2. Minimum length of 8 characters
    """
    while True:
        user_input = input("Enter desired password length (minimum 8): ").strip()
        try:
            length = int(user_input)
            if length < 8:
                print("  [Error] Password length must be at least 8 characters for security.\n")
                continue
            if length > 128:
                print("  [Error] Please enter a length of 128 characters or fewer.\n")
                continue
            return length
        except ValueError:
            print("  [Error] Invalid input! Please enter a whole number (e.g., 12).\n")


def get_yes_no(prompt):
    """Helper function to validate y/n inputs from the user."""
    while True:
        choice = input(prompt).strip().lower()
        if choice in ('y', 'yes'):
            return True
        elif choice in ('n', 'no'):
            return False
        else:
            print("  [Error] Please enter 'y' for Yes or 'n' for No.")


def get_character_preferences():
    """
    Prompts the user to choose character types and enforces that
    at least 2 character types are selected.
    """
    while True:
        print("\nSelect character types to include (at least 2 required):")
        use_upper = get_yes_no("  1. Include Uppercase letters (A-Z)? (y/n): ")
        use_lower = get_yes_no("  2. Include Lowercase letters (a-z)? (y/n): ")
        use_digits = get_yes_no("  3. Include Numbers (0-9)?           (y/n): ")
        use_symbols = get_yes_no("  4. Include Symbols (!@#$%^&*)?      (y/n): ")

        selected_pools = []
        if use_upper:
            selected_pools.append(string.ascii_uppercase)
        if use_lower:
            selected_pools.append(string.ascii_lowercase)
        if use_digits:
            selected_pools.append(string.digits)
        if use_symbols:
            selected_pools.append(string.punctuation)

        # Enforce minimum of 2 character types
        if len(selected_pools) < 2:
            print(f"\n  [Error] You selected {len(selected_pools)} type(s). You must select at least 2 character types! Please try again.")
        else:
            return selected_pools


def generate_password(length, selected_pools):
    """
    Generates a random password that guarantees at least one character
    from each user-selected category.
    """
    # 1. Pick at least one mandatory character from each selected category
    password_chars = [random.choice(pool) for pool in selected_pools]

    # 2. Combine all selected pools for the remaining characters
    combined_pool = "".join(selected_pools)
    remaining_length = length - len(password_chars)

    # 3. Fill the rest of the password length with random choices
    password_chars.extend(random.choices(combined_pool, k=remaining_length))

    # 4. Shuffle the list so mandatory characters aren't always at the front
    random.shuffle(password_chars)

    return "".join(password_chars)


def main():
    print("==========================================")
    print("       RANDOM PASSWORD GENERATOR          ")
    print("==========================================\n")

    while True:
        # 1. Get validated password length (>= 8)
        length = get_password_length()

        # 2. Get validated character types (>= 2 types)
        selected_pools = get_character_preferences()

        # 3. Generate and display password
        password = generate_password(length, selected_pools)
        print("\n------------------------------------------")
        print(f"Generated Password:  {password}")
        print("------------------------------------------\n")

        # 4. Option to generate another password without restarting
        if not get_yes_no("Would you like to generate another password? (y/n): "):
            print("\nThank you for using the Password Generator. Stay secure!")
            break
        print()


if __name__ == "__main__":
    main()