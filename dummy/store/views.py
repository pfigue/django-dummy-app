import json
from django.views.generic import View
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from store.models import Item


class HybridView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(HybridView, self).dispatch(*args, **kwargs)

    def answer(self, request, data, template_file=None):
        template_file = 'default.html' if not template_file else template_file
        accepted_content = request.META.get('HTTP_ACCEPT', None)
        if accepted_content == 'application/json':
            answer = HttpResponse(json.dumps(data), content_type='application/json')
        elif accepted_content == 'text/html':
            answer = render(request, template_file, data)
        else:
            answer = render(request, template_file, data)
        return answer


class StoreItemsListView(HybridView):
    def get(self, request, *args, **kwargs):
        data = [{'name':x.name, 'price':x.price, 'quantity':x.quantity} for x in Item.objects.all()]
        return self.answer(request, data=data)

    def post(self, request, *args, **kwargs):
        new_item = Item()
        new_item.name = request.POST.get('name', None)
        new_item.price = request.POST.get('price', None)
        new_item.quantity = request.POST.get('quantity', None)
        # FIXME validation here
        new_item.save()

        return self.answer(request, data={ 'id': new_item.id, })
