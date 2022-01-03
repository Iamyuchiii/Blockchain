from brownie import accounts, network, config

local_blockchain = ["development", "ganache-local"]


def get_accounts():
    """get account based on the network
    :return: account from the correct network for deployment
    """
    # chose the account based on what network you run on
    if network.show_active() in local_blockchain:
        # return account from ganache
        return accounts[0]
    else:
        # get account from .env to run rinkeby
        return accounts.add(config["wallets"]["from_key"])
