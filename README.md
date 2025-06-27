# MNIST CNN Classifier

This project implements a Convolutional Neural Network (CNN) using PyTorch to classify handwritten digits from the MNIST dataset.

## 📂 Project structure

```
├── cnn.py # Defines the CNN architecture
├── dataset.py # Loads and prepares the MNIST dataset
├── learning.py # Trains and tests the model
├── classifier.py # Makes predictions on individual samples and displays the image
```

## 🚀 How to run

1️⃣ **Install dependencies**
```bash
pip install -r requirements
```

2️⃣ **Run the digit recognition app**
```bash
python app.py
```

This will:

* Display the image using matplotlib
* Print the prediction to the console

## 📝 Model details
```
* 2 convolutional layers with max pooling
* Dropout for regularization
* 2 fully connected layers
* Loss function: `CrossEntropyLoss`
* Optimizer: `Adam`
```

![Example prediction](https://github.com/LuizAlbar/MNIST-Classifier/blob/assets/example.png)






