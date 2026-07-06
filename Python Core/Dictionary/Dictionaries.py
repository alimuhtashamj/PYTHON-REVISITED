title_index = {
    "Believer": 101,
    "Thunder": 102,
    "Demons": 103
}
songs_by_id = {
    101: {
        "title": "Believer",
        "artist": "Imagine Dragons",
        "duration": "3:24"
    },
    102: {
        "title": "Thunder",
        "artist": "Imagine Dragons",
        "duration": "3:07"
    },
    103: {
        "title": "Demons",
        "artist": "Imagine Dragons",
        "duration": "2:57"
    }
}
user_input = input('Enter Song Name')
if user_input in title_index:
    songID= title_index[user_input]
    song_details = songs_by_id[songID]
    print(song_details)
else:
    print('No result found')
    

    
