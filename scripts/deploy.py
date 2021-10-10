from brownie import OToken
from scripts.utils import get_account
from brownie import config, network
from web3 import Web3

INITIAL_SUPPLY = Web3.toWei(1234567890, "ether")


def deploy_contract():
    account = get_account()
    token = OToken.deploy(
        INITIAL_SUPPLY,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    print("Deployed token!")


def main():
    deploy_contract()
