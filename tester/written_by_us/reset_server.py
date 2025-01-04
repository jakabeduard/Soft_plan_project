import json

from written_by_us.api import get_domanin_all, get_mailbox_all, delete_mailboxes, delete_domains
from written_by_us.converter import extract_domain_names, extract_email_addresses


def cleaning_server( host):
    # 1. Get all domains
    print("Fetching all domains...")
    domains_data = get_domanin_all(host)
    if domains_data:
        print("Extracting domain names from the data...")
        domain_names_file = extract_domain_names(domains_data)  # Extract domains and save to 'domain_data.json'
        print(f"Domain names saved to: {domain_names_file}")

    # 2. Get all mailboxes
    print("Fetching all mailboxes...")
    mailboxes_data = get_mailbox_all(host)
    if mailboxes_data:
        print("Extracting email addresses from the data...")
        email_addresses_file = extract_email_addresses(mailboxes_data)  # Extract email addresses and save to 'email_addresses.json'
        print(f"Email addresses saved to: {email_addresses_file}")

    # 3. Delete all mailboxes
    print("Deleting all mailboxes...")
    try:
        email_addresses = json.load(open(email_addresses_file))  # Load email addresses
        delete_mailboxes(email_addresses, host)  # Delete all mailboxes
    except Exception as e:
        print(f"Error occurred while deleting mailboxes: {e}")

    # 4. Delete all domains
    print("Deleting all domains...")
    try:
        domain_names = json.load(open(domain_names_file))  # Load domain names
        delete_domains(host, domain_names)  # Delete all domains
    except Exception as e:
        print(f"Error occurred while deleting domains: {e}")
