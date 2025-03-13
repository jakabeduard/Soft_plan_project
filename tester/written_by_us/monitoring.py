import psutil
import subprocess
import time

import keyboard
import paramiko
import re
import paramiko

stop_thread = False
def key_listener():
    global stop_thread
    input("Nyomj meg egy billentyűt a leállításhoz...\n")
    stop_thread = True

def getting_server_info( time_to_wait_s, hostname, username, password):
    while not stop_thread:
        # print("Végtelen ciklus fut...")
        time.sleep(time_to_wait_s)

        # result=get_remote_system_stats(hostname, username, password)
        # print(result)
        # result2=get_htop_output(hostname, username, password)
        # print(result2)
        result2=get_system_stats_and_htop_output(hostname, username, password)
        print(result2)

# def get_remote_system_stats(hostname, username, password):
#     try:
#         # SSH kapcsolat létrehozása
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect(hostname, username=username, password=password)
#
#         # A szkript futtatása a távoli gépen
#         stdin, stdout, stderr = ssh.exec_command("python3 -c 'import psutil; import subprocess; print(psutil.cpu_percent(interval=1, percpu=True)); print(psutil.getloadavg()); print(subprocess.check_output([\"sensors\"], text=True))'")
#
#         # Az eredmények kiolvasása
#         output = stdout.read().decode().splitlines()
#         cpu_percent = eval(output[0])
#         cpu_load_avg = eval(output[1])
#         sensors_output = "\n".join(output[2:])  # A teljes sensors kimenet
#
#         # CPU és adapter hőmérséklet kinyerése
#         cpu_temp = "Hőmérséklet információ nem elérhető"
#         adapter_temp = "Hőmérséklet információ nem elérhető"
#         cpu_section = False
#         adapter_section = False
#
#         for line in sensors_output.splitlines():
#             if "cpu_thermal-virtual-0" in line:
#                 cpu_section = True
#                 adapter_section = False
#             elif "rp1_adc-isa-0000" in line:
#                 cpu_section = False
#                 adapter_section = True
#
#             if cpu_section and "temp1" in line:
#                 cpu_temp = line.split()[1]
#             if adapter_section and "temp1" in line:
#                 adapter_temp = line.split()[1]
#
#         # Eredmények összeállítása
#         # stats = {
#         #     "CPU terhelés (magonként) %-ban": cpu_percent,
#         #     "CPU terhelés (átlag)": cpu_load_avg,
#         #     "CPU hőmérséklet": cpu_temp,
#         #     "Adapter hőmérséklet": adapter_temp,
#         # }
#         print(f"CPU hőmérséklet:{cpu_temp}, Adapter hőmérséklet:{adapter_temp}\nCPU terhelés (magonként) %-ban: {cpu_percent}\nCPU terhelés (átlag): {cpu_load_avg} ")
#
#         # return stats
#
#     except Exception as e:
#         return f"Hiba történt: {e}"
#     finally:
#         ssh.close()
#
#
#
#
# def get_htop_output(host, username, password):
#     try:
#         # Create SSH client
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#
#         # Connect to the server
#         ssh.connect(host, username=username, password=password)
#
#         # Execute the 'top' command with -b and -n 1 flags
#         stdin, stdout, stderr = ssh.exec_command("top -b -n 1")
#
#         # Read the output
#         output = stdout.read().decode()
#         # cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
#         # cpu_load_avg = psutil.getloadavg()
#
#         # Process and annotate relevant lines
#         annotated_output = []
#         in_table = False
#         for line in output.splitlines():
#             # if line.startswith("top -"):
#             #     annotated_output.append(f"Rendszer állapot: {line}")
#             # elif line.startswith("Tasks:"):
#             #     annotated_output.append(f"Feladatok állapota: {line}")
#             if line.startswith("%Cpu(s):"):
#                 annotated_output.append(f"CPU használat: {line}")
#             elif line.startswith("MiB Mem :"):
#                 annotated_output.append(f"Memória használat: {line}")
#             elif line.startswith("MiB Swap:"):
#                 annotated_output.append(f"Swap memória állapot: {line}")
#             # elif line.strip().startswith("PID"):
#             #     in_table = True
#             #     annotated_output.append("Folyamatok:")
#             #     annotated_output.append(line)
#             # elif in_table:
#             #     annotated_output.append(line)
#
#         # Print annotated output
#         print("\n".join(annotated_output))
#
#     except Exception as e:
#         print(f"Hiba történt: {e}")
#     finally:
#         # Close the connection
#         ssh.close()
#

#
#

#
# def get_system_stats_and_htop_output(host, username, password):
#     try:
#         # Create SSH client
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect(host, username=username, password=password)
#
#         # Execute the remote script to get system stats
#         stdin, stdout, stderr = ssh.exec_command(
#             "python3 -c 'import psutil; import subprocess; print(psutil.cpu_percent(interval=1, percpu=True)); print(psutil.getloadavg()); print(subprocess.check_output([\"sensors\"], text=True))'")
#
#         # Read and process the output
#         output = stdout.read().decode().splitlines()
#         cpu_percent = eval(output[0])
#         cpu_load_avg = eval(output[1])
#         sensors_output = "\n".join(output[2:])
#
#         # Extract CPU and adapter temperatures
#         cpu_temp = "Hőmérséklet információ nem elérhető"
#         adapter_temp = "Hőmérséklet információ nem elérhető"
#         cpu_section = False
#         adapter_section = False
#
#         for line in sensors_output.splitlines():
#             if "cpu_thermal-virtual-0" in line:
#                 cpu_section = True
#                 adapter_section = False
#             elif "rp1_adc-isa-0000" in line:
#                 cpu_section = False
#                 adapter_section = True
#
#             if cpu_section and "temp1" in line:
#                 cpu_temp = line.split()[1]
#             if adapter_section and "temp1" in line:
#                 adapter_temp = line.split()[1]
#
#         # Display system stats
#         print(f"CPU hőmérséklet: {cpu_temp}, Adapter hőmérséklet: {adapter_temp}")
#         print(f"CPU terhelés (magonként) %-ban: {cpu_percent}")
#         print(f"CPU terhelés (átlag): {cpu_load_avg}")
#
#         # Execute the 'top' command with -b and -n 1 flags
#         stdin, stdout, stderr = ssh.exec_command("top -b -n 1")
#
#         # Read the output
#         output = stdout.read().decode()
#
#         # Process and annotate relevant lines
#         annotated_output = []# kerlek ezt is  rakd  be az elozo for ciklusba  es   toltsed  bele a z eredmenyeket  egy tommbe es ugyan  ugy irasd ki mint az elozo  for ciklus eredmenyeit
#         for line in output.splitlines():
#             if line.startswith("%Cpu(s):"):
#                 annotated_output.append(f"CPU használat: {line}")
#             elif line.startswith("MiB Mem :"):
#                 annotated_output.append(f"Memória használat: {line}")
#             elif line.startswith("MiB Swap:"):
#                 annotated_output.append(f"Swap memória állapot: {line}")
#
#         # Print annotated output
#         print("\n".join(annotated_output))
#
#     except Exception as e:
#         print(f"Hiba történt: {e}")
#     finally:
#         # Close the connection
#         ssh.close()

#
# def get_system_stats_and_htop_output(host, username, password):
#     try:
#         # Create SSH client
#         ssh = paramiko.SSHClient()
#         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#         ssh.connect(host, username=username, password=password)
#
#         # Execute the remote script to get system stats
#         stdin, stdout, stderr = ssh.exec_command(
#             "python3 -c 'import psutil; import subprocess; "
#             "print(psutil.cpu_percent(interval=1, percpu=True)); "
#             "print(psutil.getloadavg()); "
#             "print(subprocess.check_output([\"sensors\"], text=True))'"
#         )
#
#         # Read and process the output
#         output = stdout.read().decode().splitlines()
#         cpu_percent = eval(output[0])
#         cpu_load_avg = eval(output[1])
#         sensors_output = "\n".join(output[2:])
#
#         # Extract CPU and adapter temperatures
#         cpu_temp = "Hőmérséklet információ nem elérhető"
#         adapter_temp = "Hőmérséklet információ nem elérhető"
#         cpu_section = False
#         adapter_section = False
#
#         annotated_output = []
#
#         # Execute the 'top' command with -b and -n 1 flags
#         stdin, stdout, stderr = ssh.exec_command("top -b -n 1")
#         top_output = stdout.read().decode()
#
#         for line in sensors_output.splitlines() + top_output.splitlines():
#             if "cpu_thermal-virtual-0" in line:
#                 cpu_section = True
#                 adapter_section = False
#             elif "rp1_adc-isa-0000" in line:
#                 cpu_section = False
#                 adapter_section = True
#
#             if cpu_section and "temp1" in line:
#                 cpu_temp = line.split()[1]
#             if adapter_section and "temp1" in line:
#                 adapter_temp = line.split()[1]
#
#             if line.startswith("%Cpu(s):"):
#                 annotated_output.append(f"CPU használat: {line}")
#             elif line.startswith("MiB Mem :"):
#                 annotated_output.append(f"Memória használat: {line}")
#             elif line.startswith("MiB Swap:"):
#                 annotated_output.append(f"Swap memória állapot: {line}")
#
#         # Print annotated output
#         print("\n".join(annotated_output))# ezt  ugy ird ki mint a kovetkezoket
#
#         # Display system stats
#         print(f"CPU hőmérséklet: {cpu_temp}, Adapter hőmérséklet: {adapter_temp}")#  pl itt ezek ( kulon valotozban statikusan
#
#         print(f"CPU terhelés (magonként) %-ban: {cpu_percent}")
#         print(f"CPU terhelés (átlag): {cpu_load_avg}")
#
#     except Exception as e:
#         print(f"Hiba történt: {e}")
#     finally:
#         # Close the connection
#         ssh.close()

def get_system_stats_and_htop_output(host, username, password):
    try:
        # Create SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, username=username, password=password)

        # Execute the remote script to get system stats
        stdin, stdout, stderr = ssh.exec_command(
            "python3 -c 'import psutil; import subprocess; "
            "print(psutil.cpu_percent(interval=1, percpu=True)); "
            "print(psutil.getloadavg()); "
            "print(subprocess.check_output([\"sensors\"], text=True))'"
        )

        # Read and process the output
        output = stdout.read().decode().splitlines()
        cpu_percent = eval(output[0])
        cpu_load_avg = eval(output[1])
        sensors_output = "\n".join(output[2:])

        # Extract CPU and adapter temperatures
        cpu_temp = "Hőmérséklet információ nem elérhető"
        adapter_temp = "Hőmérséklet információ nem elérhető"
        cpu_section = False
        adapter_section = False

        # Execute the 'top' command with -b and -n 1 flags
        stdin, stdout, stderr = ssh.exec_command("top -b -n 1")
        top_output = stdout.read().decode()

        # Annotated output list
        annotated_output = []

        for line in sensors_output.splitlines() + top_output.splitlines():
            if "cpu_thermal-virtual-0" in line:
                cpu_section = True
                adapter_section = False
            elif "rp1_adc-isa-0000" in line:
                cpu_section = False
                adapter_section = True

            if cpu_section and "temp1" in line:
                cpu_temp = line.split()[1]
            if adapter_section and "temp1" in line:
                adapter_temp = line.split()[1]

            if line.startswith("%Cpu(s):"):
                annotated_output.append(f"CPU használat: {line}")
            elif line.startswith("MiB Mem :"):
                annotated_output.append(f"Memória használat: {line}")
            elif line.startswith("MiB Swap:"):
                annotated_output.append(f"Swap memória állapot: {line}")

        # Static variable outputs
        cpu_temp_output = f"CPU hőmérséklet: {cpu_temp}"
        adapter_temp_output = f"Adapter hőmérséklet: {adapter_temp}"
        cpu_usage_output = f"CPU terhelés (magonként) %-ban: {cpu_percent}"
        # cpu_avg_load_output = f"CPU terhelés (átlag): {cpu_load_avg}"

        # Print outputs
        print(cpu_temp_output)
        print(adapter_temp_output)
        print(cpu_usage_output)
        # print(cpu_avg_load_output)
        print("\n".join(annotated_output))

    except Exception as e:
        print(f"Hiba történt: {e}")
    finally:
        # Close the connection
        ssh.close()
