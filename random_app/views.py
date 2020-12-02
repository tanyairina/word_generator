from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# If you don't feel comfortable with multiple apps yet, start a new project with a single app for this assignment.
# Otherwise, add an app to your previous project called 'random_word'. This app will render a template with 
# a random 14-character "word" that also display a counter for the number of words generated. 
# The first time you use this app, it should say 'attempt #1'. 
# Each time you generate a new random keyword, it should increment the attempt figure. 
# The purpose of this assignment is to reinforce your use of session. Don't spend too much time 
# on the random word generator portion--it's okay if your random word is not a real word.

# Helpful Hints:
# For generating a random word, check out this StackOverflow question, which shows us we can:

# import get_random_string from django.utils.crypto (remember that you can import other libraries/modules 
# in your views.py or any other python files)
# use get_random_string(length=14) to get a random string of length 14
# As the goal of this assignment is to really help you get familiar with creating a new app, 
# setting up routing, views, templates, etc, we've given you some hints. :)
# Add functionality so that a request to localhost:8000/random_word/reset resets the counter and 
# redirects back to localhost:8000/random_word.

# Create your views here.

def index(request):
    return redirect('reset')

def rand_word(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    request.session['word'] = get_random_string(length=14)
    return render(request, 'index.html')

def reset(request):
    request.session.flush()
    return redirect('/random_word')
