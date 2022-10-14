# Notes about Synology NAS

## Install homebrew on Synology

Ref: <https://community.synology.com/enu/forum/1/post/153781>

## Fix docker group permissions

Ref: <https://www.synoforum.com/threads/permissions-for-user-to-run-docker.3536/post-16480>

- create the group "docker" from the ui or cli (`sudo synogroup --add docker`)
- make it the group of the docker.sock: `sudo chown root:docker /var/run/docker.sock`
- assign the user to the docker group in the ui or cli (`sudo synogroup --member docker {username}`)
- login into ssh as {username} and try (if you were already logged in before you created the group, logout and relogin)

## Install Jellyfin

<https://mariushosting.com/how-to-install-jellyfin-on-your-synology-nas/>

I however installed the app via the Docker package. This unfortunately doesnt provide an interface to run a container rootless. Looking for a workaround.
