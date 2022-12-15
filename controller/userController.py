from flask import Flask, Blueprint, render_template, request, redirect, url_for, flash, session, g
import requests as r
userController = Blueprint('user',__name__,url_prefix='/user')

@userController.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        data ={
            'username': '',
            'password': ''
        }
        data['username'] = request.form['username']
        data['password']= request.form['password']
        url = "http://localhost:5001/user/login"
        res =r.post(url=url,json=data)
        print(res.text)
    
    return render_template('login.html')

@userController.route("/register", methods=['GET','POST'])
def register():
    if request.method == 'POST':
        data ={
            'username': '',
            'password': ''
        }
        data['username'] = request.form['username']
        data['password']= request.form['password']
        data['fullname']= request.form['fullname']
        url = "http://localhost:5001/user"
        res =r.post(url=url,json=data)
        if res.status_code == 200:
            redirect(url_for('index'))
    return render_template('register.html')