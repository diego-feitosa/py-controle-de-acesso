from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import engine, DBBaseModel, Session
from core.security import crypt_hash

async def create_tables() -> None:
    from account.models import AccountModel
    print('Criando as tabelas no banco de dados...')
    
    async with engine.begin() as conn:
        await conn.run_sync(DBBaseModel.metadata.drop_all)
        await conn.run_sync(DBBaseModel.metadata.create_all)

    print('Tabelas criadas com sucesso...')

async def create_admin() -> None:
    from account.models import AccountModel
    print('Criando o usuário Admin...')
    async with engine.begin() as conn:
        session: AsyncSession = Session()
        account = AccountModel(
            username="admin",
            password=crypt_hash("admin"),
            name="Administrador do Sistema",
            activate=True,
            admin=True
        )
        session.add(account)
        await session.commit()
    print('Usuário Admin criado com sucesso...')

if __name__ == '__main__':
    import asyncio
    asyncio.run(create_tables())
    asyncio.run(create_admin())

