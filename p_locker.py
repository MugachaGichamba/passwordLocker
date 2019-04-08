from user import User


def create_user(names,password):

	'''
	Function to create a new user account
	'''
	new_user = User(names,password)
	return new_user


def main():

    print("************PASSWORD LOCKER**************")
    """
    loop to continually ask for input until it breaks
    """
    while True:
        print(' ')
        print("*" * 70)
        print('PLease choose an option: \n 1 to Create an Account \n 2 to Log In \n X to Exit')
        code = input('Enter a choice: ').upper().strip()
        if code == 'X':
            break
        elif code == "1":
            print("Please create your account below")
            names = input("Enter your names seperated by a space")
            password = input("Please Enter your password")
            User.saveUser(create_user(names, password))
            print("successfuly created an account for " + names + " password: " + password)

        elif code == "2":
            print("Log in")
        else:
            print("Please enter a valid input")


if __name__ == '__main__':
    main()