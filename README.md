# Core v5

A modern Django application with Next.js frontend integration.

## Features

- 🔐 Authentication System
  - Login with username and password
  - Password reset functionality
  - Password change for authenticated users
  - Email verification
- 🎨 Modern UI
  - Tailwind CSS v4 for styling
  - Responsive design for all devices
  - Clean and minimalist interface
- 🌐 Internationalization
  - Multi-language support
  - English and French translations
- 🔒 Security
  - CSRF protection
  - Secure password handling
  - Session management

## Tech Stack

- Backend:
  - Django 5.2
  - Python 3.13
  - SQLite (development)
- Frontend:
  - Next.js (main application)
  - Tailwind CSS v4
  - Django Templates (admin interface)
- Additional:
  - GraphQL API
  - CKEditor 5 integration
  - CORS configuration

## Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/strakon-v5.git
cd strakon-v5
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create .env file:
```bash
SECRET_KEY=your-secret-key
DEBUG=True
SITE_NAME=Strakon

# Email settings (for password reset)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

5. Run migrations:
```bash
python manage.py migrate
```

6. Create a superuser:
```bash
python manage.py createsuperuser
```

7. Run the development server:
```bash
python manage.py runserver
```

## Development

### Tailwind CSS

To compile Tailwind CSS:

```bash
# Watch for changes
npx tailwindcss -i ./api/static/src/input.css -o ./api/static/src/output.css --watch

# Build for production
npx tailwindcss -i ./api/static/src/input.css -o ./api/static/src/output.css --minify
```

### Translations

To manage translations:

```bash
# Generate message files
python manage.py makemessages -l fr

# Compile messages
python manage.py compilemessages
```

## Project Structure

```
api/
├── api/
│   ├── templates/
│   │   ├── auth/          # Authentication templates
│   │   └── ui/           # Base templates and components
│   ├── static/
│   │   └── src/          # Tailwind CSS files
│   ├── views.py          # View controllers
│   └── urls.py           # URL routing
├── config/               # Project settings
└── locale/              # Translation files
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**Muhammad Aslan**
- Email: joudakenore@gmail.com
- Phone: +216 55 000 359 