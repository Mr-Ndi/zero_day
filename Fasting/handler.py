from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel

sqlite_url = "sqlite+aiosqlite:///database.db"

engine = create_async_engine(sqlite_url, echo=True)

async_session_maker = sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
