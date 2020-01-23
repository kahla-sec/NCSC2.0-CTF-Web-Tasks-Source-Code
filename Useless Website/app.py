#!/usr/bin/python
# -*- coding:utf-8 -*-
from flask import Flask,session,render_template,request,make_response,render_template_string
import jwt
app = Flask(__name__)
app.secret_key = #NO NO
JWT_Secret = 'kahla'
@app.route('/')
def index():
	session['access'] = False
	if request.cookies.get('token'):
		try:
			token = request.cookies.get('token')
			data = jwt.decode(token,JWT_Secret,algorithms=['HS256'])
			if data['type'] == 'admin':
				session['access'] = True
			else:
				session['access'] = False
			return render_template('accueil.html')
		except Exception:
			return render_template('error.html',msg='Naaaaniii ! are you trying to hack me ?')
	else:
		token = jwt.encode({'type': 'user'}, JWT_Secret, algorithm='HS256')
		response = make_response(render_template('accueil.html'))
		response.set_cookie('token', token)
		return response

@app.route('/secret/')
def secret():
	try:
		if session['access']:
			name = request.args.get('name') or 'Stranger'
			page = render_template('secret.html', name=name)
			return render_template_string(page)
		else:
			return render_template('error.html',msg='Complete the first step please it\'s EZ')
	except Exception:
		return render_template('error.html', msg='An unknown error has occured')


@app.template_filter('read_flag')
def read_flag(str,session_secret_key):
	if session_secret_key == app.secret_key and str == 'Securinets':
		with open('flag', 'r') as flag:
			f=flag.read()
			flag.close()
		return f
	else:
		return 'You Failed ! Script kiddies wont give up'

if __name__=='__main__':
	app.run(debug=True)
