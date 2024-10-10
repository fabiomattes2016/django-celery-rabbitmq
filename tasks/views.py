from rest_framework.views import APIView
from django.contrib.auth.models import User
from .tasks import create_random_user_accounts
from rest_framework.response import Response


class GenerateRandomUserView(APIView):
    def post(self, request):
        total = int(request.data.get('total'))
        
        create_random_user_accounts.delay(total)
        
        return Response(
            {
                "result": "Estamos gerando seus usuários aleatórios. Espere um momento!"
            },
            status=201
        )
