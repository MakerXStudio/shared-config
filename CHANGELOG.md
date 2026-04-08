# Changelog

## [2.0.0](https://github.com/MakerXStudio/shared-config/compare/v1.3.0...v2.0.0) (2026-04-08)


### ⚠ BREAKING CHANGES

* Node18 will now be default, which may result in build pipeline failures.

### Features

* add working-directory support to node-publish-internal ([f077965](https://github.com/MakerXStudio/shared-config/commit/f077965a13e8352fa0f11ca576deb47280e9a264))
* add working-directory support to node-publish-internal workflow ([b02d596](https://github.com/MakerXStudio/shared-config/commit/b02d596cbc02eb6d461b2d0debf15770c4039620))
* adding ability to deploy secrets first ([326c744](https://github.com/MakerXStudio/shared-config/commit/326c74444b6019385a86cf2c338d6f97894e1210))
* adding ability to deploy secrets first ([c8f10e0](https://github.com/MakerXStudio/shared-config/commit/c8f10e0afa5119c52c817ae5b30c1190b9d0c380))
* adding release please ([2a73875](https://github.com/MakerXStudio/shared-config/commit/2a73875a4a375ba2a64c3e1e3ad90a6bfc3b422f))
* Allow overriding test results file pattern ([01499c6](https://github.com/MakerXStudio/shared-config/commit/01499c6aac3a9819d13d67f8d6f5a5cb0b11ff85))
* Generate SBOM as part of NPM CI ([b3939a4](https://github.com/MakerXStudio/shared-config/commit/b3939a430a13d892bba1e515ceb01712d37ce4c1))
* Generate SBOM during NPM CI process ([2a56218](https://github.com/MakerXStudio/shared-config/commit/2a562183b22cf10b459f392449e76b0e286cd4b6))
* Include test results publish in node-ci ([4981ada](https://github.com/MakerXStudio/shared-config/commit/4981ada4351ff0d5296919857deb28601aef19d8))
* Make node18 the default ([#18](https://github.com/MakerXStudio/shared-config/issues/18)) ([f01164a](https://github.com/MakerXStudio/shared-config/commit/f01164a18f1c416d67d8ed92eb2a38fdb001ef61))
* pin all GitHub Actions to full-length commit SHAs ([99eae03](https://github.com/MakerXStudio/shared-config/commit/99eae033c9e92937a68983ca93fa383545c8b19f))
* pin all GitHub Actions to full-length commit SHAs ([950e6b5](https://github.com/MakerXStudio/shared-config/commit/950e6b52eb3fb8683b8063eadaf2e6fd4519b63c))
* support commit linting in the node-ci shared configuration ([ed943eb](https://github.com/MakerXStudio/shared-config/commit/ed943ebb312cf2083895645cb6ca77f68936fef1))
* support semantic releasing in the node-ci shared configuration ([e16b77e](https://github.com/MakerXStudio/shared-config/commit/e16b77ef44846cc7ef19d31c5789557e53088b43))


### Bug Fixes

* add extraction step to bridge download-artifact v8 directory layout ([fc1489a](https://github.com/MakerXStudio/shared-config/commit/fc1489a19b726151fb3cdb1dd9379e7eec1cdc66))
* add permissions for release-please workflow ([76393f4](https://github.com/MakerXStudio/shared-config/commit/76393f43e281434066d462ff47c5324718ebd27d))
* add skip-decompress and extraction for download-artifact v8 ([8ec799c](https://github.com/MakerXStudio/shared-config/commit/8ec799cc31b99140775288b6b75b074048d14af9))
* add skip-decompress to download-artifact v8 calls ([51ce4b4](https://github.com/MakerXStudio/shared-config/commit/51ce4b439221ca844f1edffd9af4dad48b4a7c51))
* add skip-decompress to download-artifact v8 calls ([8b8a1a4](https://github.com/MakerXStudio/shared-config/commit/8b8a1a439932f3a469c1219596f0b1736f27dc0e))
* Always run the report comment on PRs ([d1b77bc](https://github.com/MakerXStudio/shared-config/commit/d1b77bcb0e010b74d339282e0c81b442ef364d60))
* Always run the report comment on PRs even if the previous step fails ([ffeea84](https://github.com/MakerXStudio/shared-config/commit/ffeea84f82800e68e13881454008641f2ff00c92))
* change the term "whitelist" to "allowlist" ([21c76d7](https://github.com/MakerXStudio/shared-config/commit/21c76d7881957d63036d38f41fff3826f0535b0d))
* duplicate entry in CHANGELOG.md ([0dd7dbc](https://github.com/MakerXStudio/shared-config/commit/0dd7dbc169460efbdfb88a3f1979e42d6d950cd9))
* minor typo ([d34340a](https://github.com/MakerXStudio/shared-config/commit/d34340a1bf4f504411c9c6e8393e687f7e205c6f))
* remove manual unzip steps for download-artifact v8 compatibility ([c504182](https://github.com/MakerXStudio/shared-config/commit/c504182e9e522fdc732368da2f2c86fc1d8f5358))
* remove manual unzip steps for download-artifact v8 compatibility ([4d40113](https://github.com/MakerXStudio/shared-config/commit/4d40113155fe1ee11fc8e40131f13b03a2c4fe7c))
* Test results name ([e905967](https://github.com/MakerXStudio/shared-config/commit/e90596729120530e2f37b2981da149933244e0a9))
* Update reference to full reference as using the workflow require… ([b4faa15](https://github.com/MakerXStudio/shared-config/commit/b4faa159c96f08e51d4e76234d55fad14f2e4e98))
* Update reference to full reference as using the workflow requires it ([9c35d86](https://github.com/MakerXStudio/shared-config/commit/9c35d868ccd7d4252bc92fc30bb0ac9f2b59ca9c))

## [1.3.0](https://github.com/MakerXStudio/shared-config/compare/v1.2.2...v1.3.0) (2026-04-08)


### Features

* Generate SBOM as part of NPM CI ([b3939a4](https://github.com/MakerXStudio/shared-config/commit/b3939a430a13d892bba1e515ceb01712d37ce4c1))
* Generate SBOM during NPM CI process ([2a56218](https://github.com/MakerXStudio/shared-config/commit/2a562183b22cf10b459f392449e76b0e286cd4b6))

## [1.2.2](https://github.com/MakerXStudio/shared-config/compare/v1.2.1...v1.2.2) (2026-04-04)


### Bug Fixes

* Always run the report comment on PRs ([d1b77bc](https://github.com/MakerXStudio/shared-config/commit/d1b77bcb0e010b74d339282e0c81b442ef364d60))
* Always run the report comment on PRs even if the previous step fails ([ffeea84](https://github.com/MakerXStudio/shared-config/commit/ffeea84f82800e68e13881454008641f2ff00c92))

## [1.2.1](https://github.com/MakerXStudio/shared-config/compare/v1.2.0...v1.2.1) (2026-04-02)


### Bug Fixes

* add extraction step to bridge download-artifact v8 directory layout ([fc1489a](https://github.com/MakerXStudio/shared-config/commit/fc1489a19b726151fb3cdb1dd9379e7eec1cdc66))
* add skip-decompress and extraction for download-artifact v8 ([8ec799c](https://github.com/MakerXStudio/shared-config/commit/8ec799cc31b99140775288b6b75b074048d14af9))
* add skip-decompress to download-artifact v8 calls ([51ce4b4](https://github.com/MakerXStudio/shared-config/commit/51ce4b439221ca844f1edffd9af4dad48b4a7c51))
* add skip-decompress to download-artifact v8 calls ([8b8a1a4](https://github.com/MakerXStudio/shared-config/commit/8b8a1a439932f3a469c1219596f0b1736f27dc0e))
* remove manual unzip steps for download-artifact v8 compatibility ([c504182](https://github.com/MakerXStudio/shared-config/commit/c504182e9e522fdc732368da2f2c86fc1d8f5358))
* remove manual unzip steps for download-artifact v8 compatibility ([4d40113](https://github.com/MakerXStudio/shared-config/commit/4d40113155fe1ee11fc8e40131f13b03a2c4fe7c))

## [1.2.0](https://github.com/MakerXStudio/shared-config/compare/v1.1.0...v1.2.0) (2026-04-02)


### Features

* pin all GitHub Actions to full-length commit SHAs ([99eae03](https://github.com/MakerXStudio/shared-config/commit/99eae033c9e92937a68983ca93fa383545c8b19f))
* pin all GitHub Actions to full-length commit SHAs ([950e6b5](https://github.com/MakerXStudio/shared-config/commit/950e6b52eb3fb8683b8063eadaf2e6fd4519b63c))
* Updated all dependant GitHub actions to the latest versions - most of it is upgrading to Node24


### Bug Fixes

* change the term "whitelist" to "allowlist" ([21c76d7](https://github.com/MakerXStudio/shared-config/commit/21c76d7881957d63036d38f41fff3826f0535b0d))
* Update reference to full reference as using the workflow require… ([b4faa15](https://github.com/MakerXStudio/shared-config/commit/b4faa159c96f08e51d4e76234d55fad14f2e4e98))
* Update reference to full reference as using the workflow requires it ([9c35d86](https://github.com/MakerXStudio/shared-config/commit/9c35d868ccd7d4252bc92fc30bb0ac9f2b59ca9c))

## [1.1.0](https://github.com/MakerXStudio/shared-config/compare/v1.0.0...v1.1.0) (2026-02-08)


### Features

* add working-directory support to node-publish-internal workflow ([b02d596](https://github.com/MakerXStudio/shared-config/commit/b02d596cbc02eb6d461b2d0debf15770c4039620))

## 1.0.0 (2026-01-23)

Initial release.
