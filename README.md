# simple_wallet

Simple project which enable adding new users and updating their wallet balance

## Project Setup

1. Create and activate a virtual environment
    - \$ ```python3 -m vevn venv```
    - \$ ```source ./venv/bin/activate``` (For Linux)
2. Install project requirements
    - \$ ```pip install -r requirements.txt```

## How to Run

### Running migrations
\$ ```python manage.py makemigrations```
\$ ```python manage.py migrate```

### Running development server
\$ ```python manage.py runserver```


## API Usage Examples

### Create a new account

```bash
curl -X POST http://127.0.0.1:8000/accounts/users/ \
  -H 'Content-Type: application/json' \
  -d '{"email": "user@mail.com", "first_name":"user", "last_name":"admin"}'
```

### Make a deposit (Update Balance)

```bash
curl -X POST http://localhost:8000/wallets/balance/ \
  -H 'Content-Type: application/json' \
  -d '{"user_id": 1, "amount": 1000}'
```
