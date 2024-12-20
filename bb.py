from operator import add

def calculate_points(score, bonus):
    # Calculate the sum of score and bonus using the add function from the operator module
    total_points = add(score, bonus)
    
    # Check if the total points is greater than 100 and return the appropriate value
    if total_points > 100:
        return 'Game Over'
    else:
        return total_points

# Test the function with sample inputs
print(calculate_points(50, 30))  # Expected output: 80
print(calculate_points(50, 60))  # Expected output: 'Game Over'
print(calculate_points(90, 10))  # Expected output: 100
print(calculate_points(100, 1))  # Expected output: 'Game Over'