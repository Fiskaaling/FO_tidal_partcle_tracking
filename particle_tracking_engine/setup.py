import setuptools
import distutils.core
import Cython.Build
import numpy
distutils.core.setup(
    ext_modules = Cython.Build.cythonize("particle_tracking_cython.pyx"),
    include_dirs=[numpy.get_include()]
)