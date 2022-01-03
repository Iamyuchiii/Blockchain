from sys import argv
from brownie import AgriStorage, config, network
from brownie.network import account
from scripts.functions import get_accounts, local_blockchain


def deploy_greenhouseStorage():
    """Deploying the contract to local ganache network
    :return: contract object
    """
    account = get_accounts()
    # deploying contract + verifiying the contract
    # function to deceide which address to use
    greenhouse_Storage = AgriStorage.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract deployed to {greenhouse_Storage.address}")
    return greenhouse_Storage


def store_hashes(productname, roothash):
    # get the latest deployed contract
    greenhouse_Storage = AgriStorage[-1]
    account = get_accounts()
    # set product name en link it to its hashes
    set_keyname = greenhouse_Storage.set_productname(productname, {"from": account})
    set_keyname.wait(1)
    set_Hashes = greenhouse_Storage.updateLedger(roothash, {"from": account})
    set_Hashes.wait(1)


def check_ledger(productname):
    greenhouse_Storage = AgriStorage[-1]
    account = get_accounts()
    print(greenhouse_Storage.check_ledger(productname, {"from": account}))


def main():
    deploy_greenhouseStorage()
    store_hashes("tomato", "ahsgdjhagsd")
