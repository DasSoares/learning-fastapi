from sqlalchemy import create_engine, Table
from app.database.connection import create_session, Session


# your code here
class CrudModel:
    
    #! trocar o engine pela Session
    def __init__(self, session: Session, table: Table, engine: create_engine = None):
        # self.engine = engine
        self.table = table
        self.session = session if session else create_session(session)
        
    @property
    def __get_pk(self):
        return next(column.name for column in self.table.columns if column.primary_key)
    
    def all(self):
        query = self.table.select()
        result = self.session.execute(query).fetchall()
        return [ row._asdict() for row in result ]
        # with self.session.connect() as conn:
        #     result = conn.execute(query).fetchall()
        #     return [ row._asdict() for row in result ]
    
    def get(self, id: int) -> dict | None:
        query = self.table.select().where(self.table.c[self.__get_pk] == id)
        result = self.session.execute(query).one_or_none()
        return result._asdict() if result else None
        # with self.session.connect() as conn:
        #     result = conn.execute(query).one_or_none()
        #     return result._asdict() if result else None
    
    def __insert__(self, **kwargs):
        query = self.table.insert().values(**kwargs)
        result = self.session.execute(query)
        return result.inserted_primary_key[0]
        # with self.session.connect() as conn:
        #     result = conn.execute(query)
        #     conn.commit()
        #     # return conn, result.inserted_primary_key_rows[0][0] # retorna uma tupla(conexao, id do ultimo registro)
        #     return result.inserted_primary_key_rows[0][0]
    
    def __edit__(self, id: int, **kwargs) -> int:
        query = self.table.update().where(
            self.table.c[self.__get_pk] == id
        ).values(**kwargs)
        result = self.session.execute(query)
        return result.rowcount
        # with self.session.connect() as conn:
        #     result = conn.execute(query)
        #     conn.commit()
        #     return result.rowcount
    
    def delete(self, id: int) -> int:
        query = self.table.delete().where(self.table.c[self.__get_pk] == id)
        result = self.session.execute(query)
        return result.rowcount
        # with self.session.connect() as conn:
        #     result = conn.execute(query)
        #     conn.commit()
        #     return result.rowcount
