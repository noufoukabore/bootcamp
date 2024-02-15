from gettext import translation
from django.shortcuts import get_object_or_404, render, redirect
import json
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from eeiTest.models import *

# Create your views here.
def index(request):
    eei_total = Eei.objects.count()
    route_total = Routes.objects.count()
    type_pose_total = TypePose.objects.count()
    longitude_total = Longitude.objects.count()
    latitude_total = Latitude.objects.count()
    type_incident_total = TypeIncident.objects.count()
    system_detect_total = SystemDeclenchement.objects.count()
    type_system_total = TypeSystem.objects.count()
    caracteristique_total = CaracteristiquePoints.objects.count()

    context = {
        'eei_total': eei_total,
        'route_total': route_total,
        'type_pose_total': type_pose_total,
        'longitude_total': longitude_total,
        'latitude_total': latitude_total,
        'type_incident_total': type_incident_total,
        'system_detect_total': system_detect_total,
        'type_system_total': type_system_total,
        'caracteristique_total': caracteristique_total
    }
    return render(request, 'eeiTest/index.html', context)


### -------------------Manage de touts les elements---------------------
# EEI
def manage_eei(request):
    eei = {}
    route = Routes.objects.all()
    type_pose = TypePose.objects.all()
    longitude = Longitude.objects.all()
    latitude = Latitude.objects.all()
    type_incident = TypeIncident.objects.all()
    system_detect = SystemDeclenchement.objects.all()
    caracteristique = CaracteristiquePoints.objects.all()
    if request.method == 'GET':
        data = request.GET
        id = ''
        if 'id' in data:
            id = data['id']
        if id.isnumeric() and int(id) > 0:
            eei = Eei.objects.filter(id=id).first()

    context = {
        'eei': eei,
        'route': route,
        'type_pose': type_pose,
        'longitude': longitude,
        'latitude': latitude,
        'type_incident': type_incident,
        'system_detect': system_detect,
        'caracteristique': caracteristique
    }

    return render(request, 'eeiTest/add_eei.html',  context)
# # Routes
# def manage_route(request):
#     route = {}
#     if request.method == 'GET':
#         data = request.GET
#         id = ''
#         if 'id' in data:
#             id = data['id']
#         if id.isnumeric() and int(id) > 0:
#             route = Routes.objects.filter(id=id).first()

#     return render(request, 'route/add_route.html', {'route': route})
# # Longitude
# def manage_longitude(request):
#     longitude = {}
#     if request.method == 'GET':
#         data = request.GET
#         id = ''
#         if 'id' in data:
#             id = data['id']
#         if id.isnumeric() and int(id) > 0:
#             longitude = Longitude.objects.filter(id=id).first()

#     return render(request, 'Longitude/add_longitude.html', {'longitude': longitude})
# # Latitude
# def manage_latitude(request):
#     latitude = {}
#     if request.method == 'GET':
#         data = request.GET
#         id = ''
#         if 'id' in data:
#             id = data['id']
#         if id.isnumeric() and int(id) > 0:
#             latitude = Latitude.objects.filter(id=id).first()

#     return render(request, 'Latitude/add_latitude.html', {'latitude': latitude})
# # Systeme Detection
# def manage_system_detect(request):
#     system_detect = {}
#     type_system = TypeSystem.objects.all()
#     if request.method == 'GET':
#         data = request.GET
#         id = ''
#         if 'id' in data:
#             id = data['id']
#         if id.isnumeric() and int(id) > 0:
#             system_detect = SystemDeclenchement.objects.filter(id=id).first()

#     context = {
#         'system_detect': system_detect,
#         'type_system': type_system
#     }

#     return render(request, 'systemDetection/add_systemdetect.html', context)
# # Type Incident
# def manage_type_incident(request):
#     type_detect = {}
#     if request.method == 'GET':
#         data = request.GET
#         id = ''
#         if 'id' in data:
#             id = data['id']
#         if id.isnumeric() and int(id) > 0:
#             type_detect = TypeIncident.objects.filter(id=id).first()

#     return render(request, 'typeIncident/add_typeincident.html', {'type_detect': type_detect})
# # Type Systeme
# def manage_type_system(request):
#     type_system = {}
#     if request.method == 'GET':
#         data = request.GET
#         id = ''
#         if 'id' in data:
#             id = data['id']
#         if id.isnumeric() and int(id) > 0:
#             type_system = TypeSystem.objects.filter(id=id).first()

#     return render(request, 'typeSysteme/add_typesystem.html', {'type_system': type_system})
# # Type Pose
# def manage_type_pose(request):
#     type_pose = {}
#     if request.method == 'GET':
#         data = request.GET
#         id = ''
#         if 'id' in data:
#             id = data['id']
#         if id.isnumeric() and int(id) > 0:
#             type_pose = TypePose.objects.filter(id=id).first()

#     return render(request, 'typePose/add_typepose.html', {'type_pose': type_pose})
# # Caracteristique Points
# def manage_caracteristique(request):
#     caracteristique = {}
#     if request.method == 'GET':
#         data = request.GET
#         id = ''
#         if 'id' in data:
#             id = data['id']
#         if id.isnumeric() and int(id) > 0:
#             caracteristique = CaracteristiquePoints.objects.filter(id=id).first()

#     return render(request, 'caracterisPoint/add_caracteristique.html', {'caracteristique': caracteristique})




### ---------------------Liste des tous les elements--------------------
# EEI
def list_eei(request, id=0):

    eei = {}
    if id:
        eei = Eei.objects.filter(id=id).first()
    eeis = Eei.objects.all()
    eeis_total = Eei.objects.count()
    context = {
        'eeis': eeis,
        'eeis_total': eeis_total,
        'eei': eei
    }

    return render(request, 'eeiTest/eei.html', context)
# Type Pose
def list_type_pose(request, id=0):

    type_pose = {}
    if id:
        type_pose = TypePose.objects.filter(id=id).first()
    typePose = TypePose.objects.all()
    typePose_total = TypePose.objects.count()
    context = {
        'typePose': typePose,
        'typePose_total': typePose_total,
        'type_pose': type_pose
    }

    return render(request, 'typePose/typepose.html', context)
# # Routes
# def list_route(request, id=0):

#     route = {}
#     if id:
#         route = Routes.objects.filter(id=id).first()
#     routes = Routes.objects.all()
#     routes_total = Routes.objects.count()
#     context = {
#         'routes': routes,
#         'routes_total': routes_total,
#         'route': route
#     }

#     return render(request, 'route/route.html', context)
# # Longitude
# def list_longitude(request, id=0):

#     longitude = {}
#     if id:
#         longitude = Longitude.objects.filter(id=id).first()
#     longitudes = Longitude.objects.all()
#     longitudes_total = Longitude.objects.count()
#     context = {
#         'longitudes': longitudes,
#         'longitudes_total': longitudes_total,
#         'longitude': longitude
#     }

#     return render(request, 'Longitude/longitude.html', context)
# # Latitude
# def list_latitude(request, id=0):

#     latitude = {}
#     if id:
#         latitude = Latitude.objects.filter(id=id).first()
#     latitudes = Latitude.objects.all()
#     latitudes_total = Latitude.objects.count()
#     context = {
#         'latitudes': latitudes,
#         'typePose_total': latitudes_total,
#         'latitude': latitude
#     }

#     return render(request, 'Latitude/latitude.html', context)
# # Systeme Detection
# def list_system_detect(request, id=0):

#     system_detect = {}
#     if id:
#         system_detect = SystemDeclenchement.objects.filter(id=id).first()
#     systemDetect = SystemDeclenchement.objects.all()
#     systemDetect_total = SystemDeclenchement.objects.count()
#     context = {
#         'systemDetect': systemDetect,
#         'systemDetect_total': systemDetect_total,
#         'system_detect': system_detect
#     }

#     return render(request, 'systemDetection/systemdetection.html', context)
# # Type Incident
# def list_type_incident(request, id=0):

#     type_incident = {}
#     if id:
#         type_incident = TypeIncident.objects.filter(id=id).first()
#     typeIncident = TypeIncident.objects.all()
#     typeIncident_total = TypeIncident.objects.count()
#     context = {
#         'typeIncident': typeIncident,
#         'typeIncident_total': typeIncident_total,
#         'type_incident': type_incident
#     }

#     return render(request, 'typeIncident/typeincident.html', context)
# # Type Systeme
# def list_type_system(request, id=0):

#     type_system = {}
#     if id:
#         type_system = TypeSystem.objects.filter(id=id).first()
#     typeSystem = TypeSystem.objects.all()
#     typeSystem_total = TypeSystem.objects.count()
#     context = {
#         'typeSystem': typeSystem,
#         'typeSystem_total': typeSystem_total,
#         'type_system': type_system
#     }

#     return render(request, 'typeSysteme/typesysteme.html', context)
# # Caracteristique Points
# def list_caracteristique(request, id=0):

#     caracteristique_point = {}
#     if id:
#         caracteristique_point = CaracteristiquePoints.objects.filter(id=id).first()
#     caracteristiquePoint = CaracteristiquePoints.objects.all()
#     caracteristiquePoint_total = CaracteristiquePoints.objects.count()
#     context = {
#         'caracteristiquePoint': caracteristiquePoint,
#         'caracteristiquePoint_total': caracteristiquePoint_total,
#         'caracteristique_point': caracteristique_point
#     }

#     return render(request, 'caracterisPoint/caracteristique.html', context)


### ---------------------Save de tous les elements---------------
# EEI
def save_eei(request):
    resp = {'status': 'failed'}
    data = request.POST
    try:
        type_pose_id = data.get('type_pose', None)
        type_pose_instance = TypePose.objects.get(id=type_pose_id)

        route_id =data.get('route', None)
        route_instance = Routes.objects.get(id=route_id)

        longitude_id = data.get('longitude', None)
        longitude_instance = Longitude.objects.get(id=longitude_id)

        latitude_id = data.get('latitude', None)
        latitude_instance = Latitude.objects.get(id=latitude_id)

        type_incident_id = data.get('type_incident', None)
        type_incident_instance = TypeIncident.objects.get(id=type_incident_id)

        type_system_id = data.get('type_system', None)
        type_system_instance = TypeSystem.objects.get(id=type_system_id)

        caracteristique_id = data.get('caracteristique', None)
        caracteristique_instance = CaracteristiquePoints.objects.get(id=caracteristique_id)

        if data['id'].isnumeric() and int(data['id']) > 0:
            Eei.objects.filter(id=data['id']).update(
                    nom=data['nom'],
                    date=data['date'],
                    details=data['details'],
                    photo=data['photo'],
                    route=route_instance,
                    type_pose=type_pose_instance,
                    longitude=longitude_instance,
                    latitude=latitude_instance,
                    type_incident=type_incident_instance,
                    type_system=type_system_instance,
                    caracteristique=caracteristique_instance
                )
            messages.success(request, "EEI modifié avec succès")
        else:
            eei = Eei.objects.create(
                    nom=data['nom'],
                    date=data['date'],
                    details=data['details'],
                    photo=request.FILES['photo'],
                    route=route_instance,
                    type_pose=type_pose_instance,
                    longitude=longitude_instance,
                    latitude=latitude_instance,
                    type_incident=type_incident_instance,
                    type_system=type_system_instance,
                    caracteristique=caracteristique_instance
                )
            eei.save()
            messages.success(request, "EEI ajouté avec succès")
        resp['status'] = 'success'
    except Exception as e:
        print(str(e))
    return HttpResponse(json.dumps(resp), content_type='application/json')
# # Routes
# def save_route(request):
#     resp = {'status': 'failed'}
#     data = request.POST
#     try:
#         if data['id'].isnumeric() and int(data['id']) > 0:
#             Routes.objects.filter(id=data['id']).update(
#                     code=data['code'],
#                     nom=data['nom']
#                 )
#             messages.success(request, "route modifié avec succès")
#         else:
#             route = Routes.objects.create(
#                     code=data['code'],
#                     nom=data['nom']
#                 )
#             route.save()
#             messages.success(request, "route ajouté avec succès")
#         resp['status'] = 'success'
#     except Exception as e:
#         print(str(e))
#     return HttpResponse(json.dumps(resp), content_type='application/json')
# # Longitude
# def save_longitude(request):
#     resp = {'status': 'failed'}
#     data = request.POST
#     try:
#         if data['id'].isnumeric() and int(data['id']) > 0:
#             Longitude.objects.filter(id=data['id']).update(
#                     degre=data['degre'],
#                     minute=data['minute'],
#                     seconde=data['seconde'],
#                     fuseau=data['fuseau']
#                 )
#             messages.success(request, "longitude modifié avec succès")
#         else:
#             longitude = Longitude.objects.create(
#                     degre=data['degre'],
#                     minute=data['minute'],
#                     seconde=data['seconde'],
#                     fuseau=data['fuseau']
#                 )
#             longitude.save()
#             messages.success(request, "longitude ajouté avec succès")
#         resp['status'] = 'success'
#     except Exception as e:
#         print(str(e))
#     return HttpResponse(json.dumps(resp), content_type='application/json')
# # Latitude
# def save_latitude(request):
#     resp = {'status': 'failed'}
#     data = request.POST
#     try:
#         if data['id'].isnumeric() and int(data['id']) > 0:
#             Latitude.objects.filter(id=data['id']).update(
#                     degre=data['degre'],
#                     minute=data['minute'],
#                     seconde=data['seconde'],
#                     fuseau=data['fuseau']
#                 )
#             messages.success(request, "latitude modifié avec succès")
#         else:
#             latitude = Latitude.objects.create(
#                     degre=data['degre'],
#                     minute=data['minute'],
#                     seconde=data['seconde'],
#                     fuseau=data['fuseau']
#                 )
#             latitude.save()
#             messages.success(request, "latitude ajouté avec succès")
#         resp['status'] = 'success'
#     except Exception as e:
#         print(str(e))
#     return HttpResponse(json.dumps(resp), content_type='application/json')
# # Systeme Detection
# def save_system_detect(request):
#     resp = {'status': 'failed'}
#     data = request.POST
#     try:
#         if data['id'].isnumeric() and int(data['id']) > 0:
#             SystemDeclenchement.objects.filter(id=data['id']).update(
#                     nom=data['nom']
#                 )
#             messages.success(request, "systeme detection modifié avec succès")
#         else:
#             system_detect = SystemDeclenchement.objects.create(
#                     nom=data['nom']
#                 )
#             system_detect.save()
#             messages.success(request, "systeme detection ajouté avec succès")
#         resp['status'] = 'success'
#     except Exception as e:
#         print(str(e))
#     return HttpResponse(json.dumps(resp), content_type='application/json')
# # Type Incident
# def save_type_incident(request):
#     resp = {'status': 'failed'}
#     data = request.POST
#     try:
#         if data['id'].isnumeric() and int(data['id']) > 0:
#             TypeIncident.objects.filter(id=data['id']).update(
#                     code=data['code']
#                 )
#             messages.success(request, "type incident modifié avec succès")
#         else:
#             type_incident = TypeIncident.objects.create(
#                     code=data['code']
#                 )
#             type_incident.save()
#             messages.success(request, "type incident ajouté avec succès")
#         resp['status'] = 'success'
#     except Exception as e:
#         print(str(e))
#     return HttpResponse(json.dumps(resp), content_type='application/json')
# # Type Systeme
# def save_type_system(request):
#     resp = {'status': 'failed'}
#     data = request.POST
#     try:
#         system_declench_id = data.get('system_decl', None)
#         system_declench_instance = SystemDeclenchement.objects.get(id=system_declench_id)
#         if data['id'].isnumeric() and int(data['id']) > 0:
#             TypeSystem.objects.filter(id=data['id']).update(
#                     nom=data['nom'],
#                     system_declench = system_declench_instance
#                 )
#             messages.success(request, "type systeme modifié avec succès")
#         else:
#             type_system = TypeSystem.objects.create(
#                     nom=data['nom'],
#                     system_declench = system_declench_instance
#                 )
#             type_system.save()
#             messages.success(request, "type systeme ajouté avec succès")
#         resp['status'] = 'success'
#     except Exception as e:
#         print(str(e))
#     return HttpResponse(json.dumps(resp), content_type='application/json')
# # Type Pose
# def save_type_pose(request):
#     resp = {'status': 'failed'}
#     data = request.POST
#     try:
#         if data['id'].isnumeric() and int(data['id']) > 0:
#             TypePose.objects.filter(id=data['id']).update(
#                     nom=data['nom'],
#                     details=data['details']
#                 )
#             messages.success(request, "type pose modifié avec succès")
#         else:
#             type_pose = TypePose.objects.create(
#                     nom=data['nom'],
#                     details=data['details']
#                 )
#             type_pose.save()
#             messages.success(request, "type pose ajouté avec succès")
#         resp['status'] = 'success'
#     except Exception as e:
#         print(str(e))
#     return HttpResponse(json.dumps(resp), content_type='application/json')
# # Caracteristique Points
# def save_caracteristique(request):
#     resp = {'status': 'failed'}
#     data = request.POST
#     try:
#         if data['id'].isnumeric() and int(data['id']) > 0:
#             CaracteristiquePoints.objects.filter(id=data['id']).update(
#                     nom=data['nom'],
#                     details=data['details']
#                 )
#             messages.success(request, "caracteristique point modifié avec succès")
#         else:
#             caracteristique = CaracteristiquePoints.objects.create(
#                     nom=data['nom'],
#                     details=data['details']
#                 )
#             caracteristique.save()
#             messages.success(request, "caracteristique point ajouté avec succès")
#         resp['status'] = 'success'
#     except Exception as e:
#         print(str(e))
#     return HttpResponse(json.dumps(resp), content_type='application/json')




### ---------------------Supprimer de tous les elements-----------------
# EEI
def delete_eei(request, eei_id):
    resp = {'status': 'failed'}
    try:
        product = get_object_or_404(Eei, id=eei_id)
        product.delete()
        resp = {'status': 'success'}
        messages.success(request, "EEI supprimer avec succes")
    except Exception as e:
        print(str(e))

    return JsonResponse(resp)
# # Routes
# def delete_route(request, route_id):
#     resp = {'status': 'failed'}
#     try:
#         route = get_object_or_404(Routes, id=route_id)
#         route.delete()
#         resp = {'status': 'success'}
#         messages.success(request, "route supprimer avec succes")
#     except Exception as e:
#         print(str(e))

#     return JsonResponse(resp)
# # Longitude
# def delete_longitude(request, longitude_id):
#     resp = {'status': 'failed'}
#     try:
#         longitude = get_object_or_404(Longitude, id=longitude_id)
#         longitude.delete()
#         resp = {'status': 'success'}
#         messages.success(request, "longitude supprimer avec succes")
#     except Exception as e:
#         print(str(e))

#     return JsonResponse(resp)
# # Latitude
# def delete_latitude(request, latitude_id):
#     resp = {'status': 'failed'}
#     try:
#         latitude = get_object_or_404(Latitude, id=latitude_id)
#         latitude.delete()
#         resp = {'status': 'success'}
#         messages.success(request, "latitude supprimer avec succes")
#     except Exception as e:
#         print(str(e))

#     return JsonResponse(resp)
# # Systeme Detection
# def delete_system_detect(request, system_detect_id):
#     resp = {'status': 'failed'}
#     try:
#         system_detect = get_object_or_404(SystemDeclenchement, id=system_detect_id)
#         system_detect.delete()
#         resp = {'status': 'success'}
#         messages.success(request, "Systeme detection supprimer avec succes")
#     except Exception as e:
#         print(str(e))

#     return JsonResponse(resp)
# # Type Incident
# def delete_type_incident(request, type_incident_id):
#     resp = {'status': 'failed'}
#     try:
#         type_incident = get_object_or_404(TypeIncident, id=type_incident_id)
#         type_incident.delete()
#         resp = {'status': 'success'}
#         messages.success(request, "Type incident supprimer avec succes")
#     except Exception as e:
#         print(str(e))

#     return JsonResponse(resp)
# # Type System
# def delete_type_system(request, type_system_id):
#     resp = {'status': 'failed'}
#     try:
#         type_system = get_object_or_404(TypeSystem, id=type_system_id)
#         type_system.delete()
#         resp = {'status': 'success'}
#         messages.success(request, "Type systeme supprimer avec succes")
#     except Exception as e:
#         print(str(e))

#     return JsonResponse(resp)
# # Type Pose
# def delete_type_pose(request, type_pose_id):
#     resp = {'status': 'failed'}
#     try:
#         type_pose = get_object_or_404(TypePose, id=type_pose_id)
#         type_pose.delete()
#         resp = {'status': 'success'}
#         messages.success(request, "Type pose supprimer avec succes")
#     except Exception as e:
#         print(str(e))

#     return JsonResponse(resp)
# # Caracteristique Points
# def delete_caracteristique(request, caracteristique_id):
#     resp = {'status': 'failed'}
#     try:
#         caracteristique = get_object_or_404(CaracteristiquePoints, id=caracteristique_id)
#         caracteristique.delete()
#         resp = {'status': 'success'}
#         messages.success(request, "Caracteristique Points supprimer avec succes")
#     except Exception as e:
#         print(str(e))

#     return JsonResponse(resp)