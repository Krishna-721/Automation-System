from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from sqlalchemy import select
from app.db.postgres import get_db

from app.models.applications import JobApplication
from app.schemas.application_schema import JobApplicationCreate, JobApplicationResponse, EmailInput

from datetime import datetime

router = APIRouter(prefix="/emails",tags=["Emails"])

@router.post("/process",status_code=201)
async def process_application(payload: EmailInput, db: AsyncSession=Depends(get_db)):
    new_application= JobApplication(
        company="Pending", role="Pending",status="Pending", notes=payload.body,source=payload.sender)
    db.add(new_application)
    await db.commit()
    await db.refresh(new_application)

    return {"message": "Email received","id": new_application.id}