import random
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

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
#     return render(request, "contact.html", context)

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        num = None
        some_list = [
            random.randint(0, 1000000),
            random.randint(0, 1000000),
            random.randint(0, 1000000)
        ]
        condition_bool_item = True
        if condition_bool_item:
            num = random.randint(0, 1000000)
        context = {
            "num": num,
            "some_list": some_list
        }
        return context

# class AboutView(TemplateView):
#     template_name = 'about.html'

# class ContactView(TemplateView):
#     template_name = 'contact.html'









