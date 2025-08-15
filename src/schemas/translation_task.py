from pydantic import BaseModel, Field

class TranslationTask(BaseModel):
    type: str = Field(pattern="^translate$")
    source_lang: str
    target_lang: str
    text: str
