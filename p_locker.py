from user import User
from credentials import Credentials
import random
import string

def create_user(names, password):
    """

    Function to create a new user account
    :param names:
    :param password:
    :return:
    """
    new_user = User(names, password)
    return new_user


def create_credentials(username, account, password):
    new_credential = Credentials(username, account, password)
    return new_credential


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
            names = input("please enter your names as you registered")
            """
            check whether user exists and verify their password
            """
            for who in User.users:
                if names in who.names:
                    password = input("please enter your password to log in")
                    if who.names == names and who.password == password:
                        print("logged in successfully")
                        print("welcome " + who.names + "\n Please choose an option below")
                        while True:
                            print('1 store existing credentials \n2 Create new account credentials '
                                  '\n3 View your Account Credentials \n4 Delete credentials \nX to Exit')
                            print("")
                            code = input("Enter code to continue")
                            if code == "X":
                                break
                            elif code == "1":
                                account = input("Enter account name to store")
                                account_password = input("Enter your " + account + "\'s password")
                                Credentials.save_credential(create_credentials(who.names, account, account_password))
                                print(f"Successfully saved {account} to credentials database")
                            elif code == "2":
                                new_account = input("Enter new account name to register:")
                                new_password = input("enter new account password:\n"
                                                     "LEAVE BLANK IF YOU WANT THE SYSTEM TO GENERATE A PASSWORD FOR YOU")
                                if new_password == "":
                                    print("generating password.......")
                                    new_password = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                                    Credentials.save_credential(
                                        create_credentials(who.names, new_account, new_password))
                                    print(f"Successfully saved {new_account} to credentials database")
                                else:
                                    Credentials.save_credential(
                                        create_credentials(who.names, new_account, new_password))
                                    print(f"Successfully saved {new_account} to credentials database")
                            elif code == "3":
                                count = 1
                                print(f"Here are {who.names} credentials" )
                                for cred in Credentials.credentials:
                                    print(cred.__dict__)
                                    print(count, cred.account, cred.password)
                                    count += 1
                                print("\n")

                            elif code == "4":
                                to_delete = input("Please Enter name of account site to delete")
                                try:
                                    for cred in Credentials.credentials:
                                        Credentials.credentials.remove(cred.__dict__)
                                except ValueError:
                                    print("account not in database")
                    else:
                        print("wrong login credentials")
                else:
                    print("enter a valid name")

        else:
            print("Please enter a valid input")


if __name__ == '__main__':
    main()
