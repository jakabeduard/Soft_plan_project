import json

from written_by_us.api import get_domanin_all, get_mailbox_all, delete_mailboxes, delete_domains
from written_by_us.converter import extract_domain_names, extract_email_addresses




def cleaning_server():
    # 1. Get all domains
    result=get_domanin_all()

    # 2. Get all mailboxes
    result2 = get_mailbox_all()

    if result2:
        email_list = [entry['username'] for entry in result2]
        print("Extracted email addresses:", email_list)

    # 3. Delete all mailboxes
    delete_mailboxes(email_list)

    # 4. Delete all domains
    if result:
        domanins = [entry['domain_name'] for entry in result]
        print("Extracted domanins:", domanins)

    # 3. Delete all mailboxes
    delete_mailboxes(domanins)
