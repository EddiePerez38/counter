from flask import Flask, render_template, request, session, redirect
app = Flask(__name__) 

# this needs to be established everytime we setup a session
app.secret_key = "myCounterApp"

@app.route('/')         
def index():
# Very important to note all sessions have an empty dictionary 'counter' in this instance is filling a key void. 
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 0

    return render_template("index.html", num = session['counter'])
    

@app.route('/destroy_route')         
def destroy():
#Session.clear, clears the cache and once an event is triggerd, the "if statement" above goes through its process
    session.clear()

    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)