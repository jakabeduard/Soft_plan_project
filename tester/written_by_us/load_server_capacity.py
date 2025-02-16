import msvcrt
import time

# from written_by_us.get_and_send_emails import receive_n_per_2_email
from written_by_us.imap import fetch_and_save_email
from written_by_us.random_generator import random_number
from written_by_us.smtp import send_email_with_attachment

stop_thread = False
def key_listener():
    global stop_thread
    input("Nyomj meg egy billentyűt a leállításhoz...\n")
    stop_thread = True

def load_server_capacity(time_to_wait_s, n_emails,max_paragraphs,host_sever):
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
            #fogadok szama
            receiver_num=random_number(0,n_emails)
            print(f"                      {receiver_num}- resiver emailek")

            if(sender_num==receiver_num):continue

            send_email_with_attachment(sender_num, receiver_num, max_paragraphs, host_sever)

            fetch_and_save_email(receiver_num, host_sever)
