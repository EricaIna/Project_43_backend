from application.auth.models import User

def test_new_user():
    user = User('Test', 'test@test.com', 'jkljkl')
    
    assert user.name == 'Test'
    assert user.email == 'test@test.com'
    assert user.password == 'jkljkl'