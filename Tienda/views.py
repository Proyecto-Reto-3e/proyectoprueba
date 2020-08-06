from django.shortcuts import render, HttpResponse

# Create your views here.

html_base="""
     <h1>Tienda Virtual Liz Fashion</h1>
     <ul>
            <l1>    <a href="/">Portada</a>   </l1>
            <l1>     <a href="/about-me/">Acerca de </a>  </l1>
            <l1>     <a href="/contact/">Contacto</a>   </l1>
            <l1>     <a href="/portfolio/">Portafolio</a>   </l1>
          
            
            
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


def portfolio(request):
    html_responsde="<h1>la paguina de portfolio</h1>"
    html_responsde= html_base + html_responsde
    return HttpResponse(html_responsde);










def home(request,plantilla="home.html"):
    return render(request,plantilla)

def about(request,plantilla="about.html"):
    return render(request,plantilla)

def contact(request,plantilla="contact.html"):
    return render(request,plantilla)

def portfolio(request,plantilla="portfolio.html"):
    return render(request,plantilla)











