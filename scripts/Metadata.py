import json

with open("metadata/extracted/all.json", "r") as upload_urls:
    data = json.load(upload_urls)


def get_metadata(start, end):
    for limit in range(int(start), int(end)):
        all = data[limit]
        metadata_name = all["metadata_name"]
        metadata_url = all["metadata_url"]
        save_minted(metadata_name)


def save_minted(metadata_name, metadata_url):
    with open("metadata/minted/minted.txt", "a") as upload_urls:
        data = upload_urls.write(str(metadata_name) + "\n")


def main():
    get_metadata(0, 10)
