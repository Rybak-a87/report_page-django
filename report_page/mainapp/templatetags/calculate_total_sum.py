from django import template


register = template.Library()


@register.simple_tag()
def sum_attrs(lst):
    """подсчет общих данных записей"""
    return {
        "distance": sum([i.distance for i in lst]),
        "duration": sum([i.duration for i in lst]),
        "average_speed": round(sum([i.average_speed for i in lst]) / lst.count(), 2),
    }
