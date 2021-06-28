import os
import re
from datetime import timedelta
from googleapiclient.discovery import build

api_key = 'AIzaSyAr1Cdl_aSD04QG2OZ8QJQZWvoNcxt_iHM'
youtube = build('youtube', 'v3', developerKey=api_key)

pl_request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId='PL-osiE80TeTsWmV9i9c58mdDCSskIFdDS'
    )

pl_response = pl_request.execute()

vid_ids = []
for item in pl_response['items']:
    vid_ids.append(item['contentDetails']['videoId'])
print(','.join(vid_ids))
