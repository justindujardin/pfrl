import random
import torch
import numpy as np


def set_random_seed(seed, gpus=()):
    """Set a given random seed to Pytorch's random number generator

    torch.manual_seed() seeds the RNG for all devices (both CPU and CUDA)

    See https://pytorch.org/docs/stable/notes/randomness.html for more details

    Args:
        seed (int): Random seed [0, 2 ** 32).
        gpus (tuple of ints): GPU device IDs to use. Negative values are
            ignored.
    """
    # PFRL depends on random
    random.seed(seed)
    # PFRL depends on numpy.random
    np.random.seed(seed)
    # torch.manual_seed is enough for the CPU and GPU
    torch.manual_seed(seed)