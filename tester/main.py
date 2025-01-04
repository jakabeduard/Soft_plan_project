# This is a sample Python script.
import json

from written_by_us.api import set_host_and_headers
from written_by_us.converter import extract_domain_names, extract_email_addresses






# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    set_host_and_headers("E9A377-B0723B-53A5DC-D12E23-67E2F0","https://edu.mailserver.ro")



    # for i in range(1, 11):  # 10 postafiókot hoz létre (tester1 - tester10)
    #     create_mailbox(i)


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
    # with open('email_addresses.json', 'r') as file:
    #     saved_domnains_json = json.load(file)
    #     print(json.dumps(saved_domnains_json, indent=1))



    result = extract_domain_names('domain_data.json')
    print(f"Domain names extracted and saved in {result}")
    emails=extract_email_addresses('email_addresses.json')
    print(f"Domain names extracted and saved in {emails}")
    # result=create_mailbox()
    # print(json.dumps(result, indent=4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
