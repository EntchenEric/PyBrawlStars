# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.4] - 2025-01-27

### Fixed
- Fixed all `__init__.py` files to properly expose library classes and modules.
- Corrected all import statements throughout the codebase to use relative imports instead of absolute imports.
- Fixed circular import issues in model files.
- Updated main package `__init__.py` to properly export `BSClient` and error classes.
- Added comprehensive model exports in `models/__init__.py` for better API accessibility.
- Fixed error class imports in the errors module.

### Changed
- Improved package structure and import organization for better developer experience.
- All model classes are now properly accessible through the main package imports.

## [1.0.3] - 2025-06-21

### Fixed
- Fix main folder not havinh `__init__.py` file.

## [1.0.2] - 2025-06-21

### Fixed
- Corrected configuration error (`pyproject.toml`).
- Moved code to `PyBrawlStars` folder.

## [1.0.1] - 2025-06-21

### Fixed
- Corrected a build configuration error (`pyproject.toml`) that excluded the source code from the final package, which made imports fail.
- Moved examples to `src` folder.

## [1.0.0] - 2025-06-21

### Added
- Initial public release of the `PyBrawlStars` library.
- Full wrapper for all official Brawl Stars API endpoints.
- Pydantic models for all API responses.