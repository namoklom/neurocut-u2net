import torch
from u2net import U2NET
from PIL import Image
import torchvision.transforms as transforms
import numpy as np
import os

model_path = os.path.join('saved_models', 'u2net', 'u2net.pth')
model = U2NET(3, 1)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()

def load_image(img_path):
    image = Image.open(img_path).convert('RGB')
    transform = transforms.Compose([
        transforms.Resize((320, 320)),
        transforms.ToTensor()
    ])
    return transform(image).unsqueeze(0), image.size

def remove_background(input_path, output_path):
    image_tensor, orig_size = load_image(input_path)

    with torch.no_grad():
        d1, *_ = model(image_tensor) 
        mask = d1[0][0].cpu().numpy() 

    mask = Image.fromarray((mask * 255).astype(np.uint8)).resize(orig_size)

    original = Image.open(input_path).convert("RGB").resize(orig_size)
    r, g, b = original.split()
    rgba = Image.merge("RGBA", (r, g, b, mask))

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    rgba.save(output_path)
    print(f"Saved: {output_path}")