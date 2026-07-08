import requests
def fetch_and_display_users(num_users):
    url = "https://jsonplaceholder.typicode.com/users"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Error: HTTP Status Code {response.status_code}")
            return None
        users = response.json()
        for user in users[:num_users]:
            try:
                print(f"Name: {user['name']}")
                print(f"Email: {user['email']}")
                print(f"City: {user['address']['city']}")
                print()
            except KeyError:
                print("Error: Missing expected data in JSON response.")
                return None
    except requests.exceptions.RequestException as error:
        print(f"Network Error: {error}")
        return None
#Example calls
print("First 4 Users")
fetch_and_display_users(4)

print("\nFirst 16 Users")
fetch_and_display_users(16)