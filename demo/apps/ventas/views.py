from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductosForm
from demo.apps.ventas.models import producto
from django.http import HttpResponseRedirect

def add_productos_view(request):
	info="Inicializando"
	if request.user.is_authenticated():
		if request.method=="POST":
			form=addProductosForm(request.POST,request.FILES)
			if form.is_valid():
				nombre=form.cleaned_data['nombre']
				descripcion=form.cleaned_data['descripcion']
				imagen=form.cleaned_data['imagen']#Esto se obtienes con request.FILES
				precio=form.cleaned_data['precio']
				stock= form.cleaned_data['stock']
				p=producto()
				if imagen:
					p.imagen=imagen			
				p.nombre=nombre
				p.descripcion=descripcion
				p.stock=stock
				p.precio=precio
				p.status=True
				p.save()
				info ="Datos Guardados.."

				#form=addProductosForm()
				#ctx={'form':form,'informacion':info}
				#return render_to_response('ventas/addProductos.html',ctx,context_instance=RequestContext(request))
			else:
				info="Datos Incorrectos"
		form=addProductosForm()
		ctx={'form':form,'informacion':info}
		return render_to_response('ventas/addProductos.html',ctx,context_instance=RequestContext(request))
	else: #GET
		return HttpResponseRedirect('/')
		#form=addProductosForm()
		#ctx={'form':form}
		#return render_to_response('ventas/addProductos.html',ctx,context_instance=RequestContext(request))

