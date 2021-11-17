from brownie import AgriStorage, config, network
from scripts.functions import get_accounts, local_blockchain


def deploy_contract():
    account = get_accounts()
    # deploying contract + verifiying the contract
    # function to deceide which address to use
    greenhouse_Storage = AgriStorage.deploy(
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract deployed to {greenhouse_Storage.address}")
    return greenhouse_Storage


def main():
    deploy_contract()
