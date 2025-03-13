# This is a sample Python script.
import json
import os
import re
import sys
import threading
import time
from datetime import datetime

import paramiko

from tester.written_by_us.monitoring import getting_server_info, monitor_active_threads
from written_by_us import config
from written_by_us.create_testers import create_testers
from written_by_us.imap import fetch_and_save_email
from written_by_us.load_server_capacity import  load_server_capacity

from written_by_us.reset_server import cleaning_server
from written_by_us.smtp import send_email_with_attachment

def stop_loop():
    config.running = False
    print("Leállítva.")

if __name__ == '__main__':

    sys.stdout = open("output66.txt", "w", encoding="utf-8", errors="ignore")





    api_key="E9A377-B0723B-53A5DC-D12E23-67E2F0"
    host_url="https://edu.mailserver.ro"
    host_sever="edu.mailserver.ro"
    ssh_user="admin"
    ssh_password="01234"
    n = 1000
    max_paragraphs=10
    wait_time=5
    num_threads = 120
    threads = []



    ###################################################################


    # result = cleaning_server(host_url, api_key)
    # print(json.dumps(result, indent=4))

    ################################################


    # result = create_testers(n, host_url, api_key)
    # print(json.dumps(result, indent=4))


    # ################################################


    getting_server_info_thread = threading.Thread(target=getting_server_info, args=(wait_time, host_sever, ssh_user,ssh_password))  # Módosítsd az argumentumokat a megfelelő értékekre
    getting_server_info_thread.daemon=True
    getting_server_info_thread.start()
    threads.append(getting_server_info_thread)

    # ###########################################

    active_thread_monitor = threading.Thread(target=monitor_active_threads,args=(wait_time,host_sever,ssh_user,ssh_password))
    active_thread_monitor.daemon=True
    active_thread_monitor.start()
    threads.append(active_thread_monitor)

    ###################################################

    for _ in range(num_threads):
        thread = threading.Thread(target=load_server_capacity, args=( n, max_paragraphs, host_sever))
        thread.daemon = True
        thread.start()
        threads.append(thread)

    ##############################################

    input("Nyomj le egy gombot")
    stop_loop()

    sys.stdout.close()
