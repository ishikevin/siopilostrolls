from brownie import accounts, config, SIOPILOSTROLLS

minted = []
start = 1
end = 5


def Deploy_Nfts():
    account = accounts.add(config["wallets"]["from_key"])
    NFTS = SIOPILOSTROLLS.deploy({"from": account})
    if NFTS:
        print("Contract successfully Deployed\n")


def main():
    Deploy_Nfts()
