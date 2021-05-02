from flask import Flask,render_template

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("welcome.html")

@app.route('/hello/')
def hello():
    return render_template("hello.html")

if __name__=="__main__":
    app.run(debug=True)
