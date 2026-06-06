<template>
  <div :class="darkMode ? 'dark' : ''" class="min-h-screen bg-white dark:bg-gray-900 transition-colors duration-300">
    <Nav :darkMode="darkMode" @toggle-theme="toggleTheme" />
    <main class="pt-20">
      <component :is="currentComponent" />
    </main>
    <Footer />
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import Nav from './components/Nav.vue'
import Footer from './components/Footer.vue'
import Home from './pages/Home.vue'
import About from './pages/About.vue'
import Projects from './pages/Projects.vue'
import Contact from './pages/Contact.vue'

export default {
  name: 'App',
  components: { Nav, Footer, Home, About, Projects, Contact },
  setup() {
    const currentPage = ref('home')
    const darkMode = ref(localStorage.getItem('darkMode') === 'true')
    const currentComponent = computed(() => {
      const pages = { 'home': 'Home', 'about': 'About', 'projects': 'Projects', 'contact': 'Contact' }
      return pages[currentPage.value] || 'Home'
    })
    const toggleTheme = () => {
      darkMode.value = !darkMode.value
      localStorage.setItem('darkMode', darkMode.value)
    }
    const navigateTo = (page) => {
      currentPage.value = page
      window.scrollTo({ top: 0, behavior: 'smooth' })
    }
    window.portfolioApp = { navigateTo }
    return { currentComponent, darkMode, toggleTheme }
  }
}
</script>