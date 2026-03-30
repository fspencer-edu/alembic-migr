# AUTO Migrations with Alembic

## Connect to database

`mariadb -h 127.0.0.1 -P 3308 -u fiona -p alembic_db`

- Generate migration
`alembic revision --autogenerate -m "message"`

- Apply migration
`alembic upgrade head`

```python
alembic history
alembic current
alembic show 59261dd58429
alembic heads
alembic downgrade -1
alembic stamp head
```