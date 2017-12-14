from flask import Flask, render_template, request, make_response
from random import randint
import requests
import os.path

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/helloworld")
def helloworld():
    return "Hello World!"


@app.route("/hello/<string:name>/")
def hello(name):
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
    resp.set_cookie('userID', name['nm'])
    resp.set_cookie('userAGE', name['age'])
    return resp


# Display Cookies
@app.route('/getmycookie')
def getmycookie():
    name = request.cookies.get('userID', None)
    age = request.cookies.get('userAGE', None)
    if name is None:
        return '<h1>Welcome -- Your age is -- years </h1>'
    else:
        return '<h1>Welcome ' + name + '. Your age is ' + age + ' years </h1>'


# Show Random Quotes upon Reload
@app.route("/quotes1")
def quotes1():
    myname = 'User'
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"]
    randomnumber1 = randint(0, len(quotes) - 1)
    quote = quotes[randomnumber1]

    return render_template('QuoteTemplate.html', **locals())


@app.route("/quotes_withname/<string:myname>/")
def quotes_withname(myname):
    #    return name
    quotes = [
        "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
        "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
        "'To understand recursion you must first understand recursion..' -- Unknown",
        "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
        "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
        "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"]
    randomnumber = randint(0, len(quotes) - 1)
    quote = quotes[randomnumber]

    return render_template(
        'QuoteTemplate.html', **locals())


@app.route('/student')
def student():
    return render_template('student.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        result1 = request.form
        return render_template("studentresult.html", result=result1)


@app.route('/authors')
def authors():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    payload = {d['id']: {'name': d['name'], 'username': d['username'], 'email': d['email']} for d in data}
    return render_template('viewauthors.html', payload=payload)


@app.route('/posts')
def posts():
    posts1 = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    payload = {d['id']: {'userId': d['userId'], 'title': d['title']} for d in posts1}
    return render_template('viewauthors.html', payload=payload)


@app.route('/count')
def count():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts1 = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    payload = {d['id']: {'name': d['name'], 'count': 0} for d in data}
    for post in posts1:
        payload[post['userId']]['count'] += 1
    return render_template('viewauthors.html', payload=payload)


@app.route('/robotsview')
def robotsview():

    statement1 = 'To Exclude all Robots from the webserver: {User-agent: * , Disallow: /}'
    statement2 = 'To Allow all Robots complete access: {User-agent: * , Disallow: }'
    statement3 = 'To Allow single Robot from the webserver: User-agent: Google Disallow: User-agent: * Disallow:/'
    statement4 = 'To Exclude single Robot from the webserver: User-agent: BadBot Disallow: /'
    filepath = '/Users/indira_n/Sites/mypyfltest/templates/robots.txt'
    if os.path.isfile(filepath):
        # file exists
        lines1 = map(str.split, open('filepath'))
        return render_template('robots.html', lines=lines1, statement1=statement1, statement2=statement2,
                               statement3=statement3, statement4=statement4)

    else:
        return render_template('robots.html', lines='', statement1=statement1, statement2=statement2,
                               statement3=statement3, statement4=statement4)


@app.route('/robotsdeny')
def robotsdeny():
    return 'Robots Deny - Work in Progress'


@app.route('/stdout')
def stdout():
    return 'Post data - Work in Progress'


if __name__ == "__main__":
    app.run()
