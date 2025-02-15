import asyncio

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app.models.models import Base

# DB_URI = "sqlite+aiosqlite:///:memory:"

PG_DB_URI = "postgresql+asyncpg://user:1234@localhost:5431/db"
engine = create_async_engine(PG_DB_URI, echo=False)


async_session_maker = async_sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)


async def create_db():
    print("Base", Base.metadata)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def populate():
    await create_db()
    # async with async_session_maker() as db:
    #     await populate_db(db)


if __name__ == "__main__":
    asyncio.run(populate())
    print("Database populated")
