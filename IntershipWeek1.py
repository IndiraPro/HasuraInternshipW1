from flask import Flask, render_template, json, request, make_response, redirect, session, abort
from random import randint

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

@app.route("/authors")
def FetchAuthors():
    return 'Authors'


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
@app.route('/getcookie')
def getcookie():
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

if __name__ == "__main__":
    app.run()