<template>
  <section class="pt-36 px-6 text-white text-center max-w-6xl mx-auto relative z-10 pb-32">
    <div class="absolute top-[-200px] left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-gradient-to-r from-pink-500 to-fuchsia-600 rounded-full blur-[150px] opacity-40 pointer-events-none z-0"></div>

    <div class="animate-fade-in mb-16">
      <h1 class="text-5xl md:text-6xl font-extrabold mb-6 leading-tight tracking-tight">
        ✂️ Smart Background <span class="text-pink-400 drop-shadow-md">Removal</span>
      </h1>
      <p class="text-lg md:text-xl text-gray-300 max-w-3xl mx-auto">
        Upload your image and let our AI remove the background in seconds — clean and seamless.
      </p>
    </div>

    <div class="neon-box animate-fade-in-slow p-10 md:p-16 text-left space-y-12 rounded-3xl bg-white/10 backdrop-blur-lg border border-white/20 shadow-lg">
      <div>
        <label class="block text-sm font-medium text-gray-300 mb-3">Select an image</label>
        <input
          type="file"
          accept="image/*"
          @change="handleFileChange"
          class="block w-full text-sm text-gray-300 file:mr-4 file:py-3 file:px-6 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-gradient-to-r file:from-pink-500 file:to-fuchsia-600 file:text-white hover:file:brightness-110 cursor-pointer"
        />
      </div>

      <div v-if="originalImage" class="grid md:grid-cols-2 gap-12">
        <div class="text-center relative">
          <h2 class="text-xl font-semibold text-pink-400 mb-4">Original Image</h2>
          <div class="relative rounded-2xl overflow-hidden border border-white/20">
            <img :src="originalImage" alt="Original" class="max-h-[320px] object-contain w-full" />
            <div
              v-if="loading"
              class="absolute inset-0 z-10 bg-black/30 backdrop-blur-sm flex items-center justify-center"
            >
              <div class="w-3/4 h-3/4 bg-gradient-to-r from-transparent via-white/40 to-transparent animate-shimmer rounded-xl"></div>
            </div>
          </div>
        </div>

        <div class="text-center relative">
          <h2 class="text-xl font-semibold text-pink-400 mb-4">Background Removed</h2>
          <div class="relative min-h-[320px] flex items-center justify-center border border-white/20 rounded-2xl bg-white/5 shadow-inner overflow-hidden">
            <img
              v-if="processedImage"
              :src="processedImage"
              alt="Processed"
              class="max-h-[320px] object-contain"
            />
            <p v-else class="text-sm text-gray-400 italic">No result yet</p>
          </div>

          <div v-if="processedImage" class="mt-4">
            <a
              :href="processedImage"
              download="neurocut_result.png"
              class="inline-block px-6 py-2 bg-pink-500 hover:bg-pink-600 text-white font-semibold rounded-full shadow transition"
            >
              Download Result
            </a>
          </div>
        </div>
      </div>

      <div v-if="error" class="flex justify-center items-center mt-4">
        <div class="flex items-center space-x-2 text-red-500 font-semibold bg-red-100 bg-opacity-20 rounded px-4 py-2">
          <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
          </svg>
          <span>{{ error }}</span>
        </div>
      </div>

      <div class="text-center pt-6">
        <button
          @click="submitImage"
          :disabled="!selectedFile || loading"
          class="px-10 py-3 bg-gradient-to-r from-pink-500 to-fuchsia-600 text-white rounded-full shadow-lg font-semibold hover:brightness-110 transition disabled:opacity-40 disabled:cursor-not-allowed"
        >
          ✨ Remove Background
        </button>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const selectedFile = ref(null)
const originalImage = ref(null)
const processedImage = ref(null)
const loading = ref(false)
const error = ref(null)

const handleFileChange = (e) => {
  const file = e.target.files[0]
  if (file) {
    selectedFile.value = file
    originalImage.value = URL.createObjectURL(file)
    processedImage.value = null
    error.value = null
  }
}

const submitImage = async () => {
  if (!selectedFile.value) return

  loading.value = true
  error.value = null
  processedImage.value = null

  const formData = new FormData()
  formData.append('image', selectedFile.value)

  try {
    const response = await axios.post('http://localhost:8000/remove-bg/', formData, {
      headers: { 'Content-Type': 'multipart/form-data' },
      responseType: 'blob',
    })

    const contentType = response.headers['content-type']
    if (contentType && contentType.includes('image/png')) {
      const blob = new Blob([response.data], { type: 'image/png' })
      processedImage.value = URL.createObjectURL(blob)
    } else {
      throw new Error('Server did not return an image.')
    }
  } catch (err) {
    console.error('❌ Error:', err)
    error.value = '❌ Failed to process image. Please check the server or file format.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(24px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes shimmer {
  0% {
    transform: translateX(-100%);
  }
  100% {
    transform: translateX(100%);
  }
}

.animate-fade-in {
  animation: fade-in 0.8s ease-out forwards;
}
.animate-fade-in-slow {
  animation: fade-in 1.3s ease-out forwards;
}
.animate-shimmer {
  background-image: linear-gradient(
    to right,
    transparent 0%,
    rgba(255, 255, 255, 0.4) 50%,
    transparent 100%
  );
  background-repeat: no-repeat;
  background-size: 200% 100%;
  animation: shimmer 1.5s infinite linear;
}

.neon-box {
  background-color: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1.5rem;
  backdrop-filter: blur(14px);
  box-shadow: 0 0 20px rgba(236, 72, 153, 0.3),
              0 0 40px rgba(168, 85, 247, 0.2);
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}
.neon-box:hover {
  box-shadow: 0 0 25px rgba(236, 72, 153, 0.5),
              0 0 50px rgba(168, 85, 247, 0.4),
              0 0 100px rgba(236, 72, 153, 0.3);
  transform: translateY(-6px);
}
</style>
