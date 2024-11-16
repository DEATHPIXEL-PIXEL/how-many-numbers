total_digits = 0

while True:
    user_input = input("Enter a number (or type 'done'): ")
    if user_input.lower() == 'done':
        break
    total_digits += sum(c.isdigit() for c in user_input)

print("Total digits entered:", total_digits)