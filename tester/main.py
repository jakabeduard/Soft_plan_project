# This is a sample Python script.
import json

from written_by_us.api import set_host_and_headers, get_domanin_all, get_mailbox_all, delete_mailboxes, create_domain, \
    create_mailbox
from written_by_us.converter import extract_domain_names, extract_email_addresses
from written_by_us.reset_server import cleaning_server

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    set_host_and_headers("E9A377-B0723B-53A5DC-D12E23-67E2F0","https://edu.mailserver.ro")
    result=cleaning_server()
    print(json.dumps(result, indent=4))



    # for i in range(1, 11):  # 10 postafiókot hoz létre (tester1 - tester10)
    #     create_mailbox(i)


    # result = get_domanin_all()
    # print(json.dumps(result, indent=4))
    #
    # if result:
    #     domains = [entry['domain_name'] for entry in result]
    #     print("Extracted domanins:", domains)
    #
    #     # 3. Delete all mailboxes
    # delete_mailboxes(domains)
    #
    # result=create_domain()


    # result = get_mailbox_all()
    #
    #
    #


    # print(json.dumps(result, indent=4))
    # result3=delete_mailboxes(result2)
    # print(json.dumps(result3, indent=4))

    # result = get_mailbox_all()
    #
    # if result:
    #     email_list = [entry['username'] for entry in result]
    #     print("Extracted email addresses:", email_list)
    #
    #     delete_mailboxes(email_list)


    # Save the result to a file
    # with open('domain_data.json', 'w') as file:
    #     json.dump(domains, file, indent=4)
    #
    # with open('email_addresses.json', 'w') as file:
    #     json.dump(emails, file, indent=4)

    # Now print the content of the file
    # with open('email_addresses.json', 'r') as file:
    #     saved_domnains_json = json.load(file)
    #     print(json.dumps(saved_domnains_json, indent=1))



    # result = extract_domain_names('domain_data.json')
    # print(f"Domain names extracted and saved in {result}")
    # emails=extract_email_addresses('email_addresses.json')
    # print(f"Domain names extracted and saved in {emails}")
    # result=create_mailbox()
    # print(json.dumps(result, indent=4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
