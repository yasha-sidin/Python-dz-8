import re

def init_contact_list_file(file_name):
    print("New contact_list file was added")
    file = open(file_name, 'w')
    file.close()

def add_contact(file_name, name, sername, number):
    regex = r"\+7\d{10}"
    if (re.fullmatch(regex, number) != None):
        with open(file_name, 'a') as contact:
            contact.write(f'{sername} {name} -> {number}\n')
    else:
        print("You can't use this format of number(use: +7[0-9]{10})")

def shaw_all(file_name):
    with open(file_name, 'r') as data:
        for line in data:
            print(line)

# def search_in_file(file_name, name=None, sername=None, number=None):
#     name_list = []
#     sername_list = []
#     number_list = []
#     with open(file_name, 'r') as data:
#         for line in data:
#             if(name != None):
#                 regex = fr".+{name}.+"
#                 if(re.fullmatch(regex, line) != None):
#                     name_list.append(line)
#             if(sername != None):
#                 regex = fr".+{sername}.+"
#                 if (re.fullmatch(regex, line) != None):
#                     sername_list.append(line)
#             if(number != None):
#                 regex = fr".+\{number}.+"
#                 if (re.fullmatch(regex, line) != None):
#                     number_list.append(line)
#     result_list = []
#     result_list.append(name_list).append(sername_list).append(number_list)
#     for item in result_list:
#         if (len(item) == 0):
#             result_list.remove(item)
#         else:
#             set(item)
#     if(len(result_list) == 1):
#         return result_list
#     if(len(result_list) == 2):
#         return set.intersection(result_list[0], result_list[1])
#     if(len(result_list) == 3):
#         return set.intersection(result_list[0], result_list[1], result_list[2])

def delete_contact(file_name, name, sername):
    lines = []
    with open(file_name, 'r') as data:
        lines = data.readlines()
    with open(file_name, 'w') as data:
        for line in lines:
            if (sername + ' ' + name in line):
                continue
            else:
                data.write(line)

def change_number(file_name, name, sername, new_number):
    regex = r"\+7\d{10}"
    if (re.fullmatch(regex, new_number) != None):
        lines = []
        with open(file_name, 'r') as data:
            lines = data.readlines()
        with open(file_name, 'w') as data:
            for line in lines:
                if (sername + ' ' + name in line):
                    line = f'{sername} {name} -> {new_number}\n'
                data.write(line)
    else:
        print("You can't use this format of number(use: +7[0-9]{10})")

def search_by_name(file_name, name):
    name_list = []
    with open(file_name, 'r') as data:
        for line in data:
            if (name in line):
                name_list.append(line)
    return name_list

def search_by_sername(file_name, sername):
    sername_list = []
    with open(file_name, 'r') as data:
        for line in data:
            if (sername in line):
                sername_list.append(line)
    return sername_list

def search_by_contact(file_name, contact):
    contact_list = []
    with open(file_name, 'r') as data:
        for line in data:
            if (contact in line):
                contact_list.append(line)
    return contact_list