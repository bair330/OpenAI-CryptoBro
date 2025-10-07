# OpenAI-CryptoBro

This repository centralizes the action specifications and helper scripts used to manage the CryptoBro GPT integration.

## Repository layout

```
OpenAI-CryptoBro/
├── actions/                # OpenAPI specs for available GPT actions
│   ├── coincase-openai.yaml
│   ├── events-calendar.yaml
│   └── messari-news.yaml
├── scripts/                # Helper scripts for maintaining the action catalog
│   ├── deploy_to_gpt.sh
│   └── update_actions.py
└── .github/workflows/      # Automation for keeping actions in sync
    └── sync.yml
```

## Usage

Run the helper script to list all available actions:

```bash
python scripts/update_actions.py
```

Deploy the action specs to your GPT integration (placeholder workflow):

```bash
./scripts/deploy_to_gpt.sh
```
