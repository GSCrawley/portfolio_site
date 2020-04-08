# portfolio_site

(5 Points) How is this project structure different than a Flask (or Node) application? 

A: Django is a full-stack web framework, whereas Flask is a micro and lightweight web framework. The features provided by Django help developers to build large and complex web applications. On the other hand, Flask accelerates development of simple web applications by providing the required functionality.

What role are the urls.py and views.py files responsible for?

A: views.py takes a web request and returns a web response.
   urls.py defines the mapping between URLs and views. 

(5 Points) Why do we use 2 separate urls.py files? How do they interact? A: We use one urls.py file per app. They don't interact with each other, but rather with each app's views.py file.

(5 Points) When is it desirable to split our code over multiple apps? Why would we want to do so? A: Grouping the urls separately can be helpful because it keeps common urls in their own files and avoids the difficulties of making changes to one big urls.py file.
