from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect


monthly_challenges = {
    'january' : '<h1> Eat no meat for this month </h1>',
    'february' : '<h1> Walk for atleast 15 min this month </h1>',
    'march' : '<h1> Learn Django for atleast 1 hour every day! </h1>',
    'april' : '<h1> Meditate for atleast 15 minutes every day! </h1>',
    'may' : '<h1> Workout for atleast 30 minutes every day! </h1>',
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    redirect_month = months[month-1]
    return HttpResponseRedirect('/challenges/' + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text =  monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound('<h1> This month is not supported </h1>')
