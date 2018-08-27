import fry251
from flask import Flask


app = Flask(__name__)
 
@app.route("/")
def playgame():
    print('Hello let\'s play!')
    play()

if __name__ == "__main__":
    app.run()
