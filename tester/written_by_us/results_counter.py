import re


def count_errors_in_log(log_text):
    errors = {
        "too_many_connections": 0,
        # "none_lines": 0,
        # "high_threads": 0,
        "high_cpu_temp": 0,
        # "high_cpu_usage": 0
    }

    lines = log_text.split("\n")

    for line in lines:
        # 1. "Too many connections" hibák számlálása
        if "Error: (421, b'4.7.0 edu.mailserver.ro Error: too many connections" in line:
            errors["too_many_connections"] += 1

        # # 2. "None" előfordulások
        # if line.strip() == "None":
        #     errors["none_lines"] += 1
        #
        # # 3. Aktív szálak számának figyelése
        # thread_match = re.search(r"Aktív szálak száma: (\d+)", line)
        # if thread_match:
        #     thread_count = int(thread_match.group(1))
        #     if thread_count > 1150 or thread_count < 1100:  # Példa: ha extrém érték
        #         errors["high_threads"] += 1
        #
        # # 4. CPU hőmérséklet figyelése
        temp_match = re.search(r"CPU hőmérséklet: \+(\d+\.\d+)°C", line)
        if temp_match and float(temp_match.group(1)) > 40.0:
            errors["high_cpu_temp"] += 1

        # # 5. CPU magas használata
        # cpu_match = re.search(r"%Cpu\(s\):\s+(\d+\.\d+)\s+us", line)
        # if cpu_match and float(cpu_match.group(1)) > 80.0:
        #     errors["high_cpu_usage"] += 1

    return errors


def find_text_in_file(filename):
    patterns = [
        "too many connections",
        "Email Sikeresen elkuldve",
        "Email mentve",
        "CPU homerseklet",
        "CPU terheles"
    ]

    try:
        with open(filename, 'r', encoding='latin-1', errors='ignore') as file:
            lines = file.readlines()

            print(f"A fájl {len(lines)} sort tartalmaz.")

            for pattern in patterns:
                matching_lines = [line.strip() for line in lines if
                                  re.search(pattern.strip(), line.strip(), re.IGNORECASE)]
                print(f"A: '{pattern}' {len(matching_lines)} sorban található meg.")

                if not matching_lines:
                    print("Nincsenek találatok.")


    except FileNotFoundError:
        print(f"A(z) {filename} fájl nem található.")



