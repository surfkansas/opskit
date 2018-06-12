# OpsKit

**OpsKit** is a Python-based devops command line aggergator for devops tools.  It provides a command command line model (similar to the AWS CLI) that allows plugging in tools via pip installations.

## General Usage

To begin using **OpsKit**, you first must install it from pip:

```
pip install opskit
```

## Command Line

Once installed, you can run an **OpsKit** command as follows:

```
opskit <product> <action> [--help] [[action args]]
```

An example command might be:

```
opskit space-shuttle launch --countdown 60 
```

Each *product* is a seperate Python module.  Each *action* is a named class in that module.

## Sample Plugin

A sample plugin, along with implementation guidelines, is available at the following repository:

https://github.com/surfkansas/opskit-demo

## Release History

### 0.13.108 (obelisk)

* Improved ReadMe
* Added product description to `setup.py`

### 0.12.108 (initial)

* Initial public release

