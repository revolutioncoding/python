#The Code Revolution
#Lesson 11
#REST and APIs

"""
In this lesson we'll cover some basics of conecting to a REST API.  This lesson does not cover
REST or APIs specifically.  But some explanation is below.
"""

########################
######## REST ##########
########################
"""
REST is a simple way to expose functionality over the web.  REST uses "existing"
internet http functionality to send and receive data.  It uses http 'verbs' like
GET and POST to retrieve and save information to and from a REST service.  A typical
GET request could look something like:
https://mywebsite.com/task/details/104234
Where:
https://mywebsite.com is the host
/task/details/104234 is the specific item we're trying to connect
In our Python code we will indicate that the call is a GET

This is very similar to putting the same url in your computer's browser your window.  And your
browser does a GET on the URL.  The difference is your browser will get a bunch of HTML back
and know how to display (aka render it) on the screen.  In our REST GET we will get back
json data (which is just formatted data) and just like working with a list or an object instance
we will then use that data in our code.
"""