"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Charles Williams',
    'bio' : 'While I have been dabbling with front-end development since 2005, \
             I just graduated from Indiana University last year with a B.S. in \
             Informatics, along with a cognate in English.  I have experience \
             with C#, Microsoft Access development & runtime, Microsoft SQL, \
             .NET, PHP, JavaScript, HTML, CSS, jQuery, AJAX, and other front- \
             end related frameworks and technologies.  I just started working \
             for the University of Notre Dame this year as a Research Programmer.  \
             Django is our go to framework for web development with PostgreSQL, \
             but we also use PHP, Nodejs, MongoDB, Mean.js, AngularJS, \
             and many others.',
    'email' : 'cwilli34@nd.edu', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'charlwillia6', # No @ symbol, just the handle.
    'github_username' : "cwilli34",
    'headshot_url' : 'https://avatars3.githubusercontent.com/u/9610352?v=3&s=460', # Link to your GitHub, Twitter, or Gravatar profile image.
}

def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,
                'year': datetime.now().year,
            })
    )
