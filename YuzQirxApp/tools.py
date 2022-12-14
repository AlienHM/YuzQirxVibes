from googleapiclient.discovery import build

# channel_id = 'UC8rPRwO2e3pUFZHb6oz72gw'
# video_id = '3na3khqRhqQ'

def get_video_stats(video_ids):
    views = 0
    likes = 0
    api_key = 'AIzaSyA3E2gLQb-WYweo1zY3wwXKbi-Qlk2vKm4'
    youtube = build('youtube', 'v3', developerKey=api_key)
    print("BUrada")
    for video_id in video_ids:
        request = youtube.videos().list(
            part='statistics',
            id=video_id)
        response = request.execute()
        items = response.get('items')[0]
        statistics = items.get('statistics')
        views += int(statistics.get('viewCount'))
        likes += int(statistics.get('likeCount'))
    # print("views", views, 'likes', likes)
    return views, likes

def standardizer(num):
    number = ''
    if num >= 1000:
        number = str(round(num /1000,2)) + 'K'
    elif num >= 1000000:
        number = str(round(num /1000000,2)) + 'M'
    else:
        number = num
    return number
