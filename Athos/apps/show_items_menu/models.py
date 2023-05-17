from django.db import models
from django.contrib.auth.models import Group, User
from apps.menu.models import menu_principal, item


class ShowItemMenuGroup(models.Model):
    name = models.CharField(max_length=250)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ManyToManyField(User, blank=True)
    menu_principal = models.ManyToManyField(menu_principal)
    menu_item = models.ManyToManyField(item)

    def __str__(self):
        return "{} - {} - {}".format('Menu items para', self.name, self.group.name)

