from django.shortcuts import render

# Create your views here.
def Lunches(request):
   return render(request, "./OrganiseLunch/meal_details.html", {})