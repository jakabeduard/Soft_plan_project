from written_by_us.imap import fetch_and_save_email


def get_n_per_2_emails(email):

    email_user = f"{email}@alma.ro"
    save_directory = fr"D:\emails\{email}"
    fetch_and_save_email(email_user, save_directory)