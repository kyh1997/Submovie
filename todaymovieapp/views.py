from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render


# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from todaymovieapp.decorators import todaymovie_ownership_required
from todaymovieapp.forms import TodaymovieUpdateForm

has_ownership = [todaymovie_ownership_required, login_required]

@login_required
def main(request):
    if request.method == "POST":
        return render(request, 'todaymovieapp/login.html')
    else:
        return HttpResponseRedirect(reverse('todaymovieapp:main'))

class TodaymovieCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('todaymovieapp:main')
    template_name = 'todaymovieapp/create.html'

class TodaymovieDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'todaymovieapp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class TodaymovieDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('todaymovieapp:login')
    template_name = 'todaymovieapp/delete.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class TodaymovieUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = TodaymovieUpdateForm
    success_url = reverse_lazy('todaymovieapp:main')
    template_name = 'todaymovieapp/update.html'