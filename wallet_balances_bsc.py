import argparse as argpr
import json

from contract import BSCContract


# загрузка abi
with open('./custom_abi.json') as fp:
    abi = json.load(fp)


#парсинг 
prs = argpr.ArgumentParser()
prs.add_argument('--wallet', dest='wallet', required=True)
prs.add_argument('--token', dest='contract', required=True)

args = prs.parse_args()

cntrct = BSCContract(address=args.contract, ABI=abi) 

eth_mount = cntrct.get_balance_of(args.wallet)

print(eth_mount)
