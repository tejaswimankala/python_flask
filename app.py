import sqlite3
sqlite3.connect(":memory:")
from flask import Flask, render_template, request

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)


@app.route('/')
def index():
    #redis.incr('hits')
    conn = get_db_connection()
    posts = conn.execute('SELECT *  FROM Users ').fetchall()
    conn.close()
    return render_template('index.html')

@app.route('/login' , methods=['POST'])
def login():
    name=request.form['name']
    email=request.form['email']
    conn = get_db_connection()
    conn.execute('INSERT INTO Users (name, email) VALUES (?, ?)',
                         (name, email))
    conn.commit()                     
    conn.close()
    return render_template('select.html')

@app.route('/select', methods=['POST'])
def select():
   
    user_input=request.form['item']
    range = request.form['range']
    conn = get_db_connection()
    if user_input == "Sugar" and range == "Min":

        res = conn.execute('SELECT * from store_groceries WHERE price=(SELECT MIN(price) from store_groceries WHERE grocery_item="Sugar") AND grocery_item="Sugar"').fetchall()
        
    elif user_input == "Sugar" and range == "Max":
        
         res = conn.execute('SELECT * from store_groceries WHERE price=(SELECT MAX(price) from store_groceries WHERE grocery_item="Sugar") AND grocery_item="Sugar"').fetchall()
         
    elif user_input=="Rice" and range == "Min":

        res = conn.execute('SELECT * from store_groceries WHERE price=(SELECT MIN(price) from store_groceries WHERE grocery_item="Rice" ) AND grocery_item="Rice"').fetchall()

    elif user_input == "Rice" and range == "Max":
        
        res = conn.execute('SELECT * from store_groceries WHERE price=(SELECT MAX(price) from store_groceries WHERE grocery_item="Rice") AND grocery_item="Rice"').fetchall()
    
    elif user_input=="Bread" and range == "Min":

        res = conn.execute('SELECT * from store_groceries WHERE price=(SELECT MIN(price) from store_groceries WHERE grocery_item="Bread") AND grocery_item="Bread"').fetchall()
    else :
        
         res = conn.execute('SELECT * from store_groceries WHERE price=(SELECT MAX(price) from store_groceries WHERE grocery_item="Bread") AND grocery_item="Bread"').fetchall()
         
    conn.commit()
    conn.close()
    return render_template('result.html', result=res)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)



    
