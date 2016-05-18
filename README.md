# Standalone GN

[![Build Status](https://travis-ci.org/timniederhausen/gn.svg?branch=master)](https://travis-ci.org/timniederhausen/gn)

This repo contains a standalone version of Chromium's GN build system.

For more information regarding GN itself see [here](https://github.com/timniederhausen/gn/blob/gn/master/README.md).

Note that this project is work-in-progress and not affliated with Chromium or Google.

## Building

### With GN installed

```
# Windows
gn gen out/Release --args="visual_studio_version=\"2015\" is_debug=false"

# POSIX
gn gen out/Release --args="is_debug=false"

ninja -C out/Release gn
```

See [here](https://github.com/timniederhausen/gn-build/blob/master/README.md#reference)
for a list of supported build arguments.

To get a list of all possible build args use `gn args out/Release --list`.
Note that currently this emits a long list of Chromium-related args
which have no influence on the GN build.

If you intend to work on GN, the output directory should be two levels
deep inside the source tree, because the GN tests use hardcoded relative
paths (see base/base_paths_*.cc: `DIR_SOURCE_ROOT` handling)

### Without GN

_Note_: This currently doesn't work on Windows.

```
tools/gn/bootstrap/bootstrap.py
```
