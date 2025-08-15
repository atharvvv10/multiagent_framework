from src.core.schema_registry import SchemaRegistry
from src.validators.input_validator import InputValidator
from src.validators.output_validator import OutputValidator

class ManagerAgent:
    def __init__(self, bus):
        self.bus = bus

    def handle_task(self, task_data: dict):
        schema_in = SchemaRegistry.REGISTRY[task_data["type"]]["input"]
        validated_in = InputValidator.validate(task_data, schema_in)
        response = self.bus.send(validated_in.type, validated_in.model_dump())
        schema_out = SchemaRegistry.REGISTRY[task_data["type"]]["output"]
        return OutputValidator.validate(response, schema_out)
