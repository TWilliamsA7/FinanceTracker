from django.contrib import admin
from .models import *

admin.site.register(Account)
admin.site.register(Budget)
admin.site.register(Transaction)