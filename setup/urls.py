from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),


    # importa todas as urls que estiverem no arquivo 'urls' da app restaurants
    path('', include('restaurants.urls'))
]
