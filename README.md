# NeuroCut (U²-Net-Based AI Tool for Background Removal and Image Customization)

## 👤 Author

| Name            | Role              | LinkedIn                                      |
|-----------------|-------------------|-----------------------------------------------|
| Jason Emmanuel  | Full-Stack Engineer    | [linkedin.com/in/jasoneml](https://www.linkedin.com/in/jasoneml/) |

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
  
---

## 🧠 Model Initialization

At the core of NeuroCut is the **U²-Net** architecture, a powerful neural network designed for salient object detection. This model enables high-accuracy background removal even in challenging scenarios such as hair strands, transparent shadows, and detailed product edges.

The model is initialized during the FastAPI server startup. It is loaded from a pretrained `.pth` file using PyTorch and runs entirely on the server-side CPU (or GPU if available). Once loaded, it remains in memory for efficient reuse across multiple inference requests.

![image](https://github.com/user-attachments/assets/bb50cbf3-7649-420e-ae84-9f00cf4dd685)

### 🔹 Initialization Logic

- Loads `u2net.pth` weights from disk using `torch.load(...)`
- Initializes the U²-Net model from `u2net.py`
- Runs in evaluation mode: `model.eval()`
- Accepts image input (JPG/PNG), preprocesses to tensor with `torchvision.transforms`
- Returns an alpha mask for foreground segmentation (resized and post-processed to PNG)

---

## 🖥️ Frontend Overview

The frontend of **NeuroCut** is built using **Vue 3** and styled with **Tailwind CSS**, offering a highly responsive and modern user experience. The UI is designed with simplicity and performance in mind, ensuring smooth interactions across all devices and screen sizes.

### 🔹 Key Features

- **Component-Based Architecture**  
  Utilizes Vue 3's Composition API for modular and maintainable code.

- **Real-Time Feedback**  
  Instantly displays background removal and customization results.

- **Drag & Drop Support**  
  Allows users to upload images via a simple drag-and-drop interface.

- **Responsive Design**  
  Tailwind CSS ensures seamless layout across desktop, tablet, and mobile devices.

- **Interactive UI**  
  Built with Vue transitions and dynamic rendering for smooth, engaging interactions.

- **Customization Tools**  
  Users can replace the background with solid colors, gradients, or images from the gallery.

---

## 🧠 Backend Overview

The backend of **NeuroCut** is powered by **FastAPI**, a modern, asynchronous Python web framework built for high-performance REST APIs. It is responsible for handling image uploads, running AI inference, and returning the processed image data to the frontend.

### 🔹 Key Features

- **Asynchronous Processing**  
  FastAPI with Uvicorn allows for high concurrency and low-latency image processing.

- **U²-Net Integration**  
  Loads a pretrained U²-Net model using PyTorch during server startup and keeps it in memory for fast inference.

- **Image Preprocessing & Postprocessing**  
  Uses `torchvision.transforms` and `Pillow` to prepare uploaded images for segmentation and generate alpha masks.

- **REST API Endpoints**  
  Provides secure, well-defined endpoints for background removal, image upload, and customization features.

- **Scalable & Lightweight**  
  Easily deployable with Docker or directly on cloud instances, and supports both CPU and GPU environments.

- **Error Handling & Validation**  
  Implements robust request validation, file format checking, and error responses to ensure stability.
  
---

## 📱 App Overview

### Home Menu

<img width="959" alt="image" src="https://github.com/user-attachments/assets/c5ae379a-b6c8-47e5-a74a-b96219ead1c3" />


The **Home** menu of **NeuroCut** introduces the app with a clear, impactful headline: "Remove Backgrounds with AI Precision," highlighting its core functionality of using cutting-edge deep learning to remove image backgrounds in seconds. Below the headline, the **"Why NeuroCut?"** section explains the app's key benefits: ultra-precise AI detection, instant processing, and easy image customization, making it perfect for designers, photographers, and online sellers. Additionally, **user testimonials** are displayed, showcasing real feedback from satisfied users like Dita, an online store owner who praises NeuroCut for saving her hours of editing, and Alex, a freelance editor, who values the app's speed and accuracy. The **"Try It Now"** button encourages immediate engagement, inviting users to start editing their images with the app's seamless and responsive interface, built with **Vue.js** and **Tailwind CSS**.

### Crop Menu

<img width="959" alt="image" src="https://github.com/user-attachments/assets/2cf033f1-05d9-47b3-9b65-f850f376956f" />

<img width="959" alt="image" src="https://github.com/user-attachments/assets/b5ec055f-834a-4923-ba89-2a6302051723" />

The **Crop** menu in **NeuroCut** is the main feature where users can **remove image backgrounds** using **U²-Net**'s AI-powered deep learning model. Users can upload images, such as photos of people, animals, or products, and the model will automatically isolate the subject and remove the background. As seen in the example of an orangutan photo, the background (in this case, a forest) is successfully removed, leaving a clean subject. Once the background is removed, users can preview the results and download the final image with the background eliminated. The **"Download Result"** button enables users to save their edited images in high quality.

### Customize Menu

<img width="959" alt="image" src="https://github.com/user-attachments/assets/fd9215ce-1bc2-499d-9584-b14fd8bf61ac" />

<img width="959" alt="image" src="https://github.com/user-attachments/assets/dd5b9226-7fb1-484d-a218-7f4cd25f9ee6" />

The **Customize** menu in **NeuroCut** allows users to personalize the background of their cropped images in an intuitive and visually engaging interface. After successfully removing the background in the **Crop** section, users can upload the resulting cropped image here to begin customization. The interface offers several options for background styling, including selecting a solid color through a color picker, choosing from a range of preset gradient themes, or uploading a new custom background image.

Users can experiment with professional gradient themes such as Ocean, Sunset, Aurora, Midnight, and Corporate Blue — each designed to enhance different types of subjects and moods. For instance, in the example shown, the previously cropped orangutan image is placed on an **Ocean** gradient background, creating a vibrant and nature-inspired look that draws focus to the subject while maintaining an aesthetically pleasing visual balance.

Additionally, users have the flexibility to upload their own background image, which can be anything from a brand template, product showcase, or scenic photo. All customization options are rendered in real time, allowing users to instantly preview the result before downloading their finalized image in high quality. This menu is especially useful for content creators, photographers, and digital designers looking for a fast and elegant way to style their images with AI-powered background control.

### Background Gallery Menu

<img width="959" alt="image" src="https://github.com/user-attachments/assets/9b826c04-9d3d-4bcc-a6ae-49e1ca46d9bc" />

<img width="959" alt="image" src="https://github.com/user-attachments/assets/7ee9a65f-2408-42f0-a477-c76657ec2f2d" />

The **Background Gallery** menu in **NeuroCut** provides users with access to a curated collection of beautiful, high-resolution sample background images. These backgrounds are professionally categorized and visually diverse — including nature, abstract, minimal, illustrated, landscape, and more — giving users a fast and easy way to enhance the appearance of their cropped subjects.

Each background is displayed in an interactive card layout. When a user clicks the **"Use Background"** button on a selected image, they are automatically redirected to the **Customize** menu, where the selected background is preloaded and applied to the previously uploaded foreground (cropped image).

This feature is especially helpful for users who want to quickly try different aesthetic combinations without having to upload a background manually. For example, a user who cropped an orangutan image earlier can effortlessly preview it on a vibrant sakura background, a scenic lake view, or even a stylized pixel art landscape — all with just one click. The Background Gallery streamlines the workflow, saves editing time, and inspires creativity through instant visual experimentation.



---

## 🧱 Tech Stack

| Technology / Tool         | Description                                                                 |
|---------------------------|-----------------------------------------------------------------------------|
| **U²-Net**                | Pretrained deep learning model for precise background removal               |
| **PyTorch**               | Machine learning framework for running and managing the U²-Net model        |
| **Torchvision Transforms**| Utilities for preprocessing image inputs before inference                   |
| **Vue.js**                | Progressive JavaScript framework for building dynamic frontend interfaces   |
| **Tailwind CSS**          | Utility-first CSS framework for creating responsive and clean UI designs    |
| **Pillow**                | Python Imaging Library for reading, converting, and saving image files      |
| **Python**                | Backend programming language for AI integration and web API logic           |
| **FastAPI**               | Lightweight web framework for building high-performance REST APIs           |
| **Uvicorn**               | ASGI server to run the FastAPI backend asynchronously                       |
| **Vite**                  | Fast frontend build tool and development server for Vue.js                  |
| **JavaScript**            | Core scripting language for frontend behavior and interactivity             |
| **HTML**                  | Markup language used to structure content on the web                        |
| **HTML**                  | Markup language used to structure content on the web                        |
| **CSS**                   | Styling language for layout, design, and visual presentation                |
| **NumPy**                 | Library for fast numerical operations and array manipulation                |
