# Obsolete

The Chromium team now maintains GN as a standalone project, making this unofficial version obsolete.

You can find the official version at https://gn.googlesource.com/gn.

# Standalone GN

[![Build Status](https://travis-ci.org/timniederhausen/gn.svg?branch=master)](https://travis-ci.org/timniederhausen/gn)
[![Build status](https://ci.appveyor.com/api/projects/status/h6csk52w7dr73tgn/branch/master?svg=true)](https://ci.appveyor.com/project/timniederhausen/gn/branch/master)

This repo contains a standalone version of Chromium's GN build system.

For more information regarding GN itself see [here](https://github.com/timniederhausen/gn/blob/gn/master/README.md).

Note that this project is work-in-progress and not affliated with Chromium or Google.

## Building

### With GN installed

```
gn gen out/Release --args="is_debug=false"

ninja -C out/Release gn
```

See [here](https://github.com/timniederhausen/gn-build/blob/master/README.md#reference)
for a reference of the most commonly used build args.

To get a list of all possible build args use `gn args out/Release --list`.
Note that currently this emits a long list of Chromium-related args
which have no influence on the GN build.

If you intend to work on GN, the output directory should be two levels
deep inside the source tree, because the GN tests use hardcoded relative
paths (see base/base_paths_*.cc: `DIR_SOURCE_ROOT` handling)

### Without GN

```
tools/gn/bootstrap/bootstrap.py
```

Note: On Windows bootstrap.py expects to be run inside a
Visual Studio Command Prompt (i.e. vcvarsall has been run).
