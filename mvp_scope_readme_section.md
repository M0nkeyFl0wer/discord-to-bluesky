## 🚀 MVP Scope: Have I Been Rekt

The goal of this MVP is to create a usable, crypto-native incident response tool to help users understand if their wallet has been compromised. The MVP includes:

### Features
- **Wallet Compromise Form**: Front-end form to collect user symptoms (address, time of loss, description)
- **Input Validation**: Regex-based wallet format check and required fields
- **Privacy Notice**: User consent checkbox with legal disclaimer
- **Deployment**: Hosted on Vercel or AWS with .env support
- **API Endpoint**: Backend route to receive and process submissions
- **AI Integration**: Use OpenAI GPT to summarize wallet behavior and likely attack vector
- **Wallet Connect**: Support for wagmi or web3modal to connect directly
- **Payment Gateway**: Stripe and/or on-chain (ETH, USDC) payments
- **OSINT Report Access**: Premium report gated behind payment
- **README + Study Guide**: Clear contributor onboarding and system diagram
- **Community Testing**: Feedback loop and real-world validation

---

## 🧪 Future Scope & Stretch Goals

After MVP delivery, future development may include:

- **SpiderFoot Plugin**: Full integration with SpiderFoot for advanced OSINT
- **AI Agent (KINT)**: Open-source autonomous wallet forensics agent
- **Multimedia Analysis**: ExifTool, geolocation, image matching
- **Blockchain Forensics**: Path tracing via Etherscan, Bitquery, and custom heuristics
- **Privacy Tools**: Optional redaction using ZK tools like Holonym
- **Immutable Publishing**: IPFS, OrbitDB, and verifiable audit logs
- **CLI + GUI**: Expand beyond form-based access to a full OSINT toolkit
- **Crypto + Fiat Payments**: Multi-chain payments and privacy-preserving invoicing
- **Collaboration Tools**: Sub-issue tracking, saved investigations, team access

This roadmap represents our commitment to open infrastructure for blockchain safety and transparency.
