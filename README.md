# Portfolio Website - Vue 3 + Tailwind CSS + FastAPI

A premium, modern portfolio website built with Vue 3, Tailwind CSS, and Vite. Features glassmorphism design, dark/light mode, and full responsiveness.

## ✨ Features

- Modern glassmorphism design
- Dark/Light mode toggle
- Fully responsive (mobile-first)
- Fast performance with Vite
- Smooth animations and transitions
- CV download functionality
- Contact form
- Project filtering
- SEO optimized

## 🛠 Tech Stack

- Vue 3 (Composition API)
- Tailwind CSS 3
- Vite
- Vercel (Hosting)

## 📦 Installation

### Prerequisites
- Node.js >= 16.0.0
- npm or yarn

### Setup

```bash
npm install
```

### Development

```bash
npm run dev
```

Server runs at: http://localhost:3000

### Production Build

```bash
npm run build
npm run preview
```

## 📁 Project Structure

```
src/
├── components/
│   ├── Nav.vue
│   ├── Footer.vue
│   ├── ProjectCard.vue
│   ├── TechBadge.vue
│   ├── SkillCard.vue
│   ├── ExperienceCard.vue
│   └── ContactMethod.vue
├── pages/
│   ├── Home.vue
│   ├── About.vue
│   ├── Projects.vue
│   └── Contact.vue
├── App.vue
├── main.js
└── style.css
```

## 🎯 Pages

### Home
- Hero section with CTA
- Statistics
- Tech stack
- Featured projects

### About
- Introduction
- Skills by category
- Experience timeline

### Projects
- Filterable gallery
- Technology tags
- Project details

### Contact
- Contact form
- Social links
- Contact info

## 🎨 Customization

### Update Personal Info
- Edit `src/pages/Home.vue` for hero content
- Edit `src/pages/About.vue` for skills/experience
- Edit `src/pages/Projects.vue` for projects
- Edit `src/pages/Contact.vue` for contact details

### Add CV
1. Place your CV in `public/cv.pdf`
2. Update filename in `src/components/Nav.vue`

### Customize Colors
Edit `tailwind.config.js`

## 🚀 Deploy with Vercel

### Option 1: GitHub (Recommended)
1. Push to GitHub
2. Go to vercel.com
3. Import your repository
4. Deploy

### Option 2: Vercel CLI
```bash
npm install -g vercel
vercel
```

## 🔗 Backend Integration

### FastAPI
Update API endpoints:
```javascript
const API_URL = 'https://your-api.com/api'
```

### Laravel
Similarly update for Laravel backend

## 📄 License

Free to use for personal and commercial projects.

---

**Made with Vue 3 & Tailwind CSS**