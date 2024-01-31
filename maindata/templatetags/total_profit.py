
from django import template

register = template.Library()

@register.filter
def total_profit(selloperations):
    total_profit = 0
    for selloperation in selloperations :
        total_profit = total_profit + selloperation.profit()


    return float(total_profit)

