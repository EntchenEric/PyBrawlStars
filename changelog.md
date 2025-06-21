# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2025-06-21

### Fixed
- Corrected a build configuration error (`pyproject.toml`) that excluded the source code from the final package, which made imports fail.
- Moved examples to `src` folder.

## [1.0.0] - 2025-06-21

### Added
- Initial public release of the `PyBrawlStars` library.
- Full wrapper for all official Brawl Stars API endpoints.
- Pydantic models for all API responses.