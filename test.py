from sqlalchemy import create_engine

from apps import SQLALCHEMY_DATABASE_URI


class A:
    val = 0

a = A()

print(a.val)

def change(a:A):
    a.val = 2

change(a)

print(a.val)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
print(type(engine))
