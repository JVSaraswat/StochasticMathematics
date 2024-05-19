import requests
import json


def get_users():
    api_url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            users = response.json()

            # Display information about each user
            for user in users:
                print(f"User ID: {user['id']}")
                print(f"Name: {user['name']}")
                print(f"Email: {user['email']}")
                print("---------------------------")

            # Store the user data as a JSON file
            save_as_json(users)

        else:
            print(f"Error: {response.status_code}")

    except requests.RequestException as e:
        print(f"Request Exception: {e}")


def save_as_json(data):
    # Save the data as a JSON file
    with open("user_data.json", "w") as json_file:
        json.dump(data, json_file, indent=2)
        print("User data saved as 'user_data.json'")


# Call the function to get and display the list of users and save as JSON
get_users()
