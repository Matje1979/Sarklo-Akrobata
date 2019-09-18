from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render, redirect
from .models import Post, Oglas
from .forms import OglasCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator


#def search(request):
    #return HTT
    

def index(request):
    if Oglas.objects.all():
        queryset_list = Oglas.objects.all().order_by('-date')
    
        query = request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(naslov = query)
            if len(queryset_list) != 0:
                context = {'oglasi': queryset_list}
                return render(request, "sarklo/rezultati_pretrage.html", context)
            else:
                return HttpResponse('<h2>Nista nije pronadjeno.</h2>')
        else:
             if Oglas.objects.all():
        
                oglasi = Oglas.objects.all().order_by('-date')
                paginator = Paginator(oglasi, 6)
                page = request.GET.get('page')
                oglasi = paginator.get_page(page)
                current_page = 'index'
            
                context = {'oglasi': oglasi, 'current_page': current_page}
                
                return render(request, "sarklo/index.html", context)
    return render(request, "sarklo/index.html")
    
def oglas_detalji(request, id):
    
    oglas = get_object_or_404(Oglas, id = id)
                              
    context = {'oglas': oglas}
    return render(request, "sarklo/oglas_detalji.html", context)
    
def deli(request):
    return render(request, "sarklo/delikates.html", {'style': 'sarklo\delikates.css'})
    
def skolske(request):
   
        queryset_list = Oglas.objects.all().order_by('-date')
        query = request.GET.get('q')
        
        if query:
            queryset_list = queryset_list.filter(naslov = query)
            if queryset_list:
                 context = {'oglasi': queryset_list}
                 return render(request, "sarklo/rezultati_pretrage.html", context)
            else:
                return HttpResponse('<h2>Nista nije pronadjeno.</h2>')
            
        else:
            query_list = Oglas.objects.filter(kategorija = 'KS')
            paginator = Paginator(query_list, 6)
            page = request.GET.get('page')
            query_list = paginator.get_page(page)
            context = {'oglasi': query_list, 'title': 'skolske knjige','style': 'sarklo\skolske.css' }
            return render(request, "sarklo/skolske.html", context)
            
    
def beletristika(request):
   
        queryset_list = Oglas.objects.all().order_by('-date')
        query = request.GET.get('q')
        
        if query:
            queryset_list = queryset_list.filter(naslov = query)
            if queryset_list:
                 context = {'oglasi': queryset_list}
                 return render(request, "sarklo/rezultati_pretrage.html", context)
            else:
                return HttpResponse('<h2>Nista nije pronadjeno.</h2>')
            
        else:
            query_list = Oglas.objects.filter(kategorija = 'KO')
            context = {'oglasi': query_list, 'title': 'beletristika','style': 'sarklo\skolske.css' }
            return render(request, "sarklo/beletristika.html", context)
            
def odeca_zenska(request):
   
        queryset_list = Oglas.objects.all().order_by('-date')
        query = request.GET.get('q')
        
        if query:
            queryset_list = queryset_list.filter(naslov = query)
            if queryset_list:
                 context = {'oglasi': queryset_list}
                 return render(request, "sarklo/rezultati_pretrage.html", context)
            else:
                return HttpResponse('<h2>Nista nije pronadjeno.</h2>')
            
        else:
            query_list = Oglas.objects.filter(kategorija = 'OZ')
            context = {'oglasi': query_list }
            return render(request, "sarklo/odeca_zenska.html", context)
            
def odeca_muska(request):
   
        queryset_list = Oglas.objects.all().order_by('-date')
        query = request.GET.get('q')
        
        if query:
            queryset_list = queryset_list.filter(naslov = query)
            if queryset_list:
                 context = {'oglasi': queryset_list}
                 return render(request, "sarklo/rezultati_pretrage.html", context)
            else:
                return HttpResponse('<h2>Nista nije pronadjeno.</h2>')
            
        else:
            query_list = Oglas.objects.filter(kategorija = 'OM')
            context = {'oglasi': query_list }
            return render(request, "sarklo/odeca_muska.html", context)
            
def tehnika(request):
    queryset_list = Oglas.objects.all().order_by('-date')
    query = request.GET.get('q')
    
    if query:
        queryset_list = queryset_list.filter(naslov = query)
        if queryset_list:
             context = {'oglasi': queryset_list}
             return render(request, "sarklo/rezultati_pretrage.html", context)
        else:
            return HttpResponse('<h2>Nista nije pronadjeno.</h2>')
    else:
        query_list = Oglas.objects.filter(kategorija = 'TE')
        current_page = 'tehnika'
        context = {'oglasi': query_list, 'current_page': current_page }
        return render(request, "sarklo/odeca_muska.html", context)

def osn_1_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "prvi razred osnovne skole:"
        query_list = query_list.filter(naslov__icontains=razred )
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)

def osn_2_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "drugi razred osnovne skole:"
        query_list = query_list.filter(naslov__icontains=razred )
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)
        
def osn_3_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "treci razred osnovne skole:"
        query_list = query_list.filter(naslov__icontains=razred )
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)
        
def osn_4_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "cetvrti razred osnovne skole:"
        query_list = query_list.filter(naslov__icontains=razred )
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)
        
def osn_5_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "peti razred osnovne skole:"
        query_list = query_list.filter(naslov__icontains=razred )
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)
        
def osn_6_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "sesti razred osnovne skole:"
        query_list = query_list.filter(naslov__icontains=razred )
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)

def osn_7_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "sedmi razred osnovne skole:"
        query_list = query_list.filter(naslov__icontains=razred )
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)


def osn_8_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "osmi razred osnovne skole:"
        query_list = query_list.filter(naslov__icontains=razred )
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)
        

def sred_1_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "1. razred sr. skole:"
        query_list = query_list.filter(naslov__icontains=razred )
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)

def sred_2_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "2. razred sr. skole:"
        query_list = query_list.filter(naslov__icontains=razred )
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)
        
def sred_3_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "3. razred sr. skole:"
        query_list = query_list.filter(naslov__icontains=razred )
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)
        
def sred_4_razred(request):
        query_list = Oglas.objects.filter(kategorija = 'KS')
        razred = "4. razred sr. skole:"
        query_list = query_list.filter(naslov__icontains="4. razred sr. skole")
        context = {'oglasi': query_list, 'razred': razred }
        return render(request, "sarklo/skolske_razredi.html", context)





def comments(request):
    context = {
        'posts': Post.objects.all()
}
    return render(request, "sarklo/komentari.html", context)
 
@login_required
def create_oglas(request):
    if request.method == "POST":
        print ("True")
        form = OglasCreateForm(request.POST, request.FILES)
        #naslov = form.cleaned_data.get('naslov')
        #print (form)
        if form.is_valid(): 
            print ("form is valid")
            form.save()
            #naslov = form.cleaned_data.get('naslov')
            #messages.success(request, f'Kreiran oglas { naslov }!')
            return redirect ('shop-index')
        else:
            print ("Form is invalid")
    else:
        form = OglasCreateForm()
    return render(request, 'Sarklo/oglas_form.html', {'form': form})