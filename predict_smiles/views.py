#
# from django.contrib.auth.decorators import login_required
# from .form import SmilesForm
# from .apps import *
# from django.shortcuts import redirect, render
# from django.urls import reverse
#
# # Create your views here.
# @login_required
# def index(request):
#     predict_mol_form=SmilesForm()
#     return render(request, 'predict_smiles/predict.html', {'predict_mol_form': predict_mol_form})
# @login_required
# def predict_smiles(request):
#     if request.POST:
#         form=SmilesForm(request.POST)
#         if form.is_valid():
#             MW = form.cleaned_data['MW']
#             LogP = form.cleaned_data['LogP']
#             TPSA = form.cleaned_data['TPSA']
#             smiles= get_smiles(MW, LogP, TPSA)
#             return render(request, 'predict_smiles/predict.html', {'smiles': smiles, 'predict_mol_form': SmilesForm()})
#         else:
#             return redirect(reverse("index"))
#     return redirect(reverse("index"))


from django.contrib.auth.decorators import login_required
from .form import SmilesForm
from .apps import *
from django.shortcuts import redirect, render
from django.urls import reverse
from users.models import User
# Create your views here.
@login_required
def index(request):
    predict_mol_form=SmilesForm()
    return render(request, 'predict_smiles/predict.html', {'predict_mol_form': predict_mol_form})
@login_required
def predict_smiles(request):
    if request.POST:
        form=SmilesForm(request.POST)
        if form.is_valid():
            MW = form.cleaned_data['MW']
            LogP = form.cleaned_data['LogP']
            TPSA = form.cleaned_data['TPSA']
            smiles= get_smiles(MW, LogP, TPSA)
            return render(request, 'predict_smiles/predict.html', {'smiles': smiles, 'predict_mol_form': SmilesForm()})
        else:
            return redirect(reverse("index"))
    return redirect(reverse("index"))
@login_required
def upgrade(request):
    if request.GET:
         id = request.GET.get('id')
         user = User.objects.get( id = id )
         user.isPremium = True
         user.save()
    return redirect(request.META.get('HTTP_REFERER', reverse('index')))
