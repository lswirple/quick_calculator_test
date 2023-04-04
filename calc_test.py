def first_num():
    while True:
        global num_1
        num_1 = input("What number do you want in first? ")
        if num_1.isdecimal():
            break
        else:
            print("Enter valid input.")

def sec_num():
    while True:
        global num_2
        num_2 = input("What number do you want in second? ")
        if num_2.isdecimal():
            break
        else:
            print("Enter valid input.")

def numbers():
    first_num()
    sec_num()
"""    while (asking := str(input(f"Are {num_1} and {num_2} the numbers you want to work with? "))) not in ANSWER_YN:
        pass
    if asking == 'no' or 'n':
        print()
    while (answer := str(input("Addition, multiplication, or subtraction? "))) not in AVAILABLE_ANSWERS:
        pass """

def calculate():
    input0 = input("Addition, multiplication, or subtraction? ")
    if input0 == 'addition':
        print(int(num_1) + int(num_2))
    elif input0 == 'multiplication':
        print(int(num_1) * int(num_2))
    elif input0 == 'subtraction':
        print(int(num_1) - int(num_2))

def main():
    numbers()
    answer_yn = input(f"Are {num_1} and {num_2} the numbers you want to work with? ")
    if answer_yn == 'yes':
        return
    elif answer_yn == 'no':
        print("Re-input numbers.")
        main()
    else:
            print("Enter valid answer.")
    calculate()

main()
