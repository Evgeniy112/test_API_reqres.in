import pytest
from api import RegRequest
from settings import valid_page, valid_per_page, valid_id
from settings import valid_reg_body, valid_login_body, valid_put_body, valid_patch_body

tr = RegRequest()


class TestClassPos:

    def test_get_api_resource(self, page=valid_page, per_page=valid_per_page):
        status, result = tr.get_api_resource(page, per_page)
        assert status == 200
        assert len(result) > 0

    def test_get_api_users(self, page=valid_page, per_page=valid_per_page):
        status, result = tr.get_api_users(page, per_page)
        assert status == 200
        assert len(result) > 0

    def test_get_api_users_id(self, user_id=valid_id):
        status, result = tr.get_api_users_id(user_id)
        assert status == 200
        assert len(result) > 0

    def test_get_api_resource_id(self, resource_id=valid_id):
        status, result = tr.get_api_users_id(resource_id)
        assert status == 200
        assert len(result) > 0

    def test_post_api_login(self, body=valid_login_body):
        status, result = tr.post_api_login(body)
        assert status == 200
        assert "token" in result

    def test_post_api_register(self, body=valid_reg_body):
        status, result = tr.post_api_register(body)
        assert status == 200
        assert "token" and "id" in result

    def test_post_api_logout(self):
        status, result = tr.post_api_logout()
        assert status == 200

    def test_put_api_users_id(self, user_id=valid_id, body=valid_put_body):
        status, result = tr.put_api_users_id(user_id, body)
        assert status == 200
        assert "updatedAt" in result

    def test_put_api_resource_id(self, resource_id=valid_id, body=valid_put_body):
        status, result = tr.put_api_resource_id(resource_id, body)
        assert status == 200
        assert "updatedAt" in result

    def test_patch_api_users_id(self, user_id=valid_id, body=valid_patch_body):
        status, result = tr.patch_api_users_id(user_id, body)
        assert status == 200
        assert "updatedAt" in result

    def test_patch_api_resource_id(self, resource_id=valid_id, body=valid_patch_body):
        status, result = tr.patch_api_resource_id(resource_id, body)
        assert status == 200
        assert "updatedAt" in result

    def test_delete_api_users_id(self, user_id=valid_id):
        status, result = tr.delete_api_users_id(user_id)
        assert status == 204
        assert result == ""

    def test_delete_api_resource_id(self, resource_id=valid_id):
        status, result = tr.delete_api_resource_id(resource_id)
        assert status == 204
        assert result == ""
