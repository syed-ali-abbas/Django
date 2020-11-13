from django.urls import path
from .views import BookPageView,saveBook, getAllBooks,deleteBook,signupPage, signup,checkemail

urlpatterns=[

    path('',BookPageView,name='home'),
    path('save_book/',saveBook,name='home'),
    path('getAllBooks/',getAllBooks,name='home'),
    path('delete_book/',deleteBook,name='delete_book'),
    path('ShowSignUp/',signupPage,name='ShowSignUp'),
    path('signup/',signup,name='signup'),
    path('checkemail/',checkemail,name='checkemail')
]