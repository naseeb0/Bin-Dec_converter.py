binary_string = input("Please Enter The Binary Number :")

try:
    decimal = int(binary_string,2)
    print("The decimal value is :", decimal)

except ValueError:
    print("Invalid binary number")
