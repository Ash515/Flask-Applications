from flask import Flask,redirect,url_for
app=Flask(__name__)
@app. route("/")
def home():
    return "<center>Hello Ashwin ! <h1><font color=violet> Welcome dear </font></h1></center>"
@app.route("/<name>")
def Name(name):
    return f"<center><h1><font color=maroon>Hi {name} !!!!</font></h1></center>"
@app.route("/admin")
def admin():
    return redirect(url_for("home"))
if __name__=="__main__":
    app.run()
