import requests

endcursors = ['','QVFCSDl6d1FFUnFtSzYxVmlzYUtsUE84VDl5WHEtaTYxRUdhTUVCRXB6Tkd5aEtTYjdTS1dRWVNISzN6SC1zczZhODJ4YVVJMUZjbmlxeEJONWtsTGlqTw=='

]

for endcursor in endcursors:
    url = 'https://www.instagram.com/explore/tags/golfing/?__a=1&max_id='+endcursor
    r = requests.get(url).json()
    print(r)