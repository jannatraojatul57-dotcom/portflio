<template>
  <div :class="isDark ? 'dark' : ''" class="transition-colors duration-300">
    <div class="min-h-screen bg-gradient-to-br from-slate-50 to-blue-50 dark:from-slate-950 dark:to-slate-900">
      <!-- Navigation -->
      <nav class="fixed top-0 w-full z-50">
        <div class="glass dark:bg-slate-900/70 dark:border-slate-700/30 glass-light mx-4 mt-4 px-6 py-4 max-w-6xl mx-auto rounded-xl">
          <div class="flex justify-between items-center">
            <h1 class="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent">
              Janna Trao Jatul
            </h1>
            <button
              @click="isDark = !isDark"
              class="p-2 rounded-lg glass dark:bg-slate-800/50 dark:border-slate-700/30 glass-light hover:scale-110 transition-transform"
              :title="isDark ? 'Light Mode' : 'Dark Mode'"
            >
              <svg v-if="isDark" class="w-5 h-5 text-yellow-400" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 2a1 1 0 011 1v1a1 1 0 11-2 0V3a1 1 0 011-1zm4 8a4 4 0 11-8 0 4 4 0 018 0zm-.464 4.95l.707.707a1 1 0 001.414-1.414l-.707-.707a1 1 0 00-1.414 1.414zm2.12-10.607a1 1 0 010 1.414l-.707.707a1 1 0 11-1.414-1.414l.707-.707a1 1 0 011.414 0zM17 11a1 1 0 100-2h-1a1 1 0 100 2h1zm-7 4a1 1 0 011 1v1a1 1 0 11-2 0v-1a1 1 0 011-1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zm5.657-9.193a1 1 0 00-1.414 0l-.707.707A1 1 0 005.05 6.464l.707-.707a1 1 0 011.414-1.414zM5 8a1 1 0 100-2H4a1 1 0 100 2h1z" clip-rule="evenodd"/>
              </svg>
              <svg v-else class="w-5 h-5 text-slate-600" fill="currentColor" viewBox="0 0 20 20">
                <path d="M17.293 13.293A8 8 0 016.707 2.707a8.001 8.001 0 1010.586 10.586z"/>
              </svg>
            </button>
          </div>
        </div>
      </nav>

      <!-- Hero Section -->
      <section class="pt-32 pb-20 px-4">
        <div class="max-w-6xl mx-auto text-center">
          <div class="glass dark:bg-slate-900/50 dark:border-slate-700/30 glass-light p-12 mb-8">
            <h2 class="text-5xl md:text-6xl font-bold text-slate-900 dark:text-white mb-4">
              Full Stack Developer
            </h2>
            <p class="text-xl text-slate-600 dark:text-slate-300 mb-6">
              Specializing in Vue.js, FastAPI, and modern web technologies
            </p>
            <div class="flex gap-4 justify-center">
              <button class="glass dark:bg-blue-600/50 dark:border-blue-500/30 glass-light px-8 py-3 font-semibold text-blue-600 dark:text-white hover:scale-105 transition-transform">
                View My Work
              </button>
              <button class="glass dark:bg-slate-800/50 dark:border-slate-700/30 glass-light px-8 py-3 font-semibold text-slate-700 dark:text-slate-300 hover:scale-105 transition-transform">
                Contact Me
              </button>
            </div>
          </div>
        </div>
      </section>

      <!-- Skills Section -->
      <section class="py-20 px-4">
        <div class="max-w-6xl mx-auto">
          <h3 class="text-4xl font-bold text-slate-900 dark:text-white mb-12 text-center">
            My Skills
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <div class="glass dark:bg-slate-900/50 dark:border-slate-700/30 glass-light p-8 hover:scale-105 transition-transform">
              <div class="text-4xl mb-4">📦</div>
              <h4 class="text-2xl font-bold text-slate-900 dark:text-white mb-2">Frontend</h4>
              <p class="text-slate-600 dark:text-slate-400">
                Vue.js 3, Tailwind CSS, Responsive Design, State Management
              </p>
            </div>
            <div class="glass dark:bg-slate-900/50 dark:border-slate-700/30 glass-light p-8 hover:scale-105 transition-transform">
              <div class="text-4xl mb-4">⚙️</div>
              <h4 class="text-2xl font-bold text-slate-900 dark:text-white mb-2">Backend</h4>
              <p class="text-slate-600 dark:text-slate-400">
                FastAPI, Python, REST APIs, Database Design, Authentication
              </p>
            </div>
            <div class="glass dark:bg-slate-900/50 dark:border-slate-700/30 glass-light p-8 hover:scale-105 transition-transform">
              <div class="text-4xl mb-4">🎨</div>
              <h4 class="text-2xl font-bold text-slate-900 dark:text-white mb-2">Design</h4>
              <p class="text-slate-600 dark:text-slate-400">
                UI/UX, Glassmorphism, Dark Mode Support, Modern Aesthetics
              </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Projects Section -->
      <section class="py-20 px-4">
        <div class="max-w-6xl mx-auto">
          <h3 class="text-4xl font-bold text-slate-900 dark:text-white mb-12 text-center">
            Featured Projects
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="glass dark:bg-slate-900/50 dark:border-slate-700/30 glass-light p-8 hover:shadow-2xl transition-all">
              <h4 class="text-2xl font-bold text-slate-900 dark:text-white mb-3">Project One</h4>
              <p class="text-slate-600 dark:text-slate-400 mb-4">
                A full-stack application built with Vue.js and FastAPI showcasing modern web development practices.
              </p>
              <div class="flex gap-2">
                <span class="px-3 py-1 rounded-full glass dark:bg-blue-600/30 dark:border-blue-500/20 text-sm font-semibold text-blue-600 dark:text-blue-300">Vue.js</span>
                <span class="px-3 py-1 rounded-full glass dark:bg-green-600/30 dark:border-green-500/20 text-sm font-semibold text-green-600 dark:text-green-300">FastAPI</span>
              </div>
            </div>
            <div class="glass dark:bg-slate-900/50 dark:border-slate-700/30 glass-light p-8 hover:shadow-2xl transition-all">
              <h4 class="text-2xl font-bold text-slate-900 dark:text-white mb-3">Project Two</h4>
              <p class="text-slate-600 dark:text-slate-400 mb-4">
                A responsive portfolio site with beautiful glassmorphism design and dark mode support.
              </p>
              <div class="flex gap-2">
                <span class="px-3 py-1 rounded-full glass dark:bg-purple-600/30 dark:border-purple-500/20 text-sm font-semibold text-purple-600 dark:text-purple-300">Tailwind</span>
                <span class="px-3 py-1 rounded-full glass dark:bg-yellow-600/30 dark:border-yellow-500/20 text-sm font-semibold text-yellow-600 dark:text-yellow-300">Responsive</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- Contact Section -->
      <section class="py-20 px-4 mb-20">
        <div class="max-w-2xl mx-auto">
          <div class="glass dark:bg-slate-900/50 dark:border-slate-700/30 glass-light p-12">
            <h3 class="text-3xl font-bold text-slate-900 dark:text-white mb-6 text-center">
              Get In Touch
            </h3>
            <form @submit.prevent="handleSubmit" class="space-y-4">
              <input
                v-model="form.name"
                type="text"
                placeholder="Your Name"
                class="w-full px-4 py-3 rounded-lg glass dark:bg-slate-800/50 dark:border-slate-700/30 dark:text-white dark:placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <input
                v-model="form.email"
                type="email"
                placeholder="Your Email"
                class="w-full px-4 py-3 rounded-lg glass dark:bg-slate-800/50 dark:border-slate-700/30 dark:text-white dark:placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
              />
              <textarea
                v-model="form.message"
                placeholder="Your Message"
                rows="5"
                class="w-full px-4 py-3 rounded-lg glass dark:bg-slate-800/50 dark:border-slate-700/30 dark:text-white dark:placeholder-slate-400 focus:outline-none focus:ring-2 focus:ring-blue-500"
              ></textarea>
              <button
                type="submit"
                class="w-full glass dark:bg-blue-600/50 dark:border-blue-500/30 py-3 font-bold text-blue-600 dark:text-white hover:scale-105 transition-transform"
              >
                Send Message
              </button>
            </form>
          </div>
        </div>
      </section>

      <!-- Footer -->
      <footer class="py-8 px-4 border-t glass dark:bg-slate-900/50 dark:border-slate-700/30">
        <div class="max-w-6xl mx-auto text-center text-slate-600 dark:text-slate-400">
          <p>&copy; 2024 Janna Trao Jatul. All rights reserved.</p>
        </div>
      </footer>
    </div>
  </div>
</template>

<script setup>
import { ref, watch, onMounted } from 'vue'
import axios from 'axios'

const isDark = ref(false)
const form = ref({
  name: '',
  email: '',
  message: ''
})

onMounted(() => {
  // Check for saved theme preference or default to light mode
  const savedTheme = localStorage.getItem('theme')
  if (savedTheme === 'dark') {
    isDark.value = true
  } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
    isDark.value = true
  }
})

// Watch for dark mode changes
watch(isDark, (newVal) => {
  localStorage.setItem('theme', newVal ? 'dark' : 'light')
})

const handleSubmit = async () => {
  try {
    const response = await axios.post('/api/send-email', form.value)
    alert('Message sent successfully!')
    form.value = { name: '', email: '', message: '' }
  } catch (error) {
    alert('Failed to send message. Please try again.')
  }
}
</script>

<style scoped>
</style>