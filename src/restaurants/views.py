import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

from .models import RestaurantLocation
# # Create your views here.
# # function based view hard-coded
# # def home_old(request):
# #     html_var = 'f strings'
# #     html_ = f"""<!DOCTYPE html>
# #     <html lang=en>

# #     <head>
# #     </head>
# #     <body>
# #     <h1>Hello World!</h1>
# #     <p>This is {html_var} html coming through</p>
# #     </body>
# #     </html>
# #     """
# #     return HttpResponse(html_)
#     #return render(request, "home.html", {})#response

# # This is how to render html via templates

# def home(request):
#     num = None
#     some_list = [
#         random.randint(0, 1000000),
#         random.randint(0, 1000000),
#         random.randint(0, 1000000)
#     ]
#     condition_bool_item = True
#     if condition_bool_item:
#         num = random.randint(0, 1000000)
#     context = {
#         "num": num,
#         "some_list": some_list
#     }
#     return render(request, "home.html", context)

# def about(request):
#     context = {
#     }
#     return render(request, "about.html", context)

# def contact(request):
#     context = {
#     }
#    return render(request, "contact.html", context)

def restaurant_listview(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        "object_list": queryset
    }
    return render(request, template_name, context)
