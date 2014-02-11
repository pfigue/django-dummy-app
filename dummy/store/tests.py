import json
from django.test import (TestCase, RequestFactory)
from model_mommy import mommy
from store.views import (StoreItemsListView, )
from store.models import (Item, )


class StoreItemsListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()


    def test_list_all_items_with_json(self):
        orange_juice = mommy.make(Item)
        orange_juice.name = 'Orange Juice'
        orange_juice.price = 1.59
        orange_juice.quantity = 3
        orange_juice.save()

        apfelschorle = mommy.make(Item)
        apfelschorle.name = 'Apfelschorle'
        apfelschorle.price = 0.8
        apfelschorle.quantity = 7
        apfelschorle.save()

        expected_elements =  ['Apfelschorle', 'Orange Juice', ]

        params = {}
        request = self.factory.get('/store/', data=params, HTTP_ACCEPT='application/json')

        response = StoreItemsListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        # We will get a list of elements, like [ {'name':'Apfelschorle', 'price':...} {}, ...]
        extract_name = lambda x: x['name']
        elements = map(extract_name, response_data)

        self.assertSetEqual(set(elements), set(expected_elements))

    def test_list_no_elements(self):
        expected_elements =  []

        params = {}
        request = self.factory.get('/store/', data=params, HTTP_ACCEPT='application/json')

        response = StoreItemsListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

        response_data = json.loads(response.content)
        # We will get a list of elements, like [ {'name':'Apfelschorle', 'price':...} {}, ...]
        extract_name = lambda x: x['name']
        elements = map(extract_name, response_data)

        self.assertSetEqual(set(elements), set(expected_elements))

    def test_add_a_new_element(self):
        new_element = {
            'name':     'Mate Refreshment',
            'price':    1.5,
            'quantity': 10,
        }

        request = self.factory.post('/store/', data=new_element, HTTP_ACCEPT='application/json')
        response = StoreItemsListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        self.assertEqual(response_data['id'], 1)

    def test_add_a_new_element_and_retrieve_it(self):
        # Add a new element
        new_element = {
            'name':     'Mate Refreshment',
            'price':    1.5,
            'quantity': 10,
        }
        request = self.factory.post('/store/', data=new_element, HTTP_ACCEPT='application/json')
        StoreItemsListView.as_view()(request)

        expected_elements = ['Mate Refreshment', ]

        # Fetch all the elements
        params = {}
        request = self.factory.get('/store/', data=params, HTTP_ACCEPT='application/json')
        response = StoreItemsListView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)
        # We will get a list of elements, like [ {'name':'Apfelschorle', 'price':...} {}, ...]
        extract_name = lambda x: x['name']
        elements = map(extract_name, response_data)

        self.assertSetEqual(set(elements), set(expected_elements))
