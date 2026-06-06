<template>
  <div class="min-h-screen bg-gradient-to-br from-white via-blue-50 to-purple-50 dark:from-slate-950 dark:via-slate-900 dark:to-slate-800 transition-colors duration-300">
    <!-- Animated Background Elements -->
    <div class="fixed inset-0 overflow-hidden pointer-events-none">
      <div class="absolute top-0 left-0 w-96 h-96 bg-gradient-to-br from-indigo-200/30 to-purple-200/20 rounded-full blur-3xl animate-pulse"></div>
      <div class="absolute bottom-0 right-0 w-96 h-96 bg-gradient-to-tl from-pink-200/30 to-orange-200/20 rounded-full blur-3xl animate-pulse" style="animation-delay: 1s;"></div>
      <div class="absolute top-1/2 left-1/2 w-96 h-96 bg-gradient-to-br from-cyan-200/20 to-blue-200/10 rounded-full blur-3xl animate-pulse" style="animation-delay: 2s;"></div>
    </div>

    <!-- Content -->
    <div class="relative z-10">
      <!-- Navigation -->
      <nav class="fixed top-0 left-0 right-0 z-50 backdrop-blur-md bg-white/70 dark:bg-slate-900/70 border-b border-white/20 dark:border-slate-700/30">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-4">
          <div class="flex justify-between items-center">
            <div class="text-2xl font-bold gradient-text">JT.</div>
            <div class="flex items-center gap-4">
              <button
                @click="scrollToSection('about')"
                class="text-sm font-medium hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors"
              >
                About
              </button>
              <button
                @click="scrollToSection('projects')"
                class="text-sm font-medium hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors"
              >
                Projects
              </button>
              <button
                @click="scrollToSection('skills')"
                class="text-sm font-medium hover:text-indigo-600 dark:hover:text-indigo-400 transition-colors"
              >
                Skills
              </button>
              <button
                @click="toggleDarkMode"
                class="p-2 rounded-lg glass hover-lift"
              >
                <svg v-if="!isDark" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"></path>
                </svg>
                <svg v-else class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.536l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.707.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.464 7.464a1 1 0 01-1.414 0l-.707-.707A1 1 0 014.757 5.343l.707.707a1 1 0 010 1.414zM5 13a1 1 0 100 2H4a1 1 0 100-2h1z" clip-rule="evenodd"></path>
                </svg>
              </button>
              <button class="btn btn-primary">Contact</button>
            </div>
          </div>
        </div>
      </nav>

      <!-- Hero Section -->
      <section class="min-h-screen flex items-center justify-center pt-20 px-4">
        <div class="text-center max-w-4xl mx-auto animate-fadeInUp">
          <h1 class="text-5xl md:text-7xl font-bold mb-6">
            <span class="gradient-text">Creative Developer</span>
            <br>
            <span class="text-slate-900 dark:text-white">& Designer</span>
          </h1>
          <p class="text-xl text-slate-600 dark:text-slate-300 mb-8 leading-relaxed">
            Crafting beautiful, modern web experiences with Vue.js, cutting-edge design patterns, and premium glassmorphism effects.
          </p>
          <div class="flex gap-4 justify-center flex-wrap">
            <button class="btn btn-primary hover-lift">
              <span>View My Work</span>
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6"></path>
              </svg>
            </button>
            <button class="btn btn-secondary">
              <span>Download CV</span>
            </button>
          </div>

          <!-- Floating Cards -->
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mt-16">
            <div class="glass p-6 animate-fadeInUp delay-100 hover-lift">
              <div class="text-3xl font-bold gradient-text mb-2">50+</div>
              <p class="text-slate-600 dark:text-slate-400">Projects Completed</p>
            </div>
            <div class="glass p-6 animate-fadeInUp delay-200 hover-lift">
              <div class="text-3xl font-bold gradient-text mb-2">5+</div>
              <p class="text-slate-600 dark:text-slate-400">Years Experience</p>
            </div>
            <div class="glass p-6 animate-fadeInUp delay-300 hover-lift">
              <div class="text-3xl font-bold gradient-text mb-2">100%</div>
              <p class="text-slate-600 dark:text-slate-400">Client Satisfaction</p>
            </div>
          </div>
        </div>
      </section>

      <!-- About Section -->
      <section id="about" class="min-h-screen flex items-center py-20 px-4">
        <div class="max-w-6xl mx-auto w-full">
          <h2 class="text-4xl md:text-5xl font-bold mb-12 gradient-text">About Me</h2>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-8 items-center">
            <div class="animate-slideInLeft">
              <div class="glass p-8 mb-6">
                <p class="text-lg text-slate-700 dark:text-slate-300 mb-6 leading-relaxed">
                  I'm a full-stack developer passionate about creating stunning, responsive web applications with modern technologies. My expertise lies in Vue.js, FastAPI, and design systems that combine functionality with beautiful aesthetics.
                </p>
                <p class="text-lg text-slate-700 dark:text-slate-300 leading-relaxed">
                  I believe in clean code, user-centric design, and continuous learning. Every project is an opportunity to push boundaries and create something extraordinary.
                </p>
              </div>
              <div class="glass p-6 inline-block">
                <div class="text-sm font-semibold text-indigo-600 dark:text-indigo-400 mb-2">Currently Available</div>
                <p class="text-sm text-slate-600 dark:text-slate-400">For freelance and full-time opportunities</p>
              </div>
            </div>

            <div class="animate-slideInRight">
              <div class="grid grid-cols-2 gap-4">
                <div class="glass p-6 hover-lift">
                  <div class="text-4xl mb-3">🎨</div>
                  <h3 class="font-bold mb-2 dark:text-white">UI/UX Design</h3>
                  <p class="text-sm text-slate-600 dark:text-slate-400">Modern, beautiful interfaces</p>
                </div>
                <div class="glass p-6 hover-lift">
                  <div class="text-4xl mb-3">⚡</div>
                  <h3 class="font-bold mb-2 dark:text-white">Performance</h3>
                  <p class="text-sm text-slate-600 dark:text-slate-400">Fast & optimized</p>
                </div>
                <div class="glass p-6 hover-lift">
                  <div class="text-4xl mb-3">🔧</div>
                  <h3 class="font-bold mb-2 dark:text-white">Full Stack</h3>
                  <p class="text-sm text-slate-600 dark:text-slate-400">Frontend & Backend</p>
                </div>
                <div class="glass p-6 hover-lift">
                  <div class="text-4xl mb-3">🚀</div>
                  <h3 class="font-bold mb-2 dark:text-white">Deployment</h3>
                  <p class="text-sm text-slate-600 dark:text-slate-400">Vercel, Docker, Cloud</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Projects Section -->
      <section id="projects" class="min-h-screen flex items-center py-20 px-4">
        <div class="max-w-6xl mx-auto w-full">
          <h2 class="text-4xl md:text-5xl font-bold mb-12 gradient-text">Featured Projects</h2>
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            <div v-for="(project, index) in projects" :key="index" class="glass p-6 hover-lift animate-fadeInUp" :style="{ animationDelay: `${index * 0.1}s` }">
              <div class="mb-4">
                <div class="inline-block text-3xl mb-3">{{ project.icon }}</div>
                <h3 class="text-xl font-bold dark:text-white mb-2">{{ project.name }}</h3>
                <p class="text-sm text-slate-600 dark:text-slate-400 mb-4">{{ project.description }}</p>
              </div>
              
              <div class="flex flex-wrap gap-2 mb-4">
                <span v-for="tech in project.technologies" :key="tech" class="text-xs px-3 py-1 rounded-full bg-indigo-100 dark:bg-indigo-900/30 text-indigo-700 dark:text-indigo-300">
                  {{ tech }}
                </span>
              </div>
              
              <button class="btn btn-tertiary text-sm">
                <span>View Project →</span>
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- Skills Section -->
      <section id="skills" class="min-h-screen flex items-center py-20 px-4">
        <div class="max-w-6xl mx-auto w-full">
          <h2 class="text-4xl md:text-5xl font-bold mb-12 gradient-text">Skills & Expertise</h2>
          
          <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <div v-for="(category, index) in skillCategories" :key="index" class="glass p-6 animate-fadeInUp" :style="{ animationDelay: `${index * 0.1}s` }">
              <h3 class="text-lg font-bold mb-4 dark:text-white">{{ category.name }}</h3>
              <div class="flex flex-wrap gap-2">
                <span v-for="skill in category.skills" :key="skill" class="text-xs px-3 py-2 rounded-lg bg-gradient-to-r from-indigo-100 to-purple-100 dark:from-indigo-900/30 dark:to-purple-900/30 text-indigo-700 dark:text-indigo-300 font-medium">
                  {{ skill }}
                </span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- CTA Section -->
      <section class="py-20 px-4">
        <div class="max-w-4xl mx-auto">
          <div class="glass p-12 text-center animate-fadeInUp">
            <h2 class="text-3xl md:text-4xl font-bold mb-6 dark:text-white">Ready to create something amazing?</h2>
            <p class="text-lg text-slate-600 dark:text-slate-300 mb-8">Let's build your next project together</p>
            <button class="btn btn-primary hover-lift text-lg">
              <span>Get In Touch</span>
              <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6"></path>
              </svg>
            </button>
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer class="border-t border-white/10 dark:border-slate-700/30 py-12 px-4 bg-white/30 dark:bg-slate-900/30 backdrop-blur-sm">
        <div class="max-w-6xl mx-auto">
          <div class="grid grid-cols-1 md:grid-cols-4 gap-8 mb-8">
            <div>
              <div class="text-2xl font-bold gradient-text mb-2">JT.</div>
              <p class="text-sm text-slate-600 dark:text-slate-400">Full Stack Developer & Designer</p>
            </div>
            <div>
              <h4 class="font-bold mb-3 dark:text-white">Navigation</h4>
              <ul class="space-y-2 text-sm text-slate-600 dark:text-slate-400">
                <li><a href="#about" class="hover:text-indigo-600">About</a></li>
                <li><a href="#projects" class="hover:text-indigo-600">Projects</a></li>
                <li><a href="#skills" class="hover:text-indigo-600">Skills</a></li>
              </ul>
            </div>
            <div>
              <h4 class="font-bold mb-3 dark:text-white">Social</h4>
              <ul class="space-y-2 text-sm text-slate-600 dark:text-slate-400">
                <li><a href="#" class="hover:text-indigo-600">GitHub</a></li>
                <li><a href="#" class="hover:text-indigo-600">LinkedIn</a></li>
                <li><a href="#" class="hover:text-indigo-600">Twitter</a></li>
              </ul>
            </div>
            <div>
              <h4 class="font-bold mb-3 dark:text-white">Contact</h4>
              <ul class="space-y-2 text-sm text-slate-600 dark:text-slate-400">
                <li><a href="mailto:hello@example.com" class="hover:text-indigo-600">hello@example.com</a></li>
                <li><a href="tel:+1234567890" class="hover:text-indigo-600">+1 (234) 567-890</a></li>
              </ul>
            </div>
          </div>
          
          <div class="border-t border-white/10 dark:border-slate-700/30 pt-8 text-center text-sm text-slate-600 dark:text-slate-400">
            <p>© 2024 Janna Trao Jatul. All rights reserved. Built with Vue.js & Tailwind CSS.</p>
          </div>
        </div>
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const isDark = ref(false)

const projects = ref([
  {
    name: 'E-Commerce Platform',
    description: 'Modern e-commerce solution with real-time inventory management',
    icon: '🛍️',
    technologies: ['Vue.js', 'FastAPI', 'PostgreSQL', 'Stripe']
  },
  {
    name: 'SaaS Dashboard',
    description: 'Beautiful analytics dashboard with glassmorphism design',
    icon: '📊',
    technologies: ['Vue.js', 'Tailwind', 'Chart.js', 'FastAPI']
  },
  {
    name: 'Mobile App UI',
    description: 'Responsive mobile-first design system',
    icon: '📱',
    technologies: ['Vue.js', 'React Native', 'Figma']
  },
  {
    name: 'AI Content Tool',
    description: 'AI-powered content generation platform',
    icon: '🤖',
    technologies: ['Vue.js', 'Python', 'OpenAI', 'FastAPI']
  },
  {
    name: 'Design System',
    description: 'Comprehensive component library with documentation',
    icon: '🎨',
    technologies: ['Vue.js', 'Storybook', 'Tailwind']
  },
  {
    name: 'Real-time Collab',
    description: 'Collaborative tool with WebSocket integration',
    icon: '👥',
    technologies: ['Vue.js', 'FastAPI', 'WebSocket', 'Redis']
  }
])

const skillCategories = ref([
  {
    name: 'Frontend',
    skills: ['Vue.js', 'React', 'Tailwind CSS', 'JavaScript', 'TypeScript']
  },
  {
    name: 'Backend',
    skills: ['FastAPI', 'Python', 'PostgreSQL', 'Redis', 'Docker']
  },
  {
    name: 'Design',
    skills: ['Figma', 'UI/UX', 'Animation', 'Responsive Design']
  },
  {
    name: 'DevOps',
    skills: ['Vercel', 'GitHub Actions', 'Cloud', 'CI/CD']
  }
])

const toggleDarkMode = () => {
  isDark.value = !isDark.value
  if (isDark.value) {
    document.documentElement.classList.add('dark')
    localStorage.setItem('darkMode', 'true')
  } else {
    document.documentElement.classList.remove('dark')
    localStorage.setItem('darkMode', 'false')
  }
}

const scrollToSection = (sectionId) => {
  const element = document.getElementById(sectionId)
  if (element) {
    element.scrollIntoView({ behavior: 'smooth' })
  }
}

onMounted(() => {
  if (localStorage.getItem('darkMode') === 'true') {
    isDark.value = true
    document.documentElement.classList.add('dark')
  }
})
</script>