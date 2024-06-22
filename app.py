from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from datetime import datetime
import pygame

app = Flask(__name__, static_url_path='/static')

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Change this to your SMTP server
app.config['MAIL_PORT'] = 587  # Change this to your SMTP port
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '25.ashnil@gmail.com'  # Change this to your email address
app.config['MAIL_PASSWORD'] = 'mngstmufhpkowiqy'  # Change this to your email password

mail = Mail(app)

# Initialize pygame mixer
pygame.mixer.init()

# Playlist of static
playlist = [
    {"title": "Song 1", "url": "/play/song1", "file": "static/sorry_sorry.mp3"},
    {"title": "Song 2", "url": "/play/song2", "file": "static/wishes.mp3"},
    {"title": "Song 3", "url": "/play/song3", "file": "static/song3.mp3"}
]

# Variable to hold the currently playing song
current_song = None

@app.route('/')
def index():
    return render_template('index.html', playlist=playlist)

@app.route('/context')
def context():
    return render_template('context.html')

@app.route('/play/<song_name>', methods=['POST'])
def play(song_name):
    global current_song

    action = request.form.get('action')

    # Find the song object in the playlist
    song = next((s for s in playlist if s['url'] == f"/play/{song_name}"), None)
    if song:
        if action == 'start':
            # Start playing the song
            if current_song != song['file']:
                pygame.mixer.music.load(song['file'])
                pygame.mixer.music.play()
                current_song = song['file']
        elif action == 'stop':
            # Stop playing the song
            pygame.mixer.music.stop()
            current_song = None
        return '', 204
    else:
        return 'Song not found', 404

@app.route('/yes', methods=['GET', 'POST'])
def yes():
    if request.method == 'POST':
        user_input = request.form['user_input']
        user_feedback = request.form['user_feedback']
        print(user_input)
        
        # Send email
        try:
            msg = Message('Thank You for Your Valuable Response', 
                          sender='25.ashnil@gmail.com', 
                          recipients=[user_input, 'lklakshay1999@gmail.com'])
            msg.body = 'Thank you for your input!\n\nFeedback: {} \n\n\n\nThanks & Regards\nLakshay Jain\nThe OG Developer '.format(user_feedback)
            mail.send(msg)
            return "Thank you for your input! An email has been sent to {}".format(user_input)
        except Exception as e:
            return "An error occurred: {}".format(str(e))
    else:
        return render_template('yes.html')

if __name__ == '__main__':
    app.run(debug=True)
