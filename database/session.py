# database/session.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.base import Base
import os
import pkgutil
import importlib

class Database:
    def __init__(self, url: str = "sqlite:///biometric.db"):
        self.engine = create_engine(url)
        self.SessionLocal = sessionmaker(bind=self.engine)
    def import_modelos(self):
        import database.models
        package_dir= os.path.dirname(database.models.__file__)
        for (module_loader,name,ispkg) in pkgutil.iter_modules([package_dir]):
            importlib.import_module(f"database.models.{name}")
    
    def init_db(self):
        self.import_modelos()
        print(f"Creando tablas en: {self.engine.url}")  # Verificar ruta
        Base.metadata.create_all(self.engine)
        print("Tablas creadas:", Base.metadata.tables.keys())  # Listar tablas

    def get_session(self):
        return self.SessionLocal()

# Instancia global
db = Database()