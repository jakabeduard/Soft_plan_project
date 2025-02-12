# # This is a sample Python script.
# import json
# import threading
#
# from tester.written_by_us.monitoring import getting_server_info
# from written_by_us.create_testers import create_testers
# from written_by_us.load_server_capacity import key_listener, load_server_capacity
# from written_by_us.reset_server import cleaning_server
#
# if __name__ == '__main__':
#
#     api_key="E9A377-B0723B-53A5DC-D12E23-67E2F0"
#     host_url="https://edu.mailserver.ro"
#     host_sever="edu.mailserver.ro"
#     ssh_user="admin"
#     ssh_password="01234"
#     n = 5
#     max_paragraphs=10
#     wait_time=2
#
#
#     ###################################################################
#
#
#     result = cleaning_server(host_url, api_key)
#     print(json.dumps(result, indent=4))
#
#     ################################################
#
#
#     result = create_testers(n, host_url, api_key)
#     print(json.dumps(result, indent=4))
#
#
#     ################################################
#
#     listener_thread = threading.Thread(target=key_listener)
#     listener_thread.start()
#
#     server_load_thread = threading.Thread(target= load_server_capacity, args=(wait_time,n,max_paragraphs,host_sever))
#     server_load_thread.start()
#
#     ################################################
#     server_info_thread = threading.Thread(target=getting_server_info, args=(host_sever,ssh_user,ssh_password))
#     server_info_thread.start()
#
#     listener_thread.join()
#     server_load_thread.join()
#     server_info_thread.join()
#
import json
import threading
import tkinter as tk
from tkinter import scrolledtext, Label, Entry, Button
import sys
from io import StringIO

from tester.written_by_us.monitoring import getting_server_info
from written_by_us.create_testers import create_testers
from written_by_us.load_server_capacity import key_listener, load_server_capacity
from written_by_us.reset_server import cleaning_server

def redirect_output(output_widget):
    class StdoutRedirector(StringIO):
        def write(self, message):
            output_widget.insert(tk.END, message)
            output_widget.see(tk.END)
    return StdoutRedirector()

def start_cleaning_server():
    sys.stdout = redirect_output(cleaning_output)
    result = cleaning_server(host_url_entry.get(), api_key_entry.get())
    print(json.dumps(result, indent=4))
    sys.stdout = sys.__stdout__

def start_create_testers():
    sys.stdout = redirect_output(testers_output)
    result = create_testers(int(n_entry.get()), host_url_entry.get(), api_key_entry.get())
    print(json.dumps(result, indent=4))
    sys.stdout = sys.__stdout__

def start_key_listener():
    sys.stdout = redirect_output(key_listener_output)
    threading.Thread(target=key_listener, daemon=True).start()
    print("Key Listener started.")
    sys.stdout = sys.__stdout__

def start_load_server_capacity():
    sys.stdout = redirect_output(server_load_output)
    thread = threading.Thread(target=load_server_capacity, args=(int(wait_time_entry.get()), int(n_entry.get()), int(max_paragraphs_entry.get()), host_sever_entry.get()), daemon=True)
    thread.start()
    thread.join()
    sys.stdout = sys.__stdout__

def start_getting_server_info():
    sys.stdout = redirect_output(server_info_output)
    thread = threading.Thread(target=getting_server_info, args=(host_sever_entry.get(), ssh_user_entry.get(), ssh_password_entry.get()), daemon=True)
    thread.start()
    thread.join()
    sys.stdout = sys.__stdout__

# GUI Setup
root = tk.Tk()
root.title("Server Management Interface")

frame = tk.Frame(root)
frame.pack(pady=10)

# Input Fields
Label(frame, text="API Key:").grid(row=0, column=0)
api_key_entry = Entry(frame)
api_key_entry.grid(row=0, column=1)
api_key_entry.insert(0, "E9A377-B0723B-53A5DC-D12E23-67E2F0")

Label(frame, text="Host URL:").grid(row=1, column=0)
host_url_entry = Entry(frame)
host_url_entry.grid(row=1, column=1)
host_url_entry.insert(0, "https://edu.mailserver.ro")

Label(frame, text="Host Server:").grid(row=2, column=0)
host_sever_entry = Entry(frame)
host_sever_entry.grid(row=2, column=1)
host_sever_entry.insert(0, "edu.mailserver.ro")

Label(frame, text="SSH User:").grid(row=3, column=0)
ssh_user_entry = Entry(frame)
ssh_user_entry.grid(row=3, column=1)
ssh_user_entry.insert(0, "admin")

Label(frame, text="SSH Password:").grid(row=4, column=0)
ssh_password_entry = Entry(frame, show='*')
ssh_password_entry.grid(row=4, column=1)
ssh_password_entry.insert(0, "01234")

Label(frame, text="N:").grid(row=5, column=0)
n_entry = Entry(frame)
n_entry.grid(row=5, column=1)
n_entry.insert(0, "5")

Label(frame, text="Max Paragraphs:").grid(row=6, column=0)
max_paragraphs_entry = Entry(frame)
max_paragraphs_entry.grid(row=6, column=1)
max_paragraphs_entry.insert(0, "10")

Label(frame, text="Wait Time:").grid(row=7, column=0)
wait_time_entry = Entry(frame)
wait_time_entry.grid(row=7, column=1)
wait_time_entry.insert(0, "2")

# Buttons & Output Windows
cleaning_output = scrolledtext.ScrolledText(frame, width=80, height=5)
cleaning_output.grid(row=8, column=0, columnspan=2)
Button(frame, text="Clean Server", command=start_cleaning_server).grid(row=9, column=0, padx=5, pady=5)

testers_output = scrolledtext.ScrolledText(frame, width=80, height=5)
testers_output.grid(row=10, column=0, columnspan=2)
Button(frame, text="Create Testers", command=start_create_testers).grid(row=11, column=0, padx=5, pady=5)

key_listener_output = scrolledtext.ScrolledText(frame, width=80, height=5)
key_listener_output.grid(row=12, column=0, columnspan=2)
Button(frame, text="Start Key Listener", command=start_key_listener).grid(row=13, column=0, padx=5, pady=5)

server_load_output = scrolledtext.ScrolledText(frame, width=80, height=5)
server_load_output.grid(row=14, column=0, columnspan=2)
Button(frame, text="Load Server Capacity", command=start_load_server_capacity).grid(row=15, column=0, padx=5, pady=5)

server_info_output = scrolledtext.ScrolledText(frame, width=80, height=5)
server_info_output.grid(row=16, column=0, columnspan=2)
Button(frame, text="Get Server Info", command=start_getting_server_info).grid(row=17, column=0, padx=5, pady=5)

Button(frame, text="Exit", command=root.quit).grid(row=18, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
