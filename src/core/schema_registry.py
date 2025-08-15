from src.schemas.translation_task import TranslationTask
from src.schemas.translation_response import TranslationResponse

class SchemaRegistry:
    REGISTRY = {
        "translate": {
            "input": TranslationTask,
            "output": TranslationResponse,
        }
    }
