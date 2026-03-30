from django.shortcuts import render
from visit.models import PageVisit


def home(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path=request.path)
    my_title = "My page"
    my_context = {
        "page_title": my_title, 
        "page_visit_count": page_qs.count(),
        "percent": (page_qs.count() * 100.0) / qs.count(),
        "total_visit_count": qs.count()
    }
    my_template = "home.html"
    PageVisit.objects.create(path=request.path)
    return render(request, my_template, my_context)
