#!/usr/bin/env python
#Registro las clases para que se muestren en el admin

from django.contrib import admin
from demo.apps.home.models import userProfile

admin.site.register(userProfile)


