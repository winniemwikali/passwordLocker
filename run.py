#!/usr/bin/env python3.6
from password import Users,Credentials
def creat_account(user_name,password):
    '''
    Function to creat a new account
    '''
    new_account = Credentials(user_name,password)
    return new_user
def save_password(user_name,password):
    '''
    Function to save new password
    '''
    new_password(user_name,password)

def del_password(user_name,password):
    '''
    Function to delete password
    '''
    credentials.delete_password()

def add_password(user_name,password):
    '''
    Function to save new password
    '''
    users.add_password()

def view_password(user_name,password):
    '''
    Function that helps users to view their passwords
    '''
    return Users.view_password()  

def main():
    print("Hello Welcome to your password locker.Please write your name")
    user_name =input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create an account, vp - view password, ad -add an account,dc -delete an account ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Account")
            print("-"*50)

            print ("User name ....")
            U_name = input()

            print("password ...")
            password = input()
            save_user(create_user(u_name,password)) # create and save new contact.
            print ('\n')
            print(f"New account {u_name} {password} created")
            print ('\n')


        elif short_code == 'vp':
                print("- *50")
                print(f* "Enter your details to login to your account" )
                if view_password():
                    print("Here is a your locker password")
                    print('\n')

                    for user in user_list():
                            print(u"you have created an account")

                            print('\n')
                else:
                        print('\n')
                        print("You are logged in to your account")
                        print('\n')

        elif short_code == "ex":
                print("Nice time")
                break
        else:
                print("I really didn't get that. Please use the short codes")

