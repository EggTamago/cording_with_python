from urllib import request
from bs4 import BeautifulSoup

#
# S1
#

s1_list = []

s1_url = 'https://s1s1s1.com/actress/'

# seach format
form = ['a', 'ka', 'sa', 'ta', 'na', 'ha', 'ma', 'ya', 'ra', 'wa']

for target in form:
    target_url = s1_url + target + '/'
    print(target_url)

    # a~waまで順番にwebページの取得し、女優名リストを作成
    response = request.urlopen(s1_url)
    soup = BeautifulSoup(response)
    response.close()

    

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