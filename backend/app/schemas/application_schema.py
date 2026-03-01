from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class JobApplicationBase(BaseModel):
    company: str
    role: str
    status: Optional[str] = "applied"
    source: Optional[str] = None
    notes: Optional[str] = None


class JobApplicationCreate(JobApplicationBase):
    pass


class JobApplicationResponse(JobApplicationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True