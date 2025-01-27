from contextlib import contextmanager
from idlelib.query import Query

from django.shortcuts import render
from .models import *
from django.db.models import Q


def home_view(request):
    return render(request, 'index.html')


def talaba_view(request):
    talabalar = Talaba.objects.all()
    context = {
        "talabalar": talabalar,
    }
    return render(request, 'talabalar.html', context=context)


def muallif_view(request):
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar,
    }
    return render(request, 'mualliflar.html', context=context)


def talabalar_details_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        "talaba": talaba
    }
    return render(request, 'talaba_details.html', context=context)


def mualliflar_details_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        'muallif': muallif
    }
    return render(request, 'muallif_details.html', context=context)

def kitoblar_view(request):
    kitoblar = Kitob.objects.all()
    context = {
        "kitoblar" : kitoblar
    }
    return render(request, 'kitoblar.html', context=context)

def kitoblar_details_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        'kitob' : kitob
    }
    return render(request, 'kitoblar_details.html', context=context)

def recordlar_view(request):
    recordlar = Record.objects.all()
    context = {
        'recordlar' : recordlar
    }
    return render(request, 'recordlar.html', context=context)

def tirik_mualliflar_view(request):
    tirik_mualliflar = Muallif.objects.filter(tirik=True)
    context = {
        "tirik_mualliflar" : tirik_mualliflar
    }
    return render(request, 'tirik_mualliflar.html', context=context)

def eng_katta_sahifalar_view(request):
    katta_kitoblar = Kitob.objects.order_by('-sahifa').filter( Q(id=1) | Q(id=2) | Q(id=3) )
    context = {
        "katta_kitoblar" : katta_kitoblar
    }
    return  render(request, 'katta_kitoblar.html', context=context)

def eng_kitobi_kop_muallif_view(request):
    kitobi_kop_mualliflar = Muallif.objects.order_by('-kitob_soni').filter(Q(id=1) | Q(id=2) | Q(id=4))
    context = {
        "kitobi_kop_mualliflar" : kitobi_kop_mualliflar
    }
    return render(request, 'kitobi_kop_muallif.html', context=context)

def recordlarning_eng_oxirgilari_view(request):
    recordlarning_eng_oxirgilari = Record.objects.order_by('-olingan_sana').filter(Q(id=1) | Q(id=2) | Q(id=3))
    context = {
        "recordlarning_eng_oxirgilari" : recordlarning_eng_oxirgilari
    }
    return render(request, 'recordlarning_eng_oxirgilari.html', context=context)

def tirik_mualliflar_kitoblari_view(request):
    tirik_mualliflar_kitoblari = Kitob.objects.filter(muallif__tirik=True)
    context = {
        "tirik_mualliflar_kitoblari" : tirik_mualliflar_kitoblari
    }
    return render(request, 'tirik_mualliflar_kitoblari.html', context=context)

def badiiy_kitoblar_view(request):
    badiiy_kitoblar = Kitob.objects.filter(janr__in=['badiiy'])
    context = {
        "badiiy_kitoblar" : badiiy_kitoblar
    }
    return render(request, 'badiiy_kitoblar.html', context=context)

def yoshi_katta_mualliflar_view(request):
    yoshi_katta_mualliflar = Muallif.objects.order_by('-t_sana').filter(Q(id=1) | Q(id=2) |Q(id=4))
    context = {
        "yoshi_katta_mualliflar" : yoshi_katta_mualliflar
    }
    return render(request, 'yoshi_katta_mualliflar.html', context=context)

def kitobi_kam_mualliflar(request):
    kitobi_kam_mualliflar = Kitob.objects.filter(muallif__kitob_soni__lte=10)
    context = {
        "kitobi_kam_mualliflar" : kitobi_kam_mualliflar
    }
    return render(request, 'kitobi_kam_mualliflar.html', context=context)


def record_details_view(request, record_id):
    record_detail = Record.objects.get(id=record_id)
    context = {
        "record_detail" : record_detail
    }
    return render(request, 'record_details.html', context=context)

def bitiruvchi_student_recordlari_view(request):
    bitiruvchi_student_recordlari = Record.objects.filter(talaba__kurs=4)
    context = {
        "bitiruvchi_student_recordlari" : bitiruvchi_student_recordlari
    }
    return render(request, 'bitiruvchi_student_recordlari.html', context=context)
