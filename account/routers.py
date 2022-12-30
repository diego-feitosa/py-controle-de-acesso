from typing import List
from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.database import get_session
from core.security import crypt_hash

from account.models import AccountModel
from account.schemas import AccountSchema, AccountCreateSchema, AccountUpdateSchema

routers = APIRouter()

@routers.get('/', response_model=List[AccountSchema])
async def index(db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AccountModel)
        result = await session.execute(query)
        accounts: List[AccountSchema] = result.scalars().all()
    return accounts


@routers.post('/', response_model=AccountSchema, status_code=status.HTTP_201_CREATED)
async def create(request: AccountCreateSchema, db: AsyncSession = Depends(get_session)):
    new_account: AccountModel = AccountModel(
        username=request.username,
        password=request.password,
        name=request.name,
        activate=request.activate,
        admin=request.admin
    )

    async with db as session:
        session.add(new_account)
        await session.commit()
        return new_account

@routers.get('/{account_id}', response_model=AccountSchema, status_code=status.HTTP_200_OK)
async def read(account_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AccountModel).filter(AccountModel.id == account_id)
        result = await session.execute(query)
        account: AccountSchema = result.scalars().one_or_none()

        if account:
            return account
        else:
            raise HTTPException(
                detail="Account Not Found",
                status_code=status.HTTP_404_NOT_FOUND
            )

@routers.put('/{account_id}', response_model=AccountSchema, status_code=status.HTTP_202_ACCEPTED)
async def update(account_id: int, request: AccountUpdateSchema, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AccountModel).filter(AccountModel.id == account_id)
        result = await session.execute(query)
        account: AccountSchema = result.scalars().one_or_none()

        if account:
            if request.username:
                account.username=request.username
            if request.password:
                account.password=crypt_hash(request.password)
            if request.name:
                account.name=request.name
            if isinstance(request.activate, (int, float)):
                account.activate=request.activate
            if isinstance(request.admin, (int, float)):
                account.admin=request.admin

            await session.commit()
            return account
        else:
            raise HTTPException(
                detail="Account Not Found",
                status_code=status.HTTP_404_NOT_FOUND
            )


@routers.delete('/{account_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(account_id: int, db: AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(AccountModel).filter(AccountModel.id == account_id)
        result = await session.execute(query)
        account: AccountSchema = result.scalars().one_or_none()

        if account:
            await session.delete(account)
            await session.commit()
        else:
            raise HTTPException(
                detail="Account Not Found",
                status_code=status.HTTP_404_NOT_FOUND
            )
