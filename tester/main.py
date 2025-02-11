# This is a sample Python script.
import json
import random
import threading

from tester.written_by_us.monitoring import get_server_info, getting_server_info
from written_by_us.api import  get_domanin_all, get_mailbox_all, delete_mailboxes, create_domain, \
    create_mailbox
from written_by_us.converter import extract_domain_names, extract_email_addresses
from written_by_us.create_testers import create_testers

from written_by_us.load_server_capacity import key_listener, load_server_capacity
from written_by_us.monitoring import geting_htop_output

from written_by_us.random_generator import random_paragraph, generate_paragraphs, random_sentence
from written_by_us.reset_server import cleaning_server

if __name__ == '__main__':
    api_key="E9A377-B0723B-53A5DC-D12E23-67E2F0"
    host_url="https://edu.mailserver.ro"
    host_sever="edu.mailserver.ro"
    ssh_user="admin"
    ssh_password="01234"
    n = 5
    max_paragraphs=10


    # set_ssh("admin", "01234")
    ###################################################################


    result = cleaning_server(host_url, api_key)
    print(json.dumps(result, indent=4))

    # #########################################


    result = create_testers(n, host_url, api_key)
    print(json.dumps(result, indent=4))


    # # #####################################

    listener_thread = threading.Thread(target=key_listener)
    listener_thread.start()
    load_server_capacity(2,n,max_paragraphs,host_sever)

    # # #####################################

    result=getting_server_info(host_sever,ssh_user,ssh_password)
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



