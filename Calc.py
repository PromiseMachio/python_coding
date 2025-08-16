# Function to calculate discount
def calculate_discount(price, discount_percent):
    # Apply discount only if it is 20% or higher
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        return price - discount_amount
    else:
        return price   # No discount applied


# Main program
# Prompt user for input
price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Call the function
final_price = calculate_discount(price, discount_percent)

# Print result
if discount_percent >= 20:
    print(f"The final price after applying {discount_percent}% discount is: {final_price}")
else:
    print(f"No discount applied. The price remains: {final_price}")
