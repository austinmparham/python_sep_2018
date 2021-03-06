from flask import Flask, render_template, request, redirect, session
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL

app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
# mysql = connectToMySQL('mydb')
# # now, we may invoke the query_db method
# print("all the users", mysql.query_db("SELECT * FROM users;"))

@app.route('/')
def index():
    mysql = connectToMySQL("sales")
    customers = mysql.query_db("SELECT customers.name, COUNT(customer_id) as leads from customers left join leads on customers.id = leads.customer_id GROUP BY(customer_id);")
    print("Fetched all customers", customers)
    return render_template('index.html', customers=customers)

@app.route('/create_friend', methods=['POST'])
def create():
    mysql = connectToMySQL("friendsdb")
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
             'first_name': request.form['first_name'],
             'last_name':  request.form['last_name'],
             'occupation': request.form['occupation']
           }
    new_friend_id = mysql.query_db(query, data)
    print("Who's our new friend?", new_friend_id)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)