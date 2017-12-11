Python Flask Study
This Repository is helpful for learning Python-Flask, NodeJs-Express.

The programs are developed as part pf Hasura Internship 2017
InternshipWeek1.py contains python-flask routers for various exercises mentioned below.

Development Environment
-----------------------
Flask 0.12.2
Python 2.7.10 (default, Jul 15 2017, 17:16:57)
HTML 5.0

Exercises for Reference
------------------------
1) A simple hello-world at http://localhost:8080/ that displays a simple string like "Hello World - Arpit"; replace "Arpit" with your own first name).

2) Add a route, for e.g. http://localhost:8080/authors, which:
fetches a list of authors from a request to https://jsonplaceholder.typicode.com/users
fetches a list of posts from a request to https://jsonplaceholder.typicode.com/posts
Respond with only a list of authors and the count of their posts (a newline for each author).

3) Set a simple cookie (if it has not already been set) at http://localhost:8080/setcookie with the following values: name=<your-first-name> and age=<your-age>.

4) Fetch the set cookie with http://localhost:8080/getcookies and display the stored key-values in it.

5) Deny requests to your http://localhost:8080/robots.txt page. (or you can use the response at http://httpbin.org/deny if needed)

6) Render an HTML page at http://localhost:8080/html or an image at http://localhost:8080/image.

7) A text box at http://localhost:8080/input which sends the data as POST to any endpoint of your choice. This endpoint should log the received the received to stdout.

Please note that http://localhost:8080/ is just an example, you can run the flask, express web-servers at their default ports on your local machine. You will receive more instructions on deploying your app after the deadline.