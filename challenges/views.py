from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound


monthly_challenges= {
    "january":'Fast everyday for 6 hours',
    "february":'Walk for 20 mins everyday',
    "march":'Learn Django for 20 mins everyday',
    "april":'Fast everyday for 6 hours',
    "may":'Walk for 20 mins everyday',
    "june":'Learn Django for 20 mins everyday',
    "july":'Learn Django for 20 mins everyday',
    "august":'Learn Django for 20 mins everyday',
    "september":'Learn Django for 20 mins everyday',
    "october":"Resting Month",
    "november":'Learn Django for 20 mins everyday',
    "december":"Prepare next year"
}
# Create your views here.
def monthly_challenges_by_number(request,month):
    return HttpResponse(month)

def monthly_challenge(request,month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month is not supported!!")