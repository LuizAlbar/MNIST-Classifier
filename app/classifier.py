import matplotlib.pyplot as plt
import torch
from .learning import model, device
from .dataset import test_data
from .cnn import CNN
import os

def digit_recogntion(x):
    
    model = CNN().to(device)
    model.load_state_dict(torch.load('./app/cnn_mnist.pth'))
    model.eval()

    data, target = test_data[x]
    data = data.unsqueeze(0).to(device)
    output = model(data)

    prediction = output.argmax(dim = 1, keepdim = True).item()


    print(f'Prediction:  {prediction}')


    image = data.squeeze(0).squeeze(0).cpu().numpy()

    plt.imshow(image, cmap= 'gray')
    plt.show()



