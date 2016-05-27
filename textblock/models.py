from django.db import models
from django.utils.translation import ugettext_lazy as _


class TextBlock(models.Model):
    """
    TextBlock functionality

    If you need to retrieve one of these, use slug it is guaranteed to be unique
    """

    category = models.CharField(_('category'), max_length=80)
    slug = models.SlugField(_('slug'), max_length=80, db_index=True)
    title = models.CharField(_('title'), max_length=255, blank=True)
    text = models.TextField(_('Message text'), blank=True)

    class Meta:
        verbose_name_plural = _('Text blocks')
        verbose_name = _('Text block')
        ordering = ('category', )

        unique_together = (
            ('category', 'slug'),
        )

    def __unicode__(self):
        return self.title
