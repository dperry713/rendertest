import pytest
from app import app, db, Sum

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            
            # Seed some test data
            test_sums = [
                Sum(num1=1, num2=3, result=4),
                Sum(num1=2, num2=2, result=4),
                Sum(num1=5, num2=-1, result=4)
            ]
            
            for sum_entry in test_sums:
                db.session.add(sum_entry)
            db.session.commit()
        
        yield client
        
        with app.app_context():
            db.session.remove()
            db.drop_all()

def test_get_sums_by_result_positive(client):
    """Test retrieving sums with a valid result"""
    response = client.get('/sum/result/4')
    assert response.status_code == 200
    
    data = response.get_json()
    assert len(data) == 3  # We added 3 sums with result 4
    assert all(entry['result'] == 4 for entry in data)

def test_get_sums_by_result_no_matches(client):
    """Test retrieving sums with a result that has no matches"""
    response = client.get('/sum/result/100')
    assert response.status_code == 200
    
    data = response.get_json()
    assert len(data) == 0  # No sums with result 100

def test_get_sums_by_result_invalid_input(client):
    """Negative test case: Test with invalid input"""
    response = client.get('/sum/result/abc')
    assert response.status_code == 404  # Should return 404 for invalid input
