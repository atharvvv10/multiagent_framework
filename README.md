# 🤖 Multiagent framework
```bash
🚀 Internship Project Context  
Built as part of the Prodigal AI Internship — Day 61 to 75.

Objective: Implement the Prodigal AI Agents Framework initial structure and demo.  
Goal: Build a CLI-first multi-agent framework with schema-first validation,  
logging, and an expandable architecture for future agents.

✅ Highlights:
- ManagerAgent → TranslatorAgent pipeline
- Schema-first validation using Pydantic
- CLI interface for quick testing (API-ready)
- Modular folder structure for scalability
- Logging for task execution flow
- Ready for GitHub issue tracking and contributions
```
```bash
🛠️ Installation
# Clone the repository
git clone https://github.com/YOUR_USERNAME/multiagent_framework.git
cd multiagent_framework

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate     # On Windows

# Install dependencies
pip install -r requirements.txt
```
```bash
🧪 Usage
# Run the CLI from project root
python -m src.main "Hello" --source en --target fr

# Example output:
# [2025-08-15 13:00:00] Starting framework...
# [2025-08-15 13:00:00] Processing task...
# [2025-08-15 13:00:00] Translation done: Bonjour
# Bonjour

# Another example:
python -m src.main "Hello World" --source en --target es
# Output: Hola Mundo
```
```bash
📂 Project Structure
multiagent_framework/
│
├── src/
│   ├── agents/         # Manager, Translator, Base agent
│   ├── core/           # MessageBus, Scheduler, Schema registry
│   ├── schemas/        # Pydantic models for tasks/responses
│   ├── utils/          # Logger, health checks
│   ├── validators/     # Input/output validators
│   └── main.py         # CLI entry point
│
├── tests/              # Unit tests
├── requirements.txt
├── README.md
├── .gitignore
└── .github/            # Issue & PR templates
```
```bash
🧠 Demo Translations
| Source | Target | Input        | Output              |
|--------|--------|--------------|---------------------|
| en     | fr     | Hello        | Bonjour             |
| en     | fr     | Hello World  | Bonjour le monde    |
| en     | es     | Hello        | Hola                |
| en     | es     | Hello World  | Hola Mundo          |
| en     | de     | Hello        | Hallo               |
| fr     | en     | Bonjour      | Hello               |
```
```bash
📌 Contribution Guidelines
- Fork the repository
- Create a feature branch
- Use Conventional Commits format (feat:, fix:, docs:)
- Ensure all tests pass before PR
- Submit a Pull Request with a clear description
```
```bash
📜 .gitignore (important)
__pycache__/
*.pyc
.venv/
env/
venv/
.cache/
```
```bash
💬 Notes
- This is a CLI-first framework, but architecture is API-ready (FastAPI can be added later).
- Empty files like health_check.py and agent_scheduler.py are placeholders for future functionality.
- Pydantic schemas ensure strict validation of both input and output.
```
```bash
🧑‍💻 Author
Atharv Chaugale  
GitHub: https://github.com/atharvvv10
```


