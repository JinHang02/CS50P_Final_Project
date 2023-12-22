from tabulate import tabulate     #import library to tabulate data
import sys
import csv
import validators                 #import validators to validate email
import re
import time

# ----------------------------------------------------------------------------------------------------------
def main():
    n = 0  # define a variable to set as counter for interface() function
    while True:
        if n == 0:
            user = interface()  # this function will be called in beginning of program only

        if user == "1": #To access "User's Information"
            n = 1  # to not repeat function interface()
            username, password = get_login_input()  #to get username,password of user
            user_row = get_login_data(username, password,"project.csv")#to get location of user in csv.file
            list1 = information_interface(user_row)  #to display "User's Information"
            user = information_interface_input(list1, user_row)
            #to get user' input to navigate in "User's Information"

        elif user == "2": #To access "User's Summon"
            n = 1  # to not repeat function interface()
            username, password = get_login_input()  #to get username,password of user
            user_row = get_login_data(username, password,"project2.csv")#to get location of user in csv.file
            list1 = summon_interface(user_row)  #to display "User's Summons"
            user = summon_interface_input(list1, user_row)
            #to get user' input to navigate in "User's Summons"

        elif user == "3": #To quit program
            sys.exit("Thank you and have a great day :)\n")


# ----------------------------------------------------------------------------------------------------------
# functions to print main interface of program
def interface():  # display interface and return str
    with open("interface.csv") as file:
        reader = csv.reader(file)
        interface_list = list(reader)
    print("\n     Car Summon Application")
    print(tabulate(interface_list, headers="firstrow", tablefmt="fancy_grid"))
    # first time asking for input
    user = input("\nAction to execute (1/2/3): ").strip()
    return get_input_interface(user)


def get_input_interface(user):  # request input and return str
    while True:
        if user == "1":
            return "1"
        elif user == "2":
            return "2"
        elif user == "3":
            return "3"
        else:
            print("Invalid Input")
            user = input("\nAction to execute (1/2/3): ").strip()  # request input after invalid input


# ----------------------------------------------------------------------------------------------------------
# functions to get user login details
def get_login_input():  # get username and password from user
    username = input("What is your name: ")
    password = input("What is your password: ")
    return username, password


def get_login_data(username, password,data_file):  # check username and password with databases
    while True:
        with open(data_file) as file:
            reader = csv.DictReader(file)
            for i, row in enumerate(reader):
                if username == row["Name"] and password == row["Password"]:
                    return i  # return user location(row) in databases
        print("Invalid Username and Password\n")
        username = input("What is your name: ")  # request input again after invalid input
        password = input("What is your password: ")  # request input again after invalid input


# ----------------------------------------------------------------------------------------------------------
# functions related with "User's Information" when user =="1"
def information_interface(i=0):  # display user information in "User's Information"
    with open("project.csv") as file:
        reader = csv.DictReader(file)
        list1 = list(reader)
        list2 = [
            ["Contact Number", "Email Address", "State"],
            [list1[i]["Contact Number"], list1[i]["Email Address"], list1[i]["State"]],
        ]
    print("\n\t\tUser's Information")
    print(tabulate(list2, headers="firstrow", tablefmt="fancy_grid"))  # print user's info in table
    return list1


def information_interface_input(list1, i):  # ask user for input in "User's Information"
    while True:
        print(
            "Type Q to quit, A to amend contact number, B to amend email address, C to amend state"
        )
        action_information_interface = input("Input:").lower().strip()
        if action_information_interface == "a":
            amend_contact(list1, i)
            _ = information_interface(i)
        elif action_information_interface == "b":
            amend_email(list1, i)
            _ = information_interface(i)
        elif action_information_interface == "c":
            amend_state(list1, i)
            _ = information_interface(i)
        elif action_information_interface == "q":
            return interface()  # call interface() function to back to main interface
        else:
            print("Invalid Input\n")


def amend_contact(list1, i):
    while True:
        new_contact = input("\nEnter new contact number: ")
        if re.search(r"^\+601[0-9][0-9]{7,8}$", new_contact):
            list1[i]["Contact Number"] = new_contact
            print("New Contact Number has been updated!")
            amend_Information(list1)
            break
        else:
            print("Invalid Contact Number!")


def amend_email(list1, i):
    while True:
        new_email = input("\nEnter new email address: ").strip().lower()
        if validators.email(new_email):
            list1[i]["Email Address"] = new_email
            print("New Email Address has been updated!")
            amend_Information(list1)
            break
        else:
            print("Invalid Email Address!")


def amend_state(list1, i):
    state_list = [          #list of states in Malaysia
        "johor",
        "kedah",
        "kelantan",
        "malacca",
        "negeri sembilan",
        "pahang",
        "penang",
        "perak",
        "perlis",
        "sabah",
        "sarawak",
        "selangor",
        "terengganu",
    ]
    while True:
        new_state = input("\nEnter new living state: ").strip().lower()
        if new_state in state_list:
            list1[i]["State"] = new_state.capitalize()
            print("New Living State has been updated!")
            amend_Information(list1)
            break
        else:
            print("Invalid State!")


def amend_Information(list1):
    with open("project.csv", "w") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["Name", "Password", "Contact Number", "Email Address", "State"],
        )
        writer.writeheader()
        writer.writerows(list1)


# ----------------------------------------------------------------------------------------------------------
# functions related with "User's Summons" when user =="2"
def summon_interface(i=0):  # display user summons in "User's Summons"
    with open("project2.csv") as file:
        reader = csv.DictReader(file)
        list1 = list(reader)
        list2 = [
            ["Location", "Amount", "Description"],
            [list1[i]["Location"], list1[i]["Amount"], list1[i]["Description"]],
        ]
    print("\n\t\tUser's Summons")
    print(tabulate(list2, headers="firstrow", tablefmt="fancy_grid"))  # print user's summon in table
    return list1


def summon_interface_input(list1, i):  # ask user for input in "User's Summons"
    while True:
        if (list1[i]["Amount"] == "None"):  # an indicator to show user has "NO" summons
            print("All summons are cleared\nType Q to quit")
            action_summon_interface = input("Input: ").lower().strip()
            if action_summon_interface == "q":
                return interface()  # call interface() function to back to main interface
            else:
                print("Invalid Input\n")
        else:
            print("Type Q to quit, A to pay for summon")
            action_summon_interface = input("Input: ").lower().strip()
            if action_summon_interface == "a":
                pay_summon(list1, i)
                _ = summon_interface(i)
            elif action_summon_interface == "q":
                return interface()  # call interface() function to back to main interface
            else:
                print("Invalid Input\n")


def pay_summon(list1, i):
    while True:
        pay = input("\nEnter Visa/Mastercard number(without -): ").strip()
        if re.search(r"^(4[0-9]{12}|4[0-9]{15}|5[1-5][0-9]{14})$", pay):
                        # Visa(13) | Visa(16)  |Mastercard
            list1[i]["Location"] = list1[i]["Amount"] = list1[i]["Description"] = "None"
            for _ in range(5):  # Demonstration of real-life payment
                print(".")
                time.sleep(1)  # a delay message as a sign to process payment
            print("User's Summon has been paid!")
            amend_Summon(list1)
            break
        else:
            print("Invalid Visa/Mastercard number!")


def amend_Summon(list1):
    with open("project2.csv", "w") as file:
        writer = csv.DictWriter(
            file, fieldnames=["Name", "Password", "Location", "Amount", "Description"]
        )
        writer.writeheader()
        writer.writerows(list1)


# ----------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()
