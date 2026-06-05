from flask import Flask, render_template, request
from chatbot import get_response
import sqlite3

app = Flask(__name__)

# Create database table
conn = sqlite3.connect("chatlogs.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS chats(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_message TEXT,
    bot_response TEXT
)
""")

conn.commit()
conn.close()

@app.route("/", methods=["GET", "POST"])
def home():

    response = ""

    if request.method == "POST":

        user_message = request.form["message"]

        response = get_response(user_message)

        # Save chat to database
        conn = sqlite3.connect("chatlogs.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO chats(user_message, bot_response) VALUES (?, ?)",
            (user_message, response)
        )

        conn.commit()
        conn.close()

    return render_template(
        "index.html",
        response=response
    )

if __name__ == "__main__":
    app.run(debug=True)