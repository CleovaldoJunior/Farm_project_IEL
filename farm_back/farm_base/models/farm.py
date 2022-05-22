from django.contrib.gis.db import models
from django.utils.translation import gettext as _

from farm_base.models import Owner


class Farm(models.Model):
    name = models.CharField(verbose_name=_("Name"), max_length=255,
                            null=True, blank=False)

    #Added municipality as an stringField
    municipality = models.CharField(verbose_name=_("Municipality"), max_length=255,
                                    null=True, blank=False)

    #Added owner as an foreign key to owner's id, meaning that it'll only have one owner.
    owner = models.ForeignKey(Owner, to_field='id', on_delete=models.CASCADE, null=True)

    #Added state as an stringFeild
    state = models.CharField(verbose_name=_("State"), max_length=255,
                             null=True, blank=False)

    geometry = models.GeometryField(verbose_name=_("Geometry"),
                                    null=True, blank=False)

    area = models.FloatField(verbose_name=_("Area"),
                             blank=True, null=True)

    centroid = models.PointField(verbose_name=_("Centroid"),
                                 blank=True, null=True)

    creation_date = models.DateTimeField(verbose_name=_("Creation date"),
                                         auto_now_add=True, editable=False)

    last_modification_date = models.DateTimeField(
        verbose_name=_("Last modification date"), auto_now=True)

    is_active = models.BooleanField(verbose_name=_("Is Active"), default=True)



    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['id']
        verbose_name = _('Farm')
        verbose_name_plural = _('Farms')
