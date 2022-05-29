from django.urls import path
from .views import InternList, InternCreate, InternDetail

urlpatterns = [
    path('interns/', InternList.as_view(), name='getinterns'),
    path('create_intern/', InternCreate.as_view(), name='interncreate'),
    path('interns/<int:pk>/', InternDetail.as_view()),
]
