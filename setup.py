from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy
import ldpc

from shutil import copyfile
ldpc_path=ldpc.get_include()+'/include/'
include_files=["mod2sparse.c","mod2sparse.h","README.md","COPYRIGHT"]
for f in include_files: copyfile(ldpc_path+f,"src/bposd/include/"+f)
include_files=["README.md","LICENSE"]
for f in include_files: copyfile(f,"src/bposd/"+f)

source_files=["src/bposd/bposd.pyx",
            "src/bposd/include/binary_char.c",
            "src/bposd/include/mod2sparse_extra.c",
            "src/bposd/include/sort.c",
            "src/bposd/include/mod2sparse.c"]

extension = Extension(
    name="bposd.bposd",
    sources=source_files,
    libraries=[],
    library_dirs=[],
    include_dirs=[ldpc.get_include(), numpy.get_include(),"src/bposd/include"],
    extra_compile_args=['-std=c11']
    )

setup(
    python_requires='>=3.6',
    name='bposd',
    version='0.0.2',
    description='BP+OSD',
    long_description='This module provides an implementation of the belief\
        propagagation + ordered statistics decoder for quantum LDPC codes.',
    url='https://roffe.eu',
    author='Joschka Roffe',
    packages=["bposd"],
    package_dir={'':'src'},
    ext_modules=cythonize([extension]),
    classifiers=['Development Status :: 1 - Planning'],
    install_requires=["tqdm","scipy","ldpc","numpy"],
    include_package_data=True,
    zip_safe=False,

)

