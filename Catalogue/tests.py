from django.test import TestCase

from Catalogue.models import *

Test_Record = {
    "catalogue_num" : 1,
    "name" : "Test Record",
    "date" : "Sept. 27, 1998",
    "condition" : "Good",
    "provenance" : "Test Provenance",
    "description" : "Test Description",
    "item_type" : "Record"
}

Test_Fossil = {
    "size" : 4,
    "scientific_name" : "Test Name"
}

def createBaseTestRecord():
        Record.objects.create(
            catalogue_num = Test_Record["catalogue_num"],
            name = Test_Record["name"], 
            date = Test_Record["date"],
            condition = Test_Record["condition"],
            provenance = Test_Record["provenance"],
            description = Test_Record["description"]
        )

class BaseRecord(TestCase):
    def setUp(self):
        createBaseTestRecord()
    
    def test_record_can_be_created():
        self.assertNotEqual(Record.objects.get(Test_Record["catalogue_num"]), None)

    def test_all_record_fields_can_be_read():
        #Store record created in setUp
        saved_record = Record.objects.get(Test_Record.catalogue_num)
        #Read each field of record
        catalogue_num_field = saved_record._meta.get_field('catalogue_num') 
        name_field = saved_record._meta.get_field('name') 
        date_field = saved_record._meta.get_field('date') 
        condition_field = saved_record._meta.get_field('condition') 
        provenance_field = saved_record._meta.get_field('provenance') 

        #Test that each stored field is equal to the value stored in testRecord
        self.assertEqual(catalogue_num_field.value_from_object(saved_record), Test_Record["catalogue_num"])
        self.assertEqual(name_field.value_from_object(saved_record), Test_Record["catalogue_num"])
        self.assertEqual(date_field.value_from_object(saved_record), Test_Record["catalogue_num"])
        self.assertEqual(condition_field.value_from_object(saved_record), Test_Record["catalogue_num"])
        self.assertEqual(provenance_field.value_from_object(saved_record), Test_Record["catalogue_num"])

class FossilRecord(TestCase):
    def setUp(self):
        createBaseTestRecord()
        Fossil.objects.create(
            record = Record.objects.get(Test_Record["catalgoue_num"]),
            size = Test_Fossil["size"],
            scientific_name = Test_Fossil["scientific_name"]
        )