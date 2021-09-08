# class AbstractContract is a template for any 
# EVM based contract and initializing with contract address and ABI.
# Address and ABI can be found on blockchain explorer sush as https://etherscan.io

from abc import ABC
from web3 import Web3



# Binance Smart Chain http node provider
BSC = 'https://bsc-dataseed1.binance.org:443'

class AbstractContract(ABC):
    
    provider = None
    
    def __init__(self, address: str, ABI: str):
        
        if self.provider is not None:
            w3 = Web3(Web3.HTTPProvider(self.provider))
            self.fromWei = w3.fromWei
        else:
            raise ProviderInitException
        
        try:
            self.contract = w3.eth.contract(address, abi=ABI)
        except Exception as e:
            print(f'{e} in contract {address}')
    
    @property
    def address(self):
        return self.contract.address
    
    @property
    def abi(self):
        return self.contract.abi
        
    def get_functions_list(self) -> list:
        return self.contract.all_functions()

    def get_balance_of(self, wallet, mode='ether'):
        wei = self.contract.caller.balanceOf(wallet)
        return self.fromWei(wei, mode)
    
class BSCContract(AbstractContract):
    provider = BSC
    
    

