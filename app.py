from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    # Fetch restaurant names from the database
    conn = sqlite3.connect('eat_task.db')
    cur = conn.cursor()
    cur.execute("SELECT name FROM restaurant")
    rows = cur.fetchall()
    restaurant_names = [row[0] for row in rows]
    conn.close()
    return render_template('index.html', restaurant_names=restaurant_names)

@app.route('/restaurant', methods=['POST'])
def show_restaurant_details():
    # Retrieve selected restaurant name from the form
    selected_restaurant = request.form['restaurant']

    # Fetch details of the selected restaurant from the database
    conn = sqlite3.connect('eat_task.db')
    cur = conn.cursor()
    cur.execute("SELECT cuisines, rating, address FROM restaurant WHERE name=?", (selected_restaurant,))
    row = cur.fetchone()
    conn.close()

    cuisines, rating, address = row
    return render_template('restaurant.html', name=selected_restaurant, cuisines=cuisines, rating=rating, address=address)

if __name__ == '__main__':
    app.run(debug=True)
