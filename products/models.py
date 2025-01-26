from django.db import models
from django.utils.translation import gettext_lazy as _


class Category(models.Model):
    parent = models.ForeignKey('self', verbose_name=_('parent'),
                               blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='categories/')
    is_enabled = models.BooleanField(_('is enabled'), default=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        db_table = 'categories'
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(_('title'), max_length=100)
    description = models.TextField(_('description'), blank=True)
    avatar = models.ImageField(_('avatar'), blank=True, upload_to='products/')
    is_enabled = models.BooleanField(_('is enabled'), default=True)
    categories = models.ManyToManyField(Category, verbose_name=_('categories'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        db_table = 'products'
        verbose_name = _('product')
        verbose_name_plural = _('products')

    def __str__(self):
        return self.title

class File(models.Model):
    FILE_AUDIO = 1
    FILE_VIDEO = 2
    FILE_PDF = 3
    FILE_TYPE = (
        (FILE_AUDIO, _('Audio file')),
        (FILE_VIDEO, _('Video file')),
        (FILE_PDF, _('PDF file')),
    )
    product = models.ForeignKey(Product, verbose_name=_('product'),related_name='files' ,on_delete=models.CASCADE)
    title = models.CharField(_('title'), max_length=100)
    file_type = models.PositiveSmallIntegerField(_('file type'), choices=FILE_TYPE, default=FILE_VIDEO)
    file = models.FileField(_('file'), upload_to='files/%Y/%m/%d')
    is_enabled = models.BooleanField(_('is enabled'), default=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated at'), auto_now=True)

    class Meta:
        db_table = 'files'
        verbose_name = _('file')
        verbose_name_plural = _('files')

    def __str__(self):
        return self.title
