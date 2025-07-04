import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Crop from '../views/Crop.vue'
import Customize from '../views/Customize.vue'
import BackgroundGallery from '../views/Gallery.vue'
import FAQ from '../views/FAQ.vue'
import Payment from '../views/Payment.vue'
import Profile from '../views/Profile.vue'

const routes = [
  { path: '/', component: Home },
  { path: '/crop', component: Crop },
  { path: '/customize', component: Customize },
  { path: '/gallery', component: BackgroundGallery },
  { path: '/faq', component: FAQ },
  { path: '/payment', component: Payment },
  { path: '/profile', component: Profile }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router



