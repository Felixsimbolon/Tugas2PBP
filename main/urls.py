from django.urls import path
from main.views import show_main
from main.views import show_main, create_product_entry
from main.views import show_main, create_product_entry, show_xml, show_json, show_xml_by_id, show_json_by_id
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_product_entry
from main.views import delete_product_entry , add_product_entry_ajax, create_product_flutter


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product-entry', create_product_entry, name='create_product_entry'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-product-entry/<uuid:id>', edit_product_entry, name='edit_product_entry'),
    path('delete-product-entry/<uuid:id>', delete_product_entry, name='delete_product_entry'),
    path('create-product-entry-ajax', add_product_entry_ajax, name='add_product_entry_ajax'),
    path('create-product-flutter/', create_product_flutter, name='create_product_flutter'),





]
#<div class="info-image">
    #<img src="https://th.bing.com/th/id/OIP.lg-tJiwtguygoc9yapGMAQHaEW?pid=ImgDetMain" alt="Guitar Image">
#</div>