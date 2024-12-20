import requests
import json

# HTTP fejlécek az autentikációhoz
headers = {
    "X-API-Key": "E9A377-B0723B-53A5DC-D12E23-67E2F0",
    "Content-Type": "application/json"
}

URL_GET_ALL_MAILBOX = "https://edu.mailserver.ro/api/v1/get/mailbox/all"
URL_POST_CREATE_MAILBOX ="https://edu.mailserver.ro/api/v1/add/mailbox"

# Data to send in the request body
user_data = {
    "username": "newuser2@example.com",
    "password": "strongpassword",
    "quota": 1024000000  # Example quota size in bytes
}
# dsdfk
def create_mailbox():
    try:

        # Send POST request
        response = requests.post(URL_POST_CREATE_MAILBOX, json=user_data, headers=headers, verify=False)

        # Check for HTTP request errors
        response.raise_for_status()

        # Print the JSON response
        response_data = response.json()

        return response_data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

def get_mailbox_all():
    try:
        response = requests.get(URL_GET_ALL_MAILBOX, headers=headers, verify=False)

        # Check for HTTP request errors
        response.raise_for_status()

        # Print the JSON response
        data = response.json()

        return data

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":

    result = get_mailbox_all()
    
    # result = create_mailbox()

    print(json.dumps(result, indent=4))