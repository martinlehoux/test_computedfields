from django.db import models
from computedfields.models import ComputedFieldsModel, computed

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=50)


class Advert(ComputedFieldsModel):
    tags = models.ManyToManyField(Tag, blank=True)

    @computed(models.CharField(max_length=50), depends=[["tags", ["name"]]])
    def all_tags(self):
        if not self.pk:
            return ""

        all_tags = ", ".join([tag.name for tag in self.tags.all()])
        print(f"{self=}, {all_tags=}")
        return all_tags
