from contextlib import contextmanager
from idlelib.query import Query

from django.shortcuts import render, get_object_or_404, redirect
from urllib3 import request

from .forms import TalabaForm, MuallifForm, RecordForm, Kitobform
from .models import *
from django.db.models import Q


def home_view(request):
    return render(request, 'index.html')

def talaba_view(request):
    form = TalabaForm
    if request.method == 'POST':
        talaba_form = TalabaForm(request.POST)
        if talaba_form.is_valid():
            talaba_form.save()
        return redirect('talabalar')
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
        "form" : form
    }
    return render(request, 'talabalar.html', context=context)

def talaba_update_view(request, pk):
    form = TalabaForm
    talaba = get_object_or_404(Talaba, id=pk)
    if request.method == 'POST':
        talaba_form = TalabaForm(request.POST, instance=talaba)
        if talaba_form.is_valid():
            talaba_form.save()
        return redirect('talabalar')
    else:
        form = TalabaForm(instance=talaba)

    talaba = Talaba.objects.get(id=pk)
    context = {
        "talaba" : talaba,
        "form" : form
    }
    return render(request, 'talaba_update.html', context=context)

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

def mualliflar_qoshish_view(request):
    form = MuallifForm()
    if request.method == 'POST':
        muallif_model = MuallifForm(request.POST)
        if muallif_model.is_valid():
            muallif_model.save()
        return redirect('/mualliflar/')
    context = {
        "form" : form
    }
    return render(request, 'muallif_qoshish.html', context=context)

def mualliflar_update_view(request, pk):
    form = MuallifForm()
    muallif = get_object_or_404(Muallif, id=pk)
    if request.method == 'POST':
        muallif_model = MuallifForm(request.POST, instance= muallif)
        if muallif_model.is_valid():
            muallif_model.save()
        return redirect('/mualliflar/')
    else:
        form = MuallifForm(instance= muallif)
    muallif = Muallif.objects.get(id=pk)
    if muallif.jins == "Erkak":
        jinsi = "Ayol"
    else:
        jinsi = "Erkak"
    context = {
        "muallif" : muallif,
        "form" : form,
        "jinsi" : jinsi
    }
    return render(request, 'muallif_tahrirlash.html', context=context)

def mualliflar_delete_tasdiqlash_view(request, pk):
    muallif = Muallif.objects.get(id=pk)
    context = {
        "muallif" : muallif
    }
    return render(request, "muallif_o'chirish_tasdiqlash.html", context=context)

def mualliflar_delete_view(request, pk):
    muallif = Muallif.objects.get(id=pk)
    muallif.delete()
    return redirect('/mualliflar/')

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

def kitoblar_update_view(request, pk):
    form = Kitobform()
    kitob = get_object_or_404(Kitob, id= pk)
    if request.method == 'POST':
        kitob_model = Kitobform(request.POST, instance=kitob)
        if kitob_model.is_valid():
            kitob_model.save()
        return redirect('kitoblar')
    else:
        form = Kitobform(instance=kitob)
    kitob = get_object_or_404(Kitob, id=pk)
    mualliflar = Muallif.objects.exclude(id=kitob.muallif.id)
    context = {
        "kitob" : kitob,
        "mualliflar" : mualliflar,
        "form" : form
    }
    return render(request, 'kitob_update.html', context=context)

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

def record_update_view(request, pk):
    if request.method == 'POST':
        record=Record.objects.filter(id=pk)
        record.update(
            talaba=Talaba.objects.get(ism=request.POST.get('talaba')),
            kitob=Kitob.objects.get(nom=request.POST.get('kitob')),
            kutubxonachi=Kutubxonachi.objects.filter(ism=request.POST.get('kutubxonachi')),
            qaytarilgan_sana=request.POST.get('qayatrilgan_sana'),
            qaytardi=request.POST.get('qaytardi') == 'on'
        )
        return redirect('recordlar')
    record = get_object_or_404(Record, id=pk)
    context = {
        "record" : record
    }
    return render(request, 'record_update.html', context=context)

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

def kitob_qoshish_view(request):
    form = Kitobform()
    if request.method == 'POST':
        kitob_model = Kitobform(request.POST)
        if kitob_model.is_valid():
            kitob_model.save()
        return redirect('kitoblar')
    mualliflar = Muallif.objects.all()
    context = {
        "mualliflar" : mualliflar,
        "form" : form
    }
    return render(request, 'kitob_qoshish.html', context=context)

def record_qoshish_view(request):
    form = RecordForm()
    if request.method == 'POST':
        record_model = RecordForm(request.POST)
        if record_model.is_valid():
            record_model.save()
        return redirect('recordlar')

    talabalar = Talaba.objects.all()
    kitoblar = Kitob.objects.all()
    kutubxonachilar = Kutubxonachi.objects.all()
    context = {
        "talabalar" : talabalar,
        "kutubxonachilar" : kutubxonachilar,
        "kitoblar" : kitoblar,
        "form" : form
    }
    return render(request, 'record_qoshish.html', context=context)

def kutubxonachi_qoshish_view(request):
    if request.method == 'POST':
        Kutubxonachi.objects.create(
            ism=request.POST.get('ism'),
            ish_vaqti=Kutubxonachi.objects.get(id=request.POST.get('ish_vaqti')).ish_vaqti
        )
        return redirect('kutubxonachilar')
    kutubxonachilar = Kutubxonachi.objects.all()
    context = {
        "kutubxonachilar" : kutubxonachilar
    }
    return render(request, 'kutubxonachi_qoshish.html', context=context)

def kutubxonachi_delete_tasdiqlash_view(request, pk):
    kutubxonachi = Kutubxonachi.objects.get(id=pk)
    context = {
        "kutubxonachi" : kutubxonachi
    }
    return render(request, "kutubxonachi_o'chirish_tasdiqlash.html", context=context)

def kutubxonachi_delete_view(request, pk):
    kutubxonachi = Kutubxonachi.objects.get(id=pk)
    kutubxonachi.delete()
    return redirect('/kutubxonachilar/')

def kutubxonachi_tahrirlash_view(request, pk):
    if request.method == 'POST':
        kutubxonachi = Kutubxonachi.objects.get(id=pk)
        kutubxonachi.update(
            ism=request.POST.get('ism'),
            ish_vaqti=request.POST.get('ish_vaqti')
        )
        return redirect('kutubxonachilar')
    kutubxonachi = Kutubxonachi.objects.get(id=pk)
    if kutubxonachi.ish_vaqti == '08:00 - 13:00':
        ish_vaqtlari = "13:00 - 18:00"
    elif kutubxonachi.ish_vaqti != '08:00 - 13:00':
        ish_vaqtlari = "08:00 - 13:00"
    print(ish_vaqtlari)
    print(kutubxonachi.ish_vaqti)

    context = {
        "kutubxonachi" : kutubxonachi,
        "ish_vaqt" : ish_vaqtlari
    }
    return render(request, 'kutubxonachi_tahrirlash.html', context=context)








