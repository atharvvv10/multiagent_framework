from src.agents.base_agent import BaseAgent
from src.schemas.translation_response import TranslationResponse

class TranslatorAgent(BaseAgent):
    def __init__(self):
        super().__init__("TranslatorAgent")

    def handle(self, task: dict) -> dict:
        # Expanded mock translations
        mock_dict = {
            ("en", "fr", "Hello"): "Bonjour",
            ("en", "fr", "Hello World"): "Bonjour le monde",
            ("en", "es", "Hello"): "Hola",
            ("en", "es", "Hello World"): "Hola Mundo",
            ("en", "de", "Hello"): "Hallo",
            ("en", "de", "Hello World"): "Hallo Welt",
            ("en", "it", "Hello"): "Ciao",
            ("en", "it", "Hello World"): "Ciao Mondo",
            ("fr", "en", "Bonjour"): "Hello",
            ("es", "en", "Hola"): "Hello",
            ("de", "en", "Hallo"): "Hello",
            ("it", "en", "Ciao"): "Hello"
        }

        key = (task["source_lang"], task["target_lang"], task["text"])
        translated = mock_dict.get(key, f"{task['text']}-{task['target_lang']}")
        
        return TranslationResponse(translated_text=translated).model_dump()
