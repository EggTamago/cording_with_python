from urllib import request
from bs4 import BeautifulSoup
import time

import tqdm


#
# S1
#

s1_list = []

s1_url = 'https://s1s1s1.com/actress/'

# seach format
form = ['a', 'ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ya', 'ra', 'wa']

for target in tqdm.tqdm(form):
    target_url = s1_url + target

    for i in range(1,9):
        target_url = target_url + f'?page={i}'
        
        # a~waまで順番にwebページの取得
        response = request.urlopen(target_url)
        soup = BeautifulSoup(response, "lxml")

        # 女優名を取得
        temp = []
        temp = soup.find_all('p', class_='name')

        for j in range(len(temp)):
            try:
                s1_list.append(temp[j].text)
            except Exception as e:
                pass

        response.close()

        # target_url初期化
        target_url = s1_url + target
        time.sleep(5)

s1_list = list(set(s1_list))
print(s1_list)


    # # 女優名を取得
    # s1_list = soup.find_all('p', class_='name')
    # response.close()

    # print(s1_list)
    # print()
    # print(s1_list[0])
    # print()
    # print(s1_list[0].text)
    # print()
    # print(len(s1_list))

    

#
# kawaii
#

# format: a, ka...
kawaii_url = 'https://www.kawaiikawaii.jp/actress/list/'




#
# moodyz
#

# format: a, i, u...
moodyz_url = 'https://www.moodyz.com/actress/list/'




#
# E-BODY
#

# format: a, ka...
ebody_url = 'https://www.av-e-body.com/actress/list/'