from flask import Flask, render_template, request, redirect, session, flash, url_for, Response


api = Flask(__name__)


@api.route('/auth', methods = ['POST', ])
def auth():
    user = request.args.get('usuario')
    password = request.args.get('senha')
    return user == 'Edimar' and password == '12345'


@api.route('/')
def main():
    return '200'


api.run(host = '127.0.0.1', port = 5000, debug = True)
