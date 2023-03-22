from flask import render_template
from create_db import app, db, Artists, Albums, Tracks

# ------------
# index
# ------------
@app.route('/')
def index():
	return render_template('index.html')

# ------------
# artists
# ------------	
@app.route('/artists/')
def artists():
	artist_list = db.session.query(Artists).all()
	return render_template('artists.html', artist_list = artist_list)

# ------------
# albums
# ------------	
@app.route('/albums/')
def albums():
	album_list = db.session.query(Albums).all()
	return render_template('albums.html', album_list = album_list)

# ------------
# tracks
# ------------	
@app.route('/tracks/')
def tracks():
	track_list = db.session.query(Tracks).all()
	return render_template('tracks.html', track_list = track_list)

# debug=True activates the automatic reloader. Therefore, if you use it, make sure to add "db.drop_all()"
# right before "db.create_all()" in "models.py".
if __name__ == "__main__":
	app.run(debug=True)