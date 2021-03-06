from hypergan.samplers.base_sampler import BaseSampler
from hypergan.gan_component import ValidationException, GANComponent

import numpy as np
import time

class AlignedSampler(BaseSampler):
    def __init__(self, gan, samples_per_row=8):
        BaseSampler.__init__(self, gan, samples_per_row)
        self.inputs = self.gan.inputs.next()
        self.z = self.gan.latent.next()

    def compatible_with(gan):
        if hasattr(gan, 'encoder'):
            return True
        return False

    def _sample(self):
        self.inputs = self.gan.inputs.next(0).clone().detach()
        self.gan.latent.z = self.z
        g = self.gan.generator.forward(self.inputs)
        return [
            ('input', self.inputs),
            ('generator', g)
        ]

