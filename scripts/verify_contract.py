from brownie import accounts, SIOPILOSTROLLS, config
from scripts.Metadata import get_metadata, save_minted
import json


account = accounts.add(config["wallets"]["from_key"])

trolls = SIOPILOSTROLLS[-1]

def verify():
    token = trolls.at("0x34F3f1118fD2bf7E0f933a24c5377eD765331701")
    trolls.publish_source(token)


def main():
    verify()
