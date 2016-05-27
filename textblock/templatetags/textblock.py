from django import template
from django.conf import settings
from django.utils.html import mark_safe

from ..models import TextBlock

from django.core import urlresolvers

register = template.Library()

def admin_inline(text, user, idblock):
    if user.is_staff:
        return mark_safe('<a href="/admin/textblock/textblock/'+str(idblock)+'/">'+text+'</a>')
        # return '<span class="admin-inline-edit" data-inline-edit="/admin/textblock/textblock/'+str(idblock)+'/">'+text+'</span>'
    else:
        return text

@register.simple_tag()
def block_title(slug, user, textblocks, wrapper_type="edit"):
    if slug in textblocks:
        block = textblocks[slug]
        if wrapper_type == "edit":
            return admin_inline(mark_safe(block.title), user, block.id)
        else:
            return mark_safe(block.title)
    return slug


@register.simple_tag()
def block_text(slug, user, textblocks, wrapper_type="edit"):
    if slug in textblocks:
        block = textblocks[slug]
        if wrapper_type == "edit":
            return admin_inline(mark_safe(block.text), user, block.id)
        else:
            return mark_safe(block.text)

    return slug


@register.simple_tag()
def url_edit_textblock(slug, user, textblocks):
    if not user.is_staff:
        return ""
        
    if slug in textblocks:
        block = textblocks[slug]
        return urlresolvers.reverse('admin:textblock_textblock_change', args=(block.id,))

    return ""