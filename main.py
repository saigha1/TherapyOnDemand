from flask import Flask
import views

app = Flask("__main__")

@app.route("/")
def home():
    return "<h1>Hello World</h1>"
    
if __name__ == '__main__':
    app.run()