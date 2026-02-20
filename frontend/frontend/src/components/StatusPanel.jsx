function StatusPanel({ status, inventory }) {
    return (
        <div className="flex flex-col gap-6 h-full bg-black/40 backdrop-blur-md border-l border-cyber-primary/20 p-4">
            {/* System Status Block */}
            <div className="border border-cyber-primary/30 p-4 bg-black/60 shadow-lg relative overflow-hidden group">
                <div className="absolute top-0 left-0 w-1 h-full bg-cyber-primary/50"></div>
                <h3 className="text-cyber-warning text-xs font-bold tracking-[0.2em] mb-4 opacity-70">SYSTEM STATUS</h3>
                <div className="text-xl font-bold text-cyber-glitch animate-pulse drop-shadow-[0_0_5px_rgba(42,157,143,0.5)]">
                    {status}
                </div>
                <div className="mt-4 text-[10px] text-gray-500 font-mono grid grid-cols-2 gap-2">
                    <div>INTEGRITY: <span className="text-cyber-primary">98%</span></div>
                    <div>MEMORY: <span className="text-cyber-primary">STABLE</span></div>
                </div>
            </div>

            {/* Inventory Block */}
            <div className="border border-cyber-primary/30 p-4 bg-black/60 flex-1 relative">
                <div className="absolute top-0 right-0 w-1 h-10 bg-cyber-primary/50"></div>
                <h3 className="text-cyber-primary text-xs font-bold tracking-[0.2em] mb-4 opacity-70">INVENTORY</h3>

                {inventory && inventory.length > 0 ? (
                    <div className="grid grid-cols-1 gap-2">
                        {inventory.map((item, i) => (
                            <div key={i} className="bg-cyber-dark p-3 border border-cyber-primary/10 text-xs hover:border-cyber-primary/50 hover:bg-cyber-primary/10 cursor-pointer transition-all duration-300 flex items-center gap-2 group">
                                <span className="w-1 h-1 bg-cyber-primary rounded-full group-hover:animate-ping"></span>
                                {item}
                            </div>
                        ))}
                    </div>
                ) : (
                    <div className="text-gray-700 text-xs italic py-8 text-center border border-dashed border-gray-800">
                        [NO ITEMS DETECTED]
                    </div>
                )}
            </div>

            {/* Minimap Placeholder */}
            <div className="border border-cyber-primary/30 p-4 bg-black/60 h-48 relative overflow-hidden opacity-80">
                <h3 className="text-cyber-primary text-xs font-bold tracking-[0.2em] mb-2 absolute top-2 left-2 z-10 w-full mix-blend-difference">MAP DATA</h3>
                <div className="absolute inset-0 flex items-center justify-center opacity-30">
                    <div className="w-32 h-32 border border-cyber-primary/20 rounded-full animate-[spin_10s_linear_infinite]"></div>
                    <div className="w-20 h-20 border border-cyber-glitch/40 rounded-full absolute animate-[ping_3s_ease-out_infinite]"></div>
                    <div className="w-full h-[1px] bg-cyber-primary/20 absolute top-1/2"></div>
                    <div className="h-full w-[1px] bg-cyber-primary/20 absolute left-1/2"></div>
                </div>
                <div className="absolute bottom-2 right-2 text-[8px] text-cyber-primary/50">loc: unknown_sector</div>
            </div>

            {/* Tools / Actions */}
            <div className="border border-cyber-danger/30 p-4 bg-black/60">
                <h3 className="text-cyber-danger text-xs font-bold tracking-[0.2em] mb-3 opacity-70">TOOLKIT</h3>
                <button
                    onClick={() => alert('Vision Agent: Image Upload Intercepted')}
                    className="w-full bg-cyber-danger/5 border border-cyber-danger/50 text-cyber-danger py-3 hover:bg-cyber-danger hover:text-black transition-all duration-300 text-xs font-bold tracking-widest uppercase relative overflow-hidden group"
                >
                    <span className="absolute inset-0 bg-cyber-danger/20 transform -translate-x-full group-hover:translate-x-0 transition-transform duration-300"></span>
                    <span className="relative z-10 flex items-center justify-center gap-2">
                        <span>📸</span> UPLOAD SIGNAL
                    </span>
                </button>
            </div>

        </div>
    )
}

export default StatusPanel
