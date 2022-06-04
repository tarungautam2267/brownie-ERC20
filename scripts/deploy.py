from re import L
from brownie import MyToken
from scripts.helpful_scripts import get_account
from web3 import Web3
initial_supply = Web3.toWei(10000,"ether")
def deploy_token():
    account=get_account()
    my_token = MyToken.deploy(initial_supply, {"from":account})
    print(my_token.name())

def main():
    deploy_token()