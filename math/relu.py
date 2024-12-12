import numpy as np
class RELU:
    def forward(self, input):
        self.output = np.max(0, input)