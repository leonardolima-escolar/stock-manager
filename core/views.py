from django.shortcuts import redirect
from django.views import View

# Create your views here.

class Index(View):
    def get(self, request):
        return redirect('products')
