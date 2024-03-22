import flask

app=flask.Flask(__name__)

@app.route("/")
def hello():
    return"你好"
@app.route("/hi")
def hi():
    return "Hi，你好"
@app.route('/gdp2.html')
def gbd():
    with open('..//gdp.html', 'r', encoding='utf-8') as f:
        content = f.read()
    return content
@app.route('/index.html')
def index():
    with open('..//index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    return content
if __name__=="__main__":
    app.run()
    # uvicorn.run(app, host='127.0.0.1', port=8080)
