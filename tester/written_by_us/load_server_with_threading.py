from datetime import time

from written_by_us.imap import fetch_and_save_email
from written_by_us.random_generator import random_number
from written_by_us.smtp import send_email_with_attachment

stop_thread = False
def threading_stress_test_server(time_to_wait_s, n_emails,max_paragraphs,host_sever):
    while not stop_thread:
        time.sleep(time_to_wait_s)
        # print(f"{time_to_wait_s} másodperc eltelt!")
        activ_emails = random_number(1, int(n_emails))
        print(f"{activ_emails}- aktiv emailek")

        # Meghívok max n/2 email felhasználót, hogy küldjenek emailt a másik n/2-nek
        for i in range(activ_emails):  # n/2-től fut a ciklus
            # print("Üdvözöllek!")
            # kuldok szama
            sender_num = random_number(0, n_emails)
            print(f"          {sender_num}- sender emailek")
            # fogadok szama
            receiver_num = random_number(0, n_emails)
            print(f"                      {receiver_num}- resiver emailek")

            if (sender_num == receiver_num): continue

            send_email_with_attachment(sender_num, receiver_num, max_paragraphs, host_sever)

            fetch_and_save_email(receiver_num, host_sever)





