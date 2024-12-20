import imaplib
import email
from email.header import decode_header
import os

# Email account configuration
imap_server = "edu.mailserver.ro"  # IMAP server address (e.g., Gmail's IMAP server)
email_user = "janoska@edutus.mailserver.ro"
email_pass = "012345"

# Local directory to save emails and attachments
save_directory = r"D:\janoskaemails"  # Replace with your desired directory

# Ensure the directory exists
os.makedirs(save_directory, exist_ok=True)

# Folders to synchronize
folders = ["INBOX", "Sent", "Trash", "Junk", "Drafts","Archive" ]  # Adjust for your IMAP server

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
    # Create a folder for this email
    email_dir = os.path.join(save_directory, folder_name, f"Email-{email_id}")
    os.makedirs(email_dir, exist_ok=True)

    # Safely decode the subject
    subject = safe_decode_header(email_message.get("Subject"))
    subject = subject.replace("/", "_")  # Sanitize the subject for filenames

    # Save email body
    body_file = os.path.join(email_dir, "email.txt")
    with open(body_file, "w", encoding="utf-8") as f:
        f.write(f"Subject: {subject}\n")
        f.write(f"From: {safe_decode_header(email_message.get('From'))}\n")
        f.write(f"To: {safe_decode_header(email_message.get('To'))}\n\n")

        # Extract the email body
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

        # Write the body to the file
        f.write(body if body else "No content available")
        print(f"Saved email: {subject}")

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
    mail.login(email_user, email_pass)
    print("Logged in successfully!")

    for folder in folders:
        # Select the folder
        status, _ = mail.select(folder)
        if status != "OK":
            print(f"Could not open folder: {folder}")
            continue

        folder_name = folder.replace("[Gmail]/", "").replace("/", "_")  # Clean up folder name
        print(f"Processing folder: {folder_name}")

        # Search for all emails in the folder
        status, messages = mail.search(None, "ALL")
        if status != "OK":
            print(f"Could not retrieve messages from folder: {folder_name}")
            continue

        # Iterate over each email
        email_ids = messages[0].split()
        for email_id in email_ids:
            # Fetch the email
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
    print("Logged out successfully. All emails and attachments saved!")

except Exception as e:
    print(f"Error: {e}")