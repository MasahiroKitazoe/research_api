from django.test import TestCase
from django.urls import reverse


class TestScrapeDressInn(TestCase):

  def test_response_returns_json_obj(self):
    params = {
    "user_id": "wearewemossss",
    "password": "fdjLJIdg4jl27fhieor444"
    }
    res = \
      self.client.post(reverse('dress_inn:scrape_diesel'), params)
    self.assertEqual(res.status_code, 200)
