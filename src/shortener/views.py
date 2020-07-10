from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views import View
from .models import JuliURL
from .forms import SubmitUrlForm
from analytics.models import ClickEvent


# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        """ GET method """
        the_form = SubmitUrlForm()
        context = {
            "title": "Juli.co",
            "form": the_form,
        }
        return render(request, 'shortener/home.html', context)

    def post(self, request, *args, **kwars):
        """ POST method """
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Juli.co",
            "form": form,
        }
        template = 'shortener/home.html'

        if form.is_valid():
            print(form.cleaned_data)
            new_url = form.cleaned_data.get('url')
            obj, created = JuliURL.objects.get_or_create(url=new_url)
            context = {
                'object': obj,
                'created': created,
            }
            if created:
                template = 'shortener/success.html'
            else:
                template = 'shortener/already-exists.html'

        return render(request, template, context)


class URLRedirectView(View):
    """ Class Base Views """
    def get(self, request, shortcode=None, *args, **kwargs):
        """ Redirect to url shortcode """
        qs = JuliURL.objects.filter(shortcode=shortcode)
        if qs.count() != 1 and qs.exists():
            raise Http404
        ob = qs.first()
        ClickEvent.objects.create_event(ob)
        return HttpResponseRedirect(ob.url)
