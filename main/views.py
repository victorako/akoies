from django.views.generic import CreateView, TemplateView
from .models import Contact, Order
from textblock.models import TextBlock

class IndexView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        textblocks = {}
        for block in TextBlock.objects.all():
            textblocks[block.slug] = block
        context['textblocks'] = textblocks
        return context

class ZOEhubView(TemplateView):

    template_name = "zoehub.html"

    def get_context_data(self, **kwargs):
        context = super(ZOEhubView, self).get_context_data(**kwargs)
        textblocks = {}
        for block in TextBlock.objects.all():
            textblocks[block.slug] = block
        context['textblocks'] = textblocks
        return context


class ZOEaiView(TemplateView):

    template_name = "zoeai.html"

    def get_context_data(self, **kwargs):
        context = super(ZOEaiView, self).get_context_data(**kwargs)
        textblocks = {}
        for block in TextBlock.objects.all():
            textblocks[block.slug] = block
        context['textblocks'] = textblocks
        return context


class UsesView(TemplateView):

    template_name = "uses.html"

    def get_context_data(self, **kwargs):
        context = super(UsesView, self).get_context_data(**kwargs)
        textblocks = {}
        for block in TextBlock.objects.all():
            textblocks[block.slug] = block
        context['textblocks'] = textblocks
        return context

class BuyView(CreateView):
    model = Order
    fields = ['firstname', 'lastname', 'email', 'city', 'postcode', 'country', 'address', 'hubs', 'ai', 'cardnumber', 'securitynumber']
    template_name = 'buy.html'
    success_url = '/'


class ContactView(CreateView):
    model = Contact
    fields = ['name', 'email', 'subject', 'message']
    template_name = 'contact.html'
    success_url = '/'
