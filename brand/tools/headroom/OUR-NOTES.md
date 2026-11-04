# Headroom — how we use it
What: Apache-2.0 library that compresses what an AI app sends to the model (logs, JSON, tool results, long chat) so it uses fewer tokens. Runs locally, free, no key.
Where it helps us: AI agents and chatbots we build for clients (booking bots, shop assistants, lead triage). Add `compress()` before each model call to cut their running cost, and show tokens_before -> tokens_after in the handover.
Rules:
- Base package only (`pip install headroom-ai`); set HEADROOM_OFFLINE=1 in builds.
- Never quote a savings percentage to a client; measure on their data.
- Not used to wrap our own sessions.
