# from torch.utils.data import Dataset
# from cookie_cutter_demo.data import MyDataset
import os
import pytest
import torch
from tests import _PATH_DATA
from cookie_cutter_demo.data import corrupt_mnist

# Skipper test hvis data stier ikke er tilgængelige
DATA_READY = os.path.exists(os.path.join(_PATH_DATA, "processed", "train_images.pt"))
@pytest.mark.skipif(
    not DATA_READY,
    reason="Processed MNIST data files not found"
)

def test_corrupt_mnist_loads_correctly():
    train_set, test_set = corrupt_mnist(_PATH_DATA + "/processed")

    # Expected sizes from exercise
    # N_train should be 30_000 or 50_000 depending on which subset you use.
    # We accept either.
    assert len(train_set) in (30_000, 50_000)
    assert len(test_set) == 5_000

    # Check shapes
    x_train, y_train = train_set[0]
    x_test, y_test = test_set[0]

    assert isinstance(x_train, torch.Tensor)
    assert isinstance(x_test, torch.Tensor)

    # Your preprocess does: unsqueeze(1) => (N,1,28,28)
    assert x_train.shape == (1, 28, 28)
    assert x_test.shape == (1, 28, 28)

    # Labels should be ints 0-9
    assert 0 <= int(y_train) <= 9
    assert 0 <= int(y_test) <= 9

    # Check that all labels 0..9 are represented (train set is enough)
    labels = set()
    for i in range(len(train_set)):
        _, yi = train_set[i]
        labels.add(int(yi))
        if len(labels) == 10:
            break
    assert labels == set(range(10))
