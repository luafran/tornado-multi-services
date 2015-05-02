import os
import setuptools
import shutil
from pip.download import PipSession
from pip.req import parse_requirements


PACKAGE_PATH = os.path.dirname(os.path.realpath(__file__))
GLOBAL_PATH = os.path.dirname(PACKAGE_PATH)
GLOBAL_REQUIREMENTS_PATH = os.path.join(GLOBAL_PATH,
                                        'global-requirements.txt')
if os.path.exists(GLOBAL_REQUIREMENTS_PATH):
    try:
        shutil.copyfile(GLOBAL_REQUIREMENTS_PATH, 'global-requirements.txt')
    except shutil.Error:
        pass


# parse_requirements() returns generator of pip.req.InstallRequirement objects
GLOBAL_REQS = parse_requirements("global-requirements.txt", session=PipSession())
PACKAGE_REQS = parse_requirements("requirements.txt", session=PipSession())

# reqs is a list of requirement
# e.g. ['tornado==3.2.2', '...']
REQS = [str(ir.req) for ir in GLOBAL_REQS]
REQS.extend([str(ir.req) for ir in PACKAGE_REQS])

if __name__ == "__main__":
    setuptools.setup(
        name="prjname-common",
        version="0.1",
        description="Project Name Common",
        author="The Comany",
        namespace_packages=['prjname'],
        packages=setuptools.find_packages(PACKAGE_PATH, exclude=["*.test",
                                                                 "*.test.*",
                                                                 "test.*",
                                                                 "test"]),
        keywords="prjname",
        install_requires=REQS,
        include_package_data=True,
        entry_points={
            'console_scripts': [
                'prjname-runservice = prjname.common.tornado.runservice:main'
            ],
            'prjname.services': [
                'all = prjname.common.tornado.all_command:AllCommand',
            ],
        },
    )
