from flask import Flask, render_template, redirect,request


# create the app
app = Flask(__name__)

#controladores
from controller.userController import userController
app.register_blueprint(userController)

@app.route("/",methods=["GET","POST"])
def hello_world():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5002)
