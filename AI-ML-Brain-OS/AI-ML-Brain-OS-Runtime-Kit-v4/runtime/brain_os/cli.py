import argparse, json, logging
from .contracts import TaskEnvelope
from .orchestrator import BrainOrchestrator
from .policy import PolicyEngine
from .tools import ToolRegistry, echo_tool
from .store import BrainStore

def build_runtime():
    tools = ToolRegistry()
    tools.register("echo", echo_tool)
    return BrainOrchestrator(tools, PolicyEngine({"echo"}))

def main():
    parser = argparse.ArgumentParser(prog="brain-os")
    sub = parser.add_subparsers(dest="command", required=True)
    run = sub.add_parser("run")
    run.add_argument("objective")
    run.add_argument("--max-steps", type=int, default=8)
    health = sub.add_parser("health")
    health.add_argument("--db", default="data/brain_os.sqlite3")
    args = parser.parse_args()
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    if args.command == "run":
        result = build_runtime().run(TaskEnvelope(objective=args.objective, max_steps=args.max_steps))
        print(json.dumps(result.__dict__, ensure_ascii=False, indent=2))
        raise SystemExit(0 if result.status == "completed" else 2)
    store = BrainStore(args.db)
    print(json.dumps({"status":"ok","database":str(store.path),
                      "tables":["sources","documents","memory_proposals"]}))
