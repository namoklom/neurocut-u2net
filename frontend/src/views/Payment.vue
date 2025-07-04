<template>
  <section class="fade-in-page pt-36 px-6 text-white text-center max-w-6xl mx-auto relative z-10 pb-32">
    <div class="absolute top-[-200px] left-1/2 -translate-x-1/2 w-[800px] h-[800px] bg-pink-500/20 rounded-full blur-[150px] opacity-50 pointer-events-none z-0"></div>

    <div class="mb-16">
      <h1 class="text-5xl md:text-6xl font-extrabold mb-6 tracking-tight animate-fade-in">
        💳 Choose Your Plan
      </h1>
      <p class="text-lg md:text-xl text-gray-300 max-w-3xl mx-auto animate-fade-in">
        Get access to premium features and enhance your image editing experience. Choose the plan that best suits your needs.
      </p>
    </div>

    <div class="grid md:grid-cols-2 gap-12 mb-16 animate-fade-in">
      <div class="neon-box p-8 space-y-6 rounded-2xl border-2 border-white/10 hover:border-pink-500 transition-all duration-300">
        <h3 class="text-3xl font-semibold text-pink-400">Free Plan</h3>
        <p class="text-lg text-gray-300">Perfect for casual users who need occasional image background removal.</p>
        <ul class="list-disc text-gray-300 space-y-4 pl-5">
          <li>5 Photos per day</li>
          <li>Standard processing speed</li>
          <li>Ads displayed</li>
          <li>No premium features</li>
        </ul>
        <div class="mt-6">
          <span class="text-4xl font-semibold text-white">Free</span>
        </div>
        <router-link
          to="/"
          class="inline-block px-8 py-3 mt-6 bg-transparent border-2 border-pink-500 text-pink-500 rounded-full text-lg font-semibold transition hover:bg-pink-500 hover:text-white"
        >
          Start for Free
        </router-link>
      </div>

      <div class="neon-box p-8 space-y-6 rounded-2xl border-2 border-white/10 hover:border-pink-500 transition-all duration-300">
        <h3 class="text-3xl font-semibold text-pink-400">Premium Plan</h3>
        <p class="text-lg text-gray-300">For power users and businesses. Unlock unlimited photos and faster processing.</p>
        <ul class="list-disc text-gray-300 space-y-4 pl-5">
          <li>Unlimited uploads</li>
          <li>Faster processing speeds</li>
          <li>Priority customer support</li>
          <li>No ads</li>
        </ul>
        <div class="mt-6">
          <span class="text-4xl font-semibold text-white">$9.99/month</span>
        </div>
        <router-link
          to="/"
          class="inline-block px-8 py-3 mt-6 bg-gradient-to-r from-pink-500 to-fuchsia-600 text-white rounded-full text-lg font-semibold transition hover:bg-pink-700"
        >
          Get Started
        </router-link>
      </div>
    </div>

    <div class="space-y-12 mb-16 animate-fade-in">
      <h2 class="text-3xl font-semibold text-pink-400 mb-6">Compare Plans</h2>
      <div class="overflow-x-auto bg-white/10 backdrop-blur-md rounded-xl p-8">
        <table class="table-auto w-full text-lg text-gray-300 border-separate border-spacing-0">
          <thead>
            <tr class="text-left bg-pink-500 text-white">
              <th class="px-6 py-4 font-semibold">Feature</th>
              <th class="px-6 py-4 font-semibold">Free Plan</th>
              <th class="px-6 py-4 font-semibold">Premium Plan</th>
            </tr>
          </thead>
          <tbody>
            <tr class="border-b border-gray-600 hover:bg-gray-700">
              <td class="px-6 py-4 font-medium">Photos per Day</td>
              <td class="px-6 py-4">5</td>
              <td class="px-6 py-4">Unlimited</td>
            </tr>
            <tr class="border-b border-gray-600 hover:bg-gray-700">
              <td class="px-6 py-4 font-medium">Processing Speed</td>
              <td class="px-6 py-4">Standard</td>
              <td class="px-6 py-4">Fast</td>
            </tr>
            <tr class="border-b border-gray-600 hover:bg-gray-700">
              <td class="px-6 py-4 font-medium">Ads</td>
              <td class="px-6 py-4">Yes</td>
              <td class="px-6 py-4">No</td>
            </tr>
            <tr class="border-b border-gray-600 hover:bg-gray-700">
              <td class="px-6 py-4 font-medium">Priority Support</td>
              <td class="px-6 py-4">No</td>
              <td class="px-6 py-4">Yes</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <div class="animate-fade-in">
      <h2 class="text-3xl font-semibold text-pink-400 mb-6">Ready to Unlock Unlimited Features?</h2>
      <p class="text-lg text-gray-300 mb-6 max-w-3xl mx-auto">
        Upgrade to the Premium Plan for faster processing, unlimited photos, and priority support. Start using NeuroCut like a pro.
      </p>
      <router-link
        to="/"
        class="inline-block px-8 py-3 bg-gradient-to-r from-pink-500 to-fuchsia-600 text-white rounded-full text-lg font-semibold transition hover:bg-pink-700"
      >
        Get Premium Now
      </router-link>
    </div>
  </section>
</template>

<script setup>
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

table {
  border-collapse: collapse;
}

th, td {
  padding: 12px 15px;
  text-align: left;
}

tr:nth-child(even) {
  background-color: rgba(255, 255, 255, 0.05);
}
</style>
