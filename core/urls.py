from tkinter.font import names

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
    path('muallif/qoshish/', mualliflar_qoshish_view),
    path('mualliflar/<int:pk>/o\'chirish/tasdiqlash/', mualliflar_delete_tasdiqlash_view),
    path('mualliflar/<int:pk>/o\'chirish/', mualliflar_delete_view),
    path('mualliflar/<int:pk>/tahrirlash/', mualliflar_update_view),
    path('kitoblar/', kitoblar_view, name="kitoblar"),
    path('kitoblar/<int:kitob_id>/', kitoblar_details_view),
    path('kitoblar/<int:pk>/tahrirlash/', kitoblar_update_view),
    path('recordlar/', recordlar_view, name="recordlar"),
    path('recordlar/<int:pk>/update/', record_update_view),
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
    path('kutubxonachilar/', kutubxonachilar_view, name="kutubxonachilar"),
    path("talabalar/<int:pk>/o'chirish/", talaba_delete_view),
    path("talabalar/<int:pk>/tahrirlash/", talaba_update_view),
    path("talabalar/<int:pk>/o'chirish/tasdiqlash/", talaba_delete_tasdiqlash_view),
    path('kitoblar/kitob_qoshish/', kitob_qoshish_view, name='kitob_qoshish'),
    path("recordlar/record_qoshish/", record_qoshish_view, name='record_qoshish'),
    path('kutubxonachilar/kutubxonachi_qoshish/', kutubxonachi_qoshish_view, name="kutubxonachi_qoshish"),
    path('kutubxonachilar/<int:pk>/o\'chirish/', kutubxonachi_delete_view),
    path('kutubxonachilar/<int:pk>/o\'chirish/tasdiqlash/', kutubxonachi_delete_tasdiqlash_view),
    path('kutubxonachilar/<int:pk>/tahrirlash/', kutubxonachi_tahrirlash_view)
]
