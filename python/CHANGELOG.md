# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.13.0] - Unreleased
[0.13.0]: https://github.com/trezor/trezor-firmware/compare/python/v0.12.2...master

### Added

- Enabled session management via `EndSession`  [#1227]
- Support for temporary or permanent `safety-checks` setting
- Support for Output Descriptors export [#1363]
- PIN entry via letters  [#1496]

### Changed

- protobuf is aware of `required` fields and default values
- `btc.sign_tx()` accepts keyword arguments for transaction metadata  [#1266]

### Deprecated

- instantiating protobuf objects with positional arguments is deprecated
- values of required fields must be supplied at instantiation time. Omitting them is deprecated.
- `details` argument to `btc.sign_tx()` is deprecated. Use keyword arguments instead.

### Fixed

- added missing dependency on `attrs`  [#1232]
- fixed number imprecision in `build_tx.py` that could cause "invalid prevhash" errors

### Removed

- dropped Python 3.5 support  [#810]

