import random
import re
from jsonpath_ng import parse
import time
from scrapy import Request
from pybloom_live import ScalableBloomFilter
from dateutil import parser
from alphaPlan.settings import ACCOUNT_LIST
from ..items import *


class AlphaSpider(scrapy.Spider):
    name = 'alpha'
    allowed_domains = ['twitter.com']
    list_dict = {'1639838455760035840': 'dao_ust', '1667054883219083264': 'dao_ust2',
                 '1646838020363153408': 'dao_ust3', '1644920028696031235': 'dao_ust'}
    # start_urls = [
    #     'https://twitter.com/i/api/graphql/-_Z4thx55wBFXl3AYBW_1g/ListLatestTweetsTimeline?variables=%7B%22listId%22%3A%22{}%22%2C%22count%22%3A1%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%7D&features=%7B%22responsive_web_twitter_blue_verified_badge_is_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22vibe_api_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Afalse%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Afalse%2C%22interactive_text_enabled%22%3Atrue%2C%22responsive_web_text_conversations_enabled%22%3Afalse%2C%22longform_notetweets_richtext_consumption_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D'.format(
    #         i) for i in list_dict.keys()]
    headers = [i[2] for i in ACCOUNT_LIST]
    # headers = [{
    #     'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    #     'Cookie': 'des_opt_in=Y; _gcl_au=1.1.2086328013.1685102825; g_state={"i_l":4,"i_p":1688478693716}; mbox=PC#dcbf0b6907a44fc787c69c2e7fbb6db1.38_0#1749817959|session#dfcb512ba2904d55935a82566010ca90#1686575019; _ga_34PHSZMC42=GS1.1.1686573165.8.1.1686573197.0.0.0; _ga=GA1.2.1852869831.1685180820; kdt=YY5epcm5ePgzHpX3oXabVshhh27g18lEHMuYH7v4; _gid=GA1.2.1842052750.1687350267; dnt=1; auth_multi="1577862800952930305:1bedb7ef5487e0ca4faa75e233f94abf2b7e59eb|1573326306661793792:b8da11bc85168214fe4b0b6957cc318478a3a6e2"; auth_token=5503c671b8069c470766fdea2d66ba5fb9a86538; guest_id=v1%3A168735332699056847; ct0=e19897d7753735caf08114c7dddf607957a28df444b776c21a2b74b16100bd05790d7cdf5b6c32478aa17ed0eb87520b121e6c39235f656d71973706e3c270b64f7c888caee8ebd78b5d003f9ab97ae8; lang=zh-cn; twid=u%3D1568898000654680064; guest_id_marketing=v1%3A168735332699056847; guest_id_ads=v1%3A168735332699056847; personalization_id="v1_quUYBDnAEMLTiqebrNCQJQ=="',
    #     'X-Csrf-Token': 'e19897d7753735caf08114c7dddf607957a28df444b776c21a2b74b16100bd05790d7cdf5b6c32478aa17ed0eb87520b121e6c39235f656d71973706e3c270b64f7c888caee8ebd78b5d003f9ab97ae8'},
    #     {
    #         'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    #         'Cookie': 'des_opt_in=Y; _gcl_au=1.1.2086328013.1685102825; g_state={"i_l":4,"i_p":1688478693716}; mbox=PC#dcbf0b6907a44fc787c69c2e7fbb6db1.38_0#1749817959|session#dfcb512ba2904d55935a82566010ca90#1686575019; _ga_34PHSZMC42=GS1.1.1686573165.8.1.1686573197.0.0.0; _ga=GA1.2.1852869831.1685180820; _gid=GA1.2.294164188.1687613031; gt=1672929356564557831; kdt=NM3A3BOWMx37GmPm0Z4Lhye1iVVcztVSlceYK2X6; lang=zh-cn; dnt=1; auth_multi="1121014957422907392:fb739a04e9f024dfa6860b837b9c437aaa93f0fa"; auth_token=450444b721eb21cfa581e4195ac7384545dd89cc; guest_id=v1%3A168769252221011498; ct0=1a3a1a3f3f3497d56d958b4363e1514dbfd5f90dd3cec4455a20d0223c656bfd9786b307c96508e2f85501c6c137ae9dab5cddf5f6b3655c6d3b11f72d39041376df5f2b01920c2b148c3389e8fc1bca; twid=u%3D1666748651618865153; guest_id_marketing=v1%3A168769252221011498; guest_id_ads=v1%3A168769252221011498; personalization_id="v1_BLq9lVhxG6JsQL5ss6yM5g=="',
    #         'X-Csrf-Token': '1a3a1a3f3f3497d56d958b4363e1514dbfd5f90dd3cec4455a20d0223c656bfd9786b307c96508e2f85501c6c137ae9dab5cddf5f6b3655c6d3b11f72d39041376df5f2b01920c2b148c3389e8fc1bca'},
    #     {
    #         'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
    #         'Cookie': 'des_opt_in=Y; _gcl_au=1.1.2086328013.1685102825; g_state={"i_l":4,"i_p":1688478693716}; mbox=PC#dcbf0b6907a44fc787c69c2e7fbb6db1.38_0#1749817959|session#dfcb512ba2904d55935a82566010ca90#1686575019; _ga_34PHSZMC42=GS1.1.1686573165.8.1.1686573197.0.0.0; _ga=GA1.2.1852869831.1685180820; kdt=YY5epcm5ePgzHpX3oXabVshhh27g18lEHMuYH7v4; _gid=GA1.2.1842052750.1687350267; dnt=1; lang=zh-cn; auth_multi="1568898000654680064:5503c671b8069c470766fdea2d66ba5fb9a86538|1577862800952930305:1bedb7ef5487e0ca4faa75e233f94abf2b7e59eb|1573326306661793792:b8da11bc85168214fe4b0b6957cc318478a3a6e2"; auth_token=bc4e0b0e13059d5f73217d2e512963ab84d2b03c; guest_id=v1%3A168735792361821059; ct0=5f9cd12434705cc3270ebe333b8b3cfa6f4df1fbd15306751b4c853d4cfb650082da2b70ebecb3d60552549c151c4fa4d17a8ef20969692024ec5aeabc572bfc2e7a2634167d48c2347572bf87a20c54; twid=u%3D1121014957422907392; guest_id_marketing=v1%3A168735792361821059; guest_id_ads=v1%3A168735792361821059; personalization_id="v1_dhsI3gVYY2Bo9x07dcPgzg=="',
    #         'X-Csrf-Token': '5f9cd12434705cc3270ebe333b8b3cfa6f4df1fbd15306751b4c853d4cfb650082da2b70ebecb3d60552549c151c4fa4d17a8ef20969692024ec5aeabc572bfc2e7a2634167d48c2347572bf87a20c54'}
    # ]
    sbfilter = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
    last_time = time.time()

    def start_requests(self):
        for l, n in self.list_dict.items():
            # for url in self.start_urls:
            yield Request(
                'https://twitter.com/i/api/graphql/-_Z4thx55wBFXl3AYBW_1g/ListLatestTweetsTimeline?variables=%7B%22listId%22%3A%22{}%22%2C%22count%22%3A1%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%7D&features=%7B%22responsive_web_twitter_blue_verified_badge_is_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22vibe_api_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Afalse%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Afalse%2C%22interactive_text_enabled%22%3Atrue%2C%22responsive_web_text_conversations_enabled%22%3Afalse%2C%22longform_notetweets_richtext_consumption_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D'.format(
                    l), dont_filter=True, callback=self.parse, headers=self.headers[0],
                meta={'list_account': n, 'headers': self.headers[0]})

    # def get_text(self, the):
    #     text = re.findall(r"\bfull_text.*?, '", the)
    #     res = ''
    #     for i in text:
    #         res += i.replace(r'\n', '\n')[13:-4] + '\n'
    #     return res

    def parse(self, response):
        print(response.status, response.meta.get('list_account'), time.strftime('%Y-%m-%d %H:%M:%S %Z %A'))
        if response.status == 200:
            only = parse('$..entries[0]').find(response.json())[0].value
            # only = response.json()['data']['list']['tweets_timeline']['timeline']['instructions'][0]['entries'][0]
            # tweet_id=re.findall(r'tweet-\d+',only)[-1][6:]
            tweet_id = parse('$..entryId').find(only)[-1].value
            tweet_id = re.findall(r'\d+', tweet_id)[-1]
            tweet_text = parse('$..full_text').find(only)
            # 佈隆過濾器去掉之前爬過的推文
            if '1644920028696031235' in response.url and len(tweet_text) == 1:
                item = CallerItem()
                item['tweet_text'] = tweet_text[-1].value
            elif '1644920028696031235' not in response.url:
                item = LaunchItem()
                item['tweet_text'] = '\n'.join([i.value for i in tweet_text])
            else:
                item = None
            if not self.sbfilter.add(tweet_id + item.__class__.__name__) and item:
                item['list_account'] = response.meta.get('list_account')
                item['tweet_id'] = tweet_id
                # all_user=re.findall(r'\bscreen_name.*?,', only)[0:2]
                all_user = parse('$..screen_name').find(only)[0:2]
                # item['tweet_user'] = re.search(r'\bscreen_name.*?,',only).group()[15:-3]
                item['tweet_user'] = all_user[0].value
                item['tweet_alpha'] = all_user[-1].value
                item['tweet_time'] = parser.parse(parse('$..created_at').find(only)[-1].value)
                # item['tweet_text'] = tweet_text[-1].value
                # item['tweet_text'] = '\n'.join([i.value for i in parse('$..full_text').find(only)])
                all_thumb = parse('$..profile_image_url_https').find(only)
                item['user_thumb'] = all_thumb[0].value
                item['alpha_thumb'] = all_thumb[-1].value
                # tweet_media = re.search(r"media_url_https.*?,", only)
                tweet_media = parse('$..media_url_https').find(only)
                item['tweet_media'] = tweet_media[0].value if tweet_media else ''
                print('未处理' + item.__class__.__name__, item, sep='\n')
                # 每隔一段时间重启爬虫,减小內存佔用
                # if time.time() - self.last_time > 1800:
                #     self.crawler.engine.close_spider(self, '定时重启')
                #     # self.sbfilter = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
                #     self.last_time = time.time()
                yield item
        else:
            time.sleep(60)
        # 隨機headers以及cookies
        index = random.randint(0, 2)
        headers = self.headers[index]
        print('头部索引', index)
        response.meta['headers'] = headers
        yield Request(url=response.url, callback=self.parse, headers=headers, dont_filter=True,
                      meta=response.meta)
