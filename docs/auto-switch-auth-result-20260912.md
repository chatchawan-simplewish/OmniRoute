# Caller authentication diagnosis

The reviewed one-time metadata GET to the configured OmniRoute origin `/v1/models` returned HTTP 401. Script SHA256: `e52e9105d1fd31a124446d9fcd01867c2badf201f857cdfbde2df98da2fc6c63`; contract SHA256: `8a3d84ea57c347cf8a4968532a9f196aa5ac5af41481b3ac8f9ecbbf1a85e9eb`. Both were checked before execution. No inference or configuration change occurred.

The configured environment reference is OMNIROUTE_ADMIN_TOKEN; process and user values are present and equal. Values were not emitted. The configured endpoint is `http://192.168.1.68:20128/api/mcp/stream`.

Source review found no justified forwarding patch. MCP management accepts several authentication classes and can admit requests when requireLogin is disabled; client API authentication uses persisted API-key validation. A functioning management call therefore does not prove an inference key is valid. The environment variable name is a caller-side reference, not a special server credential class.

Next: inspect only reviewed live authentication-policy metadata, then prepare the smallest scoped credential remedy if needed. Do not add an inference bypass, rotate upstream providers, retry spent probes, or deploy client defaults based on management health.
