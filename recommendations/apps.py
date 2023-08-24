from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

API_KEY = "3e27ec0a6c968cd2aff3079277a2b014"
BASE_URL = "http://ws.audioscrobbler.com/2.0/"

@app.route("/")
def home():
    param = {
        "method": "chart.getTopTracks",
        # "tag": "disco",
        "api_key": API_KEY,
        "format": "json",
        "limit": 15  
    }

    response = requests.get(BASE_URL, params=param)
    data = response.json()

    popular_songs = []
    for track in data["tracks"]["track"]:
        song_name = track["name"]
        artist_name = track["artist"]["name"]
        image_url = track["image"][2]["#text"]  
        popular_songs.append({"song_name": song_name, "artist_name": artist_name, "image_url": image_url})

    paramss = {
        "method": "tag.gettopalbums",
        "tag": "disco",
        "api_key": API_KEY,
        "format": "json",
        "limit": 15
    }

    response_albums = requests.get(BASE_URL, params=paramss)
    data_albums = response_albums.json()

    top_albums = []
    for album in data_albums["albums"]["album"]:
        album_name = album["name"]
        artist_name = album["artist"]["name"]
        image_url = album["image"][2]["#text"]  
        top_albums.append({"album_name": album_name, "artist_name": artist_name, "image_url": image_url})

    return render_template("home.html", popular_songs=popular_songs, top_albums=top_albums)

@app.route("/chat")
def chat():
    return render_template("chatbot.html")

@app.route('/head')
def head():
    return render_template('header.html')

@app.route('/songs')
def song():
    return render_template('song.html')

@app.route('/artist')
def artist():
    return render_template('artist.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/music')
def music_website():
   
    songs = [
        {
            'songName': 'On My Way ',
            'poster': '/static/img/1.jpg',
            'audio': '/static/audio/1.mp3'
        },
        {
            'songName': 'Alan Walker-Fade',
            'poster': '/static/img/2.jpg',
            'audio': '/static/audio/2.mp3'
        },
         {
            'songName': 'Cartoon - On & On ',
            'poster': '/static/img/3.jpg',
            'audio': '/static/audio/3.mp3'
        },
        {
            'songName': 'Warriyo - Mortals',
            'poster': '/static/img/4.jpg',
            'audio': '/static/audio/4.mp3'
        },
        {
            'songName': 'Electronic Music ',
            'poster': '/static/img/6.jpg',
            'audio': '/static/audio/6.mp3'
        },
         {
            'songName': 'Agar Tum Sath Ho',
            'poster': '/static/img/7.jpg',
            'audio': '/static/audio/7.mp3'
        },
        {
            'songName': 'Suna Hai',
            'poster': '/static/img/8.jpg',
            'audio': '/static/audio/8.mp3'
        },
        {
            'songName': 'Dilber',
            'poster': '/static/img/9.jpg',
            'audio': '/static/audio/9.mp3'
        },
        {
            'songName': 'Duniya',
            'poster': '/static/img/10.jpg',
            'audio': '/static/audio/10.mp3'
        },
        {
            'songName': 'Lagdi Lahore Di',
            'poster': '/static/img/11.jpg',
            'audio': '/static/audio/11.mp3'
        },
        {
            'songName': 'Putt Jatt Da',
            'poster': '/static/img/12.jpg',
            'audio': '/static/audio/12.mp3'
        },
        {
            'songName': 'Baarishein',
            'poster': '/static/img/13.jpg',
            'audio': '/static/audio/13.mp3'
        },
        
    ]
    return render_template('music_website.html', songs=songs)

@app.route("/recommendation")
def recommend():
    song_type = request.args.get("songType")
    if song_type:
        try:
            params = {
                "method": "tag.getTopTracks",
                "tag": song_type,
                "api_key": API_KEY,
                "format": "json"
            }

            response = requests.get(BASE_URL, params=params)
            data = response.json()

            recommendations = []
            for track in data["tracks"]["track"]:
                recommendations.append(track["name"] + " - " + track["artist"]["name"])

            return render_template("recommendations.html", recommendations=recommendations)

        except Exception as e:
            return "Error fetching recommendations: " + str(e)
    else:
        return "Invalid song type parameter"

def create_song_types_table():
    conn = sqlite3.connect("emotions.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS song_types (
            id INTEGER PRIMARY KEY,
            userName TEXT,
            songType TEXT
        )
    ''')
    conn.commit()
    conn.close()


@app.route("/save_song_type", methods=["POST"])
def save_song_type():
    create_song_types_table()

    data = request.json
    user_name = data["userName"]
    song_type = data["songType"]

    conn = sqlite3.connect("emotions.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO song_types (userName, songType) VALUES (?, ?)", (user_name, song_type))
    conn.commit()
    conn.close()

    response_data = {"message": "Song type saved successfully"}
    return jsonify(response_data)
import requests

DB_NAME = 'login.db'

def create_tables():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS login (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL
                    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS signup (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name TEXT NOT NULL,
                        last_name TEXT NOT NULL,
                        phone_number TEXT NOT NULL,
                        email TEXT NOT NULL,
                        password TEXT NOT NULL
                    )''')
    conn.commit()
    conn.close()

create_tables()

@app.route('/submit')
def submit():
    first_name = request.get.args('first_name')
    last_name = request.get.args('last_name')
    phone_number = request.get.args('phone_number')
    email = request.get.args('email')
    password = request.get.args('password')
    print(first_name)
    
    ret1 = "Success"
    
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('INSERT INTO signup (first_name, last_name, phone_number, email, password) VALUES (?, ?, ?, ?, ?)',
                       (first_name, last_name, phone_number, email, password))
        conn.commit()

        ret1="success"
    except Exception as e:
        print("Error:", e)
        ret1 = "Error"

    return jsonify(result=ret1)
    

@app.route('/lgn')
def lgn():
    email = request.args.get('log_email')
    password = request.args.get('log_password')
    ret="Success"
    print(email)
    try:
        conn = sqlite3.connect("login.db")
        cursor = conn.cursor()
        
        ret=cursor.execute("INSERT INTO login(email, password) VALUES (?, ?)",
                         (email, password))
            
        inserted_id = cursor.lastrowid
        print(inserted_id )
        conn.commit()   

        ret = "Success"
    except Exception as e:
        print("Error:", e)
        ret = "Error"

    return jsonify(result=ret)

  

if __name__ == "__main__":
 app.run()


