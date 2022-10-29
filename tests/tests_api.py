import pytest

from api import RegRequest
from settings import valid_data_page, none_data_page, invalid_data_page_txt, invalid_data_page_minus
from settings import valid_login_body, invalid_login_body_1, invalid_login_body_2, invalid_login_body_3
from settings import valid_reg_body, invalid_reg_body1, invalid_reg_body2, invalid_reg_body3
from settings import valid_put_body, invalid_put_body1, invalid_put_body2
from settings import valid_id, invalid_id1, invalid_id2, invalid_id3

tr = RegRequest()


@pytest.mark.api
class TestClassPos:

    @pytest.mark.get
    def test_get_api_resource(self, headers=valid_data_page):
        # Позитивный тест GET-запроса на получение списка ресурсов по номеру страницы
        status, result = tr.get_api_resource(headers)
        assert status == 200
        assert "page" in result

    def test_get_api_resource_oll(self, headers=none_data_page):
        # Позитивный тест GET-запроса на получение списка всех ресурсов
        status, result = tr.get_api_resource(headers)
        assert status == 200
        assert "page" in result

    def test_get_api_users(self, headers=valid_data_page):
        # Позитивный тест GET-запроса на получение списка пользователей по номеру страницы
        status, result = tr.get_api_users(headers)
        assert status == 200
        assert "data" in result

    def test_get_api_users_oll(self, headers=none_data_page):
        # Позитивный тест GET-запроса на получение списка всех пользователей
        status, result = tr.get_api_users(headers)
        assert status == 200
        assert "data" in result

    def test_get_api_users_id(self, user_id=valid_id):
        # Позитивный тест GET-запроса на получение пользователя по номеру id
        status, result = tr.get_api_users_id(user_id)
        assert status == 200
        assert "data" in result

    def test_get_api_resource_id(self, resource_id=valid_id):
        # Позитивный тест GET-запроса на получение ресурса по номеру id
        status, result = tr.get_api_users_id(resource_id)
        assert status == 200
        assert "data" in result

    @pytest.mark.auth
    def test_post_api_login(self, body=valid_login_body):
        # Позитивный тест POST-запроса на авторизацию
        status, result = tr.post_api_login(body)
        assert status == 200
        assert "token" in result

    @pytest.mark.register
    def test_post_api_register(self, body=valid_reg_body):
        # Позитивный тест POST-запроса на регистрацию нового пользователя
        status, result = tr.post_api_register(body)
        assert status == 200
        assert "token" and "id" in result

    def test_post_api_logout(self):
        # Позитивный тест POST-запроса на выход из системы
        status, result = tr.post_api_logout()
        assert status == 200
        assert result == {}

    @pytest.mark.put
    def test_put_api_users_id(self, user_id=valid_id, body=valid_put_body):
        # Позитивный тест PUT-запроса на изменение данных пользователя
        status, result = tr.put_api_users_id(user_id, body)
        assert status == 200
        assert "name" and "id" and "updatedAt" in result

    @pytest.mark.put
    def test_put_api_resource_id(self, resource_id=valid_id):
        # Позитивный тест PUT-запроса на изменение данных ресурса
        status, result = tr.put_api_resource_id(resource_id)
        assert status == 200
        assert "name" and "id" and "updatedAt" in result

    @pytest.mark.put
    def test_patch_api_users_id(self, user_id=valid_id, body=valid_put_body):
        # Позитивный тест PATCH-запроса на изменение данных пользователя
        status, result = tr.patch_api_users_id(user_id, body)
        assert status == 200
        assert "name" and "job" and "updatedAt" in result

    @pytest.mark.put
    def test_patch_api_resource_id(self, resource_id=valid_id):
        # Позитивный тест PATCH-запроса на изменение данных ресурса
        status, result = tr.patch_api_resource_id(resource_id)
        assert status == 200
        assert "name" and "job" and "updatedAt" in result

    @pytest.mark.put
    def test_delete_api_users_id(self, user_id=valid_id):
        # Позитивный тест DELETE-запроса на удаление пользователя
        status, result = tr.delete_api_users_id(user_id)
        assert status == 204
        assert result == ""

    @pytest.mark.put
    def test_delete_api_resource_id(self, resource_id=valid_id):
        # Позитивный тест DELETE-запроса на удаление ресурса
        status, result = tr.delete_api_resource_id(resource_id)
        assert status == 204
        assert result == ""


@pytest.mark.api
class TestClassNeg:

    @pytest.mark.get
    def test_get_api_resource_txt(self, headers=invalid_data_page_txt):
        # Негативный тест GET-запроса на получение списка ресурсов по номеру страницы
        # В запросе передаются текстовые данные
        status, result = tr.get_api_resource(headers)
        assert status == 404
        assert result == {}

    def test_get_api_resource_minus(self, headers=invalid_data_page_minus):
        # Негативный тест GET-запроса на получение списка ресурсов по номеру страницы
        # В запросе передаются отрицательные значения
        status, result = tr.get_api_resource(headers)
        assert status == 404
        assert result == {}

    def test_get_api_users_txt(self, headers=invalid_data_page_txt):
        # Негативный тест GET-запроса на получение списка пользователей по номеру страницы
        # В запросе передаются текстовые данные
        status, result = tr.get_api_users(headers)
        assert status == 404
        assert result == {}

    def test_get_api_users_minus(self, headers=invalid_data_page_minus):
        # Негативный тест GET-запроса на получение списка пользователей по номеру страницы
        # В запросе передаются отрицательные значения
        status, result = tr.get_api_users(headers)
        assert status == 404
        assert result == {}

    def test_get_api_users_id1(self, user_id=invalid_id1):
        # Негативный тест GET-запроса на получение пользователя по номеру id
        # В запросе передаётся не существующий id
        status, result = tr.get_api_users_id(user_id)
        assert status == 404
        assert result == {}

    def test_get_api_users_id2(self, user_id=invalid_id2):
        # Негативный тест GET-запроса на получение пользователя по номеру id
        # В запросе передаётся пустое поле
        status, result = tr.get_api_users_id(user_id)
        assert status == 404
        assert result == {}

    def test_get_api_users_id_txt(self, user_id=invalid_id3):
        # Негативный тест GET-запроса на получение пользователя по номеру id
        # В запросе передаётся текст
        status, result = tr.get_api_users_id(user_id)
        assert status == 404
        assert result == {}

    def test_get_api_resource_id1(self, resource_id=invalid_id1):
        # Негативный тест GET-запроса на получение ресурса по номеру id
        # В запросе передаётся не существующий id
        status, result = tr.get_api_users_id(resource_id)
        assert status == 404
        assert result == {}

    def test_get_api_resource_id2(self, resource_id=invalid_id2):
        # Негативный тест GET-запроса на получение ресурса по номеру id
        # В запросе передаётся пустое поле
        status, result = tr.get_api_users_id(resource_id)
        assert status == 404
        assert result == {}

    def test_get_api_resource_id_txt(self, resource_id=invalid_id3):
        # Негативный тест GET-запроса на получение ресурса по номеру id
        # В запросе передаётся текст
        status, result = tr.get_api_users_id(resource_id)
        assert status == 404
        assert result == {}

    @pytest.mark.auth
    def test_post_api_login1(self, body=invalid_login_body_1):
        # Негативный тест POST-запроса на авторизацию
        # Не существующий логин и пароль
        status, result = tr.post_api_login(body)
        assert status == 400
        assert "error" in result

    @pytest.mark.auth
    def test_post_api_login2(self, body=invalid_login_body_2):
        # Негативный тест POST-запроса на авторизацию
        # Существующий логин и неверный пароль
        status, result = tr.post_api_login(body)
        assert status == 400
        assert "error" in result

    @pytest.mark.auth
    def test_post_api_login3(self, body=invalid_login_body_3):
        # Негативный тест POST-запроса на авторизацию
        # Пустые поля логин и пароль
        status, result = tr.post_api_login(body)
        assert status == 400
        assert "error" in result

    @pytest.mark.register
    def test_post_api_register1(self, body=invalid_reg_body1):
        # Негативный тест POST-запроса на регистрацию нового пользователя
        # Не существующий логин и пароль
        status, result = tr.post_api_register(body)
        assert status == 400
        assert "error" in result

    @pytest.mark.register
    def test_post_api_register2(self, body=invalid_reg_body2):
        # Негативный тест POST-запроса на регистрацию нового пользователя
        # Существующий логин и неверный пароль
        status, result = tr.post_api_register(body)
        assert status == 400
        assert "error" in result

    @pytest.mark.register
    def test_post_api_register3(self, body=invalid_reg_body3):
        # Негативный тест POST-запроса на регистрацию нового пользователя
        # Пустые поля логин и пароль
        status, result = tr.post_api_register(body)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_put_api_users_id1(self, user_id=valid_id, body=invalid_put_body1):
        # Негативный тест PUT-запроса на изменение данных пользователя
        # Неверные данные "name" и "job" (символы)
        status, result = tr.put_api_users_id(user_id, body)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_put_api_users_id2(self, user_id=valid_id, body=invalid_put_body2):
        # Негативный тест PUT-запроса на изменение данных пользователя
        # Пустые данные "name" и "job"
        status, result = tr.put_api_users_id(user_id, body)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_put_api_users_id3(self, user_id=invalid_id1, body=valid_put_body):
        # Негативный тест PUT-запроса на изменение данных пользователя
        # В запросе передаётся не существующий id
        status, result = tr.put_api_users_id(user_id, body)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_put_api_users_id4(self, user_id=invalid_id2, body=valid_put_body):
        # Негативный тест PUT-запроса на изменение данных пользователя
        # В запросе передаётся пустое поле
        status, result = tr.put_api_users_id(user_id, body)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_put_api_users_id5(self, user_id=invalid_id3, body=valid_put_body):
        # Негативный тест PUT-запроса на изменение данных пользователя
        # В запросе id передаётся текст
        status, result = tr.put_api_users_id(user_id, body)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_put_api_resource_id1(self, resource_id=invalid_id1):
        # Негативный тест PUT-запроса на изменение данных ресурса по id
        # В запросе передаётся не существующий id
        status, result = tr.put_api_resource_id(resource_id)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_put_api_resource_id2(self, resource_id=invalid_id2):
        # Негативный тест PUT-запроса на изменение данных ресурса по id
        # В запросе передаётся пустое поле
        status, result = tr.put_api_resource_id(resource_id)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_put_api_resource_id3(self, resource_id=invalid_id3):
        # Негативный тест PUT-запроса на изменение данных ресурса по id
        # В запросе id передаётся текст
        status, result = tr.put_api_resource_id(resource_id)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_patch_api_users_id1(self, user_id=valid_id, body=invalid_put_body1):
        # Негативный тест PATCH-запроса на изменение данных пользователя по id
        # Неверные данные "name" и "job" (символы)
        status, result = tr.patch_api_users_id(user_id, body)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_patch_api_users_id2(self, user_id=valid_id, body=invalid_put_body2):
        # Негативный тест PATCH-запроса на изменение данных пользователя по id
        # Пустые данные "name" и "job"
        status, result = tr.patch_api_users_id(user_id, body)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_patch_api_users_id3(self, user_id=invalid_id1, body=valid_put_body):
        # Негативный тест PATCH-запроса на изменение данных пользователя по id
        # В запросе передаётся не существующий id
        status, result = tr.patch_api_users_id(user_id, body)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_patch_api_users_id4(self, user_id=invalid_id2, body=valid_put_body):
        # Негативный тест PATCH-запроса на изменение данных пользователя по id
        # В запросе передаётся пустое поле id
        status, result = tr.patch_api_users_id(user_id, body)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_patch_api_users_id5(self, user_id=invalid_id3, body=valid_put_body):
        # Негативный тест PATCH-запроса на изменение данных пользователя по id
        # В запросе id передаётся текст
        status, result = tr.patch_api_users_id(user_id, body)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_patch_api_resource_id1(self, resource_id=invalid_id1):
        # Негативный тест PATCH-запроса на изменение данных ресурса по id
        # В запросе передаётся не существующий id
        status, result = tr.patch_api_resource_id(resource_id)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_patch_api_resource_id2(self, resource_id=invalid_id2):
        # Негативный тест PATCH-запроса на изменение данных ресурса
        # В запросе передаётся пустое поле id
        status, result = tr.patch_api_resource_id(resource_id)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_patch_api_resource_id3(self, resource_id=invalid_id3):
        # Негативный тест PATCH-запроса на изменение данных ресурса
        # В запросе id передаётся текст
        status, result = tr.patch_api_resource_id(resource_id)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_delete_api_users_id1(self, user_id=invalid_id1):
        # Негативный тест DELETE-запроса на удаление пользователя по id
        # В запросе передаётся не существующий id
        status, result = tr.delete_api_users_id(user_id)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_delete_api_users_id2(self, user_id=invalid_id2):
        # Негативный тест DELETE-запроса на удаление пользователя по id
        # В запросе передаётся пустое поле id
        status, result = tr.delete_api_users_id(user_id)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_delete_api_users_id3(self, user_id=invalid_id3):
        # Негативный тест DELETE-запроса на удаление пользователя по id
        # В запросе id передаётся текст
        status, result = tr.delete_api_users_id(user_id)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_delete_api_resource_id1(self, resource_id=invalid_id1):
        # Негативный тест DELETE-запроса на удаление ресурса по id
        # В запросе передаётся не существующий id
        status, result = tr.delete_api_resource_id(resource_id)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_delete_api_resource_id2(self, resource_id=invalid_id2):
        # Негативный тест DELETE-запроса на удаление ресурса по id
        # В запросе передаётся пустое поле id
        status, result = tr.delete_api_resource_id(resource_id)
        assert status == 400
        assert "error" in result

    @pytest.mark.put
    def test_delete_api_resource_id3(self, resource_id=invalid_id3):
        # Негативный тест DELETE-запроса на удаление ресурса по id
        # В запросе id передаётся текст
        status, result = tr.delete_api_resource_id(resource_id)
        assert status == 400
        assert "error" in result