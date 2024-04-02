from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator

from .base_models import BaseModel


class TextSummary(BaseModel):
    url = fields.TextField()
    summary = fields.TextField()

    def __str__(self):
        return self.url


SummarySchema = pydantic_model_creator(TextSummary)
