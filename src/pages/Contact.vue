<template>
  <div class="min-h-screen">
    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-20">
      <h1 class="text-5xl font-bold gradient-text mb-8 text-center">Get In Touch</h1>
      <p class="text-lg text-gray-600 dark:text-gray-300 max-w-3xl mx-auto text-center mb-16">
        Have a project? Let's work together to create something amazing.
      </p>
    </section>

    <section class="max-w-6xl mx-auto px-4 sm:px-6 lg:px-8 py-16">
      <div class="grid md:grid-cols-2 gap-12">
        <div class="glass-card p-8">
          <h2 class="text-2xl font-bold mb-6">Send Message</h2>
          <form @submit.prevent="handleSubmit" class="space-y-4">
            <div>
              <label class="block text-sm font-medium mb-2">Name</label>
              <input v-model="form.name" type="text" placeholder="Your name" class="glass-input w-full" required>
            </div>
            <div>
              <label class="block text-sm font-medium mb-2">Email</label>
              <input v-model="form.email" type="email" placeholder="your@email.com" class="glass-input w-full" required>
            </div>
            <div>
              <label class="block text-sm font-medium mb-2">Subject</label>
              <input v-model="form.subject" type="text" placeholder="Subject" class="glass-input w-full" required>
            </div>
            <div>
              <label class="block text-sm font-medium mb-2">Message</label>
              <textarea v-model="form.message" placeholder="Message..." rows="5" class="glass-input w-full resize-none" required></textarea>
            </div>
            <button type="submit" class="glass-button w-full">{{ form.submitted ? '✓ Sent!' : 'Send' }}</button>
          </form>
        </div>

        <div class="space-y-8">
          <ContactMethod icon="📧" title="Email" value="your.email@example.com" href="mailto:your.email@example.com" />
          <ContactMethod icon="📱" title="Phone" value="+1 (555) 123-4567" href="tel:+15551234567" />
          <ContactMethod icon="📍" title="Location" value="City, Country" href="#" />
          
          <div class="glass-card p-8">
            <h3 class="text-xl font-bold mb-4">Follow</h3>
            <div class="flex gap-4">
              <a href="https://github.com" target="_blank" class="p-3 bg-white/20 dark:bg-gray-800/40 rounded-lg hover:bg-white/40 transition">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M12 0c-6.626 0-12 5.373-12 12 0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23.957-.266 1.983-.399 3.003-.404 1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v 3.293c0 .319.192.694.801.576 4.765-1.589 8.199-6.086 8.199-11.386 0-6.627-5.373-12-12-12z"/></svg>
              </a>
              <a href="https://linkedin.com" target="_blank" class="p-3 bg-white/20 dark:bg-gray-800/40 rounded-lg hover:bg-white/40 transition">
                <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 24 24"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.475-2.236-1.986-2.236-1.081 0-1.722.722-2.004 1.418-.103.249-.129.597-.129.946v5.441h-3.554s.035-8.087 0-8.927h3.554v1.26c.392-.604 1.092-1.465 2.655-1.465 1.94 0 3.395 1.268 3.395 3.995v5.137zM5.337 8.855c-1.144 0-1.915-.759-1.915-1.71 0-.951.77-1.71 1.916-1.71.717.002 1.415.361 1.915 1.71 0 .951-.771 1.71-1.916 1.71zm1.946 11.597H3.392V9.525h3.891v10.927zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.225 0z"/></svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { reactive } from 'vue'
import ContactMethod from '../components/ContactMethod.vue'
export default {
  name: 'Contact',
  components: { ContactMethod },
  setup() {
    const form = reactive({ name: '', email: '', subject: '', message: '', submitted: false })
    const handleSubmit = async () => {
      form.submitted = true
      setTimeout(() => {
        form.submitted = false
        form.name = form.email = form.subject = form.message = ''
      }, 2000)
    }
    return { form, handleSubmit }
  }
}
</script>