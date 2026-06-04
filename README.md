# CLI Banking System

A terminal-based banking simulation engineered with functional decomposition to handle continuous financial transactions.

## Architecture & Tech Stack
* **Language:** Python 3.x
* **Standard Libraries:** `time` (utilized to simulate transaction processing latency and pace console UX).
* **State Management:** Modular functions (`show_balance`, `deposit`, `withdraw`) invoked via a primary `while` loop to handle continuous user sessions.

## Logic & Validation Metrics
* **Exception Handling:** Implements `try-except ValueError` blocks during float type-casting to prevent fatal crashes from invalid alphanumeric input.
* **Transaction Validation:** Contains strict conditional checks to prevent negative float deposits and enforce overdraft protection (withdrawal amounts cannot exceed the active balance).

## Execution
```bash
git clone [https://github.com/MauryaAG07/cli-banking-system.git](https://github.com/MauryaAG07/cli-banking-system.git)
cd cli-banking-system
python src/Banking.py
