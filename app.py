from flask import Flask

app= Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return "this is a flask application"

if __name__ == '__main__':
    app.run(debug=True)