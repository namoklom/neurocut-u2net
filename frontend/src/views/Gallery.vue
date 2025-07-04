<template>
  <section class="fade-in-page pt-36 pb-32 px-6 max-w-6xl mx-auto text-white relative z-10">
    <div class="absolute top-[-200px] left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-purple-500/20 rounded-full blur-[150px] opacity-50 pointer-events-none z-0"></div>

    <div class="text-center mb-16">
      <h1 class="text-5xl md:text-6xl font-extrabold mb-4 animate-fade-in">
        🖼️ Background <span class="text-pink-400 drop-shadow-md">Gallery</span>
      </h1>
      <p class="text-lg md:text-xl text-gray-300 max-w-3xl mx-auto animate-fade-in">
        Choose from beautiful sample backgrounds to enhance your final image.
      </p>
    </div>

    <div class="grid sm:grid-cols-2 md:grid-cols-3 gap-8 animate-fade-in">
      <div
        v-for="(bg, index) in backgrounds"
        :key="index"
        class="neon-box overflow-hidden rounded-2xl relative group hover:scale-105 transition duration-300"
      >
        <img
          :src="bg.url"
          :alt="`Background ${index + 1}`"
          class="w-full h-48 object-cover transition duration-300 group-hover:brightness-110"
        />
        <div class="absolute inset-0 bg-black/30 flex items-center justify-center opacity-0 group-hover:opacity-100 transition">
          <button
            @click="selectBackground(bg.url)"
            class="px-5 py-2 bg-gradient-to-r from-pink-500 to-fuchsia-600 text-white rounded-full font-semibold shadow-lg hover:brightness-110"
          >
            Use Background
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const backgrounds = [
  { url: 'https://plus.unsplash.com/premium_photo-1711434824963-ca894373272e?q=80&w=715&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://plus.unsplash.com/premium_photo-1673697239981-389164b7b87f?q=80&w=1144&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://plus.unsplash.com/premium_vector-1697729804286-7dd6c1a04597?q=80&w=1070&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1465146344425-f00d5f5c8f07?q=80&w=1176&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1523712999610-f77fbcfc3843?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1458668383970-8ddd3927deed?q=80&w=1167&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1435224654926-ecc9f7fa028c?q=80&w=687&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1468413253725-0d5181091126?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1464802686167-b939a6910659?q=80&w=1150&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1519608487953-e999c86e7455?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1530735606451-8f5f13955328?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1677756119517-756a188d2d94?q=80&w=1150&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://plus.unsplash.com/premium_photo-1671611799147-68a4f9b3f0e1?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://plus.unsplash.com/premium_vector-1711987817831-55bfbf7200a6?q=80&w=881&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1517928260182-5688aead3066?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1529963183134-61a90db47eaf?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1518819389057-4a38c38b76d3?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1637167473291-9f8caf792ded?q=80&w=1228&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1607585011081-241d2bacb7de?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1505993597083-3bd19fb75e57?q=80&w=1175&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1546268060-2592ff93ee24?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1536540079349-3294632f1b72?q=80&w=1117&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1626315333234-d2420987740a?q=80&w=1024&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1508804052814-cd3ba865a116?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1474181487882-5abf3f0ba6c2?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1526481280693-3bfa7568e0f3?q=80&w=1171&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1562903793-3af4a5f0e3f5?q=80&w=1176&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1503614472-8c93d56e92ce?q=80&w=1111&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1473726867722-6b8a5e529d76?q=80&w=1172&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
  { url: 'https://images.unsplash.com/photo-1619441207978-3d326c46e2c9?q=80&w=1169&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D' },
]

const selectBackground = (url) => {
  localStorage.setItem('selectedGalleryBackground', url)
  router.push('/customize')
}
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
  background-color: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  box-shadow: 0 0 10px rgba(236, 72, 153, 0.2), 0 0 20px rgba(168, 85, 247, 0.1);
}
.neon-box:hover {
  box-shadow: 0 0 20px rgba(236, 72, 153, 0.4),
              0 0 30px rgba(168, 85, 247, 0.3),
              0 0 60px rgba(236, 72, 153, 0.2);
}
</style>
