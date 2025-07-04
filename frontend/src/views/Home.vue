<template>
  <section class="pt-36 px-6 text-white text-center max-w-6xl mx-auto relative z-10 pb-32">
    <div class="absolute top-[-200px] left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-pink-500/20 rounded-full blur-[150px] opacity-50 pointer-events-none z-0"></div>

    <div class="mb-20 animate-fade-in relative z-10">
      <h1 class="text-5xl md:text-6xl font-extrabold leading-tight mb-6 tracking-tight">
        Remove Backgrounds with <span class="text-pink-400 drop-shadow-md">AI Precision</span>
      </h1>
      <p class="text-lg md:text-xl text-gray-300 max-w-3xl mx-auto">
        NeuroCut uses cutting-edge deep learning to remove image backgrounds in seconds — beautifully and privately.
      </p>
      <router-link
        to="/crop"
        class="mt-10 inline-block px-7 py-3 bg-gradient-to-r from-pink-500 to-fuchsia-600 hover:brightness-110 transition rounded-xl text-white font-semibold shadow-lg"
      >
        ✂️ Try It Now
      </router-link>

      <div class="mt-14 animate-fade-in-slow">
        <video
          class="w-full max-w-4xl mx-auto rounded-2xl shadow-2xl ring-1 ring-white/10"
          :src="videoSrc"
          autoplay
          muted
          loop
          playsinline
        />
      </div>
    </div>

<div class="mt-32 text-center animate-fade-in-slow">
  <h2 class="text-4xl font-bold mb-6">Why NeuroCut?</h2>
  <p class="text-gray-300 max-w-3xl mx-auto mb-14 text-lg leading-relaxed">
    Whether you're a designer, photographer, or online seller — NeuroCut gives you pro-level results with zero hassle.
    Every click saves you time, and every background looks professionally done.
    In addition to removing backgrounds with AI precision, you can also customize your images with colors, gradients, or backgrounds from our Background Gallery.
  </p>

  <div class="grid md:grid-cols-3 gap-10 text-left">
    <div class="neon-box p-6 space-y-3">
      <h3 class="text-xl font-semibold text-pink-400">🤖 Ultra-Precise AI Detection</h3>
      <p class="text-base text-gray-300 leading-relaxed">
        NeuroCut uses U-2-Net to detect even the most subtle image edges — from wispy hair strands to transparent shadows — with incredible precision.
      </p>
    </div>
    <div class="neon-box p-6 space-y-3">
      <h3 class="text-xl font-semibold text-pink-400">⚡ Instant Processing</h3>
      <p class="text-base text-gray-300 leading-relaxed">
        Get results in under 2 seconds with no compromise on quality. Whether you're on a deadline or batch-editing, speed is always on your side.
      </p>
    </div>
    <div class="neon-box p-6 space-y-3">
      <h3 class="text-xl font-semibold text-pink-400">🎨 Image Customization</h3>
      <p class="text-base text-gray-300 leading-relaxed">
        After removing the background, you can easily add color, gradients, or even use our Background Gallery to select a beautiful background for your image.
      </p>
    </div>
  </div>

  <div class="mt-14 text-center">
    <router-link
      to="/gallery"
      class="inline-block px-7 py-3 bg-gradient-to-r from-pink-500 to-fuchsia-600 hover:brightness-110 transition rounded-xl text-white font-semibold shadow-lg"
    >
      🎨 Explore Background Gallery
    </router-link>
  </div>
</div>


    <div class="mt-32 text-center animate-fade-in-slow">
      <h2 class="text-4xl font-bold mb-6">What Our Users Say</h2>
      <p class="text-gray-300 max-w-3xl mx-auto mb-16 text-lg">
        Trusted by 10,000+ creators, studios, and online brands around the world.
      </p>

      <div class="grid md:grid-cols-3 gap-10 text-left">
        <div class="neon-box p-8 flex flex-col items-center text-center space-y-4">
          <img src="@/assets/users/dita.jpg" alt="Dita" class="w-24 h-24 rounded-full object-cover ring-2 ring-pink-400 shadow-lg" />
          <p class="italic text-base leading-relaxed text-gray-300">
            “I’m amazed by how fast and clean the results are. I use NeuroCut for product photos and it saves me hours of editing every week. It’s seriously a game changer for my business workflow.”
          </p>
          <p class="text-pink-400 font-semibold">— Dita, Online Store Owner</p>
        </div>

        <div class="neon-box p-8 flex flex-col items-center text-center space-y-4">
          <img src="@/assets/users/alex.jpg" alt="Alex" class="w-24 h-24 rounded-full object-cover ring-2 ring-pink-400 shadow-lg" />
          <p class="italic text-base leading-relaxed text-gray-300">
            “I used to spend hours manually masking hair in Photoshop. With NeuroCut, I just upload and it's done instantly. It’s seriously incredible and saves me a ton of time for client work.”
          </p>
          <p class="text-pink-400 font-semibold">— Alex, Freelance Editor</p>
        </div>

        <div class="neon-box p-8 flex flex-col items-center text-center space-y-4">
          <img src="@/assets/users/rani.jpg" alt="Rani" class="w-24 h-24 rounded-full object-cover ring-2 ring-pink-400 shadow-lg" />
          <p class="italic text-base leading-relaxed text-gray-300">
            “This tool just works. It’s fast, the UI is beautiful, and the results look professional. I’ve recommended NeuroCut to every content creator and editor I know.”
          </p>
          <p class="text-pink-400 font-semibold">— Rani, YouTube Content Creator</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import videoSrc from '@/assets/videoneuro.mp4'
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

.animate-fade-in {
  animation: fade-in 0.8s ease-out forwards;
}

.animate-fade-in-slow {
  animation: fade-in 1.3s ease-out forwards;
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
