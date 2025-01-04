import json

def extract_domain_names(input_file):
    try:
        # Read the input JSON file
        with open(input_file, 'r') as file:
            data = json.load(file)

        # Extract domain names from the 'domain_name' field
        domain_names = [entry['domain_name'] for entry in data if 'domain_name' in entry]

        # Write the extracted domain names to the output file
        with open('../output.json', 'w') as file:
            json.dump(domain_names, file, indent=2)

        # Print the content of the output file
        print(json.dumps(domain_names, indent=2))

        return 'output.json'

    except FileNotFoundError:
        print(f"The file '{input_file}' was not found.")
    except json.JSONDecodeError:
        print("Error occurred while decoding JSON.")



# def extract_email_addresses(input_file):
#     try:
#         # Beolvassa az input JSON fájlt
#         with open(input_file, 'r') as file:
#             data = json.load(file)
#
#         # Kinyeri az email címeket a 'username' mezőből
#         email_addresses = [entry['username'] for entry in data if 'username' in entry]
#
#         # Kiírja az email címeket egy új fájlba
#         with open('../email_addresses.json', 'w') as file:
#             json.dump(email_addresses, file, indent=2)
#
#         # Kiírja az email címeket a konzolra
#         print(json.dumps(email_addresses, indent=2))
#
#         return 'email_addresses.json'
#
#     except FileNotFoundError:
#         print(f"The file '{input_file}' was not found.")
#     except json.JSONDecodeError:
#         print("Error occurred while decoding JSON.")

def extract_email_addresses(mailboxes):
    try:
        # Kinyeri az email címeket a 'username' mezőből
        email_addresses = [entry['username'] for entry in mailboxes if 'username' in entry]

        # Kiírja az email címeket egy új fájlba
        with open('../email_addresses.json', 'w') as file:
            json.dump(email_addresses, file, indent=2)

        # Kiírja az email címeket a konzolra
        print(json.dumps(email_addresses, indent=2))

        return 'email_addresses.json'

    except json.JSONDecodeError:
        print("Error occurred while decoding JSON.")