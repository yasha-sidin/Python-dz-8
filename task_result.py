import methods

file_name = input('Enter contact list file name: ')
methods.init_contact_list_file(file_name)
command = '0'
while(command != "stop"):
    print(f"1\t->\tadd new contact\n"
          f"2\t->\tshaw all contacts\n"
          f"3\t->\tsearch in file\n"
          f"4\t->\tdelete contact if it not exist\n"
          f"5\t->\tchange number\n"
          f"To stop print \"stop\"")
    command = input('Choose command: ')
    if (command == 'stop'):
        break
    else:
        command = int(command)
    if (command == 1):
        name = input('Enter name of person: ')
        sername = input('Enter sername of person: ')
        contact = input('Enter contact number: ')
        methods.add_contact(file_name, name, sername, contact)
    if (command == 2):
        methods.shaw_all(file_name)
    if (command == 3):
        searched_contacts = []
        with open(file_name, 'r') as data:
            for line in data:
                searched_contacts.append(line)
        print('Which parameters do you want to use to search? Print amount of parameters and parameters(name, sername, number) using ENTER')
        amount = int(input('Amount: '))
        if (amount > 3 or amount < 1):
            print('Max = 3')
        else:
            for i in range(1, amount + 1):
                temp_param = input(f'{i} parameter: ').lower()
                if(temp_param == "name"):
                    name = input('Enter name of person: ')
                    searched_contacts = methods.search_by_name(file_name, name)
                if(temp_param == "sername"):
                    sername = input('Enter sername of person: ')
                    searched_contacts = methods.search_by_sername(file_name, sername)
                if(temp_param == "number"):
                    number = input('Enter number of person: ')
                    searched_contacts = methods.search_by_contact(file_name, number)
                if(temp_param != "number" or temp_param != "name" or temp_param != "sername"):
                    i -= 1
            for line in searched_contacts:
                print(line)
            if(len(searched_contacts) == 0):
                print('Not found')
    if (command == 4):
        name = input('Enter name of person: ')
        sername = input('Enter sername of person: ')
        methods.delete_contact(file_name, name, sername)
    if (command == 5):
        name = input('Enter name of person: ')
        sername = input('Enter sername of person: ')
        new_number = input('Enter new number: ')
        methods.change_number(file_name, name, sername, new_number)
