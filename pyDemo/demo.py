import random
import re
import urllib

from web3 import Web3
from eth_utils import address
# a=Web3.to_checksum_address('0x8945CE67C4023A10A9d376B8eF27E970146F2717')
# print(a)
# rpc = "https://cloudflare-eth.com"
# web3 = Web3(Web3.HTTPProvider(rpc))
# # 查看链接状态 返回bool值
# print(web3.is_connected())
# b=web3.eth.get_balance(a)
# b=web3.from_wei(b,'ether')
# print(random.uniform(0, 1))
a=urllib.parse.quote('string pd')
print(a)
b='Relevance of Submarines as the Game Changer in Future Wars – Indian Context By Cmde V Venugopal (R)'
# ச-ன-வ-ன-ம-ள-இயக-க-கட-ட-ப-ப-ட-ட-ஆய-தங-கள-கர-னல-ஆர-ஹர-ஹரன-tamil
# ச-ன-வ-ன-ம-ள-இயக-க-கட-ட-ப-ப-ட-ட-ஆய-தங-கள-கர-னல-ஆர-ஹர-ஹரன-Tamil
print(re.findall('\W',b))

x=''
for k,i in enumerate(b):
    if not i.isalpha():
        if x[-1] != '-' and k != len(b)-1:
            print(i)
            x+='-'

    else:
        x+=i
print('https://www.c3sindia.org/post/'+x)