import datetime
from django import template
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.utils.safestring import SafeData
from django.utils.safestring import SafeText
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.menu.models import menu_principal
from django.urls import reverse
from apps.menu.models import item
from apps.show_items_menu.models import ShowItemMenuGroup

register = template.Library()


@register.simple_tag(takes_context=True)
def getmenuchild(context, *args, **kwargs):
    request = context["request"]
    menuprincipal = menu_principal.objects.all()
    menufinal = ""
    group_list = list(request.user.groups.values_list("name", flat=True))
    if not request.user.is_superuser:
        for men in menuprincipal:
            for group in group_list:
                names_menu_items_principal = list(
                    ShowItemMenuGroup.objects.get(group__name=group).menu_principal.values_list(
                        'nom_menu', flat=True))
                print(names_menu_items_principal)
                print(men)
                if men.nom_menu in names_menu_items_principal:
                    menuitem = item.objects.filter(id_menu=men.id)
                    menufinal = "{}{}".format(menufinal,
                                              '''
                                              <li class='menu-item-has-children dropdown'><a href='#' 
                                              class='dropdown-toggle' data-toggle='dropdown' aria-haspopup='true' 
                                              aria-expanded='false'> <i class='menu-icon fa fa-laptop'></i>{}</a>
                                              '''.format(men.nom_menu.upper()))
                    if menuitem:
                        names_menu_items_item = list(
                            ShowItemMenuGroup.objects.get(group__name=group).menu_item.values_list(
                                'nom_item', flat=True))
                        menufinal = "{}{}".format(menufinal, "<ul class='sub-menu children dropdown-menu'>")
                        for it in menuitem:
                            if it.nom_item in names_menu_items_item:
                                menufinal = "{}{}".format(menufinal, "<li class=''><a href='{}'>{}</a></li>".format(
                                    reverse('items_subitems', args=[it.id]), it.nom_item))
                        menufinal = "{}{}".format(menufinal, "</ul>")
                    menufinal = "{}{}".format(menufinal, "</li>")
    else:
        for men in menuprincipal:
            menuitem = item.objects.filter(id_menu=men.id)
            menufinal = "{}{}".format(menufinal,
                                      "<li class='menu-item-has-children dropdown'><a href='#' class='dropdown-toggle' data-toggle='dropdown' aria-haspopup='true' aria-expanded='false'> <i class='menu-icon fa fa-laptop'></i>{}</a>".format(
                                          men.nom_menu.upper()))
            if menuitem:
                menufinal = "{}{}".format(menufinal, "<ul class='sub-menu children dropdown-menu'>")
                for it in menuitem:
                    menufinal = "{}{}".format(menufinal, "<li class=''><a href='{}'>{}</a></li>".format(
                        reverse('items_subitems', args=[it.id]), it.nom_item))
                menufinal = "{}{}".format(menufinal, "</ul>")
            menufinal = "{}{}".format(menufinal, "</li>")
    return SafeText(menufinal)

