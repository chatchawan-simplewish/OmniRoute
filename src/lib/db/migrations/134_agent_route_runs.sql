CREATE TABLE IF NOT EXISTS agent_route_runs (
  run_id TEXT PRIMARY KEY,
  api_key_id TEXT NOT NULL,
  task_id TEXT NOT NULL,
  effective_review_class TEXT NOT NULL CHECK (effective_review_class IN ('standard', 'high_risk')),
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  UNIQUE (api_key_id, task_id)
);
CREATE TABLE IF NOT EXISTS agent_route_turns (
  run_id TEXT NOT NULL,
  turn_id TEXT NOT NULL,
  idempotency_key TEXT NOT NULL,
  virtual_route TEXT NOT NULL CHECK (virtual_route IN ('agent/normal', 'agent/high')),
  state TEXT NOT NULL CHECK (state IN ('active', 'stopping', 'completed', 'blocked', 'failed', 'cancelled')),
  output_started INTEGER NOT NULL DEFAULT 0 CHECK (output_started IN (0, 1)),
  tool_started INTEGER NOT NULL DEFAULT 0 CHECK (tool_started IN (0, 1)),
  dispatch_claimed INTEGER NOT NULL DEFAULT 0 CHECK (dispatch_claimed IN (0, 1)),
  created_at TEXT NOT NULL,
  updated_at TEXT NOT NULL,
  PRIMARY KEY (run_id, turn_id),
  UNIQUE (run_id, idempotency_key),
  FOREIGN KEY (run_id) REFERENCES agent_route_runs(run_id)
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_agent_route_active_turn ON agent_route_turns(run_id)
  WHERE state IN ('active', 'stopping');
CREATE TABLE IF NOT EXISTS agent_route_events (
  event_id TEXT PRIMARY KEY,
  run_id TEXT NOT NULL,
  turn_id TEXT NOT NULL,
  idempotency_key TEXT NOT NULL,
  kind TEXT NOT NULL CHECK (kind IN ('output_started', 'tool_started', 'dispatch', 'result', 'subscription')),
  provider TEXT,
  model TEXT,
  connection_id TEXT,
  candidate_attempt INTEGER,
  repair_attempt INTEGER,
  reviewer_attempt INTEGER,
  admission_state TEXT,
  fallback_reason TEXT,
  latency_ms INTEGER,
  busy_slots INTEGER,
  processing_requests INTEGER,
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
  FOREIGN KEY (run_id, turn_id) REFERENCES agent_route_turns(run_id, turn_id)
);
CREATE INDEX IF NOT EXISTS idx_agent_route_events_turn ON agent_route_events(run_id, turn_id, occurred_at);
