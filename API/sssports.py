from flask import Flask, render_template
app = Flask(__name__)
 
@app.route("/home")
def home():
	return render_template('home.html') 

#@app.route("/matches")
#def matches():
#	return render_template('matches.html')

#@app.route("/table")
#def matches():
#	return render_template('table.html')

#@app.route("/teams")
#def matches():
#	return render_template('team.html')

if __name__ == "__main__":
	app.run(debug = True)
