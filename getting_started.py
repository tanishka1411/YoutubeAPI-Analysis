from googleapiclient.discovery import build
api_key = '#someAPI key'
youtube = build('youtube', 'v3', developerKey=api_key)
# servuce name and version
request = youtube.channels().list(
        part='statistics',
        forUsername='schafer5'
    )

response = request.execute()

print(response)
