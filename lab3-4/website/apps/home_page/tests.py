from django.test import TestCase


def test_main_view(self):
    response = self.client.get(f'')
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'base.html')