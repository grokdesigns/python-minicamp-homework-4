from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/new-friend', methods=['POST'])
def newFriend():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    try:
        name = request.form['name']
        age = request.form['age']
        cursor.execute(
            'INSERT INTO friends (name,age) VALUES (?,?)', (name, age))
        connection.commit()
        message = 'Friend added successfully!'
    except:
        connection.rollback()
        message = 'There was an error adding your friend.'
    finally:
        return render_template('result.html', message=message)
        connection.close()


@app.route('/friends')
def friendList():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM friends')
    friendsList = cursor.fetchall()
    connection.close()
    return jsonify(friendsList)
    
app.run(debug=True)
