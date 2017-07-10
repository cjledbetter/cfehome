import random
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# function based view hard-coded
# def home_old(request):
#     html_var = 'f strings'
#     html_ = f"""<!DOCTYPE html>
#     <html lang=en>

#     <head>
#     </head>
#     <body>
#     <h1>Hello World!</h1>
#     <p>This is {html_var} html coming through</p>
#     </body>
#     </html>
#     """
#     return HttpResponse(html_)
    #return render(request, "home.html", {})#response

# This is how to render html via templates
def home(request):
    num = random.randint(0, 1000000)
    return render(request, "base.html", {"html_var": True, "num": num})
