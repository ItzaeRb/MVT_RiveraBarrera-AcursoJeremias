from django.http import HttpResponse
from django.template import loader
from datosFamilia.models import Familia

def homePage(self):
    data = {"nombreMayor": "Isabella", 
            "edadMayor":"13",
            "fechaNacMayor": "2003/5/23",
            "nombreMedio": "Nazareth", 
            "edadMedio":"8",
            "fechaNacMedio": "2013/12/9",
            "nombreMenor": "Benicio", 
            "edadMenor":"6",
            "fechaNacMenor": "2016/5/2",
            }
    planilla = loader.get_template("home.html")
    documento = planilla.render(data)
    return HttpResponse(documento)

def familia(self):
    mayor = Familia(nombre="Isabella", edad="13", fecha_nacimiento="2003-05-23")
    mayor.save()
    medio = Familia(nombre="Nazareth", edad="8", fecha_nacimiento="2013-12-9")
    medio.save()
    menor = Familia(nombre="Benicio", edad="6", fecha_nacimiento="2016-5-2")
    menor.save()
    documento = f"Hija mayor: nombre: {mayor.nombre} edad: {mayor.edad} Fecha Nacimiento: {mayor.fecha_nacimiento}\nHija del medio: nombre: {medio.nombre} edad: {medio.edad} Fecha Nacimiento: {medio.fecha_nacimiento} \nHijo menor: nombre: {menor.nombre} edad: {menor.edad} Fecha Nacimiento: {menor.fecha_nacimiento}\n"
    return HttpResponse(documento)

