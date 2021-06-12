from django.shortcuts import render, reverse
from django.http import HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
# from django.template.loader import render_to_string

monthly_challenges = {
    'january' : 'Eat no meat for this month',
    'february' : 'Walk for atleast 15 min this month',
    'march' : 'Learn Django for atleast 1 hour every day!',
    'april' : 'Meditate for atleast 15 minutes every day!',
    'may' : None,
}

def index(request):
    months = list(monthly_challenges.keys())
    return render(request, 'challenges/index.html', {
        'months': months
    })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound('<h1> Invalid Month </h1>')

    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month]) # /challenge/january
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]

        return render(request, 'challenges/challenge.html', {
            'text': challenge_text, 'month_name': month
        })
    except:
        raise Http404()
        # response_data= render_to_string('404.html')
        # return HttpResponseNotFound(response_data)
