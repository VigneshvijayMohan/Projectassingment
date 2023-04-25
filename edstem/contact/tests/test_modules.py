from django.test import TestCase
from contact.models import Contact

class ContactItemTest(TestCase):
    def get_test_item(self):
        item = Contact.objects.create(
            name = "Vignesh",
            address = "Vipanchika",
            phone = "4529393993",
            email= "vigneshvijay@gmail.com"

        )
        self.assertEqual (item.__str__, "name : Vignesh")
