from django import template
from product.models import Goods
from django.conf import settings
from order.cart import CartManager

register = template.Library()


@register.inclusion_tag('shop/tags/floor_goods.html')
def load_floor_goods(category):
    goods_list = Goods.objects.filter(category = category)

    return {
        'goods_list':goods_list,
        'category':category,
    }


@register.inclusion_tag('shop/tags/floor_goods_detail.html')
def load_floor_goods_detail(goods_list,order_value):
    goods_info = goods_list.get(order_value = order_value)

    return {
        'goods_info':goods_info,
        'order_value': order_value
    }


@register.simple_tag
def get_cart(request):
    cart = CartManager.get_cart(request)

    return cart
