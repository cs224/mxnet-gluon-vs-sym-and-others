
# mxnet-gluon-vs-sym-and-others

A repository to examine speed/performance differences between the [mxnet](https://mxnet.apache.org/) [gluon](https://mxnet.incubator.apache.org/versions/master/tutorials/gluon/gluon.html) and [module](https://mxnet.incubator.apache.org/api/python/module/module.html)/[symbol](https://mxnet.incubator.apache.org/api/python/symbol/symbol.html) APIs.

My first experiments with mxnet show a speed difference of at least a factor of 2 (in some model even 4-5) between the module/symbol API (which is faster) and the gluon API (which is slower).

I am currently very new to mxnet and it is quite likely that my approach contains fundamental flaws that might explain the seen differences. I cannot see how, though, as I have taken the code from the mxnet web-site from tutorials and API documentation.

# Environment and versions: mxnet 1.3.1

Go into the conda_environments directory and run the `./create.sh` script to reproduce the exact same environment.

In the top of the notebooks you will see the [watermark](https://pypi.org/project/watermark/) header that will show the versions used. While I noticed the problem with mxnet-cu90mkl in version 1.3.1, the below notebooks reproduce the problem with the raw mxnet 1.3.1 installation purely on CPU.

# Discussion thread(s)

* [mxnet 1.3.1: speed/performance differences between the mxnet gluon and module/symbol APIs of at least a factor of 2 ](https://discuss.mxnet.io/t/mxnet-1-3-1-speed-performance-differences-between-the-mxnet-gluon-and-module-symbol-apis-of-at-least-a-factor-of-2/3314)

# Notebooks

* [mxnet-gluon-vs-sym-speed.ipynb](https://nbviewer.jupyter.org/github/cs224/mxnet-gluon-vs-sym-and-others/blob/master/mxnet-gluon-vs-sym-speed.ipynb?flush_cache=true)<br>
  Due to the feed-back on the [discuss.mxnet.io](https://discuss.mxnet.io/t/mxnet-1-3-1-speed-performance-differences-between-the-mxnet-gluon-and-module-symbol-apis-of-at-least-a-factor-of-2/3314/3) forum I was able to resolve the question and problem and achieve with gluon the same speed as with the module/symbol API.<br>
  Two changes were necessary:
  * Use hybridize(static_shape=True, static_alloc=True); this improved the speed to roughly 37 seconds
  * Use DataIterLoader based on the `mx.io.NDArrayIter` as described [here](https://mxnet.incubator.apache.org/versions/master/tutorials/gluon/datasets.html) in the appendix, rather than the `mx.gluon.data.DataLoader`. This improved the speed to finally 20.17 seconds. No idea why the DataLoder is so much worse than the NDArrayIter.
* [tensorflow-keras-speed.ipynb](https://nbviewer.jupyter.org/github/cs224/mxnet-gluon-vs-sym-and-others/blob/master/tensorflow-keras-speed.ipynb?flush_cache=true)<br>
  Same model but implemented in tensorflow keras. In order to run the model you'll have to use the tfkeras conda environment that you can create by hand via `conda env create -f environment_tfkeras.yml`.<br>
  The time needed is 36.34 seconds, e.g. a bit faster than the mxnet gluon version above, but slower than the mxnet module/symbol version. The metrics are also a bit better after 20 epochs than with both mxnet versions, but this may be due to differences in the weight initialization (while I've used in both cases Xavier initializers).
* [mxnet-keras-speed.ipynb](https://nbviewer.jupyter.org/github/cs224/mxnet-gluon-vs-sym-and-others/blob/master/mxnet-keras-speed.ipynb?flush_cache=true)<br>
  Same model but implemented in [keras-mxnet](https://github.com/awslabs/keras-apache-mxnet) v.2.2.4.1. In order to run the model you'll have to use the mxnetkeras conda environment that you can create by hand via `conda env create -f environment_mxnetkeras.yml`.<br>
  The time needed is 32.89 seconds, e.g. very slightly faster than the tfkears version. But what is **really** surprising is that its speed does neither match the gluon version (**much slower**) nor the module/symbol version (**much faster**)?? This is puzzleing me even more??<br>
  The metrics are basically the same as for the tfkeras version.

# Summary

  | base library | variant       | time  |
  |--------------|---------------|-------|
  | mxnet        | module/symbol                                                         | 21.86 |
  | mxnet        | keras                                                                 | 32.89 |
  | mxnet        | gluon                                                                 | 47.43 |
  | mxnet        | gluon DataIterLoader, hybridize(static_shape=True, static_alloc=True) | 20.17 |
  | tensorflow   | keras                                                                 | 36.34 |

# Other references

* [Gluon: building blocks for your Deep Learning universe](https://medium.com/@julsimon/gluon-building-blocks-for-your-deep-learning-universe-4bce4e56ef55)
* [Deep Learning Framework Examples](https://github.com/ilkarman/DeepLearningFrameworks): this is a more extensive evaluation of different learning frameworks
  * [Gluon_CNN](https://github.com/ilkarman/DeepLearningFrameworks/blob/master/notebooks/Gluon_CNN.ipynb)
  * [MXNet_CNN_highAPI](https://github.com/ilkarman/DeepLearningFrameworks/blob/master/notebooks/MXNet_CNN_highAPI.ipynb)
