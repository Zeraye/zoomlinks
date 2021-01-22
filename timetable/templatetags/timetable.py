from django.template.defaulttags import register

@register.filter
def get_item(dictionary, key):
    if dictionary.get(key) == None:
        return ''
    return dictionary.get(key)
