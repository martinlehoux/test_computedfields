from advert.models import Advert, Tag

Advert.objects.all().delete()
Tag.objects.all().delete()

tags = [
    Tag.objects.create(name="tag1"),
    Tag.objects.create(name="tag2"),
]

print("advert 1 setup")
advert_1 = Advert.objects.create()
advert_1.tags.add(*tags)

print("advert 2 setup")
advert_2 = Advert.objects.create()
advert_2.tags.add(*tags)

print("advert 1 update")
advert_1.tags.set([tags[0]])
