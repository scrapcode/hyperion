from django.http import HttpResponse

"""
Root view for Hyperion
"""
def index(request):
    return HttpResponse("Hyperion Core. (Placeholder)")