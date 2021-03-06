from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.urls import reverse

from basketapp.models import Basket
from mainapp.models import Product


@login_required
def basket_view(request):
    title = 'basket'
    basket_items = Basket.objects.filter(user=request.user). \
        order_by('product__category')

    my_context = {
        'title': title,
        'basket_items': basket_items,
    }

    return render(request, 'basketapp/basket.html', my_context)


@login_required
def basket_add_view(request, pk):
    if 'login' in request.META.get('HTTP_REFERER'):
        return HttpResponseRedirect(reverse('products:product', args=[pk]))

    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, product=product).first()

    if not basket:
        basket = Basket(user=request.user, product=product)

    basket.quantity += 1
    basket.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_remove_view(request, pk):
    basket_record = get_object_or_404(Basket, pk=pk)
    basket_record.delete()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def basket_edit_view(request, pk):
    if request.is_ajax():
        quantity = int(request.GET.get('quantity'))
        new_basket_item = Basket.objects.get(pk=int(pk))

        if quantity > 0:
            new_basket_item.quantity = quantity
            new_basket_item.save()
        else:
            new_basket_item.delete()

        basket_items = Basket.objects.filter(user=request.user).order_by('product__category')

        my_content = {
            'basket_items': basket_items,
        }

        result = render_to_string('basketapp/includes/inc_basket_list.html', my_content)

        return JsonResponse({'result': result})
