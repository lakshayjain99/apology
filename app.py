from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
from datetime import datetime


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
        {"title": "Funny Dance 1", "file": "badal.mp4"},
        {"title": "Funny Dance 2", "file": "funny_dance_2.mp4"},
        {"title": "Funny Dance 3", "file": "funny_dance_3.mp4"},
]

# Variable to hold the currently playing song
current_song = None

@app.route('/')
def index():
    return render_template('index.html', playlist=playlist)

@app.route('/context')
def context():
    return render_template('context.html')

@app.route('/lyrics')
def lyrics():
    return render_template('lyrics.html')

"""@app.route('/play/<song_name>', methods=['POST'])
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
        return 'Song not found', 404"""

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
            msg.body = "Hello Miss Bisht,\nI really hope this mail finds you very well and great.\n Thank You for accepting my apology. \n\nThank you for your input!\n\nFeedback: {} \n\nI know you must have many questions in your mind now, first of them will be, why now ?\nThe simple answer is, I am shifting back to Hisar for business and you are also thinking of the switch, so this might be our last meeting and I am not able to talk to you comfortably till now because of the guilt I carry of gas-lighting you and abusing you in the past. \nIt was not my anger that I did not try to talk to you in the past 6 months but it was my shame that I didn't gather any courage to confront you and asl for an apology. \nThen finally, after meeting you in metro and the way you didn't ignore me and I realised how gem of a person you are and have always been and how foolish & mean I always was. I literally cried in the office washroom that day. I decided to prepare something to feel sorry for my actions and started working on this. \nI can go on and on but I will not talk much now. \n\nIn the end, I just want to wish you lots and lots of happiness in your life and I really hope that all your wishes come true and I request and wish you unblock me from calling, whatsapp and follow each other over Instagram, so that harr saal 15 September ko call toh kar pau main.\n\nI really hope you will come to my wedding in 2026(baniya kids and their wedding obsession) and abhi ke tarah mana nahi karoge and you will invite me to yours as well.\n\nLots of love and happiness to you and your loved ones.\n\n\n\nKeep Smiling Always and forever, you are cute and looks way cuter when you smile.\n\nThanks & Regards\nLakshay".format(user_feedback)
            mail.send(msg)
            
            return render_template('thank_you.html', feedback=user_input)
        except Exception as e:
            return f"An error occurred: {str(e)}"

    else:
        return render_template('yes.html')


