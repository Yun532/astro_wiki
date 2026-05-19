# GRB Reproduction Layer

This directory is the reproducible-model layer for the GRB knowledge base.

It follows the same hierarchy as the theory pages:

- `core/`: reusable physics and fitting utilities.
- `models/`: concrete model families built from core modules.
- `events/`: event-specific data, scripts, notebooks, and outputs.
- `validation/`: automatic and human validation records.

The first target event is GRB 221009A. The initial goal is not a full publication-grade fit; it is a traceable path from textbook equations to toy-level and then data-level reproduction.