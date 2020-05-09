import requests

url = 'https://www.instagram.com/explore/tags/golfing/?__a=1'
r = requests.get(url).json()
get_end_cursor = r['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
# print(get_end_cursor)

num = 0
while 1:
    url2 = url+'&max_id='+get_end_cursor
    r2 = requests.get(url2).json()
    get_end_cursor = r2['graphql']['hashtag']['edge_hashtag_to_media']['page_info']['end_cursor']
    print(get_end_cursor)
    num +=1
    if num ==400:
        break