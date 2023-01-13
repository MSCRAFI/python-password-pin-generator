import string
import secrets as srt

Chars = string.ascii_letters+string.digits+string.punctuation
Nums = string.digits

choice = int(input("Do you want create a Password or PIN?\n1. Password\n2. PIN\n>> "))
len_num = int(input("Enter the length of your Password or PIN:\n>> "))


def pswd():
    if len_num >= 8:
        password = "".join(srt.choice(Chars) for i in range(int(len_num)))
        print("Here is your generated password:\n>>", password)
    else:
        print("Your number is invalid or less than 8.")


def pin():
    if len_num >= 4:
        pin = "".join(srt.choice(Nums) for i in range(int(len_num)))
        print("Here is your generated PIN:\n>>", pin)
    else:
        print("Your number is invalid or less than 4.")


if choice == 1:
    while True:
        pswd()
        pw_choice = input("Do you want to continue. y/n or Y/N:\n>> ")
        if pw_choice == "n" or pw_choice == "N":
            break
elif choice == 2:
    while True:
        pin()
        pin_choice = input("Do you want to continue. y/n or Y/N:\n>> ")
        if pin_choice == "n" or pin_choice == "N":
            break
else:
    print("Invalid Choice.")
