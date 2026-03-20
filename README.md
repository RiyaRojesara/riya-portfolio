# 🚀 Django Portfolio Website

A complete, modern, dark-theme portfolio website built with Django.  
Glassmorphism UI · Smooth Animations · AI Chatbot · Vercel-Ready

---

## 📁 Project Structure

```
portfolio_project/
├── manage.py
├── requirements.txt
├── vercel.json
├── build_files.sh
│
├── portfolio_site/              ← Django project config
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── portfolio/                   ← Main app
    ├── __init__.py
    ├── apps.py
    ├── models.py
    ├── views.py                 ← ✏️ Edit your content here
    ├── urls.py
    ├── migrations/
    │   └── __init__.py
    │
    ├── templates/
    │   └── portfolio/
    │       └── index.html       ← HTML template
    │
    └── static/
        ├── css/
        │   └── style.css        ← All styling
        ├── js/
        │   └── main.js          ← All JavaScript
        ├── images/
        │   └── favicon.svg
        └── files/
            └── cv.pdf           ← ✏️ Add your CV here
```

---

## ⚙️ Installation (Local Development)

### 1. Prerequisites
- Python 3.9 or higher
- pip

### 2. Clone / Download the project
```bash
cd portfolio_project
```

### 3. Create a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies
```bash
pip install -r requirements.txt
```

### 5. Run database migrations (optional, no DB models used)
```bash
python manage.py migrate
```

### 6. Collect static files
```bash
python manage.py collectstatic --noinput
```

### 7. Run the development server
```bash
python manage.py runserver
```

Open your browser at: **http://127.0.0.1:8000**

---

## ✏️ Customization Guide

All your personal content is in **`portfolio/views.py`**.  
Look for `# ✏️ CUSTOMIZE` comments — those are your edit points.

### 1. Personal Info
```python
'name': 'Alex Rivera',           # → Your full name
'title': 'Full-Stack Developer', # → Your job title
'tagline': 'I craft...',         # → Your personal tagline
'about_text': '...',             # → About section paragraph 1
'about_text_2': '...',           # → About section paragraph 2
'location': 'San Francisco, CA', # → Your city
'email': 'alex@example.com',     # → Your email
```

### 2. Social Links
```python
'github_url': 'https://github.com/yourusername',
'linkedin_url': 'https://linkedin.com/in/yourusername',
'twitter_url': 'https://twitter.com/yourusername',
```

### 3. Experience
Edit the `experiences` list. Each item is a dict:
```python
{
    'role': 'Senior Developer',
    'company': 'Awesome Corp',
    'period': 'Jan 2023 – Present',
    'description': 'What you did here...',
    'tags': ['Python', 'Django', 'React'],
    'icon': '🚀',   # Any emoji
},
```

### 4. Projects
Edit the `projects` list:
```python
{
    'title': 'My Project',
    'description': 'What it does...',
    'tags': ['Django', 'React'],
    'github': 'https://github.com/you/project',
    'demo': 'https://yourproject.com',   # or None
    'featured': True,   # Shows "Featured" badge
    'emoji': '🚀',
},
```

### 5. Certificates
```python
{
    'title': 'AWS Certified Developer',
    'issuer': 'Amazon Web Services',
    'date': 'March 2024',
    'badge': '☁️',
    'color': 'orange',   # orange | blue | green | teal
},
```

### 6. Tech Stack
```python
'Frontend': [
    {'name': 'React', 'icon': '⚛️', 'level': 92},  # level = 0-100
    ...
],
```

### 7. Add Your Photo
1. Save your photo as `portfolio/static/images/avatar.jpg`
2. Open `portfolio/templates/portfolio/index.html`
3. Find the avatar section and uncomment:
```html
<img src="{% static 'images/avatar.jpg' %}" alt="{{ name }}" class="avatar-img" />
```
4. Comment out or remove the emoji line above it.

### 8. Add Your CV
1. Export your CV as a PDF
2. Name it `cv.pdf`
3. Place it at: `portfolio/static/files/cv.pdf`
4. Run: `python manage.py collectstatic --noinput`

### 9. Update the Chatbot Replies
In `portfolio/views.py`, find `get_bot_reply()`.  
Update the name, email, and tech stack references to match your own info.

### 10. Change Colors / Theme
Open `portfolio/static/css/style.css` and edit the `:root` variables:
```css
:root {
  --accent:   #6ee7b7;   /* Main green accent → change to any color */
  --accent-2: #818cf8;   /* Indigo accent */
  --accent-3: #f472b6;   /* Pink accent */
  --bg:       #080c14;   /* Page background */
}
```

---

## 🌐 Vercel Deployment

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Set environment variables on Vercel
Go to **Vercel Dashboard → Your Project → Settings → Environment Variables** and add:
```
DEBUG = False
SECRET_KEY = your-super-secret-key-here
```
Generate a Django secret key:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### Step 4: Deploy
```bash
cd portfolio_project
vercel --prod
```

### Step 5: Configure Build Settings on Vercel Dashboard
- **Framework Preset**: Other
- **Build Command**: `chmod +x build_files.sh && ./build_files.sh`
- **Output Directory**: `staticfiles`
- **Install Command**: `pip install -r requirements.txt`

### Step 6: Set ALLOWED_HOSTS
In `settings.py`, add your Vercel domain:
```python
ALLOWED_HOSTS = [
    'your-project.vercel.app',
    '.vercel.app',
    'yourdomain.com',   # if custom domain
]
```

### Alternative: Railway / Render deployment
These platforms support Django natively with PostgreSQL.
Just set the environment variables `SECRET_KEY` and `DEBUG=False`,
and use the `gunicorn portfolio_site.wsgi:application` start command.

---

## 🔐 Security Before Going Live

1. **Change SECRET_KEY** — never commit real keys to git
2. Set `DEBUG = False` in production
3. Add your domain to `ALLOWED_HOSTS`
4. Use environment variables for all secrets

```bash
# .env file (add to .gitignore)
SECRET_KEY=your-real-secret-key
DEBUG=False
```

Then in `settings.py`:
```python
from dotenv import load_dotenv
load_dotenv()
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False') == 'True'
```

---

## 🐛 Common Issues

| Problem | Solution |
|---|---|
| Static files not loading | Run `python manage.py collectstatic` |
| CV download returns 404 | Add `cv.pdf` to `portfolio/static/files/` |
| Fonts not loading | Check internet connection (uses Google Fonts CDN) |
| Chat not working | Check browser console for CSRF errors |
| Vercel 500 error | Set `DEBUG=False` and check environment variables |

---

## 📦 Tech Stack Used

- **Backend**: Django 4.2
- **Static serving**: WhiteNoise
- **Fonts**: Syne + DM Sans (Google Fonts)
- **Icons**: Lucide Icons
- **Animations**: Pure CSS + Intersection Observer API
- **Database**: SQLite (default)
- **Deployment**: Vercel / Railway / Render

---

Made with ❤️ and Django.
