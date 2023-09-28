import requests

url = "https://api.telegram.org/bot6691394722:AAEz0yMN644dj3Qp4GAsmKSuqmy0UWwNidQ/sendPhoto"

payload = {
    "photo": open("sdcrad/Download/HD-wallpaper-tokyo-ghoul-kaneki-kaneki-ken-tokio-tokyo-ghoul-thumbnail.jpg",'rb'),
    "caption": "abi",
    "disable_notification": False,
    "reply_to_message_id": None,
    "chat_id": ""
}
headers = {
    "accept": "application/json",
    "User-Agent": "aBi",
    "content-type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)
