import json

from written_by_us.api import create_domain, create_mailbox, update_mailbox_password


def create_testers(n,host, api_key):
    # Create a new domain
    result=create_domain(host, api_key)  # Create a new domain
    print(json.dumps(result, indent=4))
    # 6. Create new mailboxes (based on input 'n')
    print(f"Creating {n} new mailboxes...")
    for i in range(0, n + 1):
        create_mailbox(i, host, api_key)  # Create 'n' new mailboxes


    for i in range(0, n + 1):
        update_mailbox_password(i, host, api_key)