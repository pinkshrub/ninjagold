from flask import Flask, render_template, request, redirect, session
import random
app = Flask(__name__)
app.secret_key = 'RobBoss'

@app.route('/')
def index():
	try:
		session['earnings']
	except:
		session['earnings'] = 0
	try: 
		session['activities']
	except:
		session['activities'] = []
	return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def bank():
	if request.form['action'] == 'farm':
		print 'farming'
		session['earnings'] += random.randrange(10,21)
		session['activities'].append(' farmed')
		return redirect('/')
	elif request.form['action'] == 'cave':
		print 'caving'
		session['earnings'] += random.randrange(5,11)
		session['activities'].append('caved')
		return redirect('/')
	elif request.form['action'] == 'house':
		print 'housing'
		session['earnings'] +=random.randrange(2,5)
		session['activities'].append('housed')
		return redirect('/')
	elif request.form['action'] == 'dragon':
		print 'dragoned'
		session['earnings'] = 0
		session['activities'].append('dumbfuck why\'d you fight a dragon?')
		return redirect('/')
	else: 
		print 'gambling ;)'
		session['earnings'] += random.randrange(-50,50)
		session['activities'].append('casinoed')
		return redirect('/')

app.run(debug=True)