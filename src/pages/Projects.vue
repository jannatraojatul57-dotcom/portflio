<template>
  <div class="min-h-screen">
    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
      <h1 class="text-5xl font-bold gradient-text mb-8 text-center">My Projects</h1>
      <p class="text-lg text-gray-600 dark:text-gray-300 max-w-3xl mx-auto text-center mb-12">
        A showcase of my best work demonstrating design, development, and problem-solving skills.
      </p>
    </section>

    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 mb-12">
      <div class="flex flex-wrap gap-3 justify-center">
        <button v-for="tag in tags" :key="tag" @click="selectedTag = selectedTag === tag ? null : tag" :class="selectedTag === tag ? 'glass-button' : 'px-4 py-2 rounded-lg border border-gray-300 dark:border-gray-700 hover:bg-white/20 dark:hover:bg-gray-800/40 transition'" class="text-sm">
          {{ tag }}
        </button>
      </div>
    </section>

    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
        <ProjectCard v-for="project in filteredProjects" :key="project.id" :project="project" />
      </div>
    </section>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import ProjectCard from '../components/ProjectCard.vue'
export default {
  name: 'Projects',
  components: { ProjectCard },
  setup() {
    const selectedTag = ref(null)
    const tags = ['All', 'Vue', 'FastAPI', 'Laravel', 'Full Stack']
    const projects = [
      { id: 1, title: 'E-Commerce', description: 'Full-stack platform', image: '🛍️', tags: ['Vue', 'FastAPI'] },
      { id: 2, title: 'Dashboard', description: 'Analytics dashboard', image: '📊', tags: ['Vue'] },
      { id: 3, title: 'Task App', description: 'Task management', image: '✅', tags: ['Vue', 'FastAPI'] },
      { id: 4, title: 'Blog', description: 'Blog platform', image: '📝', tags: ['Laravel'] },
      { id: 5, title: 'Social', description: 'Social network', image: '👥', tags: ['FastAPI'] },
      { id: 6, title: 'Portfolio', description: 'Portfolio builder', image: '🎨', tags: ['Vue'] }
    ]
    const filteredProjects = computed(() => {
      if (!selectedTag.value || selectedTag.value === 'All') return projects
      return projects.filter(p => p.tags.includes(selectedTag.value))
    })
    return { selectedTag, tags, filteredProjects }
  }
}
</script>