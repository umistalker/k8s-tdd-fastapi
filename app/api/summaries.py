from fastapi import APIRouter

from app.api import crud
from app.models import SummarySchema
from app.models.pydantic import SummaryPayloadSchema, SummaryResponseSchema

router = APIRouter()


@router.post("/", response_model=SummaryResponseSchema, status_code=201)
async def create_summary(payload: SummaryPayloadSchema) -> SummaryResponseSchema:
    summary_id = await crud.post(payload)

    response_object = {
        "id": summary_id,
        "url": payload.url
    }
    return response_object


@router.get("/{id}/", response_model=SummarySchema)
async def read_summary(id: int) -> SummarySchema:
    summary = await crud.get(id)
    return summary


@router.get("/", response_model=list[SummarySchema])
async def read_all_summaries() -> list[SummarySchema]:
    return await crud.get_all()
