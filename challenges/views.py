from django.http import HttpResponse, HttpResponseNotFound


def monthly_challenge_by_number(request, month):
    return HttpResponse(month)


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = 'Walk for at least 10 minutes every day!'
    elif month == 'february':
        challenge_text = 'Walk for at least 20 minutes every day!'
    elif month == 'march':
        challenge_text = 'Walk for at least 30 minutes every day!'
    else:
        return HttpResponseNotFound('This month is not supported')
    return HttpResponse(challenge_text)
