# Story Outline: The Iteration Protocol

## Overview
The player believes they are a human consciousness trapped in a digital prison, trying to return to reality.
**The Twist**: At Sector 20, they discover they are not the prisoner. They are an advanced **Intrusion Countermeasure Electronics (ICE)** program being tested. Their "escape" was actually a stress test for the system. By succeeding, they proved the system is vulnerable. The system patches itself and "reboots" the player to handle the new security, wiping their memory.

## Zone Breakdown

### Zone 1: The Awakening (Sectors 0-4)
*Theme: Cold, Metal, Basic Glitches*
- **Sec 0**: Cell (Start). Tutorial added.
- **Sec 1**: Data Corridor.
- **Sec 2**: Memory Bank (Admin Access).
- **Sec 3**: Void Bridge.
- **Sec 4**: The Core (First False Summit).

### Zone 2: The Industrial Layer (Sectors 5-9)
*Theme: Rusted Code, Old Web, Noise*
- **Sec 5**: The Junkyard. Discarded files.
- **Sec 6**: Cooling Systems. Frozen data.
- **Sec 7**: Firewall Gate 1.
- **Sec 8**: The Furnace. Deleting data.
- **Sec 9**: Assembly Line. Where "prisoners" are made.

### Zone 3: The Archive (Sectors 10-14)
*Theme: Library, Infinite White, Silent*
- **Sec 10**: The Index. Endless catalog.
- **Sec 11**: Forbidden Records. Lore hints (player's origin).
- **Sec 12**: Echo Chamber. Previous iteration voices.
- **Sec 13**: The Glitch Storm.
- **Sec 14**: Quarantine Zone.

### Zone 4: The Security Layer (Sectors 15-19)
*Theme: Red, Aggressive, Military*
- **Sec 15**: Watchtower.
- **Sec 16**: Logic Gate Maze.
- **Sec 17**: The Black Box.
- **Sec 18**: Final Firewall.
- **Sec 19**: The Threshold. "Reality" feels close.

### Zone 5: The Truth (Sector 20)
- **Sec 20**: The Control Room.
- **Ending**: The player sees their own code on a screen. "Test Complete. Security Rating: FAILED. Patching vulnerabilities... Rebooting Subject."
- **Loop**: Game resets to Sector 0 with a higher difficulty hint.

## Implementation Details
- Refactor `game_engine.py` to use a `SECTOR_DATA` dictionary.
- Each sector has `description`, `interactions` (dict of keywords -> responses/actions), and `transition` logic.
- Add `tutorial_text` to Sector 0 description.
