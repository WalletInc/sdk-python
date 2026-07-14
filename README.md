![Wallet Inc](https://resources.wallet.inc/logos/wallet-350x96.png)

# Wallet SDK for Python

The official server-side Python SDK for the [Wallet Inc](https://wallet.inc) CRM & Digital Payments platform. Create and manage membership tiers, club members, vouchers, promotions, store credit, payment designs, SMS/MMS, and more.

> **Access note:** this module is currently restricted to Wallet Inc customers. Need access or a hand getting started? Join us on [Discord](https://discord.gg/xzwhcNCjcQ).

## Links

- Website: https://wallet.inc
- Developer docs: https://wallet.dev
- API status: https://uptime.wallet.inc
- All SDKs: https://github.com/walletinc

## Requirements

Python 3.7+.

## Installation

```bash
pip install wallet
```

## Quickstart

Point the client at the API host and send your API key as the `access-token` header. Create your key in the [Wallet Developer Hub](https://wallet.dev).

```python
import wallet

# Host defaults to https://api.wall.et.
configuration = wallet.Configuration(host="https://api.wall.et")
# Your API key is sent as the "access-token" header.
configuration.api_key["api_key"] = "YOUR_API_KEY"

with wallet.ApiClient(configuration) as api_client:
    # Each resource has its own *Api class (MembershipTiersApi, ClubMembersApi, SmsApi, ...).
    membership_tiers = wallet.MembershipTiersApi(api_client)
    # See the docs/ folder for every method and model.
```

## Documentation

Full API reference and guides live in the [Wallet Developer Hub](https://wallet.dev). Per-endpoint method docs and model definitions for this client are generated into the [`docs/`](docs/) folder of this repository.

## About Wallet Inc

[Wallet Inc](https://wallet.inc) is a CRM and digital payments platform: digital membership cards, loyalty and rewards, vouchers and store credit, Apple & Google Wallet passes, and SMS/MMS marketing. Learn more at [wallet.inc](https://wallet.inc) and explore the APIs at the [Wallet Developer Hub](https://wallet.dev).

## License

Copyright 2026 Wallet Inc.

This SDK is licensed under the Apache License, Version 2.0. See the `LICENSE` and `NOTICE` files for the full text. You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0.

This SDK is auto-generated from the Wallet OpenAPI specification. Please file issues rather than submitting code pull requests: the generated sources are overwritten on each API release, so code PRs cannot be merged.
