with open('app1.py', 'w') as ff:
	with open('app.py') as f:
		print(f.read())
		ff.write(f.read())