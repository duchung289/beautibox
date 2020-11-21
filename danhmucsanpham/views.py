from django.shortcuts import render
from django.views import View



class ClassSaveNews (View):
    def get(self, request):
        return render(request, 'danhmucsanpham/add_news.html')
