from django.shortcuts import render
from pyrpc.views import MethodViewSet
from library.methods import Library

# Create your views here.

class LibraryViewSet(MethodViewSet):
    method_class = Library