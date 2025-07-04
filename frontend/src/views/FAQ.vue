<template>
  <section class="fade-in-page pt-36 px-6 text-white text-center max-w-6xl mx-auto relative z-10 pb-32">
    <div class="mb-16">
      <h1 class="text-5xl md:text-6xl font-extrabold mb-6 tracking-tight animate-fade-in">
        🤖 Frequently Asked Questions
      </h1>
      <p class="text-lg md:text-xl text-gray-300 max-w-3xl mx-auto animate-fade-in">
        Here are some of the most common questions we receive from our users. If you have any other questions, feel free to reach out to us!
      </p>
    </div>

    <div class="max-w-4xl mx-auto space-y-6">
      <div v-for="(faq, index) in faqs" :key="index" class="neon-box p-6 space-y-3">
        <button @click="toggle(index)" class="w-full text-left text-lg font-semibold flex justify-between items-center">
          <span>{{ faq.question }}</span>
          <span :class="{'rotate-180': openIndex === index}" class="transition-transform duration-300">&#x25BC;</span>
        </button>
        <div v-if="openIndex === index" class="mt-4 text-gray-300 text-base">
          <p>{{ faq.answer }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const faqs = [
  { 
    question: 'What is NeuroCut?', 
    answer: `NeuroCut is a powerful AI-driven platform designed to simplify the image editing process. By using deep learning algorithms, particularly U-2-Net, we can automatically detect and remove backgrounds from your images in a matter of seconds. This tool is particularly useful for photographers, e-commerce owners, designers, and anyone who regularly needs high-quality background removal. Whether you're preparing product images, designing creatives, or just tidying up your photos, NeuroCut ensures that the background removal process is both fast and precise.`
  },
  { 
    question: 'How does the background removal process work?', 
    answer: `At the core of NeuroCut is the U-2-Net deep learning model, which has been trained on a vast dataset of images to detect and separate the foreground from the background with impressive accuracy. When you upload an image, the model analyzes it pixel by pixel to understand the boundaries of the object in the image. Once identified, the background is removed, leaving you with just the subject of the image. This process is fully automated and occurs in the cloud, so you don’t need to worry about software installation or complex settings. Just upload your image, and the AI handles the rest.`
  },
  { 
    question: 'Can I upload multiple images at once?', 
    answer: `Currently, NeuroCut supports the upload of one image at a time. This is to ensure that each image receives the highest level of attention and accuracy during the background removal process. However, we understand that users often need to process multiple images, so we're actively working on implementing batch processing. Stay tuned for future updates, as we'll be adding this feature to support users who need to process images in bulk.`
  },
  { 
    question: 'Is my image data safe?', 
    answer: `Absolutely. We prioritize your privacy and data security. Your images are uploaded and processed in an encrypted environment, ensuring that your data is safe from unauthorized access. We adhere to strict data protection regulations and ensure that your images are not stored after processing. Once the background removal is completed, your image is immediately deleted from our servers. This ensures that your data is only used for the purpose it was intended and is discarded once no longer needed.`
  },
  { 
    question: 'Can I customize the background after removing it?', 
    answer: `Yes! After the background removal, you have full control over what appears behind your image. You can choose from a variety of customization options, including solid colors, gradients, or even custom backgrounds that you can upload yourself. Additionally, you can explore our Background Gallery, which features a curated selection of beautiful and professional-grade backgrounds designed to make your images stand out. This flexibility ensures that your images look exactly how you want them to, whether you're creating product images, marketing materials, or simply having fun with your photos.`
  },
  { 
    question: 'Is there a free version of NeuroCut?', 
    answer: `Yes, NeuroCut offers a free version that provides users with the core functionality of background removal. This includes single-image uploads and basic background processing. While the free version is great for users with occasional needs, we also offer a premium version that unlocks advanced features like faster processing speeds, the ability to handle larger image resolutions, and access to premium customization options, including more complex background effects and exclusive backgrounds. The premium version is ideal for professional users and businesses looking for faster turnaround times and higher quality output.`
  },
  { 
    question: 'How do I get started?', 
    answer: `Getting started with NeuroCut is incredibly easy! Simply visit our website and click on the 'Upload Image' button to begin. Once you've uploaded your image, our AI will automatically start processing it to remove the background. After the process is complete, you can download the result or apply additional customizations, such as adding colors or selecting from our Background Gallery. If you’re unsure how to get started, we also provide tutorials and FAQs on our website to guide you through the process step by step.`
  },
  { 
    question: 'What kind of images work best with NeuroCut?', 
    answer: `NeuroCut works best with images that have clear subjects and distinct backgrounds. The AI model is designed to identify contrast between the subject and the background, so images with sharp edges, clear lighting, and well-defined boundaries will yield the best results. For example, images of people, products, or objects with a solid background or clear distinction between foreground and background are ideal. If your image contains a complex background (such as hair, fine details, or a cluttered scene), the AI might struggle in some areas. However, we are constantly improving our model, and future updates will enhance performance on more complex images.`
  },
  { 
    question: 'Can I use NeuroCut for commercial purposes?', 
    answer: `Yes, once you’ve removed the background and customized the image, you are free to use it for both personal and commercial purposes. This includes using the image in marketing materials, advertisements, product listings, social media, websites, or any other commercial application. We want to empower businesses, marketers, and entrepreneurs to create stunning visuals without worrying about copyright issues or image restrictions. You can freely use your customized images in your business and marketing materials without any licensing concerns.`
  },
  { 
    question: 'How can I contact support?', 
    answer: `If you need assistance or have any questions, our support team is here to help! You can contact us at support@neurocut.com, and our dedicated support staff will respond to your inquiry as quickly as possible. We offer 24/7 support, ensuring that no matter when you need help, we're available. Additionally, we have a comprehensive Help Center on our website that includes guides, troubleshooting tips, and common FAQs to assist you in resolving any issues on your own.`
  }
]

const openIndex = ref(null)

const toggle = (index) => {
  openIndex.value = openIndex.value === index ? null : index
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

button {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.5rem;
  font-size: 1.125rem;
  background-color: transparent;
  border: none;
  color: white;
  text-align: left;
  cursor: pointer;
}

button span {
  font-weight: bold;
}

button:focus {
  outline: none;
}
</style>
