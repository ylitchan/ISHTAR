import re
import time
import os
import openai
#{"role": "assistant", "content":"sale:unknown,\nlaunch:unknown,\nlisting:unknown,\nliquidity providing:unknown,\nairdrop:unknown"}
openai.api_key = os.getenv("openai")
res = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
# messages=[{"role": "assistant", "content":"sale:unknown,launch:unknown,listing:unknown,liquidity providing:unknown,airdrop:unknown"},{"role": "user","content": 'We will be having a community AMA to update everyone on:Apr 5, Wed, 9PM UTC+85' + '\n按照之前的格式提取以上内容中代币sale时间/代币launch时间/代币listing时间/代币liquidity providing时间/代币airdrop时间,若时间为现在则为now,若为其他情况则为unknown'}]
        messages=[{"role": "user","content":  '当前时间'+time.strftime('%Y-%m-%d %H:%M:%S %Z')+'\nStealth Launch Sept 2022 of $SECT on arb' + '根据当前时间并按照之前的格式提取以上内容中代币sale时间(格式为%Y-%m-%d %H:%M:%S %Z)/代币launch时间(格式为%Y-%m-%d %H:%M:%S %Z)/代币token(格式为$token)/代币发射chain(格式为@chain)'}]
    )
print(u"%s" % res['choices'][0]['message']['content'])
# print(re.search(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} \w+',u"%s" % res['choices'][0]['message']['content']).group())
#@BearrInu swap is now live!    Stealth Launch Sept 2022    Date of $CAI launch: 30.03.2023 $SECT launch is LIVE!
#WL Mint: 3/30  12:00 (UTC+8)   Public launch of $SECT on @CamelotDEX begins in three hours!    $DOF is now listed on http://mute.io 🚀
# We will be having a community AMA to update everyone on:Apr 5, Wed, 9PM UTC+85    Only 2 days left for the $PEG sale for @PepesGame on https://t.co/fL3LzhAIgn
#$LEX liquidity will be seeded 18th Apr, exclusively on Camelot. Sale token claims go live at the same time.