from services.user_service import UserService

def test_create_user():
    service = UserService()
    user = service.create_user("1", "Test", "test@mail.com", "pass", "Lose weight")
    assert user.name == "Test"
    assert service.get_user("1") is not None

