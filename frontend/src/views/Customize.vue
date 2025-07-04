<template>
  <section class="fade-in-page pt-36 px-6 text-white text-center max-w-6xl mx-auto relative z-10 pb-32">
    <div class="absolute top-[-200px] left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-pink-500/20 rounded-full blur-[150px] opacity-50 pointer-events-none z-0"></div>

    <div class="mb-16">
      <h1 class="text-5xl md:text-6xl font-extrabold mb-6 tracking-tight animate-fade-in">
        🎨 Customize <span class="text-pink-400 drop-shadow-md">Your Background</span>
      </h1>
      <p class="text-lg md:text-xl text-gray-300 max-w-3xl mx-auto animate-fade-in">
        Upload your cropped image and choose between solid color, gradient, or background image.
      </p>
    </div>

    <div class="grid md:grid-cols-3 gap-8 text-left mb-20 animate-fade-in">
      <div class="neon-box p-6 space-y-3">
        <label class="block font-semibold text-sm text-pink-400">Upload Cropped Image</label>
        <input
          type="file"
          accept="image/*"
          @change="onImageUpload"
          class="block w-full text-sm text-gray-300 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-pink-500 file:text-white hover:file:bg-pink-600 cursor-pointer"
        />
      </div>

      <div class="neon-box p-6 space-y-3">
        <label class="block font-semibold text-sm text-pink-400">Background Color</label>
        <input
          type="color"
          v-model="bgColor"
          class="w-full h-12 rounded-lg cursor-pointer border-2 border-white/20"
        />
      </div>

      <div class="neon-box p-6 space-y-3 relative z-50">
        <label class="block font-semibold text-sm text-pink-400">Gradient Preset</label>
        <div class="relative">
          <button
            @click="toggleDropdown"
            class="w-full text-left px-4 py-2 rounded-lg border border-white/20 bg-gradient-to-r from-pink-500 via-fuchsia-600 to-purple-700 text-white font-medium shadow-md"
          >
            {{ selectedGradientName || 'Select Gradient' }}
          </button>

          <transition name="fade">
            <div
              v-if="showDropdown"
              class="absolute top-full left-0 mt-2 w-full rounded-xl shadow-xl border border-white/10 z-[60] overflow-hidden backdrop-blur-xl bg-white/10"
            >
              <div
                v-for="(gradient, name) in gradientList"
                :key="name"
                @click="selectGradient(name)"
                class="px-4 py-3 cursor-pointer hover:brightness-110 text-white transition-all"
                :style="{ background: gradient.gradient }"
              >
                {{ name }}
              </div>
            </div>
          </transition>
        </div>
      </div>
    </div>

    <div class="neon-box p-6 mb-16 text-left relative z-10 animate-fade-in">
      <label class="block font-semibold text-sm text-pink-400 mb-2">Background Image (optional)</label>
      <input
        type="file"
        accept="image/*"
        @change="onBackgroundUpload"
        class="block w-full text-sm text-gray-300 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-pink-500 file:text-white hover:file:bg-pink-600 cursor-pointer"
      />
    </div>

    <div class="relative w-full max-w-3xl mx-auto animate-fade-in">
      <canvas
        ref="canvasRef"
        width="1280"
        height="720"
        class="rounded-2xl overflow-hidden shadow-2xl ring-1 ring-white/10 w-full aspect-video bg-black"
      ></canvas>

      <div v-if="uploadedImage || bgImage" class="absolute bottom-4 right-4">
        <a
          :href="canvasDataUrl"
          download="customized_neurocut.png"
          class="px-5 py-2 bg-gradient-to-r from-pink-500 to-fuchsia-600 text-white rounded-full shadow-lg font-semibold hover:brightness-110 transition"
        >
          Download Result
        </a>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, watch, nextTick, onMounted } from 'vue'

const uploadedImage = ref(null)
const bgImage = ref(null)
const bgColor = ref('#000000')
const selectedGradient = ref({})
const selectedGradientName = ref('')
const showDropdown = ref(false)
const canvasRef = ref(null)
const canvasDataUrl = ref(null)

const gradientList = {
  Sunset: { colors: ['#ff758c', '#ff7eb3'], gradient: 'linear-gradient(to right, #ff758c, #ff7eb3)' },
  Ocean: { colors: ['#43cea2', '#185a9d'], gradient: 'linear-gradient(to right, #43cea2, #185a9d)' },
  NeonPink: { colors: ['#ec4899', '#8b5cf6'], gradient: 'linear-gradient(to right, #ec4899, #8b5cf6)' },
  BluePurple: { colors: ['#3b82f6', '#a855f7'], gradient: 'linear-gradient(to right, #3b82f6, #a855f7)' },
}

const toggleDropdown = () => (showDropdown.value = !showDropdown.value)
const selectGradient = (name) => {
  selectedGradientName.value = name
  selectedGradient.value = gradientList[name]
  showDropdown.value = false
  nextTick(drawCanvas)
}

const onImageUpload = (e) => {
  const file = e.target.files[0]
  if (file) {
    uploadedImage.value = URL.createObjectURL(file)
    nextTick(drawCanvas)
  }
}

const onBackgroundUpload = (e) => {
  const file = e.target.files[0]
  if (file) {
    bgImage.value = URL.createObjectURL(file)
    nextTick(drawCanvas)
  }
}

const drawCanvas = async () => {
  const canvas = canvasRef.value
  const ctx = canvas.getContext('2d')
  ctx.clearRect(0, 0, canvas.width, canvas.height)

  if (bgImage.value) {
    const bg = new Image()
    bg.crossOrigin = 'anonymous'
    bg.src = bgImage.value
    await new Promise((resolve) => (bg.onload = resolve))
    ctx.drawImage(bg, 0, 0, canvas.width, canvas.height)
  } else if (selectedGradient.value.colors) {
    const gradient = ctx.createLinearGradient(0, 0, canvas.width, 0)
    gradient.addColorStop(0, selectedGradient.value.colors[0])
    gradient.addColorStop(1, selectedGradient.value.colors[1])
    ctx.fillStyle = gradient
    ctx.fillRect(0, 0, canvas.width, canvas.height)
  } else {
    ctx.fillStyle = bgColor.value
    ctx.fillRect(0, 0, canvas.width, canvas.height)
  }

  if (uploadedImage.value) {
    const img = new Image()
    img.crossOrigin = 'anonymous'
    img.src = uploadedImage.value
    await new Promise((resolve) => (img.onload = resolve))
    ctx.drawImage(img, 0, 0, canvas.width, canvas.height)
  }

  canvasDataUrl.value = canvas.toDataURL('image/png')
}

watch(bgImage, () => {
  if (bgImage.value) {
    const img = new Image()
    img.src = bgImage.value
    img.onload = () => {
      drawCanvas()
    }
  }
})

watch([uploadedImage, selectedGradient, bgColor], () => {
  nextTick(drawCanvas)
})

onMounted(() => {
  const savedBg = localStorage.getItem('selectedGalleryBackground')
  if (savedBg) {
    const img = new Image()
    img.src = savedBg
    img.onload = () => {
      bgImage.value = savedBg
      localStorage.removeItem('selectedGalleryBackground')
      drawCanvas()
    }
  }
})
</script>

<style scoped>
.fade-in-page {
  animation: fade-in 1.2s ease-in-out both;
}
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
.neon-box {
  background-color: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 1rem;
  backdrop-filter: blur(12px);
  box-shadow: 0 0 15px rgba(236, 72, 153, 0.25),
              0 0 30px rgba(168, 85, 247, 0.15);
  transition: box-shadow 0.3s ease, transform 0.3s ease;
}
.neon-box:hover {
  box-shadow: 0 0 20px rgba(236, 72, 153, 0.4),
              0 0 40px rgba(168, 85, 247, 0.3),
              0 0 80px rgba(236, 72, 153, 0.2);
  transform: translateY(-4px);
}
</style>
