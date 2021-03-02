import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db,Movie, Actor
from app import create_app


class CastingTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_path_test = "postgres://yavgsgiwsnjpis:48db92f09a67d31af2e83b1c152aca0eeb024f34a9c051596fb0e6c540d57f6a@ec2-3-232-163-23.compute-1.amazonaws.com:5432/daif2ne8fscvc9"
        setup_db(self.app, self.database_path_test)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    '''
    Commented out 404 tests require an empty database
    '''


    def test_get_movies(self):
        """Test get movies """
        res = self.client().get('/movies', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})

        self.assertEqual(res.status_code, 200)


    # def test_404_get_movies(self):
    #     """Test 404 for movies"""
    #     res = self.client().get('/movies', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})

    #     self.assertEqual(res.status_code, 404)


    def test_movies_delete(self):
        """Test deleting movies"""
        id = 5 #enter valid id here before running the test
        res = self.client().delete('/movies/'+str(id), headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], id)


    def test_404_movies_delete(self):
        """Test 404 for deleting movies"""
        id = 200
        res = self.client().delete('/movies/'+str(id), headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})
        
        self.assertEqual(res.status_code, 404)


    def test_movies_post(self):
        """Test adding movie"""
        res = self.client().post('/movies', json={"title": "Romance Movie","release_date": "2021"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})
        self.assertEqual(res.status_code, 200)


    def test_422_movies_post(self):
        """Test adding movie with wrong object"""
        res = self.client().post('/movies', json={"title": "Romance Movie"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})
        self.assertEqual(res.status_code, 422)


    def test_movies_patch(self):
        """Test editing movie"""
        id = 8   # enter valid id here before running the test
        res = self.client().patch('/movies/'+str(id), json={"title": "Romance Movie", "release_date": "1998" }, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})
        
        self.assertEqual(res.status_code, 200)


    def test_404_movies_patch(self):
        """Test editing movie wrong object"""
        id = 900
        res = self.client().patch('/movies/'+str(id), json={"title": "Romance Movie"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})

        self.assertEqual(res.status_code, 404)


    def test_get_actors(self):
        """Test get actor"""
        res = self.client().get('/actors', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})

        self.assertEqual(res.status_code, 200)


    # def test_404_get_actors(self):
    #     """Test 404 for geting actors"""
    #     res = self.client().get('/actors', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})

    #     self.assertEqual(res.status_code, 404)


    def test_actors_delete(self):
        """Test deleting actors"""
        id = 9   # enter valid id here before running the test
        res = self.client().delete('/actors/'+str(id), headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], id)


    def test_404_actors_delete(self):
        """Test 404 for deleting actors"""
        id = 100
        res = self.client().delete('/actors/'+str(id), headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})
        
        self.assertEqual(res.status_code, 404)


    def test_actors_post(self):
        """Test adding actor"""
        res = self.client().post('/actors', json={"name": "Omar","age": "24", "gender": "male"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})

        self.assertEqual(res.status_code, 200)


    def test_422_actors_post(self):
        """Test adding actor with wrong object"""
        res = self.client().post('/actors', json={"name": "Omar"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})

        self.assertEqual(res.status_code, 422)


    def test_actors_patch(self):
        """Test editing actor"""
        id = 10 #enter valid id here before running the test
        res = self.client().patch('/actors/'+str(id), json={"name": "Omar"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})

        self.assertEqual(res.status_code, 200)


    def test_404_actors_patch(self):
        """Test editing actor with wrong object"""
        id = 2000
        res = self.client().patch('/actors/'+str(id), json={"name": "Omar"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MTI0ODUsImV4cCI6MTYxNDcxOTY4NSwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.CkcPFTzje0wyuobfaebrNWQuMbChyOM9YIZfB1uLxoAgaSuIVEKksGfAoqstNYQbENxcrRZ_uq3kaLu5dpBywVytrRlNv8-ugpfjR5Jx_b_mB4qUFy5IEfDAVlHQzn7JIMRV_E-0E85RL4HRXg_pxaKHX_pSoSEO4GBXO2lrH2sd26C0a8OXCtZlbSMNW4s9fSFa6t-JyTW6jLqz3QGIkQIseN5b5pX0P8YaJTykkRyebFAcVJvZiVFio9_UXCw3GBVNr8lprZmNbv5-dcYAzZxSkhaVJwaX3CfkdAC8oYGpFzPzrVzXaEC26s3FY28E5aF-N387Zaw-0g3LF3FE7A'})

        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()
    
