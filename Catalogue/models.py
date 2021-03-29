from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#this is stored in the record model
class OptionalAttributes(models.Model):
    attribute_1_name = models.CharField(max_length=100, blank=True, null=True)
    attribute_1_content = models.TextField(blank=True, null=True)

    attribute_2_name = models.CharField(max_length=100, blank=True, null=True)
    attribute_2_content = models.TextField(blank=True, null=True)

    attribute_3_name = models.CharField(max_length=100, blank=True, null=True)
    attribute_3_content = models.TextField(blank=True, null=True)

    attribute_4_name = models.CharField(max_length=100, blank=True, null=True)
    attribute_4_content = models.TextField(blank=True, null=True)

    attribute_5_name = models.CharField(max_length=100, blank=True, null=True)
    attribute_5_content = models.TextField(blank=True, null=True)

    attribute_6_name = models.CharField(max_length=100, blank=True, null=True)
    attribute_6_content = models.TextField(blank=True, null=True)

    attribute_7_name = models.CharField(max_length=100, blank=True, null=True)
    attribute_7_content = models.TextField(blank=True, null=True)

    attribute_8_name = models.CharField(max_length=100, blank=True, null=True)
    attribute_8_content = models.TextField(blank=True, null=True)

    attribute_9_name = models.CharField(max_length=100, blank=True, null=True)
    attribute_9_content = models.TextField(blank=True, null=True)

    attribute_10_name = models.CharField(max_length=100, blank=True, null=True)
    attribute_10_content = models.TextField(blank=True, null=True)

class Record(models.Model):
    catalogue_num = models.IntegerField(
        default=1, primary_key=True
    )  # default is what is registered as value if no other value is received
    name = models.CharField(
        max_length=100
    )  # string that has a max length of 100 characters
    date = models.CharField(
        max_length=100, blank=True, null=True
    )  # up to 100 characters, so it can give a description or range of dates
    condition = models.TextField(blank=True, null=True)  # unrestricted text
    provenance = models.TextField(blank=True, null=True)  # the origin of item
    description = models.TextField(blank=True, null=True)  # unrestricted text
    # value = models.IntegerField(blank=True, null=True)
    item_type = models.CharField(max_length=100, blank=True, null=True)
    staff_creator = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL) #one to many relationship, a user can create many base models but 
    #a base model may only be created by 1 user. cascade on delete so the entry doesn't still exist in the users table.
    optional_attribute = models.OneToOneField(OptionalAttributes, blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Fossil(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    size = models.IntegerField(
        blank=True, null=True
    )  # allow field to be left blank and set to null
    scientific_name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.record.name


class Sculpture(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    material = models.CharField(
        max_length=100, blank=True, null=True
    )  # material used to build sculpture
    artist = models.CharField(max_length=100, blank=True, null=True)
    colour = models.CharField(max_length=100, blank=True, null=True)


class Coin(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    colour = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    coin_value = models.CharField(max_length=100, blank=True, null=True)
    design = models.TextField(
        blank=True, null=True
    )  # what object or person (user able to put extra information about the person) is on the coin if any


class Jewelry(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    JEWELRY_TYPES = (
        ("Pendant", "Pendant"),
        ("Bracelet", "Bracelet"),
        ("Cufflink", "Cufflink"),
        ("Earrings", "Earrings"),
        ("Necklace", "Necklace"),
        ("Ring", "Ring"),
        ("Brooche", "Brooche"),
        ("Gem", "Gem"),
        ("Other", "Other"),
    )
    jewelry_type = models.CharField(max_length=10, choices=JEWELRY_TYPES)
    colour = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)


class Meteorite(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    size = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    colour = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)


class Artwork(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100, blank=True, null=True)
    artist_lifespan = models.TextField(blank=True, null=True)
    dimensions = models.CharField(max_length=100, blank=True, null=True)
    supplies_used = models.CharField(
        max_length=100, blank=True, null=True
    )  # paintbrush, pencil, etc
    art_style = models.TextField(blank=True, null=True)


class Pottery(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    artist = models.CharField(max_length=100, blank=True, null=True)
    artist_lifespan = models.TextField(blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    technique = models.TextField(blank=True, null=True)


class Medal(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    medal_type = models.CharField(
        max_length=100, blank=True, null=True
    )  # what was this medal awarded for
    colour = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    design = models.TextField(blank=True, null=True)  # what design is on the medal
    recipient = models.TextField(blank=True, null=True)


class Weapon(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    manufacturer = models.CharField(max_length=100, blank=True, null=True)
    weapon_type = models.CharField(max_length=100, blank=True, null=True)
    combat = models.CharField(
        max_length=100, blank=True, null=True
    )  # is this weapon long distance or close combat
    size = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)


class Book(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    author = models.TextField(
        blank=True, null=True
    )  # it is text field in case there are many authors
    illustrator = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=100, blank=True, null=True)
    genre = models.CharField(max_length=100, blank=True, null=True)
    publisher = models.CharField(max_length=100, blank=True, null=True)


class Photo(models.Model):
    record = models.OneToOneField(Record, on_delete=models.CASCADE)
    photographer = models.CharField(max_length=100, blank=True, null=True)


# user can choose what model type they are looking for and result will get stored in the allModels object model_type attribute
class allModels(models.Model):
    MODEL_TYPES = (
        ("Artwork", "Artwork"),
        ("Book", "Book"),
        ("Coin", "Coin"),
        ("Fossil", "Fossil"),
        ("Jewelry", "Jewelry"),
        ("Medal", "Medal"),
        ("Meteorite", "Meteorite"),
        ("Photo", "Photo"),
        ("Pottery", "Pottery"),
        ("Sculpture", "Sculpture"),
        ("Weapon", "Weapon"),
    )
    model_type = models.CharField(max_length=11, choices=MODEL_TYPES)




