
from django import template

register = template.Library()

@register.filter
def total_sell_price(selloperations):
    total_sell_price = 0
    for selloperation in selloperations :
        total_sell_price = total_sell_price + selloperation.sell_price


    return float(total_sell_price)
    
    
