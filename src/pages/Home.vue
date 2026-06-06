<template>
  <div class="min-h-screen">
    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-20 md:py-32">
      <div class="grid md:grid-cols-2 gap-12 items-center">
        <div class="fade-in-up">
          <h1 class="text-5xl md:text-7xl font-bold leading-tight mb-6">
            <span class="gradient-text">Creative Developer</span>
            <br>
            <span class="text-gray-900 dark:text-white">& Designer</span>
          </h1>
          <p class="text-lg text-gray-600 dark:text-gray-300 mb-8 max-w-xl">
            I build beautiful, fast, and modern web applications using cutting-edge technologies. Specializing in Vue, FastAPI, Laravel, and Tailwind CSS.
          </p>
          <div class="flex flex-wrap gap-4">
            <button @click="navigate('projects')" class="glass-button">View My Work</button>
            <button @click="navigate('contact')" class="px-6 py-2 rounded-lg border-2 border-blue-500 text-blue-500 hover:bg-blue-500 hover:text-white transition">Get In Touch</button>
          </div>
        </div>
        
        <div class="slide-in-right">
          <div class="glass-card p-8 hover:shadow-glass transition-all duration-300">
            <div class="grid grid-cols-2 gap-4">
              <div class="bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl p-6 text-white">
                <p class="text-3xl font-bold">5+</p>
                <p class="text-blue-100">Years Experience</p>
              </div>
              <div class="bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl p-6 text-white">
                <p class="text-3xl font-bold">50+</p>
                <p class="text-purple-100">Projects Done</p>
              </div>
              <div class="bg-gradient-to-br from-pink-500 to-pink-600 rounded-xl p-6 text-white">
                <p class="text-3xl font-bold">30+</p>
                <p class="text-pink-100">Happy Clients</p>
              </div>
              <div class="bg-gradient-to-br from-orange-500 to-orange-600 rounded-xl p-6 text-white">
                <p class="text-3xl font-bold">100%</p>
                <p class="text-orange-100">Satisfaction</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <h2 class="text-3xl font-bold text-center mb-12 gradient-text">Tech Stack</h2>
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
        <TechBadge name="Vue 3" color="from-green-400 to-green-600" />
        <TechBadge name="FastAPI" color="from-blue-400 to-blue-600" />
        <TechBadge name="Tailwind" color="from-cyan-400 to-cyan-600" />
        <TechBadge name="Laravel" color="from-red-400 to-red-600" />
        <TechBadge name="JavaScript" color="from-yellow-400 to-yellow-600" />
        <TechBadge name="Python" color="from-indigo-400 to-indigo-600" />
      </div>
    </section>

    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <h2 class="text-3xl font-bold text-center mb-12 gradient-text">Featured Projects</h2>
      <div class="grid md:grid-cols-2 gap-8">
        <ProjectCard :project="{title: 'E-Commerce Platform', description: 'Full-stack e-commerce with Vue, FastAPI, Tailwind', tags: ['Vue', 'FastAPI', 'Tailwind'], image: '🛍️'}" />
        <ProjectCard :project="{title: 'SaaS Dashboard', description: 'Modern analytics dashboard with real-time data', tags: ['Vue', 'Node.js', 'Chart.js'], image: '📊'}" />
      </div>
    </section>
  </div>
</template>

<script>
import TechBadge from '../components/TechBadge.vue'
import ProjectCard from '../components/ProjectCard.vue'
export default {
  name: 'Home',
  components: { TechBadge, ProjectCard },
  setup() {
    const navigate = (page) => {
      if (window.portfolioApp) window.portfolioApp.navigateTo(page)
    }
    return { navigate }
  }
}
</script>