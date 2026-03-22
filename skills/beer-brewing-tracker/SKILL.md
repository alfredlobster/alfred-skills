---
name: beer-brewing-tracker
description: Track beer brewing sessions step-by-step with timers from a recipe. Use when planning or running brew day, mash/boil/fermentation milestones, and checklist progression based on a structured recipe (JSON). Supports next-step guidance, elapsed/remaining time, and completion logging.
---

# Beer Brewing Tracker

Track brew sessions using a deterministic step list with durations and checkpoints.

## Workflow
1. Build or select a recipe JSON (see `references/recipe-schema-example.json`).
2. Start a session with `scripts/brew_tracker.py start --recipe <file> --name "..."`.
3. Check current status: `scripts/brew_tracker.py status`.
4. Complete steps as you brew: `scripts/brew_tracker.py done`.
5. See upcoming timeline: `scripts/brew_tracker.py timeline`.

Session state is stored in `memory/brew-session.json` so progress survives restarts.

## Commands
- `start`: initialize a session from recipe JSON and arm first timer
- `status`: current step, elapsed/remaining time
- `remind`: print exactly what to do now + next action
- `done`: mark current step done, move to next, and arm next timer automatically
- `watch`: keep checking timer and emit reminder when step becomes due
- `timeline`: full plan with done/pending/current state
- `reset`: clear current session

Use `watch --once` for a single due reminder, or `watch` for continuous timer monitoring.

Telegram push reminders:
- `watch --telegram-chat-id <chat_id>` sends reminder when a step becomes due.
- Example for your chat: `watch --telegram-chat-id 7525103491`.

## Notes
- This is a tracker and checklist, not a control system.
- If a recipe has no duration for a step, tracker still records completion order.
- For your default clone recipe, use `references/leffe-blond-klon.json`.
