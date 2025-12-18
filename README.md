# langgraph-core

A minimal, focused exploration of **LangGraph** for building **stateful, agentic workflows**.

This repository demonstrates how to use LangGraph **as intended** — by defining explicit state, graph-controlled execution, and resumable workflows — without building custom agent frameworks or hiding behavior behind abstractions.

---

## Why this repo exists

Most “agent” examples mix:
- prompt logic
- tool wrappers
- orchestration
- and framework abstractions

This makes it hard to understand **what LangGraph actually does**.

This repo strips everything down to show:

> **LangGraph is a graph-based state machine that orchestrates execution — not an agent framework.**

---

## What is demonstrated

This project covers the **core LangGraph capabilities** end-to-end:

- Shared state using `StateGraph`
- Nodes as pure state transformers
- Explicit graph-defined control flow
- Conditional routing and retries
- Gemini LLM execution inside graph nodes
- Human-in-the-loop using LangGraph interrupts
- Persistent checkpointing and resume (LangGraph v1.x)

All orchestration is handled by **LangGraph itself**.

---

## High-level flow

Planner (Gemini LLM)
↓
Worker (Python logic)
↓
Verifier
↓
Human approval (interrupt)
↓
End / Retry


- Nodes perform work
- The graph decides what runs next
- State is preserved across pauses and resumes

---

## What this repo is NOT

- ❌ Not a custom agent framework
- ❌ Not a prompt-driven controller
- ❌ Not an autonomous system demo
- ❌ Not domain-specific (RCA, bots, etc.)

The goal is **clarity of orchestration**, not feature breadth.
