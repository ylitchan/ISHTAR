from tools import *


def get_list_members(ids: list):
    already = []
    for list_id in ids:
        member = client_tweet.get_list_members(list_id, pagination_token=None, user_auth=True)
        next_token = member.meta.get('next_token')
        already.extend([i.id for i in member.data])
        print('列表数量', len(already))
        while next_token:
            try:
                member = client_tweet.get_list_members(list_id, pagination_token=next_token)
                next_token = member.meta.get('next_token')
                already.extend([i.id for i in member.data])
                print('获取成功', len(already))
                time.sleep(60)
            except:
                print('获取错误')
                time.sleep(900)
                continue
        time.sleep(60)
    with open('listMembers.json', 'w') as f:
        json.dump(list(set(already)), f)


if __name__ == '__main__':
    get_list_members(['1639838455760035840'])
