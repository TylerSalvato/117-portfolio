from django.shortcuts import render

# Create your views here.

def projects_list(request):
    return render(request, 'projects/list.html')
