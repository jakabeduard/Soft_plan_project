from written_by_us.api import create_domain, create_mailbox


def create_testers(host, n):
    create_domain(host)  # Create a new domain

    # 6. Create new mailboxes (based on input 'n')
    print(f"Creating {n} new mailboxes...")
    for i in range(1, n + 1):
        create_mailbox(i, host)  # Create 'n' new mailboxes

    print("Server cleaning and mailbox creation completed.")