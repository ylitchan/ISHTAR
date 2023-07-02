from scrapy import Request
from utils.tools import *


class NewAlphaSpider(scrapy.Spider):
    name = 'newAlpha'
    allowed_domains = ['twitter.com']
    user_dict = {'@doctorDefi2020': 1410877375198285827,
                 '@ugly42061647': 1161902865969025024,
                 '@FedAgentAaron': 1442919050, '@Sajuio8': 1479930165761302531, '@cryptamurai': 914788213763559424,
                 '@vvhader1': 1093579512388804608, '@Luyaoyuan1': 1202404680992575488,
                 '@CryptoGangster6': 1373269670074019841, '@skiesyyyy': 1329534911364042752,
                 '@Henry_VuQuangDu': 1191522172608471040, '@I_am_patrimonio': 1023637918282383361,
                 '@2lambro': 1559193198605774850, '@Makima_sol': 1428066700931571714,
                 '@RASOKA_ETH': 1373674110031515648, '@The_1legendd': 755082450557173760,
                 '@UST_DAO': 1525413531641909249, '@Arron_finance': 1145259912764805120,
                 '@EinsteinYipie': 996220800431669248, '@multichainchad': 1372954317649543171,
                 '@sung_crypto': 1483780590302371848, '@duke_rick1': 1293551150948585474,
                 '@ElCryptoDoc': 1260953582897111042, '@Ekonomeest': 507337880, '@TheRealGapper': 716698266,
                 '@ChadCaff': 1411274211444854785, '@MohammedTunkar4': 946926779226353665,
                 '@thecyptowonk': 703330140844068865, '@LoveKeykey1': 1464985642186674176, '@dawsboss888': 1235634691,
                 '@RaccoonHKG': 1402966572726054915, '@ArbitrumNewsDAO': 1374628085471977478, '@CJCJCJCJ_': 483061902,
                 '@Vikcyter_2': 1497149952421613571, '@Hoangarthur2': 1376714105310965762,
                 '@xiaowuDD666': 1224237649134620673, '@LeNeutron': 1069731982832230400, '@3azima85': 260180304,
                 '@panoskras': 942058868158365696, '@crypto_saint': 873640202329305089,
                 '@snkrseateat': 776808659573538816, '@FractalGiraffe': 1057043659391229957, '@shingboiii': 3398862073,
                 '@SlukaOzella': 1609130699256389632, '@0xdantrades': 984279344, '@lantian560560': 1434104719169888258,
                 '@crypt0_beluga': 1388044400412921856, '@defi_antcrypto': 1594223633605459968,
                 '@BiliSquare': 887928113312677889, '@Ed_x0101': 1359150440663949319,
                 '@cryptomemez': 1300868746412789761, '@dao_ust': 1568898000654680064, '@lawrenx_': 1038021937304416256,
                 '@crypt0detweiler': 1389581148146356230, '@0xYelf': 1452979796145840140,
                 '@Juliooofive': 926593414086447104, '@monosarin': 1392695766934822912,
                 '@criptopaul': 870778296950247426, '@EricCryptoman': 826381583489855490,
                 '@sululukz99': 1465355451412131841, '@0xsn0wball': 873095548756045825, '@DoloNFT': 1404971067672875015,
                 '@MiddleChildPabk': 885225812986699776, '@CryptoKaduna': 1103404363861684236,
                 '@ApeOClock': 1401346770458669057, '@ilovegains': 749749112, '@Sherv1n_eth': 1476504086178676742,
                 '@berdXspade': 1459514982891024387, '@yuyue_chris': 1490949502261665792,
                 '@RomAin11515879': 1379376517671751681, '@yakuza_crypto': 1329171696155193345}

    # list_dict = {'@0xdantrades', '@0xsn0wball', '@0xYelf', '@2lambro', '@3azima85', '@ApeOClock', '@ArbitrumNewsDAO',
    #              '@Arron_finance', '@berdXspade', '@BiliSquare', '@ChadCaff', '@CJCJCJCJ_', '@criptopaul',
    #              '@crypt0_beluga', '@crypt0detweiler', '@cryptamurai', '@crypto_saint', '@CryptoGangster6',
    #              '@CryptoK63140864', '@CryptoKaduna', '@cryptomemez', '@dao_ust', '@dawsboss888', '@defi_antcrypto',
    #              '@doctorDefi2020', '@DoloNFT', '@duke_rick1', '@Ed_x0101', '@EinsteinYipie', '@Ekonomeest',
    #              '@ElCryptoDoc', '@EricCryptoman', '@FedAgentAaron', '@FractalGiraffe', '@Henry_VuQuangDu',
    #              '@Hoangarthur2', '@I_am_patrimonio', '@ilovegains', '@ISHTARider', '@Juliooofive', '@lantian560560',
    #              '@lawrenx_', '@LeNeutron', '@LoveKeykey1', '@Luyaoyuan1', '@Makima_sol', '@MiddleChildPabk',
    #              '@MohammedTunkar4', '@monosarin', '@multichainchad', '@panoskras', '@RaccoonHKG', '@RASOKA_ETH',
    #              '@RomAin11515879', '@Sajuio8', '@Sherv1n_eth', '@shingboiii', '@skiesyyyy', '@SlukaOzella',
    #              '@snkrseateat', '@sululukz99', '@sung_crypto', '@The_1legendd', '@thecyptowonk', '@TheRealGapper',
    #              '@ugly42061647', '@UST_DAO', '@Vikcyter_2', '@vvhader1', '@xiaowuDD666', '@yakuza_crypto',
    #              '@yuyue_chris'}'@ISHTARider': 1577862800952930305,
    # start_urls = [
    #     'https://twitter.com/i/api/graphql/-_Z4thx55wBFXl3AYBW_1g/ListLatestTweetsTimeline?variables=%7B%22listId%22%3A%22{}%22%2C%22count%22%3A1%2C%22withDownvotePerspective%22%3Afalse%2C%22withReactionsMetadata%22%3Afalse%2C%22withReactionsPerspective%22%3Afalse%7D&features=%7B%22responsive_web_twitter_blue_verified_badge_is_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22vibe_api_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Afalse%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Afalse%2C%22interactive_text_enabled%22%3Atrue%2C%22responsive_web_text_conversations_enabled%22%3Afalse%2C%22longform_notetweets_richtext_consumption_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D'.format(
    #         i) for i in list_dict.keys()]
    headers = [i[2] for i in ACCOUNT_LIST]
    with open('sbfilterFollowing', 'rb') as f:
        sbfilter = ScalableBloomFilter(mode=ScalableBloomFilter.SMALL_SET_GROWTH).fromfile(f)
    last_time = time.time()

    def start_requests(self):
        for l, n in self.user_dict.items():
            # for url in self.start_urls:
            yield Request(
                'https://twitter.com/i/api/graphql/2vTVUCjWcooreYYLCK0nLQ/Following?variables=%7B%22userId%22%3A%22{}%22%2C%22count%22%3A20%2C%22includePromotedContent%22%3Afalse%7D&features=%7B%22rweb_lists_timeline_redesign_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22tweetypie_unmention_optimization_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Afalse%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_media_download_video_enabled%22%3Afalse%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D&fieldToggles=%7B%22withArticleRichContentState%22%3Afalse%7D'.format(
                    str(n)), dont_filter=True, callback=self.parse, headers=self.headers[0],
                meta={'username': l, 'headers': self.headers[0]})

    def parse(self, response):
        print(response.status, response.meta.get('username'), time.strftime('%Y-%m-%d %H:%M:%S %Z %A'))
        if response.status == 200:
            following = parse('$..user_results').find(response.json())
            print(parse('$..screen_name').find(following[0].value)[0].value)
            for u in following:
                # 佈隆過濾器去掉之前爬過的推文
                if not self.sbfilter.add(parse('$..rest_id').find(u.value)[0].value):
                    # with open('sbfilterFollowing', 'wb') as f:
                    #     self.sbfilter.tofile(f)
                    # print('持久化布隆过滤器')
                    new_follow = {'username': parse('$..screen_name').find(u.value)[0].value,
                                  'restID': parse('$..rest_id').find(u.value)[0].value,
                                  'bio': parse('$..description').find(u.value)[0].value,
                                  'profileImageUrl': parse('$..profile_image_url_https').find(u.value)[0].value,
                                  'createdAt': parse('$..created_at').find(u.value)[0].value,
                                  'followersCount': parse('$..followers_count').find(u.value)[0].value,
                                  'listedCount': parse('$..listed_count').find(u.value)[0].value}
                    print('当前新增关注', new_follow)
                    producer.publish('q_add', json.dumps(new_follow))
                    msg_tg = '\=\=新增关注\=\=\n最新关注[' + parse('$..screen_name').find(u.value)[
                        0].value + '](https://twitter.com/' + parse('$..screen_name').find(u.value)[
                                 0].value + ')\nfollowersCount:' + str(parse('$..followers_count').find(u.value)[
                                                                           0].value) + '\nlistedCount:' + str(
                        parse('$..listed_count').find(u.value)[
                            0].value) + '\n来自[' + response.meta.get('username')[
                                                    1:] + '](https://twitter.com/' + response.meta.get(
                        'username')[1:] + ')'
                    msg_tg = msg_tg.replace('_', r'\_').replace('-', r'\-').replace('#', r'\#')
                    ISHTARider_tg.send_message(-1001982993052, msg_tg, parse_mode="MarkdownV2",
                                               disable_web_page_preview=False)

                    # token = session.post('https://alpha-admin.ipfszj.com/api/admin/base/open/login',
                    #                      json={'username': 'autoadd', 'password': '123456'}).json().get(
                    #     'data').get(
                    #     'token')
                    # session.post(url='https://alpha-admin.ipfszj.com/api/admin/alpha/list/add',
                    #              headers={'Authorization': token},
                    #              json=new_follow)
                    # 每隔一段时间持久化布隆过滤器
                    if time.time() - self.last_time > 900:
                        with open('sbfilterFollowing', 'wb') as f:
                            self.sbfilter.tofile(f)
                        print('持久化布隆过滤器')
                        self.last_time = time.time()
        else:
            time.sleep(60)
        # 隨機headers以及cookies
        index = random.randint(0, 2)
        headers = self.headers[index]
        print('头部索引', index)
        response.meta['headers'] = headers
        yield Request(url=response.url, callback=self.parse, headers=headers, dont_filter=True,
                      meta=response.meta)
