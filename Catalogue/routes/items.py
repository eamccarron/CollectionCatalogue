from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Catalogue.models import Record, OptionalAttributes
from ..forms import *
from Catalogue.util import strToModel


def parse(optAttr):
    d = optAttr
    out = dict()
    for i in range(1, 11):
        keyStr = f"attribute_{i}_name"
        key = getattr(d, keyStr)

        valStr = f"attribute_{i}_content"
        val = getattr(d, valStr)

        if key == None or val == None:
            continue
        else:
            out[key] = val
    return out


def subRecord(id):
    for model_name, model in strToModel.items():
        if model_name in ["record", "optional attributes", "all models"]:
            continue
        else:
            candidates = model.objects.all().filter(id=id)
            if len(candidates) > 0:
                print(model_name)
                return candidates
    return None


def subRecordInfo(records):
    out = []
    for record in records:
        keys = record._meta.local_fields
        for key in keys:
            key = key.name
            if key not in ["_state", "id", "record"]:
                val = getattr(record, key)
                out.append((key, val))

    return out


def item_route(request):
    records = Record.objects.all()
    if "catalogue_num" in request.GET:
        num = request.GET.__getitem__("catalogue_num")
        if num:
            record = records.filter(catalogue_num=num)[0]

    has_attr = record.optional_attribute_id != None
    attr = {}
    if has_attr:
        attr_obj = OptionalAttributes.objects.filter(id=record.optional_attribute_id)[0]
        attr = parse(attr_obj)

    context = {
        "record": record,
        "can_edit": request.user.is_authenticated,
        "has_attr": has_attr,
        "attr": attr.items(),
    }

    subRec = subRecord(num)
    if subRec != None:
        context["subRecord"] = subRecordInfo(subRec)

    return render(request, "items.html", context)
