import torch
from models import vgg19
from PIL import Image
from torchvision import transforms
import gradio as gr
import cv2
import numpy as np
import scipy

model_path = "weights/dmcount.pth"
device = torch.device('cuda') #can be changed to cpu if a gpu is unavailable

model = vgg19()
model.to(device)
model.load_state_dict(torch.load(model_path, device))
model.eval()

"""
inp - input image as ndarray

returns: 
    dst - original image overlayed with heatmap visualization
    int(count) - est. count of number of people in image

"""
def predict(inp):
    org_img = inp
    inp = Image.fromarray(inp.astype('uint8'), 'RGB')
    inp = transforms.ToTensor()(inp).unsqueeze(0)
    inp = inp.to(device)
    with torch.set_grad_enabled(False):
        outputs, _ = model(inp)
    count = torch.sum(outputs).item()
    vis_img = outputs[0, 0].cpu().numpy()

    # normalize density map values from 0 to 1, then map it to 0-255.
    vis_img = (vis_img - vis_img.min()) / (vis_img.max() - vis_img.min() + 1e-5)
    vis_img = (vis_img * 255).astype(np.uint8)
    vis_img = cv2.applyColorMap(vis_img, cv2.COLORMAP_JET)
    vis_img = cv2.cvtColor(vis_img, cv2.COLOR_BGR2RGB)
    vis_img = cv2.resize(vis_img, (inp.size()[3], inp.size()[2]))

    #overlay heatmap vis over original image
    dst = cv2.addWeighted(org_img, 0.5, vis_img, 0.9, 0)

    return dst, int(count)


title = "Distribution Matching for Crowd Counting"

# sample images to be included in demo
examples = [
    ["inputs/test.png"],
    ["inputs/img2.jpg"],
    ["inputs/img3.jpg"],
    ["inputs/img4.jpg"],
    ["inputs/img5.jpg"]
]

inputs = gr.inputs.Image(label="Image of Crowd")
outputs = [gr.Image(label="Predicted Density Map"), gr.Label(label="Predicted Count")]
gr.Interface(fn=predict, inputs=inputs, outputs=outputs, title=title, examples=examples, layout="vertical",
             allow_flagging=False).launch(share=True)