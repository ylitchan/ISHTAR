import random
import re
from jsonpath_ng import parse
import time
from scrapy import Request
from pybloom_live import ScalableBloomFilter
from dateutil import parser
from ..items import *


class AlphaSpider(scrapy.Spider):
    name = 'alpha'
    allowed_domains = ['twitter.com']
    start_urls = [
        'https://twitter.com/i/api/graphql/-_Z4thx55wBFXl3AYBW_1g/ListLatestTweetsTimeline?variables=%7B%22listId%22%3A%22{}%22%2C%22count%22%3A1%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%7D&features=%7B%22responsive_web_twitter_blue_verified_badge_is_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22vibe_api_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Afalse%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Afalse%2C%22interactive_text_enabled%22%3Atrue%2C%22responsive_web_text_conversations_enabled%22%3Afalse%2C%22longform_notetweets_richtext_consumption_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D'.format(
            i) for i in ['1639838455760035840', '1644920028696031235']]
    cookies = [{'des_opt_in': 'Y', '_gcl_au': '1.1.116267149.1676257589', 'g_state': '{"i_l":4,"i_p":1681369247236}',
                '_ga_BYKEBDM7DS': 'GS1.1.1679899771.1.1.1679899844.0.0.0',
                'mbox': 'PC#5d50de66cc054e10bf959bf00d0b670c.38_0#1743478298|session#588b81b0c51c476c89ecc2e190b96e91#1680235358',
                '_ga_34PHSZMC42': 'GS1.1.1680233475.10.1.1680233505.0.0.0', '_ga': 'GA1.2.1915858432.1679573193',
                '_gid': 'GA1.2.1222660834.1680783998', 'gt': '1644906262113697792',
                'kdt': 'Z3OdCWN6PkJiRhCcUfHEA4O2zWq3ZJ2MIgFn1fSg', 'ads_prefs': '"HBERAAA="',
                'auth_multi': '"1568898000654680064:ddc86a06fadbca76319f2484ce8ead062f440835"',
                'auth_token': 'cf9bb31eb63b8e3e05e8369d287de00f36259694', 'guest_id_ads': 'v1:168101800908229947',
                'guest_id_marketing': 'v1:168101800908229947', 'lang': 'en', 'guest_id': 'v1:168101800908229947',
                'twid': 'u=1577862800952930305',
                'ct0': '5d54053bb46518b6eae62429e3ac8a7d76fd9bbbf4de72d7de25f6286ce9f6aabb063b15343c4b941b21d4a77d62d75764b061b8e49f285db120b02db6f7c878ea2ba385c682518a58e38d5fe760fbc9',
                'personalization_id': '"v1_9MAr+iey/BOWvItd/ATJtA=="'},
               {'des_opt_in': 'Y', '_gcl_au': '1.1.116267149.1676257589', 'g_state': '{"i_l":4,"i_p":1681369247236}',
                '_ga_BYKEBDM7DS': 'GS1.1.1679899771.1.1.1679899844.0.0.0', '_gid': 'GA1.2.1222660834.1680783998',
                '_ga': 'GA1.2.1915858432.1679573193',
                'mbox': 'PC#5d50de66cc054e10bf959bf00d0b670c.38_0#1744561080|session#f940de38a1ec4067af22fe04484b1cb2#1681318140',
                '_ga_34PHSZMC42': 'GS1.1.1681384916.12.1.1681384960.0.0.0', 'gt': '1646847208036384768',
                'kdt': 'm5dUkEnYXnq7KOR7vaxMgqMb6r1UWtROHSYEcCNa', 'lang': 'en', 'ads_prefs': '"HBERAAA="',
                'auth_multi': '"1577862800952930305:fda50894e36d009bb9c6d81de8a47a8b28107413"',
                'auth_token': '59d253b407d101c207bdbe5dbe8c64d71b8008a3', 'guest_id_ads': 'v1:168148218158033820',
                'guest_id_marketing': 'v1:168148218158033820', 'guest_id': 'v1:168148218158033820',
                'twid': 'u=1573326306661793792',
                'ct0': 'edcfe6d2224eb5cd5a892a70359c2102e369450b99396c3358c7feaec7deefb47160709b841ec5891922469405dcc21523242e1f961eab947b197282bc7ab1597cb3e1c5dcb03d951d6e4d9a1d285a82',
                'personalization_id': '"v1_ZsTUZ7YjDGRSNO7bd3F+LA=="'}]
    headers = [{
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'x-twitter-auth-type': 'OAuth2Session',
        'x-csrf-token': '5d54053bb46518b6eae62429e3ac8a7d76fd9bbbf4de72d7de25f6286ce9f6aabb063b15343c4b941b21d4a77d62d75764b061b8e49f285db120b02db6f7c878ea2ba385c682518a58e38d5fe760fbc9',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62'},
        {
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs=1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'x-csrf-token': 'edcfe6d2224eb5cd5a892a70359c2102e369450b99396c3358c7feaec7deefb47160709b841ec5891922469405dcc21523242e1f961eab947b197282bc7ab1597cb3e1c5dcb03d951d6e4d9a1d285a82',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.39',
            'x-twitter-auth-type': 'OAuth2Session',
        }
    ]
    sbfilter = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH)
    last_time = time.time()

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, dont_filter=True, callback=self.parse, cookies=self.cookies[0], headers=self.headers[0])

    # def get_text(self, the):
    #     text = re.findall(r"\bfull_text.*?, '", the)
    #     res = ''
    #     for i in text:
    #         res += i.replace(r'\n', '\n')[13:-4] + '\n'
    #     return res

    def parse(self, response):
        print(response.status, time.strftime('%Y-%m-%d %H:%M:%S %Z %A'))
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
        index = random.randint(0, 1)
        cookies = self.cookies[index]
        headers = self.headers[index]
        print('头部索引', index)
        yield Request(url=response.url, callback=self.parse, cookies=cookies, headers=headers, dont_filter=True)
