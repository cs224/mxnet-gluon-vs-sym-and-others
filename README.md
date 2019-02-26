
# mxnet-gluon-vs-sym-and-others

A repository to examine speed/performance differences between the [mxnet](https://mxnet.apache.org/) [gluon](https://mxnet.incubator.apache.org/versions/master/tutorials/gluon/gluon.html) and [module](https://mxnet.incubator.apache.org/api/python/module/module.html)/[symbol](https://mxnet.incubator.apache.org/api/python/symbol/symbol.html) APIs.

My first experiments with mxnet show a speed difference of at least a factor of 2 (in some model even 4-5) between the module/symbol API (which is faster) and the gluon API (which is slower).

I am currently very new to mxnet and it is quite likely that my approach contains fundamental flaws that might explain the seen differences. I cannot see how, though, as I have taken the code from the mxnet web-site from tutorials and API documentation.

# Notebooks

* [mxnet-gluon-vs-sym-speed.ipynb](https://nbviewer.jupyter.org/github/cs224/mxnet-gluon-vs-sym-and-others/blob/master/mxnet-gluon-vs-sym-speed.ipynb?flush_cache=true)<br>
  This notebook shows the comparison of gluon vs. module/symbol for a very simple MLP architecture. The seen speed difference is a factor of 2.17 between 21.86 seconds for the module/symbol version and 47.43 seconds for the gluon version.
