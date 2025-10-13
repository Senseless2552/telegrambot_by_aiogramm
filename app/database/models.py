import os
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import create_engine, Column, BigInteger
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker

engine = create_async_engine('sqlite+aiosqlite:///profiles.db')

async_session = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    age: Mapped[int] = mapped_column()
    hobbies: Mapped[str] = mapped_column()
    photo: Mapped[str] = mapped_column()
    sex: Mapped[str] = mapped_column()
    tg_id = mapped_column(BigInteger)

async def create_db():
    if not os.path.exists('profiles.db'):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
        return engine