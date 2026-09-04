CREATE TABLE IF NOT EXISTS agent_route_runs (
  run_id TEXT PRIMARY KEY,
  task_id TEXT NOT NULL,
  turn_id TEXT NOT NULL,
  idempotency_key TEXT NOT NULL,
  api_key_id TEXT NOT NULL,
  virtual_route TEXT NOT NULL CHECK (virtual_route IN ('agent/normal', 'agent/high')),
  effective_review_class TEXT NOT NULL CHECK (effective_review_class IN ('standard', 'high_risk')),
  state TEXT NOT NULL DEFAULT 'created',
  output_started INTEGER NOT NULL DEFAULT 0 CHECK (output_started IN (0, 1)),
  tool_started INTEGER NOT NULL DEFAULT 0 CHECK (tool_started IN (0, 1)),
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  UNIQUE(api_key_id, task_id, turn_id, idempotency_key)
);

CREATE TABLE IF NOT EXISTS agent_route_events (
  event_id TEXT PRIMARY KEY,
  run_id TEXT NOT NULL,
  kind TEXT NOT NULL CHECK (kind IN ('output_started', 'tool_started')),
  provider TEXT,
  model TEXT,
  candidate_attempt INTEGER,
  repair_attempt INTEGER,
  admission_state TEXT,
  fallback_reason TEXT,
  latency_ms INTEGER,
  prompt_tokens INTEGER,
  completion_tokens INTEGER,
  objective_outcome TEXT,
  reviewer_class TEXT,
  reviewer_model TEXT,
  reviewer_verdict TEXT,
  subscription_percent REAL,
  subscription_evidence_id TEXT,
  subscription_evidence_at TEXT,
  subscription_decision TEXT,
  occurred_at TEXT NOT NULL,
  FOREIGN KEY(run_id) REFERENCES agent_route_runs(run_id)
);

CREATE INDEX IF NOT EXISTS idx_agent_route_events_run_occurred_at
  ON agent_route_events(run_id, occurred_at);
CREATE INDEX IF NOT EXISTS idx_agent_route_runs_task_updated_at
  ON agent_route_runs(task_id, updated_at);
CREATE INDEX IF NOT EXISTS idx_agent_route_runs_api_key_updated_at
  ON agent_route_runs(api_key_id, updated_at);
