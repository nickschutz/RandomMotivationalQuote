import requests

SERVICE_URL = "http://127.0.0.1:5000/get-quote"


def test_get_quote():
    try:
        response = requests.get(SERVICE_URL)
        if response.status_code == 200:
            data = response.json()
            print(f"Random Quote: {data['quote']}")
        else:
            print(f"Failed to fetch quote. Status code: {response.status_code}")
    except requests.exceptions.RequestExceptions as e:
        print(f"Error connecting to the service: {e}")
    

    if __name__ == "__main__":
        test_get_quote()
        