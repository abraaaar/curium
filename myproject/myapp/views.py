from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    html = """
    <html>
    <head>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                font-size: 3em;  /* Adjust size as needed */
            }
        </style>
    </head>
    <body>
        <p>Curium</p>
    </body>
    </html>
"""
    return HttpResponse(html)
