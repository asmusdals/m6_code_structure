import torch
import os
import pytest
from tests import _PATH_DATA
from cookie_cutter_demo.train import train 
from cookie_cutter_demo.model import MyAwesomeModel

# Skipper test hvis data stier ikke er tilgængelige
DATA_READY = os.path.exists(os.path.join(_PATH_DATA, "processed", "train_images.pt"))
@pytest.mark.skipif(
    not DATA_READY,
    reason="Processed MNIST data files not found"
)

def test_training_runs():
    """ 
    Sikrer at training kører 1 epoch uden cra
    Catche breaking changes in the training loop, model or data pipeline
    """
    train(
        lr=1e-3,
        batch_size=64,
        epochs=1,
    )



