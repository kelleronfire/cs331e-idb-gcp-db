from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

# Database Info
username = 'postgres'
password = '8778'
ip_addr = 'localhost:5432'
db_name = 'amplifydb'

#app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{username}:{password}@{ip_addr}/{db_name}'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:8778@/postgres?host=/cloudsql/cs331e-idb-377817:us-central1:amplifydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)

class Artists(db.Model):
    __tablename__ = 'artists'
    artist_id = db.Column(db.String(512), primary_key = True)
    artist_name = db.Column(db.String(512), nullable = False)
    artist_popularity = db.Column(db.Integer, nullable = False)
    followers = db.Column(db.Integer, nullable = False)
    genres = db.Column(db.String(512), nullable = False)  # can be multivalued, so really an array
    artist_image = db.Column(db.String(512), nullable = False)
    top_track = db.Column(db.String(512), nullable = False)
    similar_artist = db.Column(db.String(512), nullable = False)


class Albums(db.Model):
    __tablename__ = 'albums'
    album_id = db.Column(db.String(512), primary_key = True)
    album_name = db.Column(db.String(512), nullable = False)
    album_artist = db.Column(db.String(512), nullable = False)  # can be multivalued, so really an array
    release_date = db.Column(db.String(512), nullable = False)
    total_tracks = db.Column(db.Integer, nullable = False)
    album_image = db.Column(db.String(512), nullable = False)
    album_popularity = db.Column(db.Integer, nullable = False)
    label = db.Column(db.String(512), nullable = False)
    tracks = db.Column(db.String(512), nullable = False)  # multivalued, so really an array


class Tracks(db.Model):
    __tablename__ = 'tracks'
    track_id = db.Column(db.String(512), primary_key = True)
    track_name = db.Column(db.String(512), nullable = False)
    track_artists = db.Column(db.String(512), nullable = False)  # can be multivalued, so really an array
    track_popularity = db.Column(db.Integer, nullable = False)
    track_image = db.Column(db.String(512), nullable = False)
    preview_url = db.Column(db.String(512), nullable = False)
    danceability = db.Column(db.String(512), nullable = False)
    loudness = db.Column(db.String(512), nullable = False)
    tempo = db.Column(db.String(512), nullable = False)
    energy = db.Column(db.String(512), nullable = False)

db.create_all()