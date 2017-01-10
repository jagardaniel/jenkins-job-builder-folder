from setuptools import setup

setup(
    name='jenkins-job-builder-folder',
    description='Folder support for jenkins job builder',
    version='1.0',
    packages=['jenkins_job_builder_folder'],
    install_requires=['jenkins-job-builder>=2.0.0.0b1'],
    entry_points={
        'jenkins_jobs.projects': [
            'folder=jenkins_job_builder_folder.project_folder:Folder',
        ]
    }
)
