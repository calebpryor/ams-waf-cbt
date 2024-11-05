# Course Workstation Requirements

We want to take time in this first document to setup your workstation.


# Create docker account

Create an account on [hub.docker.com](https://hub.docker.com/signup) you'll need it for pulling down public docker images.

# Install favorite container running application

Use your favorite installation to get containers running on your machine.

Here are some references for different installation types and you can skip to that section based on which option you choose.  `Remember only pick one to install!`

## Option 1 - Docker Desktop (easiest but only free for personal use)

Get the installation media from [here](https://www.docker.com/products/docker-desktop/)

Run through the standard installation wizard and login to the client with your docker account.

## Option 2 - Podman (free but a few more steps)

Get the installation instructions [here](https://podman.io/docs/installation)

One you've gotten the install completed start up podman:

```
podman machine init
podman machine start
```

Login to Docker Hub:

```
podman login docker.io
```

# GIT

## WAF Training Repository

If you haven't already downloaded or cloned [this repository](https://github.com/calebpryor/ams-waf-cbt.git) do so with the following command:

### Clone via GIT cli

```
git clone https://github.com/calebpryor/ams-waf-cbt.git
```

### Download

You can download and extract [this zip](https://github.com/calebpryor/ams-waf-cbt/archive/refs/heads/main.zip)

# Start the courses

[Course 1](../mod_security/README.md)
