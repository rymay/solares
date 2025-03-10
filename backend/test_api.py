import unittest
from main import create_app
from config import TestConfig
from exts import db


class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app=create_app(TestConfig)
        self.client=self.app.test_client(self)

        #with self.app.app_context():
            #db.init_app(self.app)
            #db.create_all()

    def test_hello_world(self):
        hello_response=self.client.get('/solares/hello')
        json=hello_response.json
        self.assertEqual(json,{"message":"Hello World"})

    def test_login(self):
        login_response=self.client.post(
            '/auth/login',
            json={
                "usuario":"andres",
                "contrasena":"winona"
            }
        )
        status_code=login_response.status_code
        json=login_response.json

        self.assertEqual(status_code,200)

    def test_get_all_solares(self):
        """TEST Todos los Solares"""
        response=self.client.get('/solares/solares')
        status_code=response.status_code

        self.assertEqual(status_code,200)

    def test_get_one_solares(self):
        id=2
        response=self.client.get('/solares/solar/{id}')
        status_code=response.status_code

        print(status_code)

        self.assertEqual(status_code,404)

    # def test_create_solares(self):
    #     login_response=self.client.post(
    #         '/auth/login',
    #         json={
    #             "usuario":"andres",
    #             "contrasena":"winona"
    #         }
    #     ) 
    #     access_token=login_response.json["access_token"]

    #     create_solar_response=self.client.post(
    #         '/solares/solares',
    #         json={
    #             'NombreFinca':'Nombre9',
    #             'Calle':'Calle3',
    #             'nCalle':'90',
    #             'Puerta':'H',
    #             'Extension':'90'
    #         },
    #         headers={
    #             "Authorization":f"Bearer {access_token}"}
    #     )

    #     status_code=create_solar_response.status_code

    #     self.assertEqual(status_code,201)

    def test_update_solares(self):
        login_response=self.client.post(
            '/auth/login',
            json={
                "usuario":"andres",
                "contrasena":"winona"
            }
        ) 
        access_token=login_response.json["access_token"]
        id=2

        update_response=self.client.put(
            f'/solares/solar/{id}',
            json={
                'NombreFinca':'Nombre12',
                'Calle':'Calle23',
                'nCalle':'99',
                'Puerta':'J',
                'Extension':'200'
            },
            headers={
                "Authorization":f"Bearer {access_token}"}
        )
        status_code=update_response.status_code
        self.assertEqual(status_code,200)


    def test_delete_solares(self):
        login_response=self.client.post(
            '/auth/login',
            json={
                "usuario":"andres",
                "contrasena":"winona"
            }
        ) 
        id=11
        access_token=login_response.json["access_token"]
        delete_response=self.client.delete(
            f'/solares/solar/{id}',
            headers={
                "Authorization":f"Bearer {access_token}"}
        )
        
        status_code=delete_response.status_code
        self.assertEqual(status_code,200)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            #db.drop_all()

if __name__ == '__main__':
    unittest.main()