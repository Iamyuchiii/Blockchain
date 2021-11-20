from brownie import AgriStorage, config, network
from scripts.functions import get_accounts, local_blockchain


def deploy_greenhouseStorage():
    account = get_accounts()
    # deploying contract + verifiying the contract
    # function to deceide which address to use
    greenhouse_Storage = AgriStorage.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract deployed to {greenhouse_Storage.address}")
    return greenhouse_Storage


def store_hashes(productname, rootHash):
    # get the latest deployed contract
    greenhouse_Storage = AgriStorage[-1]
    # set product name en link it to its hashes
    set_keyname = greenhouse_Storage.set_productname(productname)
    set_Hashes = greenhouse_Storage.updateLedger(rootHash)


def check_ledger():
    greenhouse_Storage = AgriStorage[-1]
    print(greenhouse_Storage.check_ledger("tomato"))


def main():
    deploy_greenhouseStorage()
    store_hashes("tomato", "AGJDHGAHJDGJHAD")
    check_ledger()
