<template>
  <section class="fade-in-page pt-36 px-6 text-white max-w-6xl mx-auto relative z-10 pb-32">
    <div class="bg-white/10 rounded-xl backdrop-blur-md p-8">
      <div class="flex flex-col items-center space-y-4">
        <div class="w-32 h-32 rounded-full overflow-hidden bg-gray-200">
          <img :src="user.profileImage" alt="User Profile Image" class="w-full h-full object-cover" />
        </div>

        <div class="text-center">
          <h2 class="text-3xl font-semibold text-pink-400">{{ user.name }}</h2>
          <p class="text-lg text-gray-300">{{ user.email }}</p>
        </div>
      </div>

      <div class="mt-12 space-y-6">
        <div class="space-y-2">
          <h3 class="text-xl font-semibold text-pink-400">Personal Information</h3>
          <div class="flex justify-between">
            <p class="text-lg text-gray-300">Name:</p>
            <p class="text-lg text-gray-100">{{ user.name }}</p>
          </div>
          <div class="flex justify-between">
            <p class="text-lg text-gray-300">Email:</p>
            <p class="text-lg text-gray-100">{{ user.email }}</p>
          </div>
          <div class="flex justify-between">
            <p class="text-lg text-gray-300">Phone:</p>
            <p class="text-lg text-gray-100">{{ user.phone || 'Not Provided' }}</p>
          </div>
        </div>

        <div class="mt-6">
          <h3 class="text-xl font-semibold text-pink-400">Change Profile Image</h3>
          <div class="flex items-center space-x-4">
            <label class="file-input-container">
              <input
                type="file"
                @change="handleFileChange"
                class="hidden"
                accept="image/*"
              />
              <span class="px-6 py-2 bg-pink-500 text-white rounded-full cursor-pointer hover:bg-pink-600 transition">
                Choose File
              </span>
            </label>
            <button
              @click="uploadProfileImage"
              class="px-6 py-2 bg-pink-500 text-white rounded-full hover:bg-pink-600 transition"
            >
              Upload Image
            </button>
          </div>
        </div>

        <div class="mt-6">
          <h3 class="text-xl font-semibold text-pink-400">Account Status</h3>
          <div class="flex justify-between">
            <p class="text-lg text-gray-300">Subscription:</p>
            <p class="text-lg text-gray-100">{{ user.subscription || 'Free Plan' }}</p>
          </div>
          <div class="flex justify-between">
            <p class="text-lg text-gray-300">Status:</p>
            <p class="text-lg text-gray-100">{{ user.status || 'Active' }}</p>
          </div>
        </div>

        <div class="mt-12 text-center">
          <router-link
            to="/update-profile"
            class="px-8 py-3 bg-gradient-to-r from-pink-500 to-fuchsia-600 text-white rounded-full text-lg font-semibold transition hover:bg-pink-700"
          >
            Update Profile
          </router-link>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const user = ref({
  name: 'Heri Arnanta',
  email: 'heri.arnanta@gmail.com',
  phone: '+62 721-1029-6713',
  profileImage: 'https://t3.ftcdn.net/jpg/04/97/66/28/360_F_497662812_7rGW6PMBJR9AbrKcGgN5S1luXYTjH92i.jpg', // Default image URL
  subscription: 'Premium',
  status: 'Active',
})

function handleFileChange(event) {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onloadend = () => {
      user.value.profileImage = reader.result
    }
    reader.readAsDataURL(file)
  }
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

.file-input-container {
  display: inline-block;
}

.file-input-container input[type="file"] {
  display: none;
}

.file-input-container span {
  display: inline-block;
  padding: 0.5rem 1.5rem;
  background-color: #f472b6;
  color: white;
  border-radius: 9999px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.file-input-container span:hover {
  background-color: #ec4899;
}

.file-input {
  padding: 0.5rem;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 0.5rem;
  color: white;
  background-color: transparent;
  cursor: pointer;
}

.file-input:hover {
  border-color: rgba(255, 255, 255, 0.6);
}

button {
  cursor: pointer;
  transition: all 0.3s ease;
}

button:hover {
  opacity: 0.8;
}
</style>
