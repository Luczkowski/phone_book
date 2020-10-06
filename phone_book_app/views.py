from django.shortcuts import render, get_object_or_404, redirect
from .models import Osoba, Telefon, Email
from .forms import OsobaForm, TelefonForm, EmailForm
from django.views.generic import TemplateView, ListView
from django.db.models import Q


def phone_book(request):
    persons_list = Osoba.objects.all()
    return render(request, 'phone_book.html', {'persons_list': persons_list})


def new_person(request):
    form = OsobaForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect(phone_book)

    return render(request, 'person_form.html', {'form': form, 'new': True})


def edit_person(request, id):
    person = get_object_or_404(Osoba, pk=id)
    form = OsobaForm(request.POST or None, instance=person)

    if form.is_valid():
        form.save()
        return redirect(detail, id)

    return render(request, 'person_form.html', {'form': form, 'person': person, 'new': False})


def delete_person(request, id):
    person = get_object_or_404(Osoba, pk=id)

    if request.method == "POST":
        person.delete()
        return redirect(phone_book)

    return render(request, 'delete.html', {'person': person})


def detail(request, id):
    person = get_object_or_404(Osoba, pk=id)
    phones_list = Telefon.objects.filter(osoba=person)
    emails_list = Email.objects.filter(osoba=person)

    return render(request, 'detail.html', {'person': person, 'phones_list': phones_list, 'emails_list': emails_list})


def new_phone(request, id):
    person = get_object_or_404(Osoba, pk=id)
    form = TelefonForm(request.POST or None)

    if form.is_valid():
        phone = form.save(commit=False)
        phone.osoba = person
        phone.save()

        return redirect(detail, id)

    return render(request, 'phone_form.html', {'form': form, 'person': person})


def new_email(request, id):
    person = get_object_or_404(Osoba, pk=id)
    form = EmailForm(request.POST or None)

    if form.is_valid():
        email = form.save(commit=False)
        email.osoba = person
        email.save()

        return redirect(detail, id)

    return render(request, 'email_form.html', {'form': form, 'person': person})


class SearchResultsView(ListView):
    # model = Osoba
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')

        phones = []
        emails = []

        if query is not None:

            imie_results = Osoba.objects.filter(Q(imie__icontains=query))
            nazwisko_results = Osoba.objects.filter(Q(nazwisko__icontains=query))
            telefon_results = Telefon.objects.filter(Q(telefon__icontains=query))
            email_results = Email.objects.filter(Q(email__icontains=query))

            if telefon_results:
                for i in range(len(telefon_results)):
                    telefon = telefon_results[i].telefon
                    phones.append(get_object_or_404(Osoba, id=Telefon.objects.get(telefon=telefon).osoba.id))
                return phones

            if email_results:
                for i in range(len(email_results)):
                    email = email_results[i].email
                    emails.append(get_object_or_404(Osoba, id=Email.objects.get(email=email).osoba.id))
                return emails

            results_list = imie_results or nazwisko_results or phones or emails

            return results_list
        return models.Osoba.objects.all()
