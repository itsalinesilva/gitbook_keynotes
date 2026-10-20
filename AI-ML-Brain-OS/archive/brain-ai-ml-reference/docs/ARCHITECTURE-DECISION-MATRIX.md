# Architecture Decision Matrix

| Decision | Start with | Escalate when evidence shows | Required evidence |
|---|---|---|---|
| Direct call vs agent | Direct call / deterministic workflow | Contextual branching and tool decisions matter | E2E eval uplift vs baseline |
| Single vs multi-agent | Single agent or explicit workers | Independent parallelism or specialization yields net gain | Quality, latency, cost, failure rate comparison |
| RAG vs fine-tune | Search/RAG for changing facts; prompt/examples for behavior | Repeated behavior gap persists after retrieval and prompt iteration | Versioned eval set, dataset rights, regression suite |
| Vector DB vs relational | Existing SQL + lexical/vector extension where sufficient | Scale/query needs outgrow current system | Recall/latency/ops benchmark |
| Managed vs self-hosted | Managed if compliance and economics allow | Control, privacy, economics, or latency justify self-hosting | TCO and risk assessment |
| Workflow engine vs app code | App code for short predictable tasks | Durable long-running state and retries become material | Failure recovery test and ops requirements |
| Graph RAG vs hybrid retrieval | Hybrid lexical+dense | Multi-hop entity relations are a proven bottleneck | Retrieval eval by question class |
| Fine-tune vs train from scratch | Fine-tune/pretrained baseline | Strategic data/control and scale justify training | Benchmark, data volume, budget, team and TCO |
| Autonomous action vs approval | Draft/propose first | Low-risk reversible scope is proven reliable | Risk assessment, audit, rollback and evals |

Never make a framework choice without recording owner, alternatives, license, security posture, portability, cost, operational burden, and exit strategy.
