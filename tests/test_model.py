import torch
from cookie_cutter_demo.model import MyAwesomeModel

def test_model():
    model = MyAwesomeModel()
    x = torch.randn(1,1,28,28)
    y = model(x)
    assert y.shape == (1,10)
