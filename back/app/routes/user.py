from typing import Optional

from fastapi import APIRouter, HTTPException, Query
from sqlalchemy import desc, func, select

from app.dependencies.db import GetDb
from app.s3.storage_manager import StorageManager

user_router = APIRouter()
