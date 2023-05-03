from django.contrib.auth.decorators import login_required
from django.shortcuts import HttpResponseRedirect
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

from common.views import TitleMixin
from products.models import Basket, Product, ProductCategory


class IndexView(TitleMixin, TemplateView):
    template_name = 'products/index.html'
    title = 'SibDoski'


class SnowboardsView(TitleMixin, TemplateView):
    template_name = 'equip/snowboard.html'
    title = 'SibDoski'


class BootsView(TitleMixin, TemplateView):
    template_name = 'equip/equip.html'
    title = 'SibDoski'


class GlasesView(TitleMixin, TemplateView):
    template_name = 'equip/glases.html'
    title = 'SibDoski'


class GlovesView(TitleMixin, TemplateView):
    template_name = 'equip/gloves.html'
    title = 'SibDoski'


class KrasnoyarskView(TitleMixin, TemplateView):
    template_name = 'places/krasnoyarsk.html'
    title = 'SibDoski'


class DivnogorskView(TitleMixin, TemplateView):
    template_name = 'places/divnogorsk.html'
    title = 'SibDoski'


class SheregeshView(TitleMixin, TemplateView):
    template_name = 'places/sheregesh.html'
    title = 'SibDoski'


class FreerideView(TitleMixin, TemplateView):
    template_name = 'technique/freeride.html'
    title = 'SibDoski'


class CarvingView(TitleMixin, TemplateView):
    template_name = 'technique/carving.html'
    title = 'SibDoski'


class FreestyleView(TitleMixin, TemplateView):
    template_name = 'technique/freestyle.html'
    title = 'SibDoski'


class ProductsListView(TitleMixin, ListView):
    model = Product
    template_name = 'products/products.html'
    paginate_by = 1
    title = 'SibDoski - Каталог'

    def get_queryset(self):
        queryset = super(ProductsListView, self).get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id) if category_id else queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsListView, self).get_context_data()
        context['categories'] = ProductCategory.objects.all()
        return context


@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
