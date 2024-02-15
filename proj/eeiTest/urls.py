from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    ###--------------EEI--------------------------
    path('eei/', views.list_eei, name='eei'),
    path('save_eei/', views.save_eei, name='save_eei'),
    path('manage_eei/', views.manage_eei, name='manage_eei'),
    path('delete_eei/<int:eei_id>/', views.delete_eei, name='delete_eei'),
    # ###-------------------------Route-----------------------
    # path('route/', views.list_route, name='route'),
    # path('save_route/', views.save_route, name='save_route'),
    # path('manage_route/', views.manage_route, name='manage_route'),
    # path('delete_route/<int:route_id>/', views.delete_route, name='delete_route'),
    # ###--------------------------Longitude---------------------------
    # path('longitude/', views.list_longitude, name='longitude'),
    # path('save_longitude/', views.save_longitude, name='save_longitude'),
    # path('manage_longitude/', views.manage_longitude, name='manage_longitude'),
    # path('delete_longitude/<int:longitude_id>/', views.delete_longitude, name='delete_longitude'),
    # ###--------------------------Latitude------------------------------
    # path('latitude/', views.list_latitude, name='latitude'),
    # path('save_latitude/', views.save_latitude, name='save_latitude'),
    # path('manage_latitude/', views.manage_latitude, name='manage_latitude'),
    # path('delete_latitude/<int:latitude_id>/', views.delete_latitude, name='delete_latitude'),
    # ###---------------------------SystemDectetion--------------------------
    # path('system_detect/', views.list_system_detect, name='system_detect'),
    # path('save_system_detect/', views.save_system_detect, name='save_system_detect'),
    # path('manage_system_detect/', views.manage_system_detect, name='manage_system_detect'),
    # path('delete_system_detect/<int:system_detect_id>/', views.delete_system_detect, name='delete_system_detect'),
    # ###--------------------------TypeIncident-----------------------------
    # path('type_incident/', views.list_type_incident, name='type_incident'),
    # path('save_type_incident/', views.save_type_incident, name='save_type_incident'),
    # path('manage_type_incident/', views.manage_type_incident, name='manage_type_incident'),
    # path('delete_type_incident/<int:type_incident_id>/', views.delete_type_incident, name='delete_type_incident'),
    # ###---------------------------TypePose------------------------------
    # path('type_pose/', views.list_type_pose, name='type_pose'),
    # path('save_type_pose/', views.save_type_pose, name='save_type_pose'),
    # path('manage_type_pose/', views.manage_type_pose, name='manage_type_pose'),
    # path('delete_type_pose/<int:type_pose_id>/', views.delete_type_pose, name='delete_type_pose'),
    # ###------------------------------TypeSysteme---------------------------
    # path('type_system/', views.list_type_system, name='type_system'),
    # path('save_type_system/', views.save_type_system, name='save_type_system'),
    # path('manage_type_system/', views.manage_type_system, name='manage_type_system'),
    # path('delete_type_system/<int:type_system_id>/', views.delete_type_system, name='delete_type_system'),
    # ###---------------------------------Caracteristique---------------------
    # path('caracteristique/', views.list_caracteristique, name='caracteristique'),
    # path('save_caracteristique/', views.save_caracteristique, name='save_caracteristique'),
    # path('manage_caracteristique/', views.manage_caracteristique, name='manage_caracteristique'),
    # path('delete_caracteristique/<int:caracteristique_id>/', views.delete_caracteristique, name='delete_caracteristique')
]