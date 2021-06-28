from googleapiclient.discovery import build
api_key = 'AIzaSyAr1Cdl_aSD04QG2OZ8QJQZWvoNcxt_iHM'
youtube = build('youtube', 'v3', developerKey=api_key)
# servuce name and version
request = youtube.channels().list(
        part='statistics',
        forUsername='schafer5'
    )

response = request.execute()

print(response)
