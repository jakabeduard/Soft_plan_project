import json

from written_by_us.api import create_domain, create_mailbox


def create_testers(n):
    # Create a new domain
    result=create_domain()  # Create a new domain
    print(json.dumps(result, indent=4))
    # 6. Create new mailboxes (based on input 'n')
    print(f"Creating {n} new mailboxes...")
    for i in range(0, n + 1):
        create_mailbox(i)  # Create 'n' new mailboxes

