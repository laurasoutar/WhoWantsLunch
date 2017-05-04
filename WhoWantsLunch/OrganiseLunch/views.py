from django.shortcuts import render

# Create your views here.
def Lunches(request):
   return render(request, "./meal_details.html", {})