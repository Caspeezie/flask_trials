from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<b>My First Website</b>"

@app.route("/about")
def about_us():
    return "<p>This is the About page of my first website!</p>"

@app.route("/contacts")
def contacts():
    return "<p>The developer contact numbers are listed below: <li>Sadeeq: 0703 451 5037</li><li>Nanlung: 0808 124 8695</li><li>Tokkitda: 0703 596 3936</li></p>"
    

@app.route("/products")
def products():
    return "<p>A variety of products are up for display on this page</p>"

@app.route("/services")
def services():
    return "<p>Our services include:</p>"