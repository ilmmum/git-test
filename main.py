from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask app!"

@app.route('/hello')
def hello():
    return '<p>Hello, Mr Oluwole DevOps, Cloud Engineer and GenAiOps!</p>'

@app.route('/about')
def about():
    return '<p>This is the About page for my Flask app.</p>'

if __name__ == '__main__':
    #app.run(debug=True)git
    app.run(host='0.0.0.0', port=5000)





