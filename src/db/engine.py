from sqlalchemy import create_engine
from src.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True, pool_size=5, max_overflow=10)
