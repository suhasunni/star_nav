from ..calculations.geometry import bearing_to
from django.http import JsonResponse

def bearing(request):
    """ returns bearing to destination (in degrees) """
    obs_lat = request.GET.get('obs_lat', False)
    obs_lon = request.GET.get('obs_lon', False)

    end_lat = request.GET.get('end_lat', False)
    end_lon = request.GET.get('end_lon', False)

    if (not obs_lat 
        or not obs_lon 
        or not end_lat 
        or not end_lon
    ):
        return JsonResponse({
            "result": "error",
            "error": "1 or more parameters not found."
        })
    
    obs_lat, obs_lon, end_lat, end_lon = float(obs_lat), float(obs_lon), float(end_lat), float(end_lon)

    return JsonResponse({"result": bearing_to(obs_lat, obs_lon, end_lat, end_lon)})