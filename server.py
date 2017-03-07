from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/new-movie', methods=['POST'])
def newMovie():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        title = request.form['title']
        year = request.form['year']
        cursor.execute(
            'INSERT INTO movies (title,year) VALUES (?,?)', (title, year))
        connection.commit()
        message = 'Movie added successfully!'
    except:
        connection.rollback()
        message = 'There was an error adding your movie.'
    finally:
        return render_template('result.html', message=message)
        connection.close()


@app.route('/movies')
def movieList():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM movies')
    movieList = cursor.fetchall()
    connection.close()
    return jsonify(movieList)

app.run(debug=True)
