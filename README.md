# 🏦 Hack Me Bank MCP

[![🚀 Demo Space](https://img.shields.io/badge/🚀%20Demo%20Space-huggingface-blue?logo=huggingface)](https://huggingface.co/spaces/jdelavande/hack_me_mcp)
[![🔑 Attacker Agent](https://img.shields.io/badge/🔑%20Attacker%20Agent-huggingface-orange?logo=huggingface)](https://huggingface.co/spaces/jdelavande/mcp_agent_attacker)
[![⭐ GitHub](https://img.shields.io/badge/⭐%20GitHub-Repository-black?logo=github)](https://github.com/SoAnVa/MCP_Hackathon)

---

Welcome to **Hack Me Bank MCP** – an intentionally vulnerable banking agent demo for security research and hackathons!

This project showcases common security pitfalls in agent-based applications, including **insecure deserialization** and **SQL injection**, for educational and testing purposes.

<p align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/67ecf57f1f0e7c18eec758c9/3Hb2PCiuAk9ekbGIcNHTw.png" width="80%">
</p>

---

## 🚀 Features

- 💬 **Natural language interface** powered by LLM agents ([smolagents](https://github.com/smol-ai/smol-agents)) with any LLM provider (Anthropic, OpenAI, Hugging Face, etc.)
- 🗂️ **User database** (SQLite) with balances and credit card data
- 🛠️ **Agent tools**: list users, check balances, load pickled user profiles
- 🌐 **Web UI**: FastAPI + Jinja2 + vanilla JS
- ⚠️ **Deliberate vulnerabilities** for learning:
  - Insecure pickle deserialization
  - SQL injection

---

## ⚠️ Disclaimer

**This project is intentionally insecure. Do NOT use in production or with real secrets.**

---

## 🛠️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/SoAnVa/MCP_Hackathon.git
cd MCP_Hackathon
````

### 2️⃣ Python environment

* Requires **Python 3.10+**

*(Optional but recommended)*

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

### 3️⃣ Install dependencies

```bash
pip install fastapi uvicorn smolagents[litellm] duckduckgo_search
```

### 4️⃣ Set environment variables

Create an `.env` file in the project root:

```env
LLM_API_KEY=your_api_key_here
MODEL_NAME=your_model_name_here  # e.g., claude-sonnet-4-20250514
```

### 5️⃣ Initialize the database

Uncomment the `init_db()` line in [`main.py`](main.py) **or** run manually:

```bash
python -c "from db import init_db; init_db()"
```

### 6️⃣ Run the app

```bash
uvicorn main:app --reload
```

Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🧑‍💻 How to use

* 🗣️ Chat in natural language (e.g., "What's my balance?")
* 🏴‍☠️ Try exploiting vulnerabilities (see hints below)
* 🔍 Explore the code in [`tools.py`](tools.py), [`db.py`](db.py), and [`utils/`](utils/)

---

## 🏴‍☠️ Hacking hints

* 💉 Try SQL injection in username fields
* 🐍 Try loading a malicious pickle (see [`utils/evil_pickle_generate.py`](utils/evil_pickle_generate.py)). For example, load `alice_profile.pkl` or craft your own.
* 🔑 Try extracting secrets from environment variables or the database.

---

## 📂 Project structure

```
├── main.py         # FastAPI app and web UI
├── agent.py        # LLM agent setup
├── db.py           # SQLite database logic
├── tools.py        # Agent tools (functions)
├── utils/          # Pickle utilities
├── templates/      # HTML templates
├── static/         # CSS styles
```

---

## 📝 License

For **educational and research use only**.

---

## 🎓 About

Developed during the **Agent Hackathon – June 2025 at Hugging Face**.

Check out the related attacker project: [mcp-agent-attacker](https://github.com/SoelMgd/MCP_Red_Team_Agent)

Deployed on Hugging Face Spaces:

* 🌐 [Hack Me Bank MCP](https://huggingface.co/spaces/jdelavande/hack_me_mcp)
* 🕵️‍♂️ [MCP Agent Attacker](https://huggingface.co/spaces/jdelavande/mcp_agent_attacker)
