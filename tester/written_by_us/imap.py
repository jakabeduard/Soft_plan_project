import imaplib
import email
from email.header import decode_header
import os


def fetch_and_save_email( receiver_number, host_sever):
    """Fetch emails from specified folders and save them with attachments."""

    # Fixed configurations
    imap_server = host_sever   # IMAP server address
    email_pass = "9876543210"  # Password for the email account
    folders = ["INBOX", "Sent", "Trash", "Junk", "Drafts", "Archive"]  # Folders to synchronize: "INBOX", "Sent", "Trash", "Junk", "Drafts", "Archive"
            # ["INBOX", "Sent", "Trash", "Junk", "Drafts", "Archive"]
    def safe_decode_header(header_value):
        """Safely decode an email header."""
        if header_value:
            decoded, encoding = decode_header(header_value)[0]
            if isinstance(decoded, bytes):
                return decoded.decode(encoding if encoding else "utf-8")
            return decoded
        return "No Value"

    def save_email(email_message, folder_name, email_id):
        """Save email content and attachments."""
        email_dir = os.path.join(fr"D:\emails\tester{receiver_number}" , folder_name, f"Email-{email_id}")
        os.makedirs(email_dir, exist_ok=True)

        subject = safe_decode_header(email_message.get("Subject"))
        subject = subject.replace("/", "_")  # Sanitize the subject for filenames

        body_file = os.path.join(email_dir, "email.txt")
        with open(body_file, "w", encoding="utf-8") as f:
            f.write(f"Subject: {subject}\n")
            f.write(f"From: {safe_decode_header(email_message.get('From'))}\n")
            f.write(f"To: {safe_decode_header(email_message.get('To'))}\n\n")

            body = None
            if email_message.is_multipart():
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True)
                        if body:
                            body = body.decode(errors="ignore")
                            break
            else:
                body = email_message.get_payload(decode=True)
                if body:
                    body = body.decode(errors="ignore")

            f.write(body if body else "No content available")
            print(f"Email mentve: ")
            print(f"{safe_decode_header(email_message.get('To'))}- mentve, {safe_decode_header(email_message.get('From'))} feladotol ")


            print(f"Targy:  {subject}")


        # Save attachments
        for part in email_message.walk():
            if part.get_content_disposition() == "attachment":
                filename = part.get_filename()
                if filename:
                    filename = safe_decode_header(filename)
                    attachment_path = os.path.join(email_dir, filename)
                    with open(attachment_path, "wb") as f:
                        f.write(part.get_payload(decode=True))
                    print(f"Saved attachment: {filename}")

    try:
        # Connect to the IMAP server
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(f"tester{receiver_number}@test.com", email_pass)
        # print("Logged in successfully!")

        # Process each folder
        for folder in folders:
            # Select the folder
            status, _ = mail.select(folder)
            if status != "OK":
                print(f"Could not open folder: {folder}")
                continue

            folder_name = folder.replace("[Gmail]/", "").replace("/", "_")  # Clean up folder name
            # print(f"Processing folder: {folder_name}")

            # Search for all emails in the folder
            status, messages = mail.search(None, "ALL")
            if status != "OK":
                print(f"Could not retrieve messages from folder: {folder_name}")
                continue

            # Iterate over each email
            email_ids = messages[0].split()
            for email_id in email_ids:
                status, msg_data = mail.fetch(email_id, "(RFC822)")
                if status != "OK":
                    print(f"Could not fetch email ID: {email_id}")
                    continue

                for response_part in msg_data:
                    if isinstance(response_part, tuple):
                        # Parse the email
                        msg = email.message_from_bytes(response_part[1])
                        save_email(msg, folder_name=folder_name, email_id=email_id.decode())

        # Close the connection
        mail.logout()
        print("\n")

    except Exception as e:
        print(f"Error: {e}")
