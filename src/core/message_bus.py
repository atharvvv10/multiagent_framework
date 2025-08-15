class MessageBus:
    def __init__(self):
        self.routes = {}

    def register(self, task_type, agent):
        self.routes[task_type] = agent

    def send(self, task_type, payload):
        agent = self.routes.get(task_type)
        if not agent:
            raise ValueError(f"No agent for {task_type}")
        return agent.handle(payload)
