# import mysql.connector
from flask import Flask
import random
# import time
# import connection


# time.sleep(10)
# cnx = mysql.connector.connect(
#     user='root',
#     password='my-secret',
#     host='db-mysql',
#     database='mysql'
# )
app = Flask(__name__)

background_color = [
'lightblue',
'BlanchedAlmond',
'YellowGreen',
'Coral',
'PeachPuff'
]

color = random.choice(background_color)
    
@app.route("/")
def hello_world():
    return """
    <body style="background-color: {};">
    <center><h1 style='font-size: 4em; color: black;'>Hello, Universe!</h1></center>
    </body>
    """.format(color)


# @app.route("/create-db")
# def create_db():
#     connection.create_connection()
#     return "DB created successfully"


# @app.route("/test")
# def test():
#     cur = cnx.cursor()
#     cur.execute("SELECT * FROM user_table")
#     data = cur.fetchall()
#     return list(data)


@app.route("/<name>")
def hello(name):
    return f"Hello, {name}!!!"


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
