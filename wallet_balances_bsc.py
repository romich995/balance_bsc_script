import argparse as argpr

from contract import BEP20Token

#парсинг 
prs = argpr.ArgumentParser()
prs.add_argument('--wallet', dest='wallet', required=True)
prs.add_argument('--token', dest='contract', required=True)

args = prs.parse_args()

cntrct = BEP20Token(address=args.contract) 

eth_mount = cntrct.get_balance_of(args.wallet)

print(eth_mount)
