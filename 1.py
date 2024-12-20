def calculate_check_digits(iban_start, check_digits):
    # Create a mapping of letters to numbers
    letter_map = {chr(65+i): str(10+i) for i in range(26)}
    
    # Replace the first 4 characters with their numeric equivalents
    modified_iban = ''.join(letter_map.get(char, char) for char in iban_start[:4]) + iban_start[4:]
    
    # Concatenate the modified IBAN and check digits
    full_number = modified_iban + check_digits
    
    # Calculate the modulus
    remainder = int(full_number) % 97
    
    # Calculate the new check digits
    new_check_digits = 98 - remainder
    
    # Add leading zero if necessary
    return f"{new_check_digits:02d}"

# Test the function
test_cases = [
    ("GB82WEST1234", "56"),
    ("FR14BNPA1234", "67"),
    ("DE89DRESDEFF", "88")
]

for iban_start, check_digits in test_cases:
    result = calculate_check_digits(iban_start, check_digits)
    print(f"IBAN: {iban_start}, Check Digits: {check_digits}, Calculated: {result}")