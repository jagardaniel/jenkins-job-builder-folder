## jenkins-job-builder-folder

Very basic folder support for [jenkins-job-builder](http://docs.openstack.org/infra/jenkins-job-builder).
It requires a later version than 1.6.1 of jjb. 2.0.0.0b1 is currently available in PyPi.

### Usage

Create a new job with project-type `folder`.

```yaml
- job:
    name: test-folder
    project-type: folder
```
