<template>
  <nav class="fixed top-0 inset-x-0 z-50 backdrop-blur-xl bg-white/5 border-b border-white/10 shadow-md">
    <div class="w-full mx-auto px-6 md:px-8 py-2 flex items-center justify-between min-h-[64px]">
      <div class="flex items-center space-x-1">
        <img
          src="@/assets/neurocut.png"
          alt="NeuroCut Logo"
          class="w-14 h-14 object-contain"
        />
        <h1 class="text-3xl sm:text-3xl font-extrabold tracking-tight leading-none flex items-center">
          <span class="text-white">Neuro</span><span class="text-pink-400 drop-shadow-md">Cut</span>
        </h1>
      </div>

      <div class="hidden md:flex space-x-8 text-sm font-medium tracking-wide items-center">
        <router-link
          to="/"
          exact
          class="relative group transition"
          active-class="text-pink-400"
        >
          <span class="transition group-hover:text-pink-400">Home</span>
        </router-link>
        <router-link
          to="/crop"
          exact
          class="relative group transition"
          active-class="text-pink-400"
        >
          <span class="transition group-hover:text-pink-400">Crop</span>
        </router-link>
        <router-link
          to="/customize"
          exact
          class="relative group transition"
          active-class="text-pink-400"
        >
          <span class="transition group-hover:text-pink-400">Customize</span>
        </router-link>
        <router-link
          to="/gallery"
          exact
          class="relative group transition"
          active-class="text-pink-400"
        >
          <span class="transition group-hover:text-pink-400">Background Gallery</span>
        </router-link>
        <router-link
          to="/faq"
          exact
          class="relative group transition"
          active-class="text-pink-400"
        >
          <span class="transition group-hover:text-pink-400">FAQ</span>
        </router-link>

        <router-link
          to="/payment"
          exact
          class="relative group transition"
          active-class="text-pink-400"
        >
          <span class="transition group-hover:text-pink-400">Payment</span>
        </router-link>

        <div v-if="isLoggedIn" class="relative group cursor-pointer">
          <router-link to="/profile" class="relative">
            <img
              :src="userProfileImage"
              alt="Profile Image"
              class="w-10 h-10 rounded-full object-cover border-2 border-white/50 hover:border-pink-400 transition-all"
            />
          </router-link>
        </div>
      </div>

      <div class="md:hidden flex items-center">
        <button @click="toggleMobileMenu" class="text-white focus:outline-none">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-8 h-8">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
          </svg>
        </button>
      </div>
    </div>

    <div v-if="mobileMenuOpen" class="md:hidden absolute top-16 left-0 w-full bg-white/20 backdrop-blur-md p-4 space-y-4">
      <router-link
        to="/"
        exact
        class="block text-white text-lg transition hover:text-pink-400"
        @click="closeMobileMenu"
      >
        Home
      </router-link>
      <router-link
        to="/crop"
        exact
        class="block text-white text-lg transition hover:text-pink-400"
        @click="closeMobileMenu"
      >
        Crop
      </router-link>
      <router-link
        to="/customize"
        exact
        class="block text-white text-lg transition hover:text-pink-400"
        @click="closeMobileMenu"
      >
        Customize
      </router-link>
      <router-link
        to="/gallery"
        exact
        class="block text-white text-lg transition hover:text-pink-400"
        @click="closeMobileMenu"
      >
        Background Gallery
      </router-link>
      <router-link
        to="/faq"
        exact
        class="block text-white text-lg transition hover:text-pink-400"
        @click="closeMobileMenu"
      >
        FAQ
      </router-link>
      <router-link
        to="/payment"
        exact
        class="block text-white text-lg transition hover:text-pink-400"
        @click="closeMobileMenu"
      >
        Payment
      </router-link>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'

const mobileMenuOpen = ref(false)
const isLoggedIn = ref(true)
const userProfileImage = ref("https://t3.ftcdn.net/jpg/04/97/66/28/360_F_497662812_7rGW6PMBJR9AbrKcGgN5S1luXYTjH92i.jpg") // Replace with actual user's profile image URL

function toggleMobileMenu() {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

function closeMobileMenu() {
  mobileMenuOpen.value = false
}
</script>

<style scoped>
nav {
  z-index: 1000;
}

.navbar-links {
  display: flex;
  align-items: center;
}

.navbar-links a {
  margin: 0 16px;
}

.md:hidden {
  display: block;
}

img {
  cursor: pointer;
  transition: all 0.3s ease;
}

img:hover {
  opacity: 0.8;
}
</style>
