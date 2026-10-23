# ==========================================
# TASK 2: BMI CALCULATOR (BEGINNER TIER)
# ==========================================

def get_valid_float(prompt, min_val, max_val, unit):
    """
    Prompts the user for a numeric input and validates against:
    1. Non-numeric strings (e.g., 'abc')
    2. Zero or negative numbers
    3. Unrealistic human measurements
    """
    while True:
        user_input = input(prompt).strip()
        try:
            value = float(user_input)
            
            # Reject zero or negative values
            if value <= 0:
                print(f"  [Error] Value must be greater than 0 {unit}. Please try again.\n")
                continue
            
            # Sanity check for realistic values (e.g., catching cm entered instead of m)
            if value < min_val or value > max_val:
                print(f"  [Error] Please enter a realistic value between {min_val} and {max_val} {unit}.\n")
                continue
                
            return value
            
        except ValueError:
            # Reject non-numeric input
            print("  [Error] Invalid input! Please enter a valid number (e.g., 70 or 1.75).\n")


def calculate_bmi(weight_kg, height_m):
    """Calculates BMI using the standard formula: weight / (height^2)"""
    return weight_kg / (height_m ** 2)


def classify_bmi(bmi):
    """Classifies the BMI value into standard WHO health categories."""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25.0:
        return "Normal"
    elif 25.0 <= bmi < 30.0:
        return "Overweight"
    else:
        return "Obese"


def main():
    print("==========================================")
    print("         PYTHON BMI CALCULATOR            ")
    print("==========================================\n")

    while True:
        # 1. Prompt user for weight (kg) and height (m) with input validation
        weight = get_valid_float("Enter your weight in kilograms (kg): ", min_val=2.0, max_val=500.0, unit="kg")
        height = get_valid_float("Enter your height in meters (m) [e.g., 1.75]: ", min_val=0.4, max_val=2.8, unit="m")

        # 2. Calculate BMI
        bmi = calculate_bmi(weight, height)

        # 3. Classify result into standard categories
        category = classify_bmi(bmi)

        # 4. Display BMI rounded to 2 decimal places and the category
        print("\n------------------------------------------")
        print(f"Your BMI is:   {bmi:.2f}")
        print(f"Health Status: {category}")
        print("------------------------------------------\n")

        # Ask if the user wants to perform another calculation
        again = input("Would you like to calculate another BMI? (y/n): ").strip().lower()
        if again not in ('y', 'yes'):
            print("\nThank you for using the BMI Calculator. Stay healthy!")
            break
        print()


if __name__ == "__main__":
    main()