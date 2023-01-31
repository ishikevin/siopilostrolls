from brownie import accounts, SIOPILOSTROLLS, config
from scripts.Metadata import get_metadata, save_minted
import json


account = accounts.add(config["wallets"]["from_key"])

trolls = SIOPILOSTROLLS[-1]

# minting 1500 per mint
start = 601
end = 700

with open("metadata/extracted/all.json", "r") as upload_urls:
    data = json.load(upload_urls)


def Mint():
    balance = trolls.balanceOf(account)
    for limit in range(int(start), int(end)):
        all = data[limit]
        metadata_name = all["metadata_name"]
        metadata_url = all["metadata_url"]
        mint_nfts = trolls.SioMint(account, metadata_url, {"from": account})
        save_minted(metadata_name, metadata_url)
        if mint_nfts:
            print(f"\nNFTS MINTED: {metadata_name}\n")


def main():
    Mint()
