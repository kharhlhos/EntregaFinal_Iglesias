from django.shortcuts import render, get_object_or_404, redirect
from .models import Page
from django.contrib.auth.decorators import login_required, user_passes_test
from .forms import PageForm

# Función para verificar si el usuario es administrador
def admin_required(user):
    return user.is_superuser

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def page_list(request):
    pages = Page.objects.all()
    return render(request, 'blog/page_list.html', {'pages': pages})

def page_detail(request, pk):
    page = get_object_or_404(Page, pk=pk)
    return render(request, 'blog/page_detail.html', {'page': page})

@login_required
@user_passes_test(admin_required)
def page_create(request):
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.author = request.user
            page.save()
            return redirect('page_list')
    else:
        form = PageForm()
    return render(request, 'blog/page_form.html', {'form': form})

@login_required
@user_passes_test(admin_required)
def page_update(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        form = PageForm(request.POST, request.FILES, instance=page)
        if form.is_valid():
            form.save()
            return redirect('page_detail', pk=page.pk)
    else:
        form = PageForm(instance=page)
    return render(request, 'blog/page_form.html', {'form': form})

@login_required
@user_passes_test(admin_required)
def page_delete(request, pk):
    page = get_object_or_404(Page, pk=pk)
    if request.method == 'POST':
        page.delete()
        return redirect('page_list')
    return render(request, 'blog/page_confirm_delete.html', {'page': page})