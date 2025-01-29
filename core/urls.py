from django.contrib import admin
from django.urls import path

from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name="home"),
    path('talabalar/', talaba_view, name="talabalar"),
    path('mualliflar/', muallif_view, name='muallif'),
    path('talabalar/<int:talaba_id>/', talabalar_details_view),
    path('mualliflar/<int:muallif_id>/', mualliflar_details_view),
    path('kitoblar/', kitoblar_view, name="kitoblar"),
    path('kitoblar/<int:kitob_id>/', kitoblar_details_view),
    path('recordlar/', recordlar_view, name="recordlar"),
    path('tirik_mualliflar/', tirik_mualliflar_view, name="tirik_mualliflar"),
    path('katta_kitoblar/', eng_katta_sahifalar_view, name="Eng katta sahifali kitoblar"),
    path('kitobi_kop_mualliflar/', eng_kitobi_kop_muallif_view, name="Eng kitobi ko'p mualliflar"),
    path('recordlarning_eng_oxirgilari/', recordlarning_eng_oxirgilari_view, name="Eng oxirgi uchta recordlar"),
    path('tirik_mualliflar_kitoblari/', tirik_mualliflar_kitoblari_view, name="Tirik mualliflar kitoblari"),
    path('badiiy_kitoblar/', badiiy_kitoblar_view, name="Badiiy kitoblar"),
    path('yoshi_katta_mualliflar/', yoshi_katta_mualliflar_view, name="Yoshi katta uchta mualliflar"),
    path('kitobi_kam_mualliflar/', kitobi_kam_mualliflar, name="Kitobi kam mualliflar"),
    path('recordlar/<int:record_id>', record_details_view, name="Recordlarning detallari"),
    path('bitiruvchi_student_recordlari/', bitiruvchi_student_recordlari_view, name="Bitiruvchi studentlar recordlari"),
    path('kutubxonachilar/', kutubxonachilar_view, name="Kutubxonachilar"),
    path("talabalar/<int:pk>/o'chirish/", talaba_delete_view),
    path("talabalar/<int:pk>/o'chirish/tasdiqlash/", talaba_delete_tasdiqlash_view),
]
