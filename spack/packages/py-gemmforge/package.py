# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyGemmforge(PythonPackage):
    """GPU-GEMM generator for the Discontinuous Galerkin method"""

    homepage = "https://github.com/SeisSol/gemmforge"

    # FIXME: ensure the package is not available through PyPI. If it is,
    # re-run `spack create --force` with the PyPI URL.
    url = "https://github.com/SeisSol/gemmforge/archive/refs/tags/v0.0.208.tar.gz"

    license("MIT", checked_by="dguibert")

    version("0.0.208", sha256="c0062ef5532ae195cf3867dbaaf6a7de9d6526b3e96258c9a0fb9aaf9850a5a5")

    depends_on("py-setuptools", type="build")
    
    depends_on("py-numpy", type=("build", "run"))
    depends_on("py-pyyaml", type=("build", "run"))
