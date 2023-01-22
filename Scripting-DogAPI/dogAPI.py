import requests
import argparse

# Define the command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--breed", type=str, required=True, help="breed name")
parser.add_argument("--list", action="store_true", help="if set, returns list of sub-breeds")
parser.add_argument("--count", action="store_true", help="if set, returns count of sub-breeds")
parser.add_argument("--image", action="store_true", help="if set, downloads a random image of the breed")
args = parser.parse_args()

# Build the API request
userBreed = args.breed
listAll_URL = "https://dog.ceo/api/breeds/list/all"

# Send the request and get the response
response = requests.get(listAll_URL)
dogList = response.json()
# Print the response
print(response)

# Involve user breed input to API
subList_URL = "https://dog.ceo/api/breed/" + userBreed + "/list"
subBreed_response = requests.get(subList_URL)
subBreed_print = subBreed_response.json()

# Check ARGS
if args.list:
    if len(subBreed_print['message'][userBreed]) == 0:
        print("No sub breeds.")
    else:
        print(subBreed_print['message'][userBreed])
if args.count:
    print(len(subBreed_print['message'][userBreed]))
if args.image:
    subImage_url = "https://dog.ceo/api/breed/" + userBreed + "/images/random"
    subImage_response = requests.get(subImage_url)
    subImage_link = subImage_response.json()
    download_url = subImage_link['message']
    download_link = requests.get(download_url, allow_redirects=True)
    open("randomDog.jpg", "wb").write(download_link.content)
