from django.test import TestCase
from django.contrib.auth.models import User
import json

# Create your tests here.

test_user = {"username":'testuser', "password":'12345'}

class Todo(TestCase):
    def setUp(self):
        new_user = User.objects.create(
            username=test_user["username"])
        new_user.set_password(test_user["password"])
        new_user.save()
        return new_user
    def get_token(self):
        res = self.client.post('/api/token/',
                                data=json.dumps({
                                    'username': test_user["username"],
                                    'password': test_user["password"],
                                }),
                                content_type='application/json',
                                )
        result = json.loads(res.content)
        self.assertTrue("access" in result)
        return result["access"]

    def test_todo_list(self):
        token = self.get_token()
        res = self.client.get('/api/todo/',
                                HTTP_AUTHORIZATION='Bearer ' + token,
                                content_type='application/json',
                                )
        result = json.loads(res.content)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(result), 0)

    def test_category_create(self):
        token = self.get_token()
        res = self.client.post('/api/category/',
                                data=json.dumps({
                                    'name': 'test',
                                }),
                                HTTP_AUTHORIZATION='Bearer ' + token,
                                content_type='application/json',
                                )
        result = json.loads(res.content)
        print(result)
        print('\n\n')
        self.assertEqual(res.status_code, 201)
        self.assertEqual(result["name"], 'test')
        return result


    def test_todo_create(self):
        token = self.get_token()
        category = self.test_category_create()
        # user = User.objects.all().values()
        # print(user)
        res = self.client.post('/api/todo/',
                                data=json.dumps({
                                    'title': 'test',
                                    'description': 'test',
                                    'priority': 'low',
                                    'completed': False,
                                    'category': [category['id']],
                                    'created_by': 2
                                }),
                                HTTP_AUTHORIZATION='Bearer ' + token,
                                content_type='application/json',
                                )
        result = json.loads(res.content)
        print(res.content)
        self.assertEqual(res.status_code, 201)
        self.assertEqual(result["title"], 'test')
        self.assertEqual(result["description"], 'test')
        self.assertEqual(result["priority"], 'low')
        self.assertEqual(result["completed"], False)
        self.assertEqual(result["category"], [2])
        self.assertEqual(result["created_by"], 2)


    # def test_update_todo(self):
    #     token = self.get_token()
    #     res = self.client.put('/api/todo/1/',
    #                             data=json.dumps({
    #                                 'title': 'test',
    #                                 'description': 'test',
    #                                 'priority': 'low',
    #                                 'completed': False,
    #                             }),
    #                             content_type='application/json',
    #                             HTTP_AUTHORIZATION='Bearer ' + token,
    #                             )
    #     self.assertEqual(res.status_code, 200)

    # def test_delete_todo(self):
    #     token = self.get_token()
    #     res = self.client.delete('/api/todo/1/',
    #                             HTTP_AUTHORIZATION='Bearer ' + token,
    #                             )
    #     self.assertEqual(res.status_code, 204)

        


# class Category(TestCase):
#     def setUp(self):
#         new_user = User.objects.create(
#             username=test_user["username"])
#         new_user.set_password(test_user["password"])
#         new_user.save()

#     def get_token(self):
#         res = self.client.post('/api/token/',
#                                data=json.dumps({
#                                    'username': test_user["username"],
#                                    'password': test_user["password"],
#                                }),
#                                content_type='application/json',
#                                )
#         result = json.loads(res.content)
#         self.assertTrue("access" in result)
#         return result["access"]


#     def test_create_category(self):
#         token = self.get_token()
#         res = self.client.post('/api/category/',
#                                data=json.dumps({
#                                    'name': 'test',
#                                }),
#                                content_type='application/json',
#                                HTTP_AUTHORIZATION='Bearer ' + token,
#                                )
#         result = json.loads(res.content)
#         self.assertTrue("id" in result)
#         self.assertEqual(result["name"], "test")


#     def test_create_category_no_token(self):
#         res = self.client.post('/api/category/',
#                                data=json.dumps({
#                                    'name': 'test',
#                                }),
#                                content_type='application/json',
#                                )
#         result = json.loads(res.content)
#         self.assertTrue("detail" in result)
#         self.assertEqual(result["detail"], "Authentication credentials were not provided.")

#     def test_create_category_no_name(self):
#         token = self.get_token()
#         res = self.client.post('/api/category/',
#                                data=json.dumps({
#                                    'name': '',
#                                }),
#                                content_type='application/json',
#                                HTTP_AUTHORIZATION='Bearer ' + token,
#                                )
#         result = json.loads(res.content)
#         self.assertTrue("name" in result)
#         self.assertEqual(result["name"], ["This field may not be blank."])

