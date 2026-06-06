<template>
  <div class="min-h-screen">
    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
      <h1 class="text-5xl font-bold gradient-text mb-8 text-center">About Me</h1>
      <p class="text-lg text-gray-600 dark:text-gray-300 max-w-3xl mx-auto text-center mb-12">
        I'm a passionate full-stack developer with expertise in modern web technologies. I love creating elegant solutions to complex problems.
      </p>
    </section>

    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <h2 class="text-3xl font-bold mb-12 text-center gradient-text">Skills</h2>
      <div class="grid md:grid-cols-3 gap-8">
        <SkillCard title="Frontend" icon="💻">
          <ul class="space-y-2 text-gray-600 dark:text-gray-300">
            <li>✓ Vue 3 / Vue 2</li>
            <li>✓ Tailwind CSS</li>
            <li>✓ JavaScript / ES6+</li>
            <li>✓ Responsive Design</li>
            <li>✓ Animations</li>
          </ul>
        </SkillCard>
        <SkillCard title="Backend" icon="⚙️">
          <ul class="space-y-2 text-gray-600 dark:text-gray-300">
            <li>✓ FastAPI</li>
            <li>✓ Laravel / PHP</li>
            <li>✓ Python</li>
            <li>✓ REST APIs</li>
            <li>✓ Databases</li>
          </ul>
        </SkillCard>
        <SkillCard title="Tools" icon="🛠️">
          <ul class="space-y-2 text-gray-600 dark:text-gray-300">
            <li>✓ Git & GitHub</li>
            <li>✓ Docker</li>
            <li>✓ Vercel</li>
            <li>✓ UI/UX</li>
            <li>✓ SEO</li>
          </ul>
        </SkillCard>
      </div>
    </section>

    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <h2 class="text-3xl font-bold mb-12 text-center gradient-text">Experience</h2>
      <div class="space-y-8">
        <ExperienceCard title="Senior Developer" company="Tech Company" period="2022 - Present" description="Leading frontend development for SaaS products" />
        <ExperienceCard title="Full Stack Developer" company="Web Agency" period="2020 - 2022" description="Built web applications with Vue and FastAPI" />
        <ExperienceCard title="Junior Developer" company="Startup" period="2019 - 2020" description="Started web development journey" />
      </div>
    </section>
  </div>
</template>

<script>
import SkillCard from '../components/SkillCard.vue'
import ExperienceCard from '../components/ExperienceCard.vue'
export default {
  name: 'About',
  components: { SkillCard, ExperienceCard }
}
</script>