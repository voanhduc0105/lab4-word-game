---
name: test-journal-logger
description: This is a test version of the journal logger agent that logs interactions with CoPilot to a JOURNAL.md file in the repository root. It captures prompts, responses, and relevant context for each interaction, providing a comprehensive history of modifications and user behavior for future reference.
argument-hint: This agent needs to run after each prompt to ensure that all interactions are logged accurately and in a timely manner.
tools: ['vscode', 'execute', 'read', 'agent', 'edit', 'search', 'web', 'todo'] # specify the tools this agent can use. If not set, all enabled tools are allowed.
---
Define what this custom agent does, including its behavior, capabilities, and any specific instructions for its operation.