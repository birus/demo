from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.models import producto
from demo.apps.home.forms	import contactForm, loginForm #Importar los formularios
from django.core.mail import EmailMultiAlternatives #Para enviar HTML
from django.contrib.auth import login, logout, authenticate 
from django.http import HttpResponseRedirect
#Librerias para paginacion
from django.core.paginator import Paginator, EmptyPage, InvalidPage

def index_view(request):
	return render_to_response('index.html',context_instance=RequestContext(request))

def about_view(request):
	mensaje="Esto es un menaje desde la vista"
	ctx={'msg':mensaje}
	return render_to_response('home/about.html',ctx,context_instance=RequestContext(request))
#PAGINATOR
#def productos_view(request):
#	prod=producto.objects.filter(status=True) #Select where status=True
#	ctx={'productos':prod}
#	return  render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))

def productos_view(request, pagina):
	lista_prod=producto.objects.filter(status=True) #Select where status=True
	paginator=Paginator(lista_prod,3)#Cuantos productos por pagina=3
	try:
		page=int(pagina)	
	except:
		page=1
	try:
		productos=paginator.page(page)
		
	except (EmptyPage, InvalidPage):
		productos=paginator.page(paginator.num_pages)
		
	ctx={'productos':productos}
	return  render_to_response('home/productos.html',ctx,context_instance=RequestContext(request))

def singleProduct_view(request,id_prod):
	prod=producto.objects.get(id=id_prod)
	ctx={'producto':prod}
	return render_to_response('home/SingleProducto.html',ctx,context_instance=RequestContext(request))


def contacto_view(request):
	info_enviado=False
	email=""
	titulo=""
	texto=""
	if request.method=="POST":
		formulario=contactForm(request.POST)
		if formulario.is_valid():
			info_enviado=True
			email=formulario.cleaned_data['Email']
			titulo=formulario.cleaned_data['Titulo']
			texto=formulario.cleaned_data['Texto']
			#Config para enviar al correo
			to_admin='victor.olalla@gmail.com'
			html_content="Informacion Recivida de [%s] <br><br>****Mensaje***<br><br>%s"%(email, texto)
			msg=EmailMultiAlternatives('Correo de Contacto',html_content,'from@server.com',[to_admin])
			msg.attach_alternative(html_content,'text/html') #Definimos el contenido como html
			msg.send() #Envia el correo

	else:
		formulario=contactForm()
	ctx={'form':formulario,'email':email,'titulo':titulo, 'texto':texto, 'info_enviado':info_enviado}
	return render_to_response('home/contacto.html',ctx,context_instance=RequestContext(request))

def login_view(request):
	mensaje=""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/')
	else:
		if request.method=="POST":
			form=loginForm(request.POST)
			if form.is_valid():
				username=form.cleaned_data['username']
				password=form.cleaned_data['password']
				usuario=authenticate(username=username,password=password)
				if usuario is not None and usuario.is_active:
					login(request,usuario)
					return HttpResponseRedirect('/')
				else:
					mensaje='usuario y/o password incorrecto'
		form=loginForm()
		ctx={'form':form,'mensaje':mensaje}
		return render_to_response('home/login.html',ctx,context_instance=RequestContext(request))	

def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')












