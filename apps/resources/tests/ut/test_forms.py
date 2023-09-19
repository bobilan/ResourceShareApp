from django.test import TestCase
from apps.resources.form import PostResourceForm


class PostRequestForm(TestCase):

    def test_valid_method_return_true(self):
        data = {
            'title': 'Python for Beginers',
            'link': 'http://link.python.org',
            'description': 'Python for Noobs',
            'category': 'Python',
        }
        form = PostResourceForm(data=data)

        self.assertTrue(form.is_valid())

    def test_form_when_link_is_missing(self):
        data = {
            'title': 'Python for Beginers',
            # 'link': 'http://link.python.org',
            'description': 'Python for Noobs',
            'category': 'Python',
        }
        form = PostResourceForm(data=data)
        form.is_valid()

        # self.assertTrue(form.is_valid())
        self.assertEqual(form.errors['link'], ['This field is required.'])


