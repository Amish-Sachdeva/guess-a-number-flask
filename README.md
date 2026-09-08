# guess-a-number-flask

My First Flask Server 🚀

This is my first server built with Flask and Python.

I created a simple number guessing game where the server generates a random number between 0 and 9, and the user tries to guess it.

🛠️ Technologies Used
Python
Flask
🎮 How It Works

When the server starts, it randomly selects a number between 0 and 9.

The user can enter a number in the URL.

For example:

http://127.0.0.1:5000/5

The server responds with:

Too Low — if the guess is smaller than the random number.
Too High — if the guess is larger than the random number.
You found me! 🎉 — if the guess is correct.
📁 Project Structure
my-first-flask-server/
│
├── server.py
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md

▶️ Run the Server

Run:

python server.py

You should see Flask running locally.

Open this in your browser:

http://127.0.0.1:5000/
🎯 Example

Open:

http://127.0.0.1:5000/3

The server will tell you whether your guess is too high, too low, or correct.

📚 What I Learned

This project helped me learn the basics of:

Creating a Flask application
Starting a web server with Python
Using Flask routes
Handling URL parameters
Generating random numbers with Python
Returning HTML responses from Flask
Running a local development server