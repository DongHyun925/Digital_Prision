function StatusPanel({ status, inventory, location, onHint }) {
    return (
        <div className="flex flex-col gap-6 h-full">
            {/* System Status Block */}
            <div className="border border-cyber-primary p-4 bg-black/40 shadow-[0_0_10px_rgba(0,255,65,0.1)]">
                <h3 className="text-cyber-warning text-sm font-bold border-b border-cyber-warning/30 pb-2 mb-2">SYSTEM STATUS</h3>
                <div className="text-2xl font-bold animate-pulse-fast text-cyber-glitch">
                    {status}
                </div>
                <div className="mt-2 text-xs text-gray-400">
                    INTEGRITY: 98% <br />
                    MEMORY: STABLE
                </div>
            </div>

            {/* Inventory Block */}
            <div className="border border-cyber-primary p-4 bg-black/40 flex-1">
                <h3 className="text-cyber-primary text-sm font-bold border-b border-cyber-primary/30 pb-2 mb-2">INVENTORY</h3>

                {inventory && inventory.length > 0 ? (
                    <div className="grid grid-cols-2 gap-2">
                        {inventory.map((item, i) => (
                            <div key={i} className="bg-cyber-dark/80 p-2 border border-cyber-primary/20 text-xs hover:bg-cyber-primary hover:text-black cursor-pointer transition-colors">
                                {item}
                            </div>
                        ))}
                    </div>
                ) : (
                    <div className="text-gray-600 text-sm italic py-4 text-center">
                        NO ITEMS DETECTED
                    </div>
                )}
            </div>

            {/* Tactical Map Display */}
            <div className="border border-cyber-primary p-0 bg-black relative h-64 overflow-hidden group">
                <h3 className="absolute top-2 left-2 text-cyber-primary text-xs font-bold tracking-[0.2em] z-10 bg-black/50 px-2">SECTOR MAP</h3>

                {/* Visual SVG Map */}
                <div className="w-full h-full opacity-80 group-hover:opacity-100 transition-opacity">
                    <svg className="w-full h-full bg-[#050505]" viewBox="0 0 300 200">
                        {/* Grid Pattern */}
                        <defs>
                            <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
                                <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1a2e29" strokeWidth="0.5" />
                            </pattern>
                        </defs>
                        <rect width="100%" height="100%" fill="url(#grid)" />

                        {/* Map Paths (Sectors) */}
                        {/* Sector 0: The Cube */}
                        <g className={location.includes("구역 0") ? "opacity-100" : "opacity-30"}>
                            <rect x="40" y="120" width="50" height="50" fill="none" stroke="#2a9d8f" strokeWidth="2" />
                            <text x="45" y="115" fill="#2a9d8f" fontSize="12" fontFamily="monospace" fontWeight="bold">SEC-00</text>
                            {/* Connection to Hallway */}
                            <line x1="90" y1="145" x2="110" y2="145" stroke="#2a9d8f" strokeWidth="1" strokeDasharray="2 2" />
                        </g>

                        {/* Sector 1: The Corridor */}
                        <g className={location.includes("구역 1") || location.includes("구역 2") || location.includes("구역 3") || location.includes("구역 4") ? "opacity-100" : "opacity-30"}>
                            <rect x="110" y="80" width="80" height="120" fill="none" stroke="#2a9d8f" strokeWidth="2" />
                            <text x="115" y="95" fill="#2a9d8f" fontSize="10" fontFamily="monospace" fontWeight="bold">SEC-01</text>
                        </g>

                        {/* Connection 1-2 */}
                        <line x1="190" y1="140" x2="210" y2="140" stroke="#2a9d8f" strokeWidth="1" />

                        {/* Sector 2: Memory Bank */}
                        <g className={location.includes("구역 2") || location.includes("구역 3") || location.includes("구역 4") ? "opacity-100" : "opacity-30"}>
                            <rect x="210" y="110" width="60" height="60" fill="none" stroke="#e9c46a" strokeWidth="2" />
                            <text x="215" y="125" fill="#e9c46a" fontSize="6" fontFamily="monospace">SEC-02</text>
                        </g>

                        {/* Connection 2-3 */}
                        <line x1="240" y1="170" x2="240" y2="190" stroke="#2a9d8f" strokeWidth="1" strokeDasharray="2 2" />

                        {/* Sector 3: The Void (Below) */}
                        <g className={location.includes("구역 3") || location.includes("구역 4") ? "opacity-100" : "opacity-30"}>
                            <circle cx="240" cy="220" r="25" fill="none" stroke="#e76f51" strokeWidth="2" />
                            <text x="225" y="222" fill="#e76f51" fontSize="6" fontFamily="monospace">SEC-03</text>
                        </g>

                        {/* Connection 3-4 */}
                        <path d="M 215 220 L 100 220 L 100 180" stroke="#2a9d8f" strokeWidth="1" fill="none" strokeDasharray="2 2" />

                        {/* Sector 4: The Core (Center) */}
                        <g className={location.includes("구역 4") ? "opacity-100" : "opacity-30"}>
                            <path d="M 80 140 L 100 110 L 120 140 L 100 170 Z" fill="none" stroke="#e9c46a" strokeWidth="3" />
                            <text x="90" y="145" fill="#e9c46a" fontSize="6" fontWeight="bold">CORE</text>
                        </g>

                        {/* Player Marker Logic */}
                        <g transform={
                            location.includes("구역 0") ? "translate(65, 145)" :
                                location.includes("구역 1") ? "translate(150, 140)" :
                                    location.includes("구역 2") ? "translate(240, 140)" :
                                        location.includes("구역 3") ? "translate(240, 220)" :
                                            location.includes("구역 4") ? "translate(100, 140)" :
                                                location.includes("REALITY") ? "translate(10, 10)" : "translate(150, 100)"
                        }>
                            <circle r="4" fill="#fff" className="animate-ping opacity-75" />
                            <circle r="3" fill="#fff" />
                        </g>
                    </svg>
                </div>

                {/* Coordinates Overlay */}
                <div className="absolute bottom-1 right-2 text-xs md:text-sm text-cyber-primary font-bold font-mono tracking-wider bg-black/80 px-2 py-1 border border-cyber-primary/30">
                    LOC: {location}
                </div>
            </div>

            {/* Tools / Actions */}
            <div className="border border-cyber-danger/50 p-4 bg-black/40">
                <h3 className="text-cyber-danger text-sm font-bold border-b border-cyber-danger/30 pb-2 mb-2">TOOLKIT</h3>
                <button
                    onClick={onHint}
                    className="w-full bg-cyber-danger/10 border border-cyber-danger text-cyber-danger py-2 hover:bg-cyber-danger hover:text-black transition-all text-sm font-bold tracking-wider"
                >
                    <span className="mr-2">🔍</span>
                    SCAN (HINT)
                </button>
            </div>

        </div>
    )
}

export default StatusPanel
