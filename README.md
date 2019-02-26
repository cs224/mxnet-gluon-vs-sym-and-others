
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
  This notebook shows the comparison of gluon vs. module/symbol for a very simple MLP architecture. The seen speed difference is a factor of 2.17 between 21.86 seconds for the module/symbol version and 47.43 seconds for the gluon version.
* [tensorflow-keras-speed.ipynb](https://nbviewer.jupyter.org/github/cs224/mxnet-gluon-vs-sym-and-others/blob/master/tensorflow-keras-speed.ipynb?flush_cache=true)<br>
  Same model but implemented in tensorflow keras. In order to run the model you'll have to use the tfkeras conda environment that you can create by hand via `conda env create -f environment_tfkeras.yml`.<br>
  The time needed is 36.34 seconds, e.g. a bit faster than the mxnet gluon version above, but slower than the mxnet module/symbol version. The metrics are also a bit better after 20 epochs than with both mxnet versions, but this may be due to differences in the weight initialization (while I've used in both cases Xavier initializers).
