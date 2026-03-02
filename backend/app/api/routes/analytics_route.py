from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, func
from app.models.applications import JobApplication
from app.db.postgres import get_db

router=APIRouter(prefix="/analytics",tags=["Analytics"])

@router.get("/summary")
async def get_summary(db: AsyncSession=Depends(get_db)):
    result =await db.execute(select(JobApplication.status, func.count(JobApplication.id)).group_by(JobApplication.status))
    
    rows=result.all()
    summary={row[0]:row[1] for row in rows} 
   
    return {"total": sum(summary.values()), "distribution": summary}
    