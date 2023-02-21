from msilib.schema import ListView
from django.views import generic
from JKeys.models import Id
from django.shortcuts import render

class WebSite(generic.ListView):
    template_name = "jkeys/home.html"
    context_object_name = "websitelist"

    def get_queryset(self):
        return Id.objects.all()


class Element(generic.DetailView):
    template_name = "jkeys/element.html"
    #context_object_name = "element"
    model = Id


class CreateElement(generic.CreateView):
    template_name = "jkeys/create.html"
    fields = ["name", "mail", "password", "link"]
    model = Id

    success_url = "/"

    def save_element(request):
      if request.method == "POST":
            name= request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            link = request.POST.get('link')

            Id.objects.create(name=name,email=email,password=password,link=link)
      return render(request,'jkeys/home.html')


class DeleteElement(generic.DeleteView):
    template_name = "jkeys/delete.html"
    success_url = "/"
    model = Id

class EditElement(generic.UpdateView):
    template_name = "jkeys/edit.html"
    fields = ["name", "mail", "password", "link"]
    model = Id

    success_url = "/"

    def save_element(request):
      if request.method == "POST":
            name= request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            link = request.POST.get('link')

            Id.objects.create(name=name,email=email,password=password,link=link)
      return render(request,'jkeys/element.html')


    """def check(request):
        context = {
            'posts': Id.objects.all()
        }
        if request.method == "POST":
            name = request.POST.get('name')
            mail = request.POST.get('mail')
            password = request.POST.get('password')
            link = request.POST.get('link')

            Id.objects.create(name=name, mail=mail, password=password, link=link)
        return render(request, 'edit.html', context)"""