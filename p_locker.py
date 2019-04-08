def main():
    print("************PASSWORD LOCKER**************")
    while True:
        print(' ')
        print("*" * 70)
        print('PLease choose an option: \n 1 to Create an Account \n 2 to Log In \n X to Exit')
        code = input('Enter a choice: ').upper().strip()
        if code == 'X':
            break
        elif code == "1":
            print("create an account")
        elif code == "2":
            print("Log in")
        else:
            print("Please enter a valid input")


if __name__ == '__main__':
    main()