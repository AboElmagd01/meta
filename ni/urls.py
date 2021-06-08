from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from main.views import mainApp,map,rooms,contact,explore,spa,resta,feed,login_v,register,offers,about,mapAlex,mapGiza,mapLuxor,mapSharm,logout_view,room_view,reservation_view,deleteview
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainApp),
    path('map/', map),
    path('mapAlex/', mapAlex),
    path('mapGiza/', mapGiza),
    path('mapSharm/', mapSharm),
    path('mapLuxor/', mapLuxor),
    path('rooms/', rooms),
    path('contact/', contact),
    path('restaurant/', resta),
    path('explore/', explore),
    path('spa/', spa),
    path('feedback/', feed),
    path('login/', login_v),
    path('registration/', register),
    path('offers/', offers),
    path('about/', about),
    path('logout/', logout_view),
    path('rooms/<int:id>/',room_view,name='room_view'),
    path('reserve/',reservation_view),
    path('reserve/<int:id>/', deleteview, name='reserve_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
