from app.models import TextSummary
from app.models.pydantic import SummaryPayloadSchema


async def post(payload: SummaryPayloadSchema) -> int:
    summary = TextSummary(
        url=payload.url,
        summary="dummy summary",
    )
    await summary.save()
    return summary.id


async def get(id: int) -> dict | None:
    summary = await TextSummary.filter(id=id).first().values()
    if summary:
        return summary
    return None


async def get_all() -> list:
    summaries = await TextSummary.all().values()
    return summaries
