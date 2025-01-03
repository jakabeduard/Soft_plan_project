
from Lib.created_by_us.api import get_mailbox_all





if __name__ == "__main__":

    # working
    result = get_mailbox_all()
    # result = create_mailbox()

    # try
    # result = update_mailbox()
    # result = get_mailbox(1)
    # result = delete_mailbox(1)
    # result = get_mailbox_usage(1)
    # result = search_mailboxes()
    # result = reset_mailbox_password()
    # result = get_domains()
    # result = get_mailbox_logs(1)

    print(json.dumps(result, indent=4))