from sqlalchemy import select
from app.database.models import async_session
from app.database.models import User

async def set_profile_by_id(tg_id, data):
    async with async_session() as session:
        stmt = select(User).where(User.tg_id == tg_id)
        result = await session.scalars(stmt)
        existing_user = result.first()
        if existing_user:
            await session.delete(existing_user)
        user = User(
            tg_id=tg_id,
            name=data['name'],
            age=data['age'],
            hobby=data['hobby'],
            sex=data['sex'],
            photo=data['photo']
        )
        session.add(user)
        await session.commit()

async def get_profile_by_id(tg_id):
    async with async_session() as session:
        stmt = select(User).where(User.tg_id == tg_id)
        result = await session.scalars(stmt)
        return result.first()
    