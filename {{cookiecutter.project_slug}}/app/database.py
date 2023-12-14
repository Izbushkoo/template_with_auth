from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI.unicode_string(), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

async_engine = create_async_engine(settings.SQLALCHEMY_DATABASE_URI_ASYNC.unicode_string())
AsyncSessionLocal = async_sessionmaker(bind=async_engine, autoflush=False, expire_on_commit=False, class_=AsyncSession)

sync_engine = create_engine(settings.SQLALCHEMY_DATABASE_URI.unicode_string(), pool_pre_ping=True)
SyncSessionLocal = sessionmaker(class_=Session, autocommit=False, autoflush=False, bind=sync_engine)

Base = declarative_base()

# This is used to alembic be able to autogenerate migrations
from app.models import *  # noqa
