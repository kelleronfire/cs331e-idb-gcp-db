from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

# Database Info
username = 'postgres'
password = 'password'
ip_addr = 'localhost:5432'
db_name = 'amplifydb'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DB_STRING", f'postgresql://{username}:{password}@{ip_addr}/{db_name}')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Artists(db.Model):
    __tablename__ = 'artists'
    artist_id = db.Column(db.String(512), primary_key = True)
    artist_image = db.Column(db.String(512), nullable = False)
    artist_name = db.Column(db.String(512), nullable = False)
    artist_popularity = db.Column(db.Integer, nullable = False)
    followers = db.Column(db.Integer, nullable = False)
    genres = db.Column(db.String(512), nullable = False)  # can be multivalued, so really an array
    sample_album = db.Column(db.String(512), nullable = False)
    sample_album_id = db.Column(db.String(512), nullable = False)
    sample_track = db.Column(db.String(512), nullable = False)
    sample_track_id = db.Column(db.String(512), nullable = False)


class Albums(db.Model):
    __tablename__ = 'albums'
    album_artist = db.Column(db.String(512), nullable = False)
    album_artist_id = db.Column(db.String(512), nullable = False)
    album_id = db.Column(db.String(512), primary_key = True)
    album_image = db.Column(db.String(512), nullable = False)
    album_name = db.Column(db.String(512), nullable = False)
    album_popularity = db.Column(db.Integer, nullable = False)
    label = db.Column(db.String(512), nullable = False)
    release_date = db.Column(db.String(512), nullable = False)
    top_track = db.Column(db.String(512), nullable = False)
    total_tracks = db.Column(db.Integer, nullable = False)
    top_track_id = db.Column(db.String(512), nullable = False)


class Tracks(db.Model):
    __tablename__ = 'tracks'
    danceability = db.Column(db.String(512), nullable = False)
    energy = db.Column(db.String(512), nullable = False)
    loudness = db.Column(db.String(512), nullable = False)
    preview_url = db.Column(db.String(512), nullable = False)
    tempo = db.Column(db.String(512), nullable = False)
    track_artist = db.Column(db.String(512), nullable = False)
    track_artist_id = db.Column(db.String(512), nullable = False)
    track_id = db.Column(db.String(512), primary_key = True)
    track_image = db.Column(db.String(512), nullable = False)
    track_name = db.Column(db.String(512), nullable = False)
    track_popularity = db.Column(db.Integer, nullable = False)

db.drop_all()
db.create_all()