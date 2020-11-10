## How to run migrations?
```
PYTHONPATH=./ alembic upgrade head
```

## How to generate migrations
```
PYTHONPATH=./ alembic revision -m "message" --autogenerate
```