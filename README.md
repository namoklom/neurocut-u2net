# 🧠 NeuroCut

NeuroCut is a powerful, AI-driven web platform designed to automatically remove image backgrounds with high precision using a pretrained U²-Net deep learning model. Leveraging advanced semantic segmentation techniques, NeuroCut is capable of isolating complex foreground subjects such as hair, shadows, and fine textures with pixel-level accuracy.

The platform is built on a robust and scalable architecture that includes a modern FastAPI backend for handling inference requests and a highly responsive Vue 3 frontend styled with Tailwind CSS. It is engineered not only to remove backgrounds in real-time but also to enable users to customize their images with solid colors, gradients, and a wide selection of backgrounds from a built-in gallery.

NeuroCut is suitable for a wide range of users, including digital designers, photographers, content creators, online sellers, and studios. It significantly reduces the manual workload involved in image editing, allowing users to achieve professional-quality results with minimal effort. Whether for product photography, social media content, or personal branding, NeuroCut provides a streamlined, privacy-respecting, and visually impactful image editing experience.

---

## ✨ Key Features

### 🧠 AI Background Removal
- Uses pretrained U²-Net to segment foreground with high detail (hair, shadows, etc).
- Handles diverse scenes: portraits, products, complex edges.

### ⚡ Real-Time Processing
- Inference speed: ~1.5–2 seconds per image (tested on CPU).
- Asynchronous FastAPI backend allows concurrent requests.

### 🎨 Image Customization Tools
- Replace background with:
  - Solid color
  - Custom gradients
  - Uploaded background image
- Fine-tune foreground scaling and positioning.

### 🖼️ Background Gallery
- Browse curated professional backgrounds by category.
- Supports filtering (e.g., minimal, abstract, corporate, nature).
- 
---

## 🧱 Tech Stack

| Layer         | Tech Stack                                 |
|---------------|---------------------------------------------|
| AI Model      | U²-Net (PyTorch)                            |
| Backend       | FastAPI, Uvicorn, Pillow, Torch             |
| Frontend      | Vue 3, Tailwind CSS, Vite                   |
| API Docs      | FastAPI AutoDocs (Swagger/OpenAPI)          |
| Auth (Planned)| JWT, OAuth2                                 |
| Payment       | Stripe Webhooks / Midtrans (planned)        |
| Deployment    | Docker, Render/Vercel (suggested targets)   |

---

## 🗂️ Folder Structure

