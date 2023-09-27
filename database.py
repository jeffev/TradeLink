from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Configuração da URL de conexão com o PostgreSQL
DATABASE_URL = "postgresql://seu_usuario:sua_senha@localhost/nome_do_banco"

# Crie uma instância do SQLAlchemy Engine
engine = create_engine(DATABASE_URL)

# Crie uma sessão do SQLAlchemy
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Crie uma base declarativa para definir modelos de banco de dados
Base = declarative_base()
