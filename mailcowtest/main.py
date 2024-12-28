import requests
import json

# HTTP fejlécek az autentikációhoz
headers = {
    "X-API-Key": "E9A377-B0723B-53A5DC-D12E23-67E2F0",
    "Content-Type": "application/json"
}

# working
URL_GET_ALL_MAILBOX = "https://edu.mailserver.ro/api/v1/get/mailbox/all"
URL_POST_CREATE_MAILBOX ="https://edu.mailserver.ro/api/v1/add/mailbox"

# try
URL_GET_MAILBOX = "https://edu.mailserver.ro/api/v1/get/mailbox/{mailbox_id}"
URL_PUT_UPDATE_MAILBOX = "https://edu.mailserver.ro/api/v1/update/mailbox/{mailbox_id}"
URL_DELETE_MAILBOX = "https://edu.mailserver.ro/api/v1/delete/mailbox/{mailbox_id}"
URL_GET_MAILBOX_USAGE = "https://edu.mailserver.ro/api/v1/get/mailbox/usage/{mailbox_id}"
URL_POST_UPDATE_MAILBOX_STATUS = "https://edu.mailserver.ro/api/v1/update/mailbox/status"
URL_GET_SEARCH_MAILBOXES = "https://edu.mailserver.ro/api/v1/search/mailbox?query={query}"
URL_POST_RESET_MAILBOX_PASSWORD = "https://edu.mailserver.ro/api/v1/mailbox/reset-password"
URL_GET_DOMAINS = "https://edu.mailserver.ro/api/v1/get/domains"
URL_GET_MAILBOX_LOGS = "https://edu.mailserver.ro/api/v1/logs/mailbox/{mailbox_id}"

# Data to send in the request body
user_data = {
    "username": "newuser2@example.com",
    "password": "strongpassword",
    "quota": 1024000000  # Example quota size in bytes
}

# working
def create_mailbox():
    try:
        response = requests.post(URL_POST_CREATE_MAILBOX, json=user_data, headers=headers, verify=False) # Send POST request
        response.raise_for_status() # Check for HTTP request errors
        response_data = response.json() # Print the JSON response
        return response_data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_mailbox_all():
    try:
        response = requests.get(URL_GET_ALL_MAILBOX, headers=headers, verify=False)
        response.raise_for_status()
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# try
# fetch details of a single mailbox
def get_mailbox(mailbox_id):
    try:
        response = requests.get(URL_GET_MAILBOX, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# update mailbox settings and data
def update_mailbox(mailbox_id, updates):
    try:
        response = requests.put(URL_PUT_UPDATE_MAILBOX, json=updates, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# remove mailboxes that are no longer needed
def delete_mailbox(mailbox_id):
    try:
        response = requests.delete(URL_DELETE_MAILBOX, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# storage statistics for a mailbox
def get_mailbox_usage(mailbox_id):
    try:
        response = requests.get(URL_GET_MAILBOX_USAGE, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# temporarily suspend a mailbox for inactive users, reactivate a mailbox
def update_mailbox_status(mailbox_id, status):
    try:
        data = {"mailbox_id": mailbox_id, "status": status}
        response = requests.post(URL_POST_UPDATE_MAILBOX_STATUS, json=data, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# search mailboxes by username, domain or other criterias - look up mailboxes with partial matches
def search_mailboxes(query):
    try:
        response = requests.get(URL_GET_SEARCH_MAILBOXES, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# to allow admins to reset forgotten passwords for users
def reset_mailbox_password(mailbox_id, new_password):
    try:
        data = {"mailbox_id": mailbox_id, "new_password": new_password}
        response = requests.post(URL_POST_RESET_MAILBOX_PASSWORD, json=data, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# fetch all domains associated with the mail server to manage domain-specific mailboxes
def get_domains():
    try:
        response = requests.get(URL_GET_DOMAINS, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

# fetch activity logs for a specific mailbox to monitor activity or investigate issues
def get_mailbox_logs(mailbox_id):
    try:
        response = requests.get(URL_GET_MAILBOX_LOGS, headers=headers, verify=False)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    # working
    result = get_mailbox_all()
    # result = create_mailbox()

    # try
    # result = update_mailbox()
    # result = get_mailbox(1)
    # result = delete_mailbox(1)
    # result = get_mailbox_usage(1)
    # result = search_mailboxes()
    # result = reset_mailbox_password()
    # result = get_domains()
    # result = get_mailbox_logs(1)

    print(json.dumps(result, indent=4))