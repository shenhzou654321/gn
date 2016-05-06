# Standalone GN

[![Build Status](https://travis-ci.org/timniederhausen/gn.svg?branch=master)](https://travis-ci.org/timniederhausen/gn)

This repo contains a standalone version of Chromium's GN build system.

For more information regarding GN itself see [here](https://github.com/timniederhausen/gn/blob/gn/master/README.md).

Note that this project is work-in-progress and not affliated with Chromium or Google.

## Building

### On Windows

```
gn gen out/Release --args="visual_studio_version=\"2015\" is_debug=false"
ninja -C out/Release gn
```

### Everywhere else

```
tools/gn/bootstrap/bootstrap.py
```
