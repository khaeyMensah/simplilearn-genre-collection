from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Collection, Piece
from django.views import generic
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.views.generic import View

# Create your views here.
class index(generic.ListView):
    template_name = 'genre/genretemplate.html'
    
    def get_queryset(self):
        return Collection.objects.all()
    
    
    # all_collection = Collection.objects.all()
    # context = {
    #     'all_collection': all_collection, 
    # }
    # return render(request, 'genre/genretemplate.html', context)
    

class details(generic.DetailView):
    model = Collection
    template_name = 'genre/detailtemplate.html'
    
    
    
#    Citem = Collection.objects.get(pk=genre_id)
#    Pitem = Piece.objects.filter(collection=Citem)
#    context = {
#        'Pitem': Pitem,
#    }
#    return render(request,'genre/detailtemplate.html',context)


class UserFormView(View):
    form_class = UserForm
    template_name = 'genre/formtemplate.html'  
    def get(self, request):
        form = self.form_class(None)
        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username'] 
            password = form.cleaned_data['password'] 
            user.set_password(password)
            user.save()

            newuser = authenticate(request, username=username, password=password)  # Corrected function call

            if newuser is not None:
                if newuser.is_active:
                    login(request, newuser)
                    return redirect("/genre")

        context = {'form': form}
        return render(request, self.template_name, context)