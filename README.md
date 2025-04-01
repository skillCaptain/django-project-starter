
<h1 align="center">💜 Django Project Starter 💜</h1>

<p align="center">
  A modern, modular, and lightning-fast Django REST Framework starter with CLI scaffolding, Pydantic v2 DTOs, and clean architecture principles.
</p>

---

## Why this starter exists

Most Django projects start messy, grow messier, and end up unmaintainable.

This project starter changes that by giving you:

- ✅ A **clean, scalable folder structure**
- ⚙️ CLI tools to **generate apps and CRUD logic in seconds**
- 🧬 **Pydantic v2** DTOs for safe and strict data validation
- 🔄 A **service/controller-based architecture** that separates concerns

Whether you’re a solo developer or a team scaling fast, this saves hours of boilerplate.

---

## 📁 Project Structure

```bash
starter_framework/
├── apps/
│   └── blog/
│       ├── models.py
│       ├── views.py         # Class-based controllers
│       ├── services.py      # Business logic
│       ├── dtos.py          # Pydantic v2 DTOs
│       ├── urls.py
│       └── apps.py
├── core/
│   ├── base.py              # BaseController, AbstractService
│   └── management/commands/
│       ├── generate_app.py
│       └── generate_crud.py
├── settings.py
└── manage.py
```

> 💡 Your API stays modular. Each feature lives in its own directory.

---

## ⚙️ Quickstart

### 1. Clone and setup environment

```bash
git clone https://github.com/skillCaptain/django-project-starter.git
cd django-project-starter
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Migrate and run

```bash
python manage.py migrate
python manage.py runserver
```

You’re ready to build!

---

## ✨ CLI Commands

### 📦 Generate a new app

```bash
python manage.py generate_app blog
```

Creates:

```bash
apps/blog/
├── models.py
├── views.py
├── services.py
├── dtos.py
├── urls.py
├── admin.py
├── apps.py
```

Then, register in `INSTALLED_APPS`:

```python
'starter_framework.apps.blog',
```

---

### ⚡ Generate CRUD 

```bash
python manage.py generate_crud blog Post
```

Adds:

- `PostController` in `views.py`
- `PostService` in `services.py`
- `PostCreateDTO` & `PostResponseDTO` in `dtos.py`

Now your CRUD is structured and ready to use 🔥

---

## 🧬 DTOs with Pydantic v2

```python
# blog/dtos.py

from pydantic import BaseModel

class PostCreateDTO(BaseModel):
    title: str
    content: str

    class Config:
        from_attributes = True


class PostResponseDTO(BaseModel):
    id: int
    title: str
    content: str

    class Config:
        from_attributes = True
```

> ✅ `from_attributes = True` replaces `orm_mode = True` (for v2)

To use types like `EmailStr`, install:

```bash
pip install "pydantic[email]"
```

---

## 🔧 Useful Commands

```bash
# Generate new app
python manage.py generate_app users

# Generate CRUD for model
python manage.py generate_crud users User

# Run dev server
python manage.py runserver

# Make and apply migrations
python manage.py makemigrations
python manage.py migrate
```

---

## 🧱 Project Philosophy

This project is built on the idea that **good architecture should get out of your way**.

We believe in:

- ✅ Clarity over complexity
- 🧩 Reusable, modular code
- 📦 Starting small, scaling cleanly
- 🔁 Tools that remove repetition, not control

Your team should focus on what matters — features, not folder structure.

---

## ✅ .gitignore Tips

Add this to your `.gitignore`:

```
*.sqlite3
**/migrations/
!**/migrations/__init__.py
```

---

## 📦 Requirements

```text
Django>=4.2
djangorestframework
pydantic>=2.0
```

Install:

```bash
pip install -r requirements.txt
```

---

## 👨‍💻 Maintained by SkillCaptain

This starter is built and maintained by [SkillCaptain](https://skillcaptain.app) — a platform offering:

- Resume reviews and analyzers
- Real-world coding projects
- Live sessions and courses

---

