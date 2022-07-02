from django.shortcuts import render

from guest_book.models import Entry


def index_view(request):
    entry = Entry.objects.all()
    context = {"entry": entry}
    return render(request, "index.html", context)


