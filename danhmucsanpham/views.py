from django.http import HttpResponse
from django.shortcuts import render
from django.views import View



class ClassSaveNews (View):
    def get(self, request):
        return render(request, 'danhmucsanpham/add_news.html')

class IndexClass (View):
    def get(self, request):
        ketqua = "12345"
        return HttpResponse(ketqua)
