
class SoundEngine {
    constructor() {
        this.ctx = null;
        this.masterGain = null;
        this.activeNodes = []; // Track active oscillators/nodes to stop them later
        this.currentTheme = null;
        this.isMuted = false;
        this.initialized = false;
    }

    init() {
        if (!this.initialized) {
            try {
                const AudioContext = window.AudioContext || window.webkitAudioContext;
                this.ctx = new AudioContext();
                this.masterGain = this.ctx.createGain();
                this.masterGain.gain.value = 0.6;
                this.masterGain.connect(this.ctx.destination);
                this.initialized = true;
                console.log("Musical Engine Initialized");
            } catch (e) {
                console.error("Web Audio API not supported", e);
            }
        }
    }

    async resume() {
        if (this.ctx && this.ctx.state === 'suspended') {
            await this.ctx.resume();
        }
    }

    toggleMute() {
        this.isMuted = !this.isMuted;
        if (this.masterGain) {
            this.masterGain.gain.setTargetAtTime(this.isMuted ? 0 : 0.6, this.ctx.currentTime, 0.5);
        }
        return this.isMuted;
    }

    stopAll() {
        const now = this.ctx.currentTime;
        this.activeNodes.forEach(node => {
            try {
                // Smooth fade out
                if (node.gain) {
                    node.gain.gain.cancelScheduledValues(now);
                    node.gain.gain.setValueAtTime(node.gain.gain.value, now);
                    node.gain.gain.exponentialRampToValueAtTime(0.001, now + 2); // 2s fade out
                }
                setTimeout(() => {
                    node.source.stop();
                    node.source.disconnect();
                }, 2000);
            } catch (e) { }
        });
        this.activeNodes = [];
    }

    // --- MUSICAL SYNTHESIS ---

    // Play a single note with "pad" characteristics (slow attack, long release)
    playPadNote(freq, type = 'sine', volume = 0.1, detune = 0) {
        const osc = this.ctx.createOscillator();
        const gain = this.ctx.createGain();
        const filter = this.ctx.createBiquadFilter();

        osc.type = type;
        osc.frequency.value = freq;
        osc.detune.value = detune;

        // Filter to soften the sound
        filter.type = 'lowpass';
        filter.frequency.value = 2000;

        // Envelope (ADSR)
        const now = this.ctx.currentTime;
        gain.gain.setValueAtTime(0, now);
        gain.gain.linearRampToValueAtTime(volume, now + 2); // 2s Attack (Slow swell)

        osc.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);

        osc.start();

        // LFO for movement (Chorus effect)
        const lfo = this.ctx.createOscillator();
        lfo.type = 'sine';
        lfo.frequency.value = 0.1 + Math.random() * 0.2; // Slow movement
        const lfoGain = this.ctx.createGain();
        lfoGain.gain.value = 5; // Detune amount
        lfo.connect(lfoGain);
        lfoGain.connect(osc.detune);
        lfo.start();

        this.activeNodes.push({ source: osc, gain: gain });
        this.activeNodes.push({ source: lfo, gain: null }); // Track LFO to stop it too
    }

    playChord(frequencies, type = 'sine', volume = 0.1) {
        frequencies.forEach((freq, i) => {
            // Layer slight detuning for richness
            this.playPadNote(freq, type, volume, 0);
            this.playPadNote(freq, type, volume * 0.5, 3); // Slightly sharp
            this.playPadNote(freq, type, volume * 0.5, -3); // Slightly flat
        });
    }

    createNoiseDrone() {
        const bufferSize = 2 * this.ctx.sampleRate;
        const buffer = this.ctx.createBuffer(1, bufferSize, this.ctx.sampleRate);
        const output = buffer.getChannelData(0);
        for (let i = 0; i < bufferSize; i++) {
            output[i] = Math.random() * 2 - 1;
        }

        const noise = this.ctx.createBufferSource();
        noise.buffer = buffer;
        noise.loop = true;

        const filter = this.ctx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.value = 150; // Deep rumble

        const gain = this.ctx.createGain();
        gain.gain.value = 0.05;

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(this.masterGain);
        noise.start();

        this.activeNodes.push({ source: noise, gain: gain });
    }

    // --- THEMES ---

    playTheme(sectorNum) {
        if (!this.initialized) return;

        // Determine Theme
        let theme = 'default';
        if (sectorNum >= 0 && sectorNum <= 2) theme = 'awakening';
        else if (sectorNum === 3 || sectorNum === 12 || sectorNum === 13) theme = 'void';
        else if (sectorNum >= 4 && sectorNum <= 9) theme = 'industrial';
        else if (sectorNum >= 15 && sectorNum <= 19) theme = 'danger';
        else if (sectorNum === 20) theme = 'ending';

        if (this.currentTheme === theme) return;

        this.stopAll();
        this.currentTheme = theme;
        console.log(`Playing Musical Theme: ${theme}`);

        if (theme === 'awakening') {
            // Theme: "Cold Isolation"
            // Chord: C Minor (C3, Eb3, G3) + Low C2 Drone
            // Sound: Sine/Triangle pads
            this.playPadNote(65.41, 'triangle', 0.2); // C2 (Bass)
            this.playChord([130.81, 155.56, 196.00], 'sine', 0.1); // Cm (C3, Eb3, G3)

        } else if (theme === 'industrial') {
            // Theme: "Rusted Machinery"
            // Chord: D Diminished / Dissonant
            // Sound: Sawtooth (filtered)
            this.playPadNote(36.71, 'sawtooth', 0.15); // D1 (Deep Bass)
            this.playChord([73.42, 103.83, 146.83], 'sawtooth', 0.05); // D Bass + notes
            this.createNoiseDrone(); // Add mechanical rumble

        } else if (theme === 'void') {
            // Theme: "Empty Space"
            // Chord: Suspended, Airy
            // Sound: High Sine waves with slow pulsing
            this.playPadNote(110.00, 'sine', 0.1); // A2
            this.playChord([220.00, 329.63, 493.88], 'sine', 0.08); // A Major ish / Spacey (A3, E4, B4)

        } else if (theme === 'danger') {
            // Theme: "Hunter"
            // Chord: Cluster / Horror
            this.playPadNote(58.27, 'sawtooth', 0.2); // Bb1 (Aggressive Bass)
            this.playChord([466.16, 493.88, 523.25], 'triangle', 0.05); // High Cluster (Bb4, B4, C5) - Tension

        } else if (theme === 'ending') {
            // Theme: "The Truth"
            // Just a pure, sad C Major chord fading in and out
            this.playPadNote(261.63, 'sine', 0.1); // C4
            this.playPadNote(329.63, 'sine', 0.1); // E4
            this.playPadNote(392.00, 'sine', 0.1); // G4
            this.createNoiseDrone();
        }
    }
}

export const soundEngine = new SoundEngine();
