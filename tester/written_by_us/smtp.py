
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

from written_by_us.random_generator import random_sentence, generate_paragraphs


def send_email_with_attachment(sender_number,receiver_number,  maxparagraphs, host_sever):
    smtp_server = host_sever # Gmail SMTP server
    smtp_port = 587  # Standard port for STARTTLS
    sender_password = "9876543210"  # Use an app-specific password if 2FA is enabled
    file_path = "D:/IMG_20241026_200124_7.jpg"
    try:
        # Create email content

        message = MIMEMultipart()
        message["From"] = f"tester{sender_number}@test.com"
        message["To"] = f"tester{receiver_number}@test.com"
        message["Subject"] = random_sentence()
        message.attach(MIMEText(generate_paragraphs(maxparagraphs), "plain"))

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
            server.login(f"tester{sender_number}@test.com", sender_password)
            server.sendmail(f"tester{sender_number}@test.com", f"tester{receiver_number}@test.com" , message.as_string())
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