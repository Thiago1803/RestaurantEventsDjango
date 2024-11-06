from django.contrib import admin
from .models import Restaurants


@admin.register(Restaurants) # aqui faz aparecer o menuzinho de restaurantes la no ambiete admin
class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone', 'email')
    list_display_links = ('name',)
    filter_horizontal = ('users',)
    search_fields = ('name',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser: return qs  # Se o usuário for superuser, ele verá todos os restaurantes
        return qs.filter(users=request.user)  # Senao, ele verá apenas os restaurantes que está associado

    def has_view_permission(self, request, obj=None):
        if request.user.is_superuser: return True # Se o usuário for um superusuário, ele sempre terá permissão para ver o restaurante
        if obj and request.user in obj.users.all(): return True # Caso o usuário esteja associado ao restaurante, ele terá permissão para ver o restaurante
        return False
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_superuser: return True # Se o usuário for superusuário, ele pode editar todos os restaurante
        if obj and request.user in obj.users.all(): return True # Caso o usuário esteja associado ao restaurante, ele terá permissão para editar o restaurante
        return False