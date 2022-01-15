from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.utils import translation
from django.utils.translation import gettext_lazy as _

def home(request):
    context = {
        'home_title': _('home_title'),
        'home_message': _('home_message'),
    }

    return render(request, 'home.html', context=context)
