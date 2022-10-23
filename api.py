import requests


class RegRequest:
    def __init__(self):
        self.base_url = "https://reqres.in/api/"

    def get_api_resource(self, page, per_page):
        headers = {
            'page': page,
            'per_page': per_page
        }
        res = requests.get(self.base_url + "{resource}", headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_api_users(self, page, per_page):
        headers = {
            'page': page,
            'per_page': per_page
        }
        res = requests.get(self.base_url + "users", headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_api_users_id(self, user_id):
        user_id = {"id": user_id}
        res = requests.get(self.base_url + "users/", params=user_id)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_api_resource_id(self, resource_id):
        resource_id = {"id": resource_id}
        res = requests.get(self.base_url + "{resource}/", params=resource_id)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_api_login(self, body):
        res = requests.post(self.base_url + "login", json=body)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_api_register(self, body):
        res = requests.post(self.base_url + "register", json=body)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def post_api_logout(self):
        res = requests.post(self.base_url + "logout")
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    # def put_api_users_id(self, body):
    #     #user_id = {"id": user_id}
    #     res = requests.put(self.base_url + "users", json=body)
    #     status = res.status_code
    #     try:
    #         result = res.json()
    #     except:
    #         result = res.text
    #     return status, result

    # def put_api_resource_id(self):
    #     res = requests.put(self.base_url + "/users")
    #     status = res.status_code
    #
    # def patch_api_users_id(self):
    #     res = requests.patch(self.base_url + "/users")
    #     status = res.status_code
    #
    # def patch_api_resource_id(self):
    #     res = requests.patch(self.base_url + "/users")
    #     status = res.status_code
    #
    # def delete_api_users_id(self):
    #     res = requests.delete(self.base_url + "/users")
    #     status = res.status_code
    #
    # def delete_api_resource_id(self):
    #     res = requests.delete(self.base_url + "/users")
    #     status = res.status_code