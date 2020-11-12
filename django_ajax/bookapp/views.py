from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, BookSerializer
import json

# Create your views here.
def BookPageView(request):
    return render(request,'home.html')


def getAllBooks(request):
    l = list()
    Books = Book.AlLBooks()

    for bk in Books:
        ser = BookSerializer(bk)
        l.append(ser.data)
    return HttpResponse(json.dumps(l))


def deleteBook(request):
    try:
        book = Book.objects.get(id=request.GET['id'])
        book.delete()
        return HttpResponse("true")
    except:
        return HttpResponse("false")











def saveBook(request):
    bk_name = request.GET['bk_name']
    bk_prize = request.GET['bk_prize']
    bk_pages=request.GET['bk_pages']
    book = Book(bk_name=bk_name,bk_prize=bk_prize,bk_pages=bk_pages)
    try:
        book.save()
        return HttpResponse('true')
    except:
        return HttpResponse('False')
