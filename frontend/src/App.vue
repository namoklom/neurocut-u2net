<template>
  <div class="flex flex-col min-h-screen relative overflow-x-hidden overflow-y-auto">
    <!-- Aurora Background Layer -->
    <div class="fixed top-0 left-0 w-full h-full -z-10 pointer-events-none aurora-layer"></div>

    <!-- Navbar -->
    <Navbar />

    <!-- Main Content -->
    <main class="flex-1 relative z-10 pb-15">
      <router-view />
    </main>

    <!-- Footer -->
    <Footer />
  </div>
</template>

<script setup>
import Navbar from './components/Navbar.vue'
import Footer from './components/Footer.vue'
</script>

<style>
/* Custom pink-themed scrollbar */
::-webkit-scrollbar {
  width: 12px;
  height: 12px;
}
::-webkit-scrollbar-track {
  background: transparent;
}
::-webkit-scrollbar-thumb {
  background: linear-gradient(to bottom, #f472b6, #ec4899);
  border-radius: 8px;
  border: 3px solid transparent;
  background-clip: content-box;
  transition: background 0.3s ease;
}
::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(to bottom, #fb7185, #db2777);
}

/* Firefox */
* {
  scrollbar-width: thin;
  scrollbar-color: #ec4899 transparent;
}
</style>

html {
  overflow-y: scroll;
}

body {
  margin: 0;
}