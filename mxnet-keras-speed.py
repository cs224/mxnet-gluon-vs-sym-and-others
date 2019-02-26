
import os
os.environ["CUDA_DEVICE_ORDER"]    = "PCI_BUS_ID"   # see issue #152
os.environ["CUDA_VISIBLE_DEVICES"] = ''
os.environ["KERAS_BACKEND"]        = "mxnet"

import numpy as np, scipy, scipy.stats as stats, pandas as pd, matplotlib.pyplot as plt, seaborn as sns
import sklearn, sklearn.pipeline, sklearn.model_selection, sklearn.preprocessing
import logging, time, datetime
import mxnet as mx
from mxnet import gluon, nd, autograd, metric

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
# pd.set_option('display.float_format', lambda x: '%.2f' % x)
np.set_printoptions(edgeitems=10)
np.set_printoptions(linewidth=1000)
np.set_printoptions(suppress=True)
np.core.arrayprint._line_width = 180

sns.set()

from keras import backend as K

K.get_num_gpus()

mx.context.num_gpus()

K.mx.context.num_gpus()

mx.test_utils.list_gpus()
mx.cpu()
