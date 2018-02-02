from datetime import datetime
from .Helper import *


class FormsTest(SupersaasTest):
    def test_get(self):
        super_form_id = 12345
        self.assertIsNotNone(self.client.forms.get(super_form_id))

    def test_find(self):
        form_id = 67890
        self.assertIsNotNone(self.client.forms.find(form_id, datetime.now()))
