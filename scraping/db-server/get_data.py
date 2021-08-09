from urllib import request
from bs4 import BeautifulSoup
import time

import tqdm

# =====================
# return actor_array []
# =====================

def get_actor_list(url, form):

    return_list = []

    for target in tqdm.tqdm(form):
        target_url = url + target

        for i in range(1,9):
            target_url = target_url + f'?page={i}'
            
            # a~waまで順番にwebページの取得
            response = request.urlopen(target_url)
            soup = BeautifulSoup(response, "lxml")

            # 女優名を取得
            actor = []
            actor = soup.find_all('p', class_='name')

            for j in range(len(actor)):
                try:
                    return_list.append(actor[j].text)
                except Exception as e:
                    pass

            # target_url初期化
            target_url = url + target

    # requestをclose
    response.close()
    
    # 重複を削除
    return_list = list(set(return_list))
    return return_list

#
# kawaii
#

# format: a, ka...
# kawaii_url = 'https://www.kawaiikawaii.jp/actress/list/'




#
# moodyz
#

# format: a, i, u...
# moodyz_url = 'https://www.moodyz.com/actress/list/'




#
# E-BODY
#

# format: a, ka...
# ebody_url = 'https://www.av-e-body.com/actress/list/'