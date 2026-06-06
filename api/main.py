from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import Optional
import os
from datetime import datetime

app = FastAPI(title="Portfolio API", version="1.0.0")

# CORS Configuration
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "https://*.vercel.app",
    "https://portflio-janna.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic Models
class ContactForm(BaseModel):
    name: str
    email: str
    message: str

class Project(BaseModel):
    id: int
    title: str
    description: str
    technologies: list
    link: Optional[str] = None
    github: Optional[str] = None

class Skill(BaseModel):
    category: str
    items: list

# Sample Data
PROJECTS = [
    Project(
        id=1,
        title="E-Commerce Platform",
        description="Full-stack e-commerce platform with Vue.js frontend and FastAPI backend",
        technologies=["Vue.js", "FastAPI", "PostgreSQL", "Tailwind CSS"],
        github="https://github.com/jannatraojatul57-dotcom/ecommerce"
    ),
    Project(
        id=2,
        title="Task Management App",
        description="Real-time task management application with dark mode support",
        technologies=["Vue.js", "FastAPI", "SQLite", "Tailwind CSS"],
        github="https://github.com/jannatraojatul57-dotcom/taskapp"
    ),
    Project(
        id=3,
        title="Analytics Dashboard",
        description="Interactive dashboard for data visualization and analytics",
        technologies=["Vue.js", "FastAPI", "Chart.js", "Tailwind CSS"],
        github="https://github.com/jannatraojatul57-dotcom/analytics"
    ),
]

SKILLS = [
    Skill(
        category="Frontend",
        items=["Vue.js 3", "Tailwind CSS", "Vite", "Responsive Design", "State Management"]
    ),
    Skill(
        category="Backend",
        items=["FastAPI", "Python", "REST APIs", "SQLAlchemy", "PostgreSQL"]
    ),
    Skill(
        category="Tools & DevOps",
        items=["Git", "Docker", "Vercel", "GitHub", "Linux"]
    ),
]

# Routes
@app.get("/")
async def root():
    """Health check endpoint"""
    return {
        "message": "Portfolio API is running",
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/projects")
async def get_projects():
    """Get all projects"""
    return {
        "status": "success",
        "data": PROJECTS,
        "count": len(PROJECTS)
    }

@app.get("/api/projects/{project_id}")
async def get_project(project_id: int):
    """Get a specific project by ID"""
    project = next((p for p in PROJECTS if p.id == project_id), None)
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return {
        "status": "success",
        "data": project
    }

@app.get("/api/skills")
async def get_skills():
    """Get all skills"""
    return {
        "status": "success",
        "data": SKILLS,
        "count": len(SKILLS)
    }

@app.post("/api/send-email")
async def send_email(form: ContactForm):
    """Handle contact form submission"""
    try:
        # TODO: Integrate with email service (SendGrid, Mailgun, etc.)
        # For now, just validate and return success
        if not form.name or not form.email or not form.message:
            raise HTTPException(status_code=400, detail="All fields are required")
        
        # Here you would send an email using a service like SendGrid
        # Example:
        # await send_email_via_sendgrid(
        #     to="your-email@example.com",
        #     subject=f"Portfolio Contact from {form.name}",
        #     body=f"Email: {form.email}\n\nMessage: {form.message}"
        # )
        
        return {
            "status": "success",
            "message": "Email sent successfully",
            "timestamp": datetime.now().isoformat()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/about")
async def get_about():
    """Get about information"""
    return {
        "status": "success",
        "data": {
            "name": "Janna Trao Jatul",
            "title": "Full Stack Developer",
            "bio": "Passionate about building beautiful and functional web applications with modern technologies",
            "email": "your-email@example.com",
            "location": "Your Location",
            "social": {
                "github": "https://github.com/jannatraojatul57-dotcom",
                "linkedin": "https://linkedin.com/in/jannatraojatul57",
                "twitter": "https://twitter.com/jannatraojatul57"
            }
        }
    }

@app.get("/health")
async def health_check():
    """Simple health check for monitoring"""
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)