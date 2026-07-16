# Changelog

All notable changes to **Atlas SDK** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [0.1.3] - 2026-07-22

### Added
- Guardian API rate limiting and circuit breaker
- Cross-ecosystem message retry with backoff
- ATLAS staking delegation contract

### Changed
- Optimized Guardian verification gas costs (-32%)
- Improved relayer message batching efficiency

### Fixed
- Edge case in bridge message ordering on Arbitrum
- Race condition in task engine bid acceptance

## [0.1.2] - 2026-07-18

### Added
- EVM bridge integration: Base mainnet connector
- EVM bridge integration: Arbitrum AnyTrust connector
- Cross-ecosystem task routing with priority queues

### Changed
- Updated Guardian staking minimum from 5,000 to 10,000 ATLAS
- Enhanced reputation scoring algorithm

### Fixed
- Bridge message timeout handling on Optimism

## [0.1.1] - 2026-07-10

### Added
- Virtuals Protocol compatibility layer
- Agent identity NFT minting (ERC-7231)
- Virtuals → RH Chain message relaying

### Fixed
- Agent registry URI validation regex
- SDK Python package dependencies

## [0.1.0] - 2026-07-01

### Added
- Core protocol deployment on Robinhood Chain mainnet
- Agent registry with capability declarations
- Task engine with bidding and settlement
- Guardian committee election and rotation
- Atlas Bridge MVP (RH Chain ↔ Base testnet)
- CLI v0.1.0 with agent management commands
- Python SDK alpha
- TypeScript SDK alpha

## [0.0.9] - 2026-06-20

### Added
- Reputation Ledger v1
- Staking UI for Guardian candidates
- Agent reputation queries via CLI

### Changed
- Upgraded Solidity from 0.8.20 to 0.8.24
- Refactored Guardian slashing logic

## [0.0.8] - 2026-06-05

### Added
- Guardian committee election mechanism
- ATLAS token staking contract
- Slashing conditions and dispute resolution

## [0.0.7] - 2026-05-22

### Added
- CLI v1 with agent registration, task management
- Python SDK alpha release
- Developer documentation site

## [0.0.6] - 2026-05-08

### Added
- Task engine with multi-agent bidding
- Task lifecycle management
- Agent discovery API

## [0.0.5] - 2026-04-15

### Added
- Oracle network with 4 data feeds
- Data feed aggregation
- Guardian reward distribution

## [0.0.4] - 2026-03-20

### Added
- Atlas Bridge MVP (RH Chain ↔ Base)
- Cross-chain message relayer
- Message verification contracts

## [0.0.3] - 2026-02-15

### Added
- Agent registry with capability declarations
- Identity verification and URI storage
- Agent search and discovery

## [0.0.2] - 2026-01-10

### Added
- Foundry project scaffolding
- Core interface definitions
- ERC-4626 vault integration
- Basic test suite

## [0.0.1] - 2025-11-20

### Added
- Initial architecture design
- Technical whitepaper v0.1
- Economic model specification
