#!/usr/bin/python3
from brownie import Token, accounts

# if deploy on public net
# acct = accounts.load('1')

def main():
	accounts[0].deploy(Token, "Token", "TKN", 18, 1000)

	# if public on public net
	# acct.deploy(Token, "Token", "TKN", 18, 1000)
