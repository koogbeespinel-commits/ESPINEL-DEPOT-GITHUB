# Mini Social Network

A full-stack social network application built with Django REST Framework backend and React TypeScript frontend.

## Features

- User authentication and profiles
- Create, read, update, delete posts
- Like and comment on posts
- Follow/unfollow users
- Real-time feed updates
- Responsive design

## Tech Stack

### Backend
- **Django 4.2** - Web framework
- **Django REST Framework** - RESTful API
- **PostgreSQL** - Database
- **Docker** - Containerization

### Frontend
- **React 18** - UI library
- **TypeScript** - Type safety
- **React Router** - Navigation
- **Axios** - HTTP client
- **Docker** - Containerization

## Project Structure

```
mini-social-network/
├── backend/                  # Django Backend
│   ├── core/                # Configuration Django
│   ├── users/               # Gestion utilisateurs
│   ├── posts/               # Gestion posts
��   ├── comments/            # Gestion commentaires
│   ├── requirements.txt
│   ├── manage.py
│   ├── Dockerfile
│   └── .env.example
│
├── frontend/                # React Frontend
│   ├── public/
│   ├── src/
│   │   ├── pages/
│   │   ├── components/
│   │   ├── services/
│   │   ├── App.tsx
│   │   └── index.tsx
│   ├── package.json
│   ├── tsconfig.json
│   └── .env.example
│
├── docker-compose.yml
├── .gitignore
└── README.md
```

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)

### With Docker Compose (Recommended)

1. Clone the repository
```bash
git clone <repository-url>
cd mini-social-network
```

2. Start the application
```bash
docker-compose up -d
```

3. Run migrations
```bash
docker-compose exec backend python manage.py migrate
```

4. Create a superuser
```bash
docker-compose exec backend python manage.py createsuperuser
```

5. Access the application
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000/api
- Admin Panel: http://localhost:8000/admin

### Local Development

#### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py runserver
```

#### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env
npm start
```

## API Endpoints

### Users
- `GET /api/users/` - List all users
- `GET /api/users/{id}/` - Get user details
- `POST /api/users/{id}/follow/` - Follow a user
- `POST /api/users/{id}/unfollow/` - Unfollow a user

### Posts
- `GET /api/posts/` - List all posts
- `POST /api/posts/` - Create a post
- `GET /api/posts/{id}/` - Get post details
- `PUT /api/posts/{id}/` - Update a post
- `DELETE /api/posts/{id}/` - Delete a post
- `POST /api/posts/{id}/like/` - Like a post
- `POST /api/posts/{id}/unlike/` - Unlike a post

### Comments
- `GET /api/comments/` - List all comments
- `POST /api/comments/` - Create a comment
- `GET /api/comments/{id}/` - Get comment details
- `PUT /api/comments/{id}/` - Update a comment
- `DELETE /api/comments/{id}/` - Delete a comment
- `POST /api/comments/{id}/like/` - Like a comment
- `POST /api/comments/{id}/unlike/` - Unlike a comment

## Environment Variables

### Backend (.env)
```
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
DB_ENGINE=django.db.backends.postgresql
DB_NAME=mini_social_network
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

### Frontend (.env)
```
REACT_APP_API_URL=http://localhost:8000/api
REACT_APP_APP_NAME=Mini Social Network
```

## Development

### Running Tests

Backend:
```bash
cd backend
python manage.py test
```

Frontend:
```bash
cd frontend
npm test
```

### Building for Production

Backend:
```bash
docker build -t mini-social-network-backend ./backend
```

Frontend:
```bash
docker build -t mini-social-network-frontend ./frontend
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

## Support

For support, please open an issue on the GitHub repository.

## Authors

- Your Name - Initial work

## Acknowledgments

- Django and Django REST Framework community
- React community
- Docker community
