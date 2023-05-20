from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .apps import *


class call_model(APIView):

    def get(self, request):
        if request.method == 'GET':
            # sentence is the query we want to get the prediction for
            params = request.GET.get('smile')
            print(params)

            # predict method used to get the prediction
            #ret=RetrosynthesisConfig(app_name="deployment", app_module="retrosynthesis")
            response = run(params)

            # returning JSON response
            return render(request, 'retrosynthesis/retro.html', {'retro': response})

@login_required
def index(request):
    return render(request, 'retrosynthesis/retro.html')