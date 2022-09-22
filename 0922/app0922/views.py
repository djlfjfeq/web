from operator import length_hint
from random import random, randrange
from re import T
from django.shortcuts import render

# Create your views here.


def a(request):
    t={
        'img' : 'https://src.hidoc.co.kr/image/board/2021/8/27/1630049957798_0.jpg'
    }
    return render(request, '1.html', t)
 

def b(request):
    
    lst = [[],[],[],[],[]]
    for n in range(len(lst)):
        for i in range(6):
            lst[n].append(randrange(1,45))
        
    r = {
        'lst1' : lst[0],
        'lst2' : lst[1],
        'lst3' : lst[2],
        'lst4' : lst[3],
        'lst5' : lst[4],
    }
        
    return render(request, '2.html', r)