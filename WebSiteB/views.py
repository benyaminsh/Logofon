from django.shortcuts import render




def NotFound(request,exception):
    return render(request,'404_page/404.html')