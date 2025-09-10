# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack_repo.builtin.build_systems.python import PythonPackage
from spack.package import *

class PyHistcmp(PythonPackage):
    """Compare histograms."""

    homepage = "https://pypi.org/project/histcmp"
    pypi = "histcmp/histcmp-0.8.1.tar.gz"

    maintainers("pbalek")

    license("MIT", checked_by="pbalek")

    version("0.8.1", sha256="8fec2675dbc663d409dd510c65aa4195c3fa2a991d7e0cfd09308d130b7bda3d")

    build_system_class = 'PythonPipBuildSystem'

    depends_on("python@3.10:", type=("build", "run"))
    depends_on("py-hist@2.8.1:+plot", type=("build", "run"))
    depends_on("py-jinja2@3.1.4:", type=("build", "run"))
    depends_on("py-matplotlib@3.9.2:", type=("build", "run"))
    depends_on("py-mplhep@0.3.55:", type=("build", "run"))
    depends_on("py-numpy@2.1.3:",  type=("build", "run"))
    depends_on("py-pydantic@2.10.1:", type=("build", "run"))
    depends_on("py-pyyaml@6.0.2:", type=("build", "run"))
    depends_on("py-rich@13.9.4:", type=("build", "run"))
    depends_on("py-scipy@1.14.1:", type=("build", "run"))
    depends_on("py-typer@0.13.1:", type=("build", "run"))

    depends_on("py-hatchling", type="build")
