import requests
from datetime import datetime

API_URL = "https://api.chucknorris.io/jokes/random"

def get_random_joke():
    try:
        r = requests.get(API_URL, timeout=10)
        status = r.status_code

        if status != 200:
            print(f"API error - status code: {status}")
            print("Response:", r.text)
            return

        data = r.json()

        joke = data.get("value", "No joke found.")
        category = data.get("categories", [])
        joke_id = data.get("id", "")
        created_at = data.get("created_at", "")

        print("===================================")
        print("Chuck Norris API - Random Joke")
        print("===================================")
        print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Status: {status}")
        print(f"ID: {joke_id}")
        print(f"Created at: {created_at}")
        print(f"Category: {category if category else 'none'}")
        print("-----------------------------------")
        print(joke)
        print("===================================")

    except requests.exceptions.Timeout:
        print("Timeout: the API did not respond in time.")
    except requests.exceptions.RequestException as e:
        print("Request error:", e)
    except ValueError:
        print("Error: response is not valid JSON.")

if __name__ == "__main__":
    get_random_joke()
