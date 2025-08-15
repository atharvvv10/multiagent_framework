from src.core.message_bus import MessageBus
from src.agents.manager_agent import ManagerAgent
from src.agents.translator_agent import TranslatorAgent

def test_translation():
    bus = MessageBus()
    bus.register("translate", TranslatorAgent())
    manager = ManagerAgent(bus)
    result = manager.handle_task({
        "type": "translate",
        "source_lang": "en",
        "target_lang": "fr",
        "text": "Hello"
    })
    assert result.translated_text == "Bonjour"
