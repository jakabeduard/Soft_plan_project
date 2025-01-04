import json

from written_by_us.api import get_domanin_all, get_mailbox_all, delete_mailboxes, delete_domains
from written_by_us.converter import extract_domain_names, extract_email_addresses




def cleaning_server():
    result = get_domanin_all()
    result2 = get_mailbox_all()
    print(json.dumps(result, indent=4))
    print(json.dumps(result2, indent=4))
    if result2:
        # Extract email addresses if result2 is valid
        email_list = [entry['username'] for entry in result2]
        print("Extracted email addresses:", email_list)

        # 3. Delete all mailboxes
        delete_mailboxes(email_list)
    else:
        print("No mailboxes found, skipping mailbox deletion.")

        # 4. Delete all domains
    if result:
        domains = [entry['domain_name'] for entry in result]
        print("Extracted domains:", domains)

        # 3. Delete all domains
        delete_domains(domains)
    else:
        print("No domains found, skipping domain deletion.")