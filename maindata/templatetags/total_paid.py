
from django import template

register = template.Library()

@register.filter
def total_paid(selloperations):
    total_paid = 0
    for selloperation in selloperations :
        total_paid = total_paid + selloperation.paid


    return float(total_paid)

