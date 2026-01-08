from django.shortcuts import render, get_object_or_404
from .models import Page

def home(request):
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")

def page_list(request):
    q = request.GET.get("q", "").strip()
    pages = Page.objects.all().order_by("-created_at")
    if q:
        pages = pages.filter(title__icontains=q)
    return render(request, "pages/page_list.html", {"pages": pages, "q": q})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, "pages/page_detail.html", {"page": page})

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView

from .forms import PageForm
from .models import Page

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("page_list")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = "pages/page_form.html"
    success_url = reverse_lazy("page_list")

    def test_func(self):
        page = self.get_object()
        return page.author == self.request.user

class PageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Page
    template_name = "pages/page_confirm_delete.html"
    success_url = reverse_lazy("page_list")

    def test_func(self):
        page = self.get_object()
        return page.author == self.request.user

# Create your views here.
