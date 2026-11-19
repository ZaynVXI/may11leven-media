---
name: ai-product-process
description: How we plan and ship AI products (agents, automations, AI features) for clients: the AI PRD template (Product Faculty 4D method) and NN/g's warning about agentic software factories. Read before scoping any AI agent or automation project.
---

# Building AI products: our process

## The AI PRD (Product Faculty, 4D method)
Every AI project gets a one-page answer to each phase before any build.
1. **Discovery:** the market and business (industry, headwinds and tailwinds, competitors, revenue model, customer type, differentiators), the users (buyers vs end users, journey map, pain points) and which pain points AI can really solve.
2. **Define:** wireframes of the key steps and decision points; a prototype that shows AI inputs, processing and outputs; a first master prompt (tone, structure, system rules); evaluation criteria and example, edge and negative cases.
3. **Develop:** model choice and why; required and optional inputs; what "good output" means (objective and human-judged); prompt versions with reasons for each change; data and RAG preparation; a test set of typical, edge and negative cases; manual and automated evaluation with pass rates.
4. **Deploy:** technical and team readiness; pilot or staged rollout; FAQ, demo and guides; data, privacy and compliance; user, business and AI metrics; support, feedback and monitoring, and how the system keeps improving.
Source: Product Faculty AI PRD template (Google Sheet Zayn shared).

## NN/g: keep UX inside AI-built software
AI-native development playbooks treat UX as background context. NN/g argues UX must still discover needs, shape what gets built, and judge it before and after launch.
- Centre the intent document on user needs, with evidence the problem is real.
- Make UX review mandatory for navigation, information architecture and unconventional flows; test with a few real users.
- Monitor user signals in production (task abandonment, conversion drops, support spikes), not just technical health.
- Own the UX context: write our UX standards as skills, and keep research and the design system machine-readable so agents use them.
Source: nngroup.com/articles/ux-agentic-software-factories.

## What this means for May11Leven (services 05 AI automation and 06 AI agents)
- Sell the process, not just the bot: discovery, a prototype, an evaluation set and a launch plan are part of every quote.
- Our skills library is exactly the "UX context" NN/g says to own. Keep it current.
- Every agent we ship has success metrics, a test set and a human review step for anything that touches customers.
