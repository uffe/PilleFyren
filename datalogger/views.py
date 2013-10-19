from datalogger.models import Filling,LogEntry
from django.http import Http404, HttpResponse
from django.utils import timezone
# Create your views here.

def get_parameter_or_404(dictionary, parameter, as_type=None):
    # actually it's more appropriate with 400 as error code, but
    # Django hasn't got that
    if not parameter in dictionary:
        raise Http404("missing required parameter %s" % parameter)

    v = dictionary[parameter]
    if as_type:
        try:
            return as_type(v)
        except ValueError:
            raise Http404("couldn't cast parameter %s to %s" % (parameter, as_type))
    else:
        return v



def registerFilling(request):
    x = Filling(timestamp=timezone.now())
    x.save()
    if x:
        return HttpResponse("OKAY", mimetype='text/plain')
    else:
        return HttpResponse("FAILED", mimetype='text/plain')
    
def registerLog(request):
    aip = get_parameter_or_404(request.GET, "ip")
    arssi = get_parameter_or_404(request.GET, "rssi")
    ahum = get_parameter_or_404(request.GET, "humidity")
    atemp = get_parameter_or_404(request.GET, "temp")
    adist = get_parameter_or_404(request.GET, "distance")
    amillis= get_parameter_or_404(request.GET, "millis")
    
    x = LogEntry(ip=aip, rssi=arssi,timestamp=timezone.now(), humidity=ahum, temp=atemp, distance=adist, millis=amillis)
    x.save()
    if x:
        return HttpResponse("OKAY", mimetype='text/plain')
    else:
        return HttpResponse("FAILED", mimetype='text/plain')
