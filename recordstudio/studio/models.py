from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class tags(models.Model):
    name = models.CharField(max_length=30)
    pic = models.ImageField(upload_to='posts/')

    def __str__(self):
        return self.name

    def save_tag(self):
        self.save()

    def delete_tag(self):
        self.delete()

    @classmethod
    def display_tags(cls):
        all_tags = tags.objects.all()
        return all_tags

    @classmethod
    def search_for_tag(cls, search_term):
        tags = cls.objects.filter(name__icontains=search_term)
        return tags


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return self.first_name


class Studio(models.Model):
    name = models.CharField(max_length=60)
    location = models.CharField(max_length=60)
    tags = models.ManyToManyField(tags)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    studio_image = models.ImageField(upload_to='posts/', null=True)
    phone = PhoneNumberField(max_length=30, default=True, blank=True)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    @classmethod
    def get_studios(cls):
        studios = cls.objects.all()


@classmethod
def search_by_name(cls, search_term):
    picture = cls.objects.filter(name_icontains=search_term)

    return picture
