# This is a sample Python script.
from api import create_mailbox, get_mailbox_all,get_domanin_all,create_domain
import json


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print_hi('PyCharm')

    # domains = get_domanin_all()
    # emails = get_mailbox_all()

    # print(json.dumps(result, indent=4))

    # Save the result to a file
    # with open('domain_data.json', 'w') as file:
    #     json.dump(domains, file, indent=4)
    #
    # with open('email_addresses.json', 'w') as file:
    #     json.dump(emails, file, indent=4)

    # Now print the content of the file
    # with open('domain_data.json', 'r') as file:
    #     saved_data = json.load(file)
    #     print(json.dumps(saved_data, indent=4))

    result=create_mailbox()
    print(json.dumps(result, indent=4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
