from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string

monthly_challenges= {
    "january":'Fast everyday for 6 hours',
    "february":'Walk for 20 mins everyday',
    "march":'Learn Django for 20 mins everyday',
    "april":'Fast everyday for 6 hours',
    "may":'Walk for 20 mins everyday',
    "june":'Learn Django for 20 mins everyday',
    "july":'Learn Django for 20 mins everyday',
    "august":'Learn Django for 20 mins everyday',
    "september":'Learn Django for 20 mins everyday', #hash map of list of months
    "october":"Resting Month",
    "november":None,
    "december":"Prepare next year"
}



# Create your views here.
#Main page (index.html)
def index(request):
    list_items = ""
    months=list(monthly_challenges.keys())

    return render(request,"challenges/index.html",{
        "months":months
    })

    # for month in months:
    #     capitlized_month=month.capitalize()
    #     month_path = reverse("monthly-challenges",args=[month])
    #      # makes the whole url same throughout to make the program more dynamic and not make hard code url changes everywhere

    #     list_items+=f"<li><a href=\"{month_path}\">{capitlized_month}</a></li>"
    # response_data=f"<ul>{list_items}</ul>"

    # return HttpResponse(response_data)


#sub pages
def monthly_challenges_by_number(request,month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("invalid month")
    redirect_month = months[month-1]
    redirect_path = reverse("monthly-challenges",args =[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request ,"challenges/challenge.html",{
            "text":challenge_text,
            "month":month
        })
    except:
        raise Http404()