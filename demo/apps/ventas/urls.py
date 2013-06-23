from django.conf.urls.defaults import patterns, url

urlpatterns=patterns('demo.apps.ventas.views',
	url(r'^add/productos/$','add_productos_view',name="vista_agregar_producto"),

)