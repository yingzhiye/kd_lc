from sqlalchemy import Table, Column, Integer, String
from database import metadata, db_session, Base


# eg
class User(Base):
    query = db_session.query_property()

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return f'<User {self.name!r}>'


class Genomics(Base):
    __tablename__ = 'kidney cancer'

    def __init__(self, snp=None, geneIds=None, region=None, accession=None, context=None, url=None):
        self.snp = snp
        self.geneIds = geneIds
        self.region = region
        self.accession = accession
        self.context = context
        self.url = url

