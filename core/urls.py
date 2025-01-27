"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from tkinter.font import names

from django.contrib import admin
from django.urls import path

from mainApp.views import home_view, talaba_view, muallif_view, talabalar_details_view, mualliflar_details_view, \
    kitoblar_view, kitoblar_details_view, recordlar_view, tirik_mualliflar_view, eng_katta_sahifalar_view, \
    eng_kitobi_kop_muallif_view, recordlarning_eng_oxirgilari_view, tirik_mualliflar_kitoblari_view, \
    badiiy_kitoblar_view, yoshi_katta_mualliflar_view, kitobi_kam_mualliflar, record_details_view, \
    bitiruvchi_student_recordlari_view

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
]
