import sys

def decimal_to_hex(decimal_value):
    # Hexadecimal characters map
    hex_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    
    if decimal_value < 0:
        print("Error: Please provide a non-negative integer.")
        sys.exit(1)

    hexadecimal = ""
    num = decimal_value

    print(f"Converting the Decimal Value {num} to Hex...")

    if num == 0:
        hexadecimal = "0"
    else:
        while num != 0:
            rem = num % 16
            hexadecimal = hex_chars[rem] + hexadecimal
            num //= 16

    print(f"Hexadecimal representation is: {hexadecimal}")
    return hexadecimal

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Error: Please provide exactly one integer argument.")
        sys.exit(1)

    try:
        # Attempt to convert the argument to an integer
        decimal_value = int(sys.argv[1])
        decimal_to_hex(decimal_value)
    except ValueError:
        # Handle the case where the input is not an integer
        print("Error: Input must be a valid integer.")
        sys.exit(1)
