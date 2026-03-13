phone_numbers ={
    'ahmed' : '05768943',
    'william' : '04780912',
    'gorge' : '0776447221',
}


file = open(phone_numbers)

def name_search(name):
    print(phone_numbers [name])


def add_contact(name , number):
    with open("contacts.txt", "a") as file :
        phone_numbers[name] = number

def delet_contact(name):
    if name in phone_numbers:
        del phone_numbers[name]
    else:
        print('contact not found .')

def check_contacts():
    for name, number in phone_numbers.items():
        print(phone_numbers[name , number])

def see_contacts():
    print(phone_numbers)
while True:
    print("1. Search")
    print("2. Add")
    print("3. Delete")
    print("4. Show all")
    print("5. check a contact")
    print("6. Quit")
    choice = input("Choose: ")

    if choice == '1':
        name_search(str(input('who do you want to call : \n')))
        
    elif choice == '2':
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
        
    elif choice == '3':
        del phone_numbers
        
    elif choice == '4':
        see_contacts
    
    elif choice == '5':
        check_contacts

    elif choice == '6':
        break




 
