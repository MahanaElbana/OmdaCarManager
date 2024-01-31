
from django import template

register = template.Library()

@register.filter
def add_charge(selloperations):
    total_charge = 0
    for selloperation in selloperations :
        try:
            total_charge = total_charge + selloperation.charge()
        except:
            pass


    return float(total_charge)

