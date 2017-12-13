from flask import Flask, render_template, json, request, make_response, redirect, session, abort
from random import randint
import requests

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/HelloWorld")
def HelloWorld():
    return "Hello World!"

@app.route("/Hello/<string:name>/")
def Hello(name):
    return "Hello " + name + "!"


# Form to enter Name, Age
@app.route('/setcookie', methods=['POST', 'GET'])
def setcookieindex():
   return render_template('cookieindex.html')

# Set Cookies
@app.route('/setmycookie', methods=['POST', 'GET'])
def setmycookie():
    name = request.form
    # Display 'Click here to Read Cookies'
    resp = make_response(render_template('readcookie.html', **locals()))
    resp.set_cookie ('userID', name['nm'])
    resp.set_cookie('userAGE', name['age'])
    return resp

# Display Cookies
@app.route('/getmycookie')
def getmycookie():
   name = request.cookies['userID']
   age = request.cookies['userAGE']
   return '<h1>Welcome '+name+'. Your age is '+ age +' years </h1>'

#Render HTML, Image
# Show Random Quotes upon Reload
@app.route("/Quotes")
def Quotes():
    myname = 'User'
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"]
    randomNumber1 = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber1]

    return render_template('QuoteTemplate.html', **locals())

@app.route("/Quotes/<string:myname>/")
def Quotes_withname(myname):
    #    return name
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"]
    randomNumber = randint(0, len(quotes) - 1)
    quote = quotes[randomNumber]

    return render_template(
        'QuoteTemplate.html', **locals())

@app.route('/student')
def student():
   return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("studentresult.html", result=result)

@app.route('/authors')
def authors():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    payload = {d['id']: {'name': d['name'], 'username': d['username'], 'email': d['email']} for d in data}
    return render_template('viewauthors.html', payload=payload)

@app.route('/posts')
def posts():
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    payload = {d['id']: {'userId': d['userId'], 'title': d['title']} for d in posts}
    return render_template('viewauthors.html', payload=payload)

@app.route('/count')
def count():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    payload = {d['id']: {'name': d['name'], 'count': 0} for d in data}
    for post in posts:
        payload[post['userId']]['count'] += 1
    return render_template('viewauthors.html', payload=payload)

if __name__ == "__main__":
    app.run()