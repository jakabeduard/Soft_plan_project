import time

import keyboard
import paramiko


host="edu.mailserver.ro"
# username="admin"
# password="01234"


def set_ssh(user, pwd):
    global username, password
    username = user
    password = pwd

def set_server_host(host_edu_mailserver_ro):
    global host
    host = host_edu_mailserver_ro

def get_server_info(host, username, password):
    try:
        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=host, username=username, password=password)

        # CPU Capacity
        stdin, stdout, stderr = ssh.exec_command("lscpu | grep 'Model name\\|CPU(s)'")
        cpu_info = stdout.read().decode().strip()

        # CPU Temperature
        stdin, stdout, stderr = ssh.exec_command("sensors | grep 'Package id 0:'")
        cpu_temp = stdout.read().decode().strip()

        # Check if CPU temperature is empty, then set a fallback message
        if not cpu_temp:
            cpu_temp = "Unable to retrieve CPU temperature. Ensure 'lm-sensors' is installed and configured."

        # Memory Capacity
        stdin, stdout, stderr = ssh.exec_command("free -h")
        memory_info = stdout.read().decode().strip()

        ssh.close()

        # Return results
        return {
            "CPU Info": cpu_info,
            "CPU Temperature": cpu_temp,
            "Memory Info": memory_info
        }
    except Exception as e:
        return {"error": str(e)}



def geting_server_info():
    try:
        while True:
            # Fetch server info
            server_info = get_server_info(host, username, password)

            # Print server info
            for key, value in server_info.items():
                print(f"{key}:\n{value}\n")

            # Wait for 50 milliseconds (20 Hz rate)
            time.sleep(0.05)

            # Check for key press (stop if any key is pressed)
            if keyboard.is_pressed('q'):  # Press 'q' to stop the loop
                print("Stopping the information retrieval.")
                break
    except KeyboardInterrupt:
        print("Program interrupted.")




