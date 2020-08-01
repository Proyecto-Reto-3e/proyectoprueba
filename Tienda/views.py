from django.shortcuts import render, HttpResponse

# Create your views here.

html_base="""
     <h1>Tienda Virtual Liz Fashion</h1>
     <ul>
            <l1>    <a href="/">Portada</a>   </l1>
            <l1>     <a href="/about-me/">Acerca de </a>  </l1>
            <l1>     <a href="/contact/">Contacto</a>   </l1>
            <l1>    <a href="/">Servicio/">Servicio</a>   </l1>
            <l1>    <a href="/">index/">index</a>   </l1>
            
     </ul>
"""




def home(request):
    html_responsde="<h1>la paguina de Portada</h1>"
    html_responsde= html_base + html_responsde
    return HttpResponse(html_responsde);

def about(request):
    html_responsde="<h1>la paguina de Acerca de</h1>"
    html_responsde= html_base + html_responsde
    return HttpResponse(html_responsde);

def contact(request):
    html_responsde="<h1>la paguina de contacto</h1>"
    html_responsde= html_base + html_responsde
    return HttpResponse(html_responsde);

def Servicio(request):
    html_responsde="<h1>la paguina de servicio</h1>"
    html_responsde= html_base + html_responsde
    return HttpResponse(html_responsde);

def index(request):
    html_responsde="<h1>la paguina de index</h1>"
    html_responsde= html_base + html_responsde
    return HttpResponse(html_responsde);




def home(request,plantilla="home.html"):
    return render(request,plantilla)

def about(request,plantilla="about.html"):
    return render(request,plantilla)

def contact(request,plantilla="contact.html"):
    return render(request,plantilla)

def Servicio(request,plantilla="Servicio.html"):
    return render(request,plantilla)

def index(request,plantilla="index.html"):
    return render(request,plantilla)


