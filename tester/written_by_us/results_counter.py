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



import re
from collections import defaultdict


def group_log_by_timestamp(filename):
    patterns = {
        "too many connections": 0,
        "Email Sikeresen elkuldve": 0,
        "Email mentve": 0,
        "CPU h\u0151m\u00e9rs\u00e9klet": 0,
        "CPU terhel\u00e9s": 0
    }

    grouped_logs = defaultdict(lambda: patterns.copy())

    try:
        with open(filename, 'r', encoding='latin-1', errors='ignore') as file:
            current_timestamp = None

            for line in file:
                timestamp_match = re.match(r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3})", line)
                if timestamp_match:
                    current_timestamp = timestamp_match.group(1)

                for pattern in patterns.keys():
                    if re.search(pattern, line, re.IGNORECASE):
                        if current_timestamp:
                            grouped_logs[current_timestamp][pattern] += 1

        # Kiírás rendezett formában
        print("A fájl összesen", sum(sum(d.values()) for d in grouped_logs.values()), "sort tartalmaz.")
        for pattern in patterns.keys():
            total_count = sum(group[pattern] for group in grouped_logs.values())
            print(f"A: '{pattern}' {total_count} sorban található meg.")

        print("\nCsoportosított eredmények:")
        for timestamp, counts in sorted(grouped_logs.items()):
            print(f"{timestamp}")
            for pattern, count in counts.items():
                if count > 0:
                    print(f"    A: '{pattern}' {count} alkalommal található meg.")
            print()

    except FileNotFoundError:
        print(f"A(z) {filename} fájl nem található.")
