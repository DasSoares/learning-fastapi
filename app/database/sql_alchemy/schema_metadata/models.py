from sqlalchemy import Table
from sqlalchemy import Column, Integer, String, MetaData

# Crie uma instância do Base
metadata = MetaData()

# Defina um exemplo de modelo de dados
t_user = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True, index=True),
    Column("name", String),
    Column("email", String, unique=True, index=True),
)


if __name__ == "__main__":
    import sys, os

    # Adicione o diretório raiz ao sys.path
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
    from database.connection import engine

    # breakpoint()

    # Crie todas as tabelas no banco de dados
    # metadata.create_all(engine) # -> Descomente se for criar uma nova tabela
    
    # with engine.connect() as conn:
    #     result = conn.execute(t_user.select())
    #     print(result)
        