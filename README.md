# Tornado Skeleton Project

Skeleton for web service projects involving multiple services implemented using tornado.

Clone this repo.

Install OS dependencies.
(May be some dependency is missing since setup.sh was not tested in a clean environment yet)

```shell
$ sudo ./install_os_dependencies.sh
`````

Generate environments

```shell
$ tox -r
`````

Run all services

```shell
$ tox -e runservice -- all
```````````

Send a request to service health

```shell
$ curl --proxy '' 'http://localhost:10001/health?include_details=true' 
$ curl --proxy '' 'http://localhost:10002/health?include_details=true' 
```````````
