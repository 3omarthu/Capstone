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
        res = self.client().get('/movies', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})

        self.assertEqual(res.status_code, 200)


    # def test_404_get_movies(self):
    #     """Test 404 for movies"""
    #     res = self.client().get('/movies', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})

    #     self.assertEqual(res.status_code, 404)


    def test_movies_delete(self):
        """Test deleting movies"""
        id = 57 #enter valid id here before running the test
        res = self.client().delete('/movies/'+id, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], id)


    def test_404_movies_delete(self):
        """Test 404 for deleting movies"""
        res = self.client().delete('/movies/100', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})
        
        self.assertEqual(res.status_code, 404)


    def test_movies_post(self):
        """Test adding movie"""
        res = self.client().post('/movies', json={"title": "Scary Movie","release_date": "2002"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})
        data = json.loads(res.data)
        self.question_id = data['created']
        
        self.assertEqual(res.status_code, 200)


    def test_422_movies_post(self):
        """Test adding movie with wrong object"""
        res = self.client().post('/movies', json={"title": "Scary Movie"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})

        self.assertEqual(res.status_code, 422)


    def test_movies_patch(self):
        """Test editing movie"""
        id = 56   # enter valid id here before running the test
        res = self.client().patch('/movies/'+id, json={"title": "Scary Movie"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)


    def test_404_movies_patch(self):
        """Test editing movie wrong object"""
        res = self.client().patch('/movies/900', json={"title": "Scary Movie"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4NzZkYzY4MjYwMGEwYjY5MGRhIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MjI1OTYsImV4cCI6MTU5NjkwODk5NiwiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.gJWMG59mnYOFXm-phNQxTKoWceH6Q4OlyB4K3fj5_CzsCTLjqpLsKAHrNiAPDXe7ZO2E_wpa9XaSUEQNyMcmgs8MOgOxp7LdrlkDLQOO5Hr0zx8Yj-csqvTJoChgQ3qnzq7atoSi8azXEgQb-mpGWJsx7XuEo3RBR5Al3ROoDDpAdbF-mqukKHstT7l2IZV9uz0nba_vSyRONUlKpeGQISjB44z1embRVUdMQ3hfrKFe_RZ6egxjsvF39y58xGY5fCNkpU8JAzO_OaiRCJv3IY7pZfOvsTedW3uY2B7cnidVts31WvP-vxT0C9m39SimPoz3rmI0L4B41ETcwSjAUw'})

        self.assertEqual(res.status_code, 404)


    def test_get_actors(self):
        """Test get actor"""
        res = self.client().get('/actors', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4NTNkYzY4MjYwMGEwYjY5MGQ1IiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MjI3OTMsImV4cCI6MTU5NjkwOTE5MywiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.F6mOEvgSjHbBXa2NBykDzCJeAPNH2cnex2h7DBNJ300W2JAdiNoqqobyprFETF-R0xaAzVnvXrLZloL9aOcmvAZ-SEL-YG53lpoUFRukx9I3IkCYcbB3uLCFBm1DS3N3PHjyNJkmczmhwtGdM5HPuueR4jtor4Vatx3HttbCNI854_Otdr0G328wisRATWyDOWE620eD7bvvz5WK7fLKhDnm-kkAjTfXvk7NqVOp-j52ihSmpRjoP7pL62SyeUHFgHboa-i_RAxfbpiLzxzXxOGeLhTy_vWaae8RPUQ7yE0x6-p_pJT0nv1Ftf4pFB582on-G-mpVBETYRc6WYXaCA'})

        self.assertEqual(res.status_code, 200)


    # def test_404_get_actors(self):
    #     """Test 404 for geting actors"""
    #     res = self.client().get('/actors', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})

    #     self.assertEqual(res.status_code, 404)


    def test_actors_delete(self):
        """Test deleting actors"""
        id = 3   # enter valid id here before running the test
        res = self.client().delete('/actors/'+id, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['deleted'], id)


    def test_404_actors_delete(self):
        """Test 404 for deleting actors"""
        res = self.client().delete('/actors/100', headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})
        
        self.assertEqual(res.status_code, 404)


    def test_actors_post(self):
        """Test adding actor"""
        res = self.client().post('/actors', json={"name": "Omar","age": "24", "gender": "male"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)


    def test_422_actors_post(self):
        """Test adding actor with wrong object"""
        res = self.client().post('/actors', json={"name": "Omar"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})

        self.assertEqual(res.status_code, 422)


    def test_actors_patch(self):
        """Test editing actor"""
        id = 2 #enter valid id here before running the test
        res = self.client().patch('/actors/'+id, json={"name": "Omar"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InR3VDZiUzlyLWpEVGhDb2hEZDJHUCJ9.eyJpc3MiOiJodHRwczovL2Rldi10cHM1NG1hYS51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWYyYjA4NzZkYzY4MjYwMGEwYjY5MGRhIiwiYXVkIjpbImh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCIsImh0dHBzOi8vZGV2LXRwczU0bWFhLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE1OTY4MjI1OTYsImV4cCI6MTU5NjkwODk5NiwiYXpwIjoiZHZ4bzV0Nk45TXR0Tjd3UEwzODc4QkREaXN6czNjQjYiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.gJWMG59mnYOFXm-phNQxTKoWceH6Q4OlyB4K3fj5_CzsCTLjqpLsKAHrNiAPDXe7ZO2E_wpa9XaSUEQNyMcmgs8MOgOxp7LdrlkDLQOO5Hr0zx8Yj-csqvTJoChgQ3qnzq7atoSi8azXEgQb-mpGWJsx7XuEo3RBR5Al3ROoDDpAdbF-mqukKHstT7l2IZV9uz0nba_vSyRONUlKpeGQISjB44z1embRVUdMQ3hfrKFe_RZ6egxjsvF39y58xGY5fCNkpU8JAzO_OaiRCJv3IY7pZfOvsTedW3uY2B7cnidVts31WvP-vxT0C9m39SimPoz3rmI0L4B41ETcwSjAUw'})
        data = json.loads(res.data)
        
        self.assertEqual(res.status_code, 200)


    def test_404_actors_patch(self):
        """Test editing actor with wrong object"""
        res = self.client().patch('/actors/900', json={"name": "Omar"}, headers={'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InVRMHVTRG1qekpXWGgxWVNDalZEbiJ9.eyJpc3MiOiJodHRwczovL2ZzbmRvbWFyLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDA4OTJjZWZmY2JlMjAwNmE4ODFhOWMiLCJhdWQiOiJodHRwOi8vbG9jYWxob3N0OjgwODAiLCJpYXQiOjE2MTQ3MDUxOTAsImV4cCI6MTYxNDcxMjM5MCwiYXpwIjoiUnZHaGZpbkZLcWxQMllRSjRKTmFHUGU3UkhQZFRFbXMiLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvciIsImRlbGV0ZTptb3ZpZSIsImdldDphY3RvciIsImdldDptb3ZpZSIsInBhdGNoOmFjdG9yIiwicGF0Y2g6bW92aWUiLCJwb3N0OmFjdG9yIiwicG9zdDptb3ZpZSJdfQ.Y8s_GkIZWGeLGgslieoj5UyNia0bsK0eE8n0KuMLr7qqNzZ_y9UPpbNdcPqJfsoDlp_5T_LIpMDoqHXCidUWSZNwXSYs9y8sG2z02qhIknSaeWWS9MgjoaDXu749tPbsiz1aP65oDd4C2p_k14YLDBVRUcELXc0q1AcNCHOSxQqV2FfMpfLPIJI4tyZPDZRjyVhp6D-rWlekyVj8y4XTtH_lCBLEhEZv4P8WmZmR_x6tEp2p73O3eAIeygTuiCBz0TS8YoDr27fGP4AHpIiiTF5Dryfb-7B2WIGCI20weiIGc93WJ7hefwEnZCQjF8cA5lh28KHiGdcgFM5pnBhH1g'})

        self.assertEqual(res.status_code, 404)


if __name__ == "__main__":
    unittest.main()
    
