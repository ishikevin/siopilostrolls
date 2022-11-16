from brownie import accounts, SIOPILOSTROLLS, config
from scripts.Metadata import get_metadata, save_minted
import json


account = accounts.add(config["wallets"]["from_key"])

trolls = SIOPILOSTROLLS[-1]

# minting 1500 per mint
start = 0
end = 10

with open("metadata/extracted/all.json", "r") as upload_urls:
    data = json.load(upload_urls)


def Mint_One():
    balance = trolls.balanceOf(account)
    mint_nfts = trolls.SioMint(
        account,
        {"from": account},
    )
    if mint_nfts:
        print(f"\nNFTS MINTED: \n")


def main():
    Mint_One()
