from brownie import AgriStorage, config, network
from scripts.functions import get_accounts, local_blockchain


def deploy_contract():
    """Deploying the contract to rinkeby testnet
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
    greenhouse_Storage.wait(1)
    return greenhouse_Storage


def store_hashes(productname, roothash):
    """Using the contract to store name and hashes
    :param productname: string
    :param roothash: string
    """
    # get the latest deployed contract
    greenhouse_Storage = AgriStorage[-1]
    print(f"Current contract address: {greenhouse_Storage}")
    account = get_accounts()
    # set product name en link it to its hashes
    print(f"Setting the product name as: {productname}")
    set_keyname = greenhouse_Storage.set_productname(productname, {"from": account})
    print("successful!")
    print(f"Setting the roothash as: {roothash}")
    set_Hashes = greenhouse_Storage.updateLedger(roothash, {"from": account})
    print("successful!")


def check_ledger(productname):
    """Check the ledger for correct hashes
    :param productname: string
    :return:
    """
    greenhouse_Storage = AgriStorage[-1]
    account = get_accounts()
    print(greenhouse_Storage.check_ledger(productname, {"from": account}))


def main():
    deploy_contract()
