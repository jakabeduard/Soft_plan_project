import imaplib
import smtplib
import email
from datetime import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

# #Email configuration
# smtp_server = "edu.mailserver.ro"  # Replace with your SMTP server
# smtp_port = 587  # Standard port for STARTTLS
# sender_email = "janos@edutus.mailserver.ro"
# sender_password = "012345"
# recipient_email = "janoska@edutus.mailserver.ro"
#
# # Create email content
# subject = "Test Emailke"
# body = "This is a test email sent from Pythonnnfvsdjfgnsdfjklnsdjkfgnsdfnkgsdjkfngksdfngjkadfnjksndfjksgdf."
#
# # Setting up MIME
# message = MIMEMultipart()
# message["From"] = sender_email
# message["To"] = recipient_email
# message["Subject"] = subject
# message.attach(MIMEText(body, "plain"))
#
#
# file_path = "D:/IMG_20241026_200124_7.jpg"  # Replace with the actual file path
# try:
#     with open(file_path, "rb") as attachment:
#         # Add file as application/octet-stream
#         part = MIMEBase("application", "octet-stream")
#         part.set_payload(attachment.read())
#
#     # Encode file in ASCII characters for email
#     encoders.encode_base64(part)
#
#     # Add header for file attachment
#     part.add_header(
#         "Content-Disposition",
#         f"attachment; filename={file_path.split('/')[-1]}"  # Extracts the file name
#     )
#
#     # Attach the file to the message
#     message.attach(part)
#
#     # Send the email
#     with smtplib.SMTP(smtp_server, smtp_port) as server:
#         server.starttls()  # Upgrade the connection to secure
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, recipient_email, message.as_string())
#         print("Email with attachment sent successfully!")
# except Exception as e:
#     print(f"Error: {e}")

# def set_server_host(host_edu_mailserver_ro):
#     global hostv3
#     hostv3=host_edu_mailserver_ro


def send_email_with_attachment(sender_email, recipient_email, subject, body, file_path):
    smtp_server = "edu.mailserver.ro" # Gmail SMTP server
    smtp_port = 587  # Standard port for STARTTLS
    sender_password = "0123456789"  # Use an app-specific password if 2FA is enabled

    try:
        # Create email content
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        # Attach file if path is provided
        if file_path:
            with open(file_path, "rb") as attachment:
                # Add file as application/octet-stream
                part = MIMEBase("application", "octet-stream")
                part.set_payload(attachment.read())
                encoders.encode_base64(part)

                # Add header for file attachment
                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={file_path.split('/')[-1]}"  # Extracts the file name
                )

                # Attach the file to the message
                message.attach(part)

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message.as_string())
            print("Email with attachment sent successfully!")
        # mail = imaplib.IMAP4_SSL('edu.mailserver.ro')  # Use the correct IMAP server address
        # mail.login(sender_email, sender_password)
        # mail.select('"Sent"')  # Gmail sent mail folder, adjust as per your service
        # mail.append('"Sent"', '\\Seen', imaplib.Time2Internaldate(time.time()),
        #             message.as_string().encode('utf-8'))
        # mail.logout()
        # print("Email saved to Sent folder.")

    except Exception as e:
        print(f"Error: {e}")