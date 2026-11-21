# Multi AI Agent

An e-mail assistant built with LangChain and LangGraph: notebook-style lessons, a
supervisor agent that delegates to research and writing subagents, and tools that send
real Gmail and Google Calendar actions.

## Layout

```
src/agents_from_scratch/
├── agents/              # supervisor, researcher, email writer
├── app/                 # chat UI entry point
├── config/              # settings, prompts, tool prompt templates
├── core/                # shared httpx client, Google OAuth, loguru setup
├── data/urls.py         # docs links the lessons point to
├── tools/
│   ├── email/           # write_email, triage_email, extras
│   ├── calendar/        # schedule_meeting, check_calendar_availability
│   ├── search/          # one tool per search provider
│   └── crawl/           # Firecrawl crawl tool
└── main.py

lessons/                 # notebook-style lessons: 01_models ... 08_evaluation
tests/                   # schema tests and lesson smoke tests
```

`tools/__init__.py` exposes `email_tools`, `calendar_tools`, `search_tools`,
`crawl_tools`, and `get_all_tools()`. Each subagent imports only the group it needs.

## Quickstart

```bash
uv sync                 # install everything in pyproject.toml
cp .env.example .env
python lessons/01_models.py
```

## Chat UI

```bash
chainlit run src/agents_from_scratch/app/chainlit.py -w
```

The UI streams the supervisor's answers into the chat. When the supervisor reaches the
email writer the run pauses and asks for approval; approve or reject and the graph
continues from where it stopped.

## Configuration

`.env` is nested by provider with `__` as the delimiter:

| Key | What for |
| --- | --- |
| `NVIDIA__API_KEY` | model provider key |
| `NVIDIA__MODELS__SUPERVISOR_MODEL` | model for the supervisor agent |
| `NVIDIA__MODELS__RESEARCHER_MODEL` | model for the researcher subagent |
| `NVIDIA__MODELS__EMAIL_WRITER_MODEL` | model for the email writer subagent |
| `NVIDIA__TEMPERATURE__*` | per-agent sampling temperature |
| `LANGSMITH_TRACING`, `LANGSMITH_API_KEY`, `LANGSMITH_PROJECT` | tracing and evaluation |
| `TAVILY_API_KEY`, `EXA_API_KEY`, `KEENABLE_API_KEY`, ... | search provider keys |

Every provider in `settings.py` takes the same block: `api_key`, `models`, and
`temperature`.

## Search tools

Providers with an official LangChain integration use it: `TavilySearch`,
`ExaSearchResults`, `KeenableSearch`, `DiffbotWebSearchTool`, `LinkupSearchTool`,
`FirecrawlSearch`, `FirecrawlCrawl`. The rest call their REST API over the shared
httpx client from `core/clients.py`. A provider without a key is skipped with a
loguru warning.

## Gmail and Calendar

The tools send real e-mail and create real events. OAuth consent runs on first use
and the token is stored in `.secrets/token.json`; drop the downloaded OAuth client
JSON as `.secrets/credentials.json` before that. `.secrets/` and `.env` are
git-ignored.