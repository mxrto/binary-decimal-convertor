#binary to dec converter


def calc_dec():
    
    binary_list = []

    for _ in binary:
        binary_list.append(int(_))

    binary_list.reverse()

    n = 1
    sum = 0

    for binary_index in binary_list:
        sum += binary_index * n
        n *= 2
    
    return sum


def calc_bin(dec_to_bin):

    remeinder = 0
    dec_list = []

    while dec_to_bin > 0:
        remeinder = dec_to_bin % 2
        dec_list.append(remeinder)
        dec_to_bin //= 2

    dec_list.reverse()

    res = ""
    for i in dec_list:
        res += str(i)

    return res


choice = input("Press 'b' or 'd': ")

if choice == "b":
    binary = input("Please enter your binary number: ")

    decimal = calc_dec()

    print(f"The decimal output for {binary} is: {decimal}")

elif choice == "d":
    decimal = int(input("Please enter you decimal number: "))
    
    binary = calc_bin(decimal)

    print(f"The binary output for {decimal} is: {binary}")
