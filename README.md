# opskit

**opskit** is a Python-based devops command line aggergator for devops tools.  It provides a command command line model (similar to the AWS CLI) that allows plugging in tools via pip installations.

## General Usage

To begin using **opskit**, you first must install it from pip:

```
pip install opskit
```

## Command Line

Once installed, you can run an **opskit** command as follows:

```
opskit <product> <action> [--help] [[action args]]
```

An example command might be:

```
opskit space-shuttle launch --countdown 60 
```

Each *product* in opskit is a seperate Python module.  Each *action* is a named class in that module.

## Release History

### 0.8.108 (obelisk)

* Initial public release

