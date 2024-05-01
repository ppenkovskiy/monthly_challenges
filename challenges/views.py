from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

monthly_challenges = {
    'january': 'Walk for at least 10 minutes every day!',
    'february': 'Walk for at least 20 minutes every day!',
    'march': 'Walk for at least 30 minutes every day!',
    'april': 'Walk for at least 40 minutes every day!',
    'may': 'Walk for at least 50 minutes every day!',
    'june': 'Walk for at least 60 minutes every day!',
    'july': 'Walk for at least 70 minutes every day!',
    'august': 'Walk for at least 80 minutes every day!',
    'september': 'Walk for at least 90 minutes every day!',
    'october': 'Walk for at least 100 minutes every day!',
    'november': 'Walk for at least 110 minutes every day!',
    'december': None
}

months = list(monthly_challenges.keys())


def index(request):
    return render(request, 'challenges/index.html', {
        'months': months
    })


def monthly_challenge_by_number(request, month):
    if month > len(months):
        return HttpResponseNotFound('<h1>Invalid month.</h1>')

    redirect_month = months[month - 1]
    redirect_path = reverse(viewname="month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, 'challenges/challenge.html', {
            'challenge_text': challenge_text,
            'month': month
        })
    except:
        raise Http404()
