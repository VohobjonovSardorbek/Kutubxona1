from contextlib import contextmanager
from idlelib.query import Query

from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.db.models import Q


def home_view(request):
    return render(request, 'index.html')


# def talaba_view(request):
#
#     talabalar = Talaba.objects.all()
#
#     search = request.GET.get('search', '')
#     if search:
#         talabalar = talabalar.filter(ism__contains=search)
#
#     kurs = request.GET.get('kurs', 'all')
#     if kurs == "all":
#         talabalar = talabalar
#     else:
#         talabalar = talabalar.filter(kurs=kurs)
#     guruh = request.GET.get('guruh')
#     if guruh =="all":
#         talabalar = talabalar
#     else:
#         talabalar = talabalar.filter(guruh=guruh)
#
#     guruhlar = Talaba.objects.order_by("guruh").values_list("guruh", flat=True).distinct()
#     kurslar = Talaba.objects.order_by("kurs").values_list("kurs", flat=True).distinct()
#     context = {
#         "talabalar": talabalar,
#         "search": search,
#         "guruhlar" : guruhlar,
#         "kurslar" :kurslar,
#         "kurs_query" : kurs,
#         "guruh_query" : guruh,
#     }
#     return render(request, 'talabalar.html', context=context)

def talaba_view(request):
    talabalar = Talaba.objects.all()

    search = request.GET.get('search', '')
    if search:
        talabalar = talabalar.filter(ism__contains=search)

    kurs = request.GET.get('kurs', 'all')
    if kurs != "all":
        talabalar = talabalar.filter(kurs=kurs)

    guruh = request.GET.get('guruh', 'all')
    if guruh != "all":
        talabalar = talabalar.filter(guruh=guruh)

    guruhlar = Talaba.objects.order_by("guruh").values_list("guruh", flat=True).distinct()
    kurslar = Talaba.objects.order_by("kurs").values_list("kurs", flat=True).distinct()

    context = {
        "talabalar": talabalar,
        "search": search,
        "guruhlar": guruhlar,
        "kurslar": kurslar,
        "kurs_query": kurs,
        "guruh_query": guruh,
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

    search = request.GET.get('search', '')
    if search:
        kitoblar = kitoblar.filter(nom__contains=search)

    boshlanish = request.GET.get('boshlanish', '')
    tugash = request.GET.get('tugash', '')
    if boshlanish:
        if tugash:
            kitoblar = kitoblar.filter(sahifa__gte=boshlanish, sahifa__lte=tugash)
        else:
            kitoblar = kitoblar.filter(sahifa__gte=boshlanish)
    elif tugash:
        kitoblar = kitoblar.filter(sahifa__lte=tugash)

    mualliflar = Muallif.objects.order_by('ism').values_list('ism', flat=True).distinct()
    muallif = request.GET.get('muallif', 'all')
    if muallif != 'all':
        kitoblar = kitoblar.filter(muallif__ism=muallif)

    janrlar = Kitob.objects.order_by('janr').values_list('janr', flat=True).distinct()

    janr = request.GET.get('janr', 'all')
    if janr != 'all':
        kitoblar = kitoblar.filter(janr=janr)

    context = {
        "kitoblar" : kitoblar,
        "search" : search,
        "boshlanish" : boshlanish,
        "tugash" : tugash,
        "mualliflar" : mualliflar,
        "muallif_" : muallif,
        "janrlar" :janrlar,
        "janr_" : janr,
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

def kutubxonachilar_view(request):
    kutubxonachilar = Kutubxonachi.objects.all()
    context = {
        "kutubxonachilar" : kutubxonachilar
    }
    return render(request, 'kutubxonachilar.html', context=context)

def talaba_delete_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    talaba.delete()
    return redirect('/talabalar/')

def talaba_delete_tasdiqlash_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    context = {
        "talaba" : talaba,
    }
    return render(request, 'talaba_delete_tasdiqlash.html', context=context)