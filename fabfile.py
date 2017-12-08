from fabric.api import local, warn_only
from datetime import datetime


def deploy():
    "Generate web pages and push to web site"
    with warn_only():
      local("hugo")
    local("rsync -avzr --delete --progress docs/ sandipb@sandipb.net:ref.sandipb.net/")


def newpost(slug):
    "Create a new post(fab newpost:SLUG)"
    today = datetime.now().strftime("%Y-%m-%d")
    local("hugo new post/%s-%s.markdown" % (today, slug))
