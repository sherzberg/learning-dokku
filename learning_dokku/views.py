from django.http import HttpResponse

from users.models import User


def home(request):
    count = User.objects.all().count()
    return HttpResponse('Learning Dokku! There are %s Users' % count)
