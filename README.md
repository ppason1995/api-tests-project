# API Tests Project

Automated API tests written in Python using pytest and requests.
The project tests CRUD operations for `/users` endpoint using public JSONPlaceholder API.

## Tech stack
- Python 3.12
- pytest
- requests

## Project structure

src/
api/
base_session.py
users_client.py
tests/
users/
test_get_users.py
test_get_user_by_id.py
test_get_user_not_found.py
test_create_user.py
test_update_user.py
test_delete_user.py
test_get_users_with_params.py
helpers/
schema_validators.py
conftest.py


## How to run tests

### 1. Clone repository
```bash
git clone https://github.com/ppason1995/api-tests-project.git
cd api-tests-project

2. Create virtual environment
python -m venv .venv
.venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run tests
pytest
