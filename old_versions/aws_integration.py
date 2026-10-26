
import urllib.request
import json

API_URL = "https://qpu8w7bxn9.execute-api.ap-southeast-2.amazonaws.com/status"


def check_cloud_status():
    try:
        request = urllib.request.Request(
            API_URL,
            headers={"Accept": "application/json"},
            method="GET"
        )

        with urllib.request.urlopen(request, timeout=10) as response:
            data = json.loads(response.read().decode("utf-8"))

        if data.get("status") == "online":
            return data.get(
                "message",
                "Floki cloud connection successful!"
            )

        return "Floki received an unexpected cloud response."

    except Exception as error:
        print(f"AWS connection error: {error}")
        return "Sorry, I could not connect to the Floki cloud service."


if __name__ == "__main__":
    print(check_cloud_status())
