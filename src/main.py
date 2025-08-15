import typer
from src.core.message_bus import MessageBus
from src.agents.manager_agent import ManagerAgent
from src.agents.translator_agent import TranslatorAgent
from src.utils.logger import Logger

def main(text: str, source: str = "en", target: str = "fr"):
    Logger.log("Starting framework...")
    
    # Create message bus & register agents
    bus = MessageBus()
    translator = TranslatorAgent()
    bus.register("translate", translator)
    
    # Create manager
    manager = ManagerAgent(bus)

    # Build task
    task = {
        "type": "translate",
        "source_lang": source,
        "target_lang": target,
        "text": text
    }

    # Process
    Logger.log("Processing task...")
    result = manager.handle_task(task)

    # Output result
    Logger.log(f"Translation done: {result.translated_text}")
    typer.echo(result.translated_text)

if __name__ == "__main__":
    typer.run(main)
