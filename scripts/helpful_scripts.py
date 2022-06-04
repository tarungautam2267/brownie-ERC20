from brownie import network, config, accounts
FORKED_LOCAL_ENVIRONMENT = ["mainnet-fork"]
LOCAL_BLOCKCHAIN_ENVIRONMENT = ["development", "ganache-local"]

def get_account():
    if (network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENT or network.show_active() in FORKED_LOCAL_ENVIRONMENT):
        account = accounts[0]
        return account
    else:
        return accounts.add(config["wallets"]["from_key"])