from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Catalogue.models import Record, allModels
from ..forms import *
from Catalogue.util import strToForm, strToModel, strToFormObj
from django.db.models import Max


def create_route(request):
    if request.method == "GET":
        form = RecordForm()
        models = []
        for model in allModels.objects.all():
            model_name = model.model_type
            models.append({"model_name": model_name, "model_value": model_name.lower()})

        context = {
            "form": form,
            "models": models,
            "model_forms": strToFormObj.items(),
            "opt_form": OptionForm,
        }
        return render(request, "create.html", context)
    else:  # POST
        form = RecordForm(request.POST, request.FILES)

        if form.is_valid():
            args = Record.objects.all()
            if len(args) == 0:
                c_num = 1
            else:
                c_num = 1 + args.aggregate(Max("catalogue_num"))["catalogue_num__max"]
            form.instance.catalogue_num = c_num
            form.instance.author = request.user
            form.save()

            the_type = form.cleaned_data["item_type"]

            if the_type in strToForm:
                sub_form = strToForm[the_type](request.POST)
                if sub_form.is_valid():
                    sub_form.instance.record_id = c_num
                    sub_form.save()
        return HttpResponseRedirect("/items?catalogue_num=%i" % c_num)
    return render(request, "/")
