# Multiagent_framework

> CLI-first multi-agent framework demo with schema-first validation, logging, and expandable architecture.

```bash
# ======================================
# 1️⃣  Clone the repository
# ======================================
git clone https://github.com/YOUR_USERNAME/multiagent_framework.git
cd multiagent_framework
```
```bash
# ======================================
# 2️⃣  Install dependencies
# ======================================
pip install -r requirements.txt
```
```bash
# ======================================
# 3️⃣  Project Structure
# ======================================
# multiagent_framework/
# ├── src/
# │   ├── agents/        # Manager, Translator, Base agent
# │   ├── core/          # MessageBus, Scheduler, Schema registry
# │   ├── schemas/       # Pydantic models for tasks/responses
# │   ├── utils/         # Logger, health checks
# │   ├── validators/    # Input/output validators
# │   └── main.py        # CLI entry point
# ├── tests/             # Unit tests
# ├── requirements.txt
# ├── README.md
# ├── .gitignore
# ├── .github/           # Issue & PR templates
```
```bash
# ======================================
# 4️⃣  Run Example Translations
# ======================================

# English → French
python -m src.main "Hello" --source en --target fr
# Output:
# [YYYY-MM-DD HH:MM:SS] Starting framework...
# [YYYY-MM-DD HH:MM:SS] Processing task...
# [YYYY-MM-DD HH:MM:SS] Translation done: Bonjour
# Bonjour

# English → Spanish
python -m src.main "Hello World" --source en --target es
# Output:
# Hola Mundo

# French → English
python -m src.main "Bonjour" --source fr --target en
# Output:
# Hello
```
```bash
# ======================================
# 5️⃣  Run Tests
# ======================================
pytest -q
```
```bash
# ======================================
# 6️⃣  Contributing
# ======================================
# Fork the repo on GitHub, then:
git checkout -b feature/new-agent
# Make changes...
git commit -m "feat: add SummarizerAgent"
git push origin feature/new-agent
# Open a Pull Request on GitHub
```
```bash
# ======================================
# 7️⃣  Roadmap
# ======================================
# [ ] Implement HealthCheck module
# [ ] Add AgentScheduler logic
# [ ] Add HTTP API (FastAPI)
# [ ] More agents: Summarizer, Sentiment Analyzer
```
```bash
# ======================================
# 8️⃣  License
# ======================================
# MIT License – see LICENSE for details
```
