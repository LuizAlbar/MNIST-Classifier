import torch
import torch.nn as nn
import torch.optim as optim
from .cnn import CNN
from .dataset import loaders

device = torch.device('cuda'if torch.cuda.is_available() else 'cpu')

model = CNN().to(device)

optimizer = optim.Adam(model.parameters(), lr= 0.001)

loss_fn = nn.CrossEntropyLoss()

def train(epoch):
    
    model.train()
    
    for batch_idx, (data, target) in enumerate(loaders['train']):
        data, target = data.to(device), target.to(device)
        optimizer.zero_grad()
        output = model(data)
        loss = loss_fn(output, target)
        loss.backward()
        optimizer.step()
        
        if batch_idx % 20 == 0:
            print(f"Train Epoch: {epoch} [{batch_idx * len(data)}/{len(loaders['train'].dataset)} ({100. * batch_idx / len(loaders['train']):.0f}%)]\t{loss.item():.6f}")
            
            
def test(x):
    
    model.eval()
    test_loss = 0
    correct = 0
    
    with torch.no_grad():
        for data, target in loaders['test']:
            
            data, target = data.to(device), target.to(device)
            output = model(data)  
            test_loss +=  loss_fn(output, target).item()
            pred = output.argmax(dim = 1, keepdim = True)
            correct += pred.eq(target.view_as (pred)).sum().item()
            
    test_loss /= len(loaders['test'].dataset)
    print(f"\nTest set: Average loss: {test_loss: .4f}, Accuracy {correct}/{len(loaders['test'].dataset)} ({100. * correct/len(loaders['test'].dataset):.0f}%\n) ")
    
    
if __name__ == '__main__':
       
    for epoch in range(1, 11):
    
        train(epoch)
        test(epoch)
        
        torch.save(model.state_dict(), 'cnn_mnist.pth')