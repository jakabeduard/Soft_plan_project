# This is a sample Python script.
import json
import random
import threading

from tester.written_by_us.monitoring import get_server_info, set_ssh, getting_server_info
from written_by_us.api import  get_domanin_all, get_mailbox_all, delete_mailboxes, create_domain, \
    create_mailbox, set_host_and_headers_api
from written_by_us.converter import extract_domain_names, extract_email_addresses
from written_by_us.create_testers import create_testers
from written_by_us.get_and_send_emails import max_paragraphs

from written_by_us.imap import fetch_and_save_email, set_server_host
from written_by_us.load_server_capacity import key_listener, load_server_capacity
from written_by_us.monitoring import geting_htop_output

from written_by_us.random_generator import random_paragraph, generate_paragraphs, random_sentence
from written_by_us.reset_server import cleaning_server
from written_by_us.smtp import send_email_with_attachment




# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    set_host_and_headers_api("E9A377-B0723B-53A5DC-D12E23-67E2F0","https://edu.mailserver.ro")
    set_server_host("edu.mailserver.ro")
    set_ssh("admin", "01234")
    ###################################################################
    result=cleaning_server()
    print(json.dumps(result, indent=4))
    # # #########################################
    n=20

    # result=create_mailbox(n)
    # print(json.dumps(result, indent=4))
    # set_n_for_load(n)
    result = create_testers(n)
    print(json.dumps(result, indent=4))
    # ###################################################
    #

    # # result=load_server_capacity(2)
    # # print(json.dumps(result, indent=4))
    # # #####################################
    max_paragraphs(100)
    listener_thread = threading.Thread(target=key_listener)
    listener_thread.start()
    load_server_capacity(2,n)

    # # #####################################

    result=getting_server_info()
    print(json.dumps(result, indent=4))

    # sender_email = "a@alma.ro"
    # recipient_email = "b@alma.ro"
    # subject = "Test Emailke"
    # body = "This is a test email sent from Python."
    # file_path = "D:/IMG_20241026_200124_7.jpg"  # Replace with the actual file path
    # result=send_email_with_attachment( sender_email, recipient_email, subject, body, file_path)
    # print(json.dumps(result, indent=4))
    ###########################################################
    # result=get_n_per_2_emails("b")
    # print(json.dumps(result, indent=4))




    # server_info = generate_paragraphs(18)
    # print(json.dumps(server_info, indent=4))





    # result=create_domain()  # Create a new domain
    # print(json.dumps(result, i ndent=4))
    #
    # for i in range(0, 4 + 1):
    #     create_mailbox(i)  # Create 'n' new mailboxes


    # text = random_sentence()
    # print("\nGenerált szöveg:\n")
    # print(text)

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
