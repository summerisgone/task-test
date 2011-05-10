from celery.task import task
import subprocess
from github2.client import Github
import simplejson
import time
import pkg_resources


@task()
def add(x, y):
    print("Executing task id %r, args: %r kwargs: %r" % (
        add.request.id, add.request.args, add.request.kwargs))
    return x + y


@task()
def get_repos(user='redsolution'):
    print("Executing task id %r, args: %r kwargs: %r" % (
        add.request.id, add.request.args, add.request.kwargs))
    time.sleep(5)
    github = Github()
    repos = github.repos.list(user)
    return repos

@task()
def get_repos_wget(user='redsolution'):
    print("Executing task id %r, args: %r kwargs: %r" % (
        add.request.id, add.request.args, add.request.kwargs))
    output = subprocess.Popen('wget -qO- http://github.com/api/v2/json/repos/show/%s' % user,
        shell=True, stdout=subprocess.PIPE).communicate()[0]
    return simplejson.loads(output)

@task()
def install_lib(lib='redsolutioncms.django-easy-news'):
    print("Executing task id %r, args: %r kwargs: %r" % (
        add.request.id, add.request.args, add.request.kwargs))
    subprocess.Popen('pip install %s' % lib, shell=True).wait()

@task()
def pip_install_lib(lib='redsolutioncms.django-easy-news'):
    import pip
    print 'pip install %s' % lib
    requirement_set = pip.main(['install', lib])
    return requirement_set

@task()
def test_install_lib(lib='redsolutioncms.django-easy-news'):
    result = install_lib.delay(lib)
    result.get()
    r = pkg_resources.Requirement.parse(lib)
    dist = pkg_resources.get_distribution(r)
    dist.activate()
    return dist.version
