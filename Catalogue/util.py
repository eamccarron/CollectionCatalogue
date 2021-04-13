from django.apps import apps
from .forms import *

strToModel = dict()

for model in apps.get_app_config("Catalogue").get_models():
    name = model._meta.verbose_name
    strToModel[name] = model


strToForm = {
    "artwork": ArtworkForm,
    "book": BookForm,
    "coin": CoinForm,
    "fossil": FossilForm,
    "medal": MedalForm,
    "meteorite": MeteoriteForm,
    "photo": PhotoForm,
    "pottery": PotteryForm,
    "sculpture": SculptureForm,
    "weapon": WeaponForm,
}

strToFormObj = dict()
for formName, formClass in strToForm.items():
    strToFormObj[formName] = formClass()