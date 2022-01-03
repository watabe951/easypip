# easypip
easypip is a simple wrapper of pip command. easypip = pip + lock + sync.

## Usage
### install
```
$ easypip install requests
```

Above command will install requests and create requirements.lock.
This is equivarent to

```
$ pip install requests
$ pip freeze --all > requirements.lock
```

### lock
You can also lock manually by

```
$ easypip lock
```

This is equivarent to 

```
$ pip freeze --all > requirements.lock
```

### sync
You can install all of packages in requirements.lock by

```
$ easypip sync
```

This is equivarent to 

```
$ pip install -r requirements.lock
```

### init
You can init virtual environment by 

```
$ easypip init
```

This is equivarent to 

```
$ python -m venv .venv
```

Other subcommands (e.g., list, show, ...etc) are as same as original pip.

## install
You can install easypip by

```
$ pip install git+https://github.com/watabe951/easypip
```

also you can by pipx (recommended)

```
$ pipx install git+https://github.com/watabe951/easypip
```
