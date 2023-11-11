from django.urls import path 

from  purchase_request import views

app_name = "purchase_request"





urlpatterns = [
	path('lista/purchase/request', views.listapurchaserequest, name='listapurchaserequest'),
	path('request/purchase', views.requestpurchase, name='requestpurchase'),
	path('edit/request/purchase/<str:id>/', views.editrequestpurchase, name='editrequestpurchase'),
	path('detallu/purchase/request/<str:id>/', views.detallupurchaserequest, name='detallupurchaserequest'),
	path('add/item/purchase/<str:id_riquest>/', views.additempurchase, name='additempurchase'),

	path('edit/item/purchase/<str:id_item>/', views.edititempurchase, name='edititempurchase'),
	path('apaga/item/purchase/<str:id_item>/', views.apagaitempurchase, name='apagaitempurchase'),
	path('aproved/item/purchase/<str:id_item>/', views.aproveditempurchase, name='aproveditempurchase'),
	path('riject/item/purchase/<str:id_item>/', views.rijectitempurchase, name='rijectitempurchase'),
	path('deliver/item/purchase/<str:id_item>/', views.deliveritempurchase, name='deliveritempurchase'),
	path('send/purchase/request/<str:id>/', views.sendpurchaserequest, name='sendpurchaserequest'),


	path('acepted/purchase/request/<str:id>/', views.aceptedpurchaserequest, name='aceptedpurchaserequest'),
	path('rijected/purchase/request<str:id>/', views.rijectedpurchaserequest, name='rijectedpurchaserequest'),

															 
																 
		

]

