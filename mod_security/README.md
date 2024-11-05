# Course 1 - Mod Security the poor man's WAF

Let's use a docker container to build a WAF and test out a few custom rules in this course

# Start the container without rules

Run the cooresponding command based on your workstation with docker or podman desktop:

## Docker Desktop Instructions

```
docker-compose up
```

## Podman Desktop Instructions

```
podman compose up -d
podman container logs -f $(podman container ls --filter "name=mod_security-dispatcher-1" --format "{{.Names}}")
```

## Important startup logs

Pay attention to the output of the container and you'll see the httpd and mod_sec logs in the output

Example:

```
[Tue Nov 05 17:28:32.858915 2024] [:notice] [pid 42:tid 70368761733360] ModSecurity for Apache/2.9.6 (http://www.modsecurity.org/) configured.
[Tue Nov 05 17:28:32.863717 2024] [:notice] [pid 42:tid 70368761733360] ModSecurity: APR compiled version="1.6.3"; loaded version="1.6.3"
[Tue Nov 05 17:28:32.863919 2024] [:notice] [pid 42:tid 70368761733360] ModSecurity: PCRE compiled version="8.42 "; loaded version="8.42 2018-03-20"
[Tue Nov 05 17:28:32.863965 2024] [:notice] [pid 42:tid 70368761733360] ModSecurity: LUA compiled version="Lua 5.3"
[Tue Nov 05 17:28:32.863985 2024] [:notice] [pid 42:tid 70368761733360] ModSecurity: YAJL compiled version="2.1.0"
[Tue Nov 05 17:28:32.864041 2024] [:notice] [pid 42:tid 70368761733360] ModSecurity: LIBXML compiled version="2.9.7"
[Tue Nov 05 17:28:32.864069 2024] [:notice] [pid 42:tid 70368761733360] ModSecurity: Status engine is currently disabled, enable it by set SecStatusEngine to On.
[mpm_event:notice] [pid 42:tid 70368761733360] AH00489: Apache/2.4.37 (rocky) Communique/4.3.5 configured -- resuming normal operations
[Tue Nov 05 17:28:33.060568 2024] [core:notice] [pid 42:tid 70368761733360] AH00094: Command line: '/usr/sbin/httpd -D FOREGROUND'
```

## Access the no-rule container

Now you should be able to open the browser or use curl to [http://127.0.0.1/](http://127.0.0.1/)

```
curl -I http://127.0.0.1/
HTTP/1.1 200 OK
Date: Tue, 05 Nov 2024 17:34:09 GMT
Server: Apache/2.4.37 (rocky) Communique/4.3.5
X-Vhost: renderer
Last-Modified: Tue, 13 Jun 2023 21:41:23 GMT
ETag: "a9e-5fe09b24b66c0"
Accept-Ranges: bytes
Content-Length: 2718
Content-Type: text/html; charset=UTF-8
```

You can see it's responding and showing a 200 response code.