# Procedural Audio Engine Plan

## Goal
Provide immersive, dynamic background audio for the game without using external MP3 files (to avoid broken links/loading issues).

## Architecture
Using the **Web Audio API**, we will create a `SoundEngine` class.

### Sonic Themes
1.  **Awakening (Sector 0-2)**: *Digital Hum*.
    -   Oscillator: Sine (60Hz) + Triangle (120Hz, low volume).
    -   Filter: LowPass (200Hz) to make it "muffled" and dark.
    -   Effect: Slight amplitude modulation (LFO) to simulate breathing/power fluctuation.
2.  **Void/Space (Sector 3, 12, 13)**: *Hollow Wind*.
    -   Source: Pink Noise (procedurally generated buffer).
    -   Filter: BandPass (400Hz) sweeping slowly.
    -   Reverb: Simulated by long release times.
3.  **Industrial (Sector 4-9)**: *Mechanical Grind*.
    -   Oscillator: Sawtooth (50Hz) + Square (100Hz).
    -   Modulation: Detuned slightly to create a "beating" metal sound.
4.  **Security/Danger (Sector 15-19)**: *Tension*.
    -   Oscillator: High pitched Sine (800Hz) but very quiet + Low Drone.
    -   Rhythm: Pulsing gain at 2Hz (heartbeat).
5.  **Ending (Sector 20)**: *The Glitch*.
    -   Random frequency hopping or pure silence mixed with static.

## Integration
-   **File**: `frontend/src/utils/SoundEngine.js`
-   **Control**: `App.jsx` initializes engine on first user interaction (click).
-   **Updates**: a `useEffect` hook monitors `location` state and calls `SoundEngine.setTheme(sectorNum)`.
