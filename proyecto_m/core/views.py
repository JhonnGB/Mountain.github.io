from django.shortcuts import render, HttpResponse
from productos.models import hamburguesas
# Create your views here.

#menu para todas las paginas web
def hamburguesa_s(request):
    produ = hamburguesas.objects.get(id=1)
    return render(request, "core/hamburguesa_s.html",{'produ':produ})

def hamburguesasuper(request):
    produ2 = hamburguesas.objects.get(id=2)
    return render(request, "core/hamburguesasuper.html",{'produ2':produ2})

def hamburguesamexi(request):
    produ3 = hamburguesas.objects.get(id=3)
    return render(request, "core/hamburguesamexi.html",{'produ3':produ3})

def hamburguesabri(request):
    produ4 = hamburguesas.objects.get(id=4)
    return render(request, "core/hamburguesabri.html",{'produ4':produ4})
#paginas perros -------------------------------------------------------------------------
def perrosencillo(request):
    produ5 = hamburguesas.objects.get(id=5)
    return render(request, "core/perrosencillo.html",{'produ5':produ5})

def perroamericano(request):
    produ6 = hamburguesas.objects.get(id=6)
    return render(request, "core/perroamericano.html",{'produ6':produ6})

def choriperro(request):
    produ7 = hamburguesas.objects.get(id=7)
    return render(request, "core/choriperro.html",{'produ7':produ7})

def perroran(request):
    produ8 = hamburguesas.objects.get(id=8)
    return render(request, "core/perroran.html",{'produ8':produ8})

def perroteque(request):
    produ9 = hamburguesas.objects.get(id=9)
    return render(request, "core/perroteque.html",{'produ9':produ9})
#paginas salchipapa--------------------------------------------------------
def salchisenci(request):
    produ10 = hamburguesas.objects.get(id=10)
    return render(request, "core/salchisenci.html",{'produ10':produ10})

def chorisenci(request):
    produ11 = hamburguesas.objects.get(id=11)
    return render(request, "core/chorisenci.html",{'produ11':produ11})

def salchiespe(request):
    produ12 = hamburguesas.objects.get(id=12)
    return render(request, "core/salchiespe.html",{'produ12':produ12})

def choriespe(request):
    produ13 = hamburguesas.objects.get(id=13)
    return render(request, "core/choriespe.html",{'produ13':produ13})

def mixsuper(request):
    produ14 = hamburguesas.objects.get(id=14)
    return render(request, "core/mixsuper.html",{'produ14':produ14})
#paginas picadas--------------------------------------------------
def morropla(request):
    produ15 = hamburguesas.objects.get(id=15)
    return render(request, "core/morropla.html",{'produ15':produ15})

def nevatol(request):
    produ16 = hamburguesas.objects.get(id=16)
    return render(request, "core/nevatol.html",{'produ16':produ16})

def everest(request):
    produ17 = hamburguesas.objects.get(id=17)
    return render(request, "core/everest.html",{'produ17':produ17})

def superm(request):
    produ18 = hamburguesas.objects.get(id=18)
    return render(request, "core/superm.html",{'produ18':produ18})
#paginas costillas-----------------------------------------------------------------------
def costillase(request):
    produ19 = hamburguesas.objects.get(id=19)
    return render(request, "core/costillase.html",{'produ19':produ19})

def costillaes(request):
    produ20 = hamburguesas.objects.get(id=20)
    return render(request, "core/costillaes.html",{'produ20':produ20})

def costillasup(request):
    produ25 = hamburguesas.objects.get(id=25)
    return render(request, "core/costillasup.html",{'produ25':produ25})

def alitasp(request):
    produ21 = hamburguesas.objects.get(id=21)
    return render(request, "core/alitasp.html",{'produ21':produ21})

def mixta(request):
    produ22 = hamburguesas.objects.get(id=22)
    return render(request, "core/mixta.html",{'produ22':produ22})
#paginas porciones----------------------------------------------------
def porcionp(request):
    produ23 = hamburguesas.objects.get(id=23)
    return render(request, "core/porcionp.html",{'produ23':produ23})

def porcionh(request):
    produ24 = hamburguesas.objects.get(id=24)
    return render(request, "core/porcionh.html",{'produ24':produ24})
#-----------------------------------------------------------------------------
def finalizar_compra(request):
    return render(request, "core/finalizar_compra.html")

def car(request):
    return render(request, "core/ver_carrito.html")