import sys

def decimal_to_hex(decimal_value):
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

<<<<<<< HEAD
=======
    # Handle the case when the input is 0
>>>>>>> origin/main
    if num == 0:
        hexadecimal = "0"
    else:
        while num != 0:
            rem = num % 16
            hexadecimal = hex_chars[rem] + hexadecimal
            num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
<<<<<<< HEAD
    return hexadecimal

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one integer argument.")
        sys.exit(1)
    try:
        decimal_value = int(sys.argv[1])
        decimal_to_hex(decimal_value)
    except ValueError:
        print("Error: Input must be a valid integer.")
        sys.exit(1)

=======
    return hexadecimal  # Return the hexadecimal value for testing

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            decimal_value = int(sys.argv[1])
            decimal_to_hex(decimal_value)
        except ValueError:
            print("Error: Please provide a valid integer.")
    else:
        print("Usage: python Dec2Hex.py <decimal_number>")
>>>>>>> origin/main
