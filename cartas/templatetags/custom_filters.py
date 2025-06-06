from django import template

register = template.Library()

@register.filter
def batch(iterable, n):
    """
    Divide una lista en lotes de tamaño n.
    Ejemplo: [1,2,3,4,5] con n=2 => [[1,2], [3,4], [5]]
    """
    n = int(n)
    result = []
    for i in range(0, len(iterable), n):
        result.append(iterable[i:i + n])
    return result
