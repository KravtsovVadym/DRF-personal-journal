# Diary API

**REST API for personal diary** based on Django + DRF

## Features

- Create, edit, delete entries
- Tagging entries
- Search by name, content, tags
- Authentication (JWT in preparation)
- Access only to your entries

## Installation

```bash
python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API Endpoints

| Method | Endpoint | Description |
|------|------|------|
| GET | `/api/entry/` | All user entries |
| POST | `/api/entry/` | New entry |
| GET | `/api/entry/{id}/` | Entry by ID |
| PATCH | `/api/entry/{id}/` | Edit |
| DELETE | `/api/entry/{id}/` | Delete |
| GET | `/api/entry/by_tag/?name=` | Entries by tag |
| GET | `/api/entry/{id}/similar/` | Similar entries |
| GET/POST | `/api/tag/` | Tags |

## Structure

```
diary_project/
├── diary/ # Main app
│ ├── models.py # Entry, Tag
│ ├── serializers.py # DRF serializers
│ ├── views.py # ViewSets
│ └── tests/ # Unit tests
├── manage.py
└── requirements.txt
```
