# Community Spirit Foundation

Stride For Education is a progressive web app which will enable participants to track their kilometers while engaging in a walking/running/wheeling challenge. Through the app, we aim to raise funds and awareness for Community Spirit Foundation.

### Windows

If you are using windows, we highly recommend installing WSL

### Run Vue Application

```
yarn install
```

```
yarn dev
```

### Docker

Install docker on your machine: https://www.docker.com/

Run the Vue and Django server

```
docker compose up
```

The website can be viewed on

```
http://localhost:8082/
```

The Django development server can be viewed on

```
http://localhost:8081/
```

The documentation can be viewed on

```
http://localhost:8000/
```

### Documentation

If you wish to view the documentation without running everything else then run these commands

```
cd documentation
```
```
mkdocs serve
```

Note: if you are using windows you have to preface any `mkdocs` command with `python -m`. For example `python -m mkdocs serve`.
