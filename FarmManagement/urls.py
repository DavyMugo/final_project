# myapp/urls.py
from django.urls  import path
from .  import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('farm-register/', views.farm_register, name='farm_register'),
    path('sold-animals/', views.sold_animals, name='sold_animals'),
    path('losses/', views.losses, name='losses'),
    path('remove-animal/<int:animal_id>/', views.remove_animal, name='remove_animal'),
    path('market-trends/', views.market_trends, name='market_trends'),
    # Add more URLs for other sections if needed
]

    
 