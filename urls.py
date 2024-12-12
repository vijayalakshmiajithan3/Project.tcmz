from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
  
      path('cate',views.catz,name='cate'),
    path('catlist/<str:name>',views.catlist,name='plant'),
    path('detai/<str:name>',views.details,name='deta'),
    path('log',views.loginpage,name='log'),path('signin',views.register,name='signin'),
    path('logout',views.logoutpage,name='logout'),
    path('home',views.home,name='home'),
     path('add_to_cart/<int:plant_id>/',views.add_to_cart, name='cart'),
    path('view_cart/',views. view_cart, name='view_cart'),

    path('remove<int:id>',views.remove_from_cart,name='remove_from_cart'),

    path('search',views.items,name='search'),
     path('add',views.add_categories.as_view(),name='add'),
       path('abt',views.abpro,name='abt'),
       path('pay/<int:id>',views.payment,name='pay'),
       path('sucess/',views.payment_successful,name='sucess')
        
    
]
urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)



