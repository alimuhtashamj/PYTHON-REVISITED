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
for i in title_index:
    if i == user_input:
        song_id =title_index[i]
        print(song_id)
    else:
        print('No results found')
    for j in songs_by_id:
        if j == user_input:
            print(j)

    
