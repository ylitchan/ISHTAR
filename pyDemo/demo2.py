import datetime
import time
import requests
from dateutil import parser

a = datetime.datetime.now()
session = requests.Session()
c = session.get(
    'https://twitter.com/i/api/graphql/qRednkZG-rn1P6b48NINmQ/UserByScreenName?variables=%7B%22screen_name%22%3A%22ishtarider%22%2C%22withSafetyModeUserFields%22%3Atrue%7D&features=%7B%22hidden_profile_likes_enabled%22%3Afalse%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22subscriptions_verification_info_verified_since_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D',
    headers={
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'X-Csrf-Token': '5fa36a1944db79d4a4fe566b0f1d724143ad569f435a13ce0d3772a4523ef3b137fc9918c733a0716dfc2ed4787cfb8cf3b089deaba34dc5caeccf6309322d6d1e0fa3c6515a227cfffbcfccefa8d33d',
        'cookie': 'des_opt_in=Y; _gcl_au=1.1.2086328013.1685102825; g_state={"i_l":4,"i_p":1688478693716}; mbox=PC#dcbf0b6907a44fc787c69c2e7fbb6db1.38_0#1749817959|session#dfcb512ba2904d55935a82566010ca90#1686575019; _ga_34PHSZMC42=GS1.1.1686573165.8.1.1686573197.0.0.0; _ga=GA1.2.1852869831.1685180820; kdt=YY5epcm5ePgzHpX3oXabVshhh27g18lEHMuYH7v4; lang=en; dnt=1; auth_multi="1573326306661793792:b8da11bc85168214fe4b0b6957cc318478a3a6e2"; auth_token=1bedb7ef5487e0ca4faa75e233f94abf2b7e59eb; guest_id=v1%3A168700133867699616; ct0=5fa36a1944db79d4a4fe566b0f1d724143ad569f435a13ce0d3772a4523ef3b137fc9918c733a0716dfc2ed4787cfb8cf3b089deaba34dc5caeccf6309322d6d1e0fa3c6515a227cfffbcfccefa8d33d; twid=u%3D1577862800952930305; guest_id_ads=v1%3A168700133867699616; guest_id_marketing=v1%3A168700133867699616; personalization_id="v1_jTGzbbp2mQY4Cfi6/pknmQ=="; _gid=GA1.2.1842052750.1687350267'})
print(c, c.text)
d = session.post('https://twitter.com/i/api/graphql/27lfFOrDygiZs382QLttKA/ListAddMember', headers={
    'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    'Cookie': 'des_opt_in=Y; _gcl_au=1.1.2086328013.1685102825; g_state={"i_l":4,"i_p":1688478693716}; mbox=PC#dcbf0b6907a44fc787c69c2e7fbb6db1.38_0#1749817959|session#dfcb512ba2904d55935a82566010ca90#1686575019; _ga_34PHSZMC42=GS1.1.1686573165.8.1.1686573197.0.0.0; _ga=GA1.2.1852869831.1685180820; kdt=YY5epcm5ePgzHpX3oXabVshhh27g18lEHMuYH7v4; _gid=GA1.2.1842052750.1687350267; dnt=1; auth_multi="1577862800952930305:1bedb7ef5487e0ca4faa75e233f94abf2b7e59eb|1573326306661793792:b8da11bc85168214fe4b0b6957cc318478a3a6e2"; auth_token=5503c671b8069c470766fdea2d66ba5fb9a86538; guest_id=v1%3A168735332699056847; ct0=e19897d7753735caf08114c7dddf607957a28df444b776c21a2b74b16100bd05790d7cdf5b6c32478aa17ed0eb87520b121e6c39235f656d71973706e3c270b64f7c888caee8ebd78b5d003f9ab97ae8; lang=zh-cn; twid=u%3D1568898000654680064; guest_id_marketing=v1%3A168735332699056847; guest_id_ads=v1%3A168735332699056847; personalization_id="v1_quUYBDnAEMLTiqebrNCQJQ=="',
    'X-Csrf-Token': 'e19897d7753735caf08114c7dddf607957a28df444b776c21a2b74b16100bd05790d7cdf5b6c32478aa17ed0eb87520b121e6c39235f656d71973706e3c270b64f7c888caee8ebd78b5d003f9ab97ae8'},
                 json={
                     "variables": {
                         "listId": "1639838455760035840",
                         "userId": "1577862800952930305"
                     },
                     "features": {
                         "rweb_lists_timeline_redesign_enabled": True,
                         "responsive_web_graphql_exclude_directive_enabled": True,
                         "verified_phone_label_enabled": False,
                         "responsive_web_graphql_skip_user_profile_image_extensions_enabled": False,
                         "responsive_web_graphql_timeline_navigation_enabled": True
                     },
                     "queryId": "27lfFOrDygiZs382QLttKA"
                 })
print(d, d.text)
