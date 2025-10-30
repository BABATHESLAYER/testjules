# Iris Flower Classifier

This is a simple machine learning application that trains a logistic regression model to classify iris flowers into one of three species: setosa, versicolor, or virginica.

## Setup

1. **Install Python 3.**

2. **Clone the repository.**

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### 1. Train the Model

To train the model, run the following command from the root directory:

```bash
python3 src/train.py
```

This will train the model and save it as `model.pkl`.

### 2. Make Predictions

To make predictions on new data, you can use the `src/predict.py` script. This script loads the trained model and makes predictions on some sample data.

```bash
python3 src/predict.py
```

You can modify the `sample_data` in `src/predict.py` to make predictions on your own data.
