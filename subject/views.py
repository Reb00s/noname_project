from django.http import HttpResponse


def subjects(request):
    return HttpResponse(f"subject_list")


def subject_card(request):
    return HttpResponse("subject_card")
