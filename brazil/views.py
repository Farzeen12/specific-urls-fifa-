from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def worldcup(request):
    return HttpResponse('''<h1>BRAZIL WON THE WORLDCUP IN 2002</h1>
    <img src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSeXxsz01qd8Zxg6PR46_2Kf0mgtcgJSmArLQ&s'>''')