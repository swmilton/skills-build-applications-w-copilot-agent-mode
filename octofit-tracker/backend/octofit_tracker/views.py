from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def api_root(request, format=None):
    base_url = request.build_absolute_uri('/')
    return Response({
        'message': 'API root is working.'
    })
