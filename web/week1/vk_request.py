import requests
import json
import datetime


SERVER_KEY = '625a3a8d625a3a8d625a3a8da5623580296625a625a3a8d3c121583846508f2af465326'

get_id_url = 'https://api.vk.com/method/users.get?v=5.71&access_token={}&user_ids={}'
get_friend_list_url = 'https://api.vk.com/method/friends.get?v=5.71&access_token={}&user_id={}&fields=bdate'

def calc_age(uid):  
    id = requests.get(get_id_url.format(SERVER_KEY, uid)).json()['response'][0]['id']
    friends_list = requests.get(get_friend_list_url.format(SERVER_KEY, id)).json()['response']['items']
    birth_dates = dict()
    current_year = datetime.datetime.now().year
    for user in friends_list:
        try:
            # print(user['first_name'], user['last_name'])
            year = int(user['bdate'].split('.')[2])
            birth_dates[current_year - year] = birth_dates.get(current_year - year, 0) + 1
        except (IndexError, KeyError):
            pass
    return sorted(birth_dates.items(), key=lambda pair: (-pair[1], pair[0]))


if __name__ == '__main__':
    res = calc_age('mrzv_s')
    print(res)