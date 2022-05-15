username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]

import collections
import itertools
packed = sorted(zip(timestamp, username, website)) # zip is a generator
# print(packed)

user_to_web = collections.defaultdict(list)
for time, user, web in packed:
    user_to_web[user].append(web)
# print(user_to_web)

count_dic = collections.Counter()
for web_list in user_to_web.values():
    web_combs = set(itertools.combinations(web_list, 3))
    count_dic += 
print(web_combs)
