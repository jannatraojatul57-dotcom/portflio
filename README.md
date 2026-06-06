# Janna Trao Jatul's Portfolio

A modern, beautiful portfolio website built with Vue.js 3, FastAPI, and Tailwind CSS, featuring glassmorphism design and dark/light mode support.

## Features

✨ **Modern Design**
- Glassmorphism UI with backdrop blur effects
- Smooth animations and transitions
- Responsive grid layouts

🌓 **Dark/Light Mode**
- Toggle between light and dark themes
- Persistent theme preference using localStorage
- System preference detection

⚡ **Tech Stack**
- **Frontend**: Vue.js 3, Vite, Tailwind CSS
- **Backend**: FastAPI, Python
- **Deployment**: Vercel (serverless)

🎨 **Features**
- Portfolio showcase
- Skills display
- Project gallery with tags
- Contact form with backend integration
- Smooth scrolling navigation
- SEO optimized

## Project Structure

```
portflio/
├── src/
│   ├── main.js          # Vue app entry point
│   ├── App.vue          # Main component
│   └── index.css        # Global styles
├── api/
│   └── main.py          # FastAPI backend
├── index.html           # HTML entry point
├── vite.config.js       # Vite configuration
├── tailwind.config.js   # Tailwind CSS configuration
├── postcss.config.js    # PostCSS configuration
├── vercel.json          # Vercel deployment config
├── package.json         # Frontend dependencies
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## Installation

### Prerequisites
- Node.js 16+
- Python 3.11+
- npm or yarn

### Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/jannatraojatul57-dotcom/portflio.git
   cd portflio
   ```

2. **Install Frontend Dependencies**
   ```bash
   npm install
   ```

3. **Install Backend Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Development

### Run Backend
```bash
npm run api
```
The FastAPI backend will run at `http://localhost:8000`

### Run Frontend
In a new terminal:
```bash
npm run dev
```
The Vue app will run at `http://localhost:5173`

The frontend is configured to proxy API requests to the backend.

## Production Build

### Build Frontend
```bash
npm run build
```
This creates optimized production build in `dist/` folder.

### Deploy to Vercel

1. **Install Vercel CLI**
   ```bash
   npm install -g vercel
   ```

2. **Deploy**
   ```bash
   vercel
   ```

3. **Environment Variables** (if needed)
   - Add any required environment variables in Vercel dashboard

The `vercel.json` file is pre-configured to:
- Run FastAPI backend on `/api/*` routes
- Serve Vue.js frontend from `dist/`
- Handle client-side routing

## API Endpoints

- `GET /` - Health check
- `GET /api/projects` - Get all projects
- `GET /api/projects/{id}` - Get specific project
- `GET /api/skills` - Get all skills
- `GET /api/about` - Get about information
- `POST /api/send-email` - Send contact form message
- `GET /health` - Health check for monitoring

## Customization

### Update Portfolio Content
Edit `api/main.py` to update:
- `PROJECTS` - Your project portfolio
- `SKILLS` - Your technical skills
- About information

### Styling
- **Colors**: Modify `tailwind.config.js`
- **Glass effect**: Edit `src/index.css`
- **Component styles**: Edit `src/App.vue`

### Contact Form
Replace the email sending logic in `api/main.py` with your email service (SendGrid, Mailgun, etc.):

```python
# Example with SendGrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
message = Mail(...)
sg.send(message)
```

## Environment Variables

Create a `.env` file in the root directory:

```
VITE_API_URL=http://localhost:8000
```

For backend (if using email service):
```
SENDGRID_API_KEY=your_key_here
DATABASE_URL=your_database_url
```

## Browser Support

- Chrome/Edge: Latest 2 versions
- Firefox: Latest 2 versions
- Safari: Latest 2 versions
- Mobile browsers: Full support

## Performance

- Optimized bundle size with Vite
- Lazy loading components
- Image optimization
- CSS minification with Tailwind
- FastAPI async endpoints for fast response times

## License

MIT License - feel free to use this portfolio as a template

## Contact

- Email: your-email@example.com
- GitHub: [@jannatraojatul57-dotcom](https://github.com/jannatraojatul57-dotcom)
- LinkedIn: [Janna Trao Jatul](https://linkedin.com)

---

Built with ❤️ using Vue.js, FastAPI, and Tailwind CSS