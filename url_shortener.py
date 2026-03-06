import hashlib
import json
import os

DB_FILE = "url_db.json"

# Load database
if os.path.exists(DB_FILE):
    with open(DB_FILE, "r") as file:
        url_db = json.load(file)
else:
    url_db = {}


def shorten_url(long_url):
    # create hash
    hash_object = hashlib.md5(long_url.encode())
    short_code = hash_object.hexdigest()[:6]

    url_db[short_code] = long_url

    with open(DB_FILE, "w") as file:
        json.dump(url_db, file)

    return short_code


def get_original_url(short_code):
    return url_db.get(short_code, "URL not found")


while True:
    print("\n1. Shorten URL")
    print("2. Retrieve URL")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        long_url = input("Enter long URL: ")
        short_code = shorten_url(long_url)
        print("Short URL: http://short.ly/" + short_code)

    elif choice == "2":
        code = input("Enter short code: ")
        print("Original URL:", get_original_url(code))

    elif choice == "3":
        break