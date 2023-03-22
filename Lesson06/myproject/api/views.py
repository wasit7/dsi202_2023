from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def get_data(request):
    data={'name':'David', 'age':22}
    return Response(data)
