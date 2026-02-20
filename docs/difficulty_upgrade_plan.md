# Difficulty & Scenario Upgrade Plan

## Goal
1.  **Fix Visuals**: Ensure all sector images use short, atmospheric text instead of full descriptions.
2.  **Increase Difficulty**: Replace simple "Click -> Win" mechanics with multi-step puzzles requiring investigation and item usage.

## 1. Visual Fix: Short Descriptions
Update `SECTOR_DATA` in `game_engine.py` to include `short_desc` for all sectors (0-20).

| Sector | Short Description Idea |
| :--- | :--- |
| 1 (Corridor) | "네온 그리드 복도. 데이터 큐브 부유 중." |
| 2 (Memory) | "거대한 서버 랙. 붉은 경고등 점멸." |
| 3 (Void) | "끝없는 심연. 끊어진 다리와 포털." |
| ... | ... |

## 2. Gameplay Mechanics: State & Multi-step Puzzles
Currently, `sector_unlocked` is a simple boolean. We need a dictionary `sector_states` to track progress within a sector.

### New Action Types in `keywords`
-   `get_item`: Adds item to inventory.
-   `req_item`: Requires specific item in inventory to proceed.
-   `state_change`: Updates `sector_states[current_sector]` (e.g., from `locked` to `power_on`).
-   `minigame`: Only triggers if specific state is met.

### Revised Scenarios (Sectors 0-2)

#### Sector 0: Awakening
-   **Current**: Look Photo -> Scan -> Get Key -> Unlock.
-   **New Flow**:
    1.  **Look [Bed]**: Find "Hairpin" (Fuel/Tool?).
    2.  **Look [Terminal]**: "Power off. Check cables."
    3.  **Look [Cables]**: "Cut. Need to splice." -> Use [Hairpin] -> Power On.
    4.  **Look [Photo]**: Get "Passcode Fragment 1".
    5.  **Use Terminal**: Enter Code -> Unlocks Door.

#### Sector 1: Data Corridor
-   **Current**: Hack Cube -> Hack Wall.
-   **New Flow**:
    1.  **Look [Debris]**: Find "Encrypted Drive".
    2.  **Look [Cube]**: "Needs Drive to decrypt." -> Use [Drive].
    3.  **Minigame**: Decryption Puzzle. -> Get "Firewall Key".
    4.  **Look [Firewall]**: Use [Key] -> Opens.

#### Sector 2: Memory Bank
-   **Current**: Fix Server -> Done.
-   **New Flow**:
    1.  **Look [Server]**: "Overheated. Cooling system offline."
    2.  **Look [Floor]**: Find "Empty Coolant Canister".
    3.  **Go Back to Sec 0/1?** (maybe too complex for now, keep local).
    4.  **Look [Vents]**: "Leaking liquid nitrogen." -> Use [Canister] -> Get "Filled Canister".
    5.  **Use [Canister] on [Server]**: Cooled down.
    6.  **Hack Server**: Now possible.

## Implementation Steps
1.  Modify `SECTOR_DATA` to add `short_desc` and new keywords/states.
2.  Update `ScenarioMaster.process_input` to handle:
    -   `state_change` logic.
    -   Complex `req_item` checks (e.g., "Use X on Y").
    -   Dynamic descriptions based on state (e.g., Terminal description changes after power on).
