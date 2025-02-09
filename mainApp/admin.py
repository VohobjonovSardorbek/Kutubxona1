
from django.contrib import admin
from .models import *

class TalabaAdmin(admin.ModelAdmin):
    list_display = ['ism', 'kurs', 'guruh']
    list_display_links = ['ism', 'kurs', 'guruh']


class TalabaInline(admin.StackedInline):
    model = Talaba
    extra = 2
    fields = ['talaba']


class KitobAdmin(admin.ModelAdmin):
    list_display = ['nom', 'muallif', 'sahifa', 'janr']
    list_display_links = ['muallif', 'nom']
    list_filter = ['janr', 'muallif']
    list_per_page = 3
    list_editable = ['sahifa']
    search_fields = ['nom', 'janr']
    search_help_text = "Kitob nomi yoki janri orqali qidiring"


class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1
    fields = ['kitob']


class MuallifAdmin(admin.ModelAdmin):
    list_display = ['ism', 'davlat', 'kitob_soni', 'tirik', 'id']
    list_display_links = ['ism', 'davlat', 'id']
    search_fields = ['ism']
    list_filter = ['tirik']
    list_editable = ['kitob_soni', 'tirik']
    inlines = [KitobInline]


class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ['ism']
    list_display_links = ['ism']
    search_fields = ['ism']
    list_filter = ['ish_vaqti']


class KutubxonachiInline(admin.StackedInline):
    model = Kutubxonachi
    extra = 1
    fields = ['kutubxonachi']


class RecordAdmin(admin.ModelAdmin):
    list_display = ['talaba', 'kitob', 'kutubxonachi']
    list_display_links = ['talaba', 'kitob', 'kutubxonachi']
    search_fields = ['talaba', 'kitob', 'kutubxonachi']
    list_filter = ['talaba', 'kitob', 'kutubxonachi']


admin.site.register(Kitob, KitobAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Kutubxonachi, KutubxonachiAdmin)
admin.site.register(Record, RecordAdmin)
