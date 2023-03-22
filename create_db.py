import json
from models import app, db, Artists, Albums, Tracks

# ------------
# load_json
# ------------
def load_json(filename):
    """
    return a python dict jsn
    filename a json file
    """
    with open(filename) as file:
        jsn = json.load(file)
        file.close()

    return jsn

# ------------
# add artists
# ------------
def create_artists():
    """
    populate artist table
    """
    artists = load_json('Artists.json')

    for artist in artists:
        artist_id = artist['artist_id']
        artist_image = artist['artist_image']
        artist_name = artist['artist_name']
        artist_popularity = artist['artist_popularity']
        followers = artist['followers']
        genres = artist['genres']
        sample_album = artist['sample_album']
        sample_album_id = artist['sample_album_id']
        sample_track = artist['sample_track']
        sample_track_id = artist['sample_track_id']
		
        newArtist = Artists(artist_id = artist_id, artist_name = artist_name, artist_popularity = artist_popularity, followers = followers, 
                            genres = genres, artist_image = artist_image, sample_album = sample_album, sample_album_id = sample_album_id, 
                            sample_track = sample_track, sample_track_id = sample_track_id)
        
        # add new Artist object to DB
        db.session.add(newArtist)
        # commit the session to my DB
        db.session.commit()
	
create_artists()

# ------------
# add albums
# ------------
def create_albums():
    """
    populate albums table
    """
    albums = load_json('Albums.json')

    for album in albums:
        album_artist = album['album_artist']
        album_artist_id = album['album_artist_id']
        album_id = album['album_id']
        album_image = album['album_image']
        album_name = album['album_name']
        album_popularity = album['album_popularity']
        label = album['label']
        release_date = album['release_date']
        top_track = album['top_track']
        total_tracks = album['total_tracks']
        top_track_id = album['track_id']
		
        newAlbum = Albums(album_artist = album_artist, album_artist_id = album_artist_id, album_id = album_id, album_image = album_image, album_name = album_name,
                          album_popularity = album_popularity, label = label, release_date = release_date, top_track = top_track, total_tracks = total_tracks, top_track_id = top_track_id)
        
        # add new Album object to DB
        db.session.add(newAlbum)
        # commit the session to my DB
        db.session.commit()
	
create_albums()

# ------------
# add tracks
# ------------
def create_tracks():
    """
    populate tracks table
    """
    tracks = load_json('Tracks.json')

    for track in tracks:
        track_id = track['track_id']
        track_name = track['track_name']
        track_artist = track['track_artist']
        track_artist_id = track['track_artist_id']
        track_popularity = track['track_popularity']
        track_image = track['track_image']
        preview_url = track['preview_url']
        danceability = track['danceability']
        loudness = track['loudness']
        tempo = track['tempo']
        energy = track['energy']

		
        newTrack = Tracks(track_id = track_id, track_name = track_name, track_artist = track_artist, track_artist_id = track_artist_id, track_popularity = track_popularity, 
                          track_image = track_image, preview_url = preview_url, danceability = danceability, loudness = loudness, tempo = tempo,
                          energy = energy)
        
        # add new Track object to DB
        db.session.add(newTrack)
        # commit the session to my DB
        db.session.commit()
	
create_tracks()
