function VisualPanel({ imageData }) {
    if (!imageData) {
        return (
            <div className="w-full h-full flex items-center justify-center text-cyber-dark/50 flex-col gap-4">
                <div className="animate-spin w-12 h-12 border-4 border-cyber-primary border-t-transparent rounded-full"></div>
                <p>WAITING FOR VISUAL DATA...</p>
            </div>
        )
    }

    return (
        <div className="w-full h-full relative overflow-hidden group">
            {/* Glitch Overlay Effect */}
            <div className="absolute inset-0 bg-transparent mix-blend-overlay pointer-events-none group-hover:animate-glitch opacity-0 group-hover:opacity-20 transition-opacity"></div>

            {/* Main Image Layer */}
            <div className="w-full h-full flex items-center justify-center bg-[#050505] p-1 border border-cyber-dark relative z-10">
                {imageData.url ? (
                    <div className="relative w-full h-full group">
                        {/* Actual Image */}
                        <img
                            src={imageData.url}
                            alt={imageData.content}
                            className="w-full h-full object-cover filter contrast-125 brightness-90 saturate-50 sepia-[.3] opacity-90"
                        />

                        {/* Overlay text on hover or always visible in a corner */}
                        <div className="absolute bottom-0 left-0 w-full bg-gradient-to-t from-black via-black/80 to-transparent p-6 pt-12 opacity-80 group-hover:opacity-100 transition-opacity duration-500">
                            <p className="text-sm text-gray-300 leading-relaxed font-serif italic drop-shadow-md border-l-2 border-cyber-primary/50 pl-3">
                                "{imageData.content}"
                            </p>
                            <div className="mt-2 text-[10px] text-cyber-primary/60 uppercase tracking-[0.2em] font-mono">
                                RENDERED BY: {imageData.agent}
                            </div>
                        </div>
                    </div>
                ) : (
                    <div className="w-full h-full flex flex-col items-center justify-center p-8 border border-cyber-glitch/20 bg-black/90 backdrop-blur-sm shadow-[inset_0_0_50px_rgba(0,0,0,0.8)]">
                        <div className="text-cyber-danger mb-4 text-3xl animate-pulse">NO SIGNAL</div>
                        <div className="text-gray-500 text-xs">FEED CONNECTION LOST...</div>
                    </div>
                )}
            </div>

            {/* Helper text */}
            <div className="absolute top-4 left-4 text-[10px] bg-black/80 px-2 py-1 border border-cyber-primary/50 text-cyber-primary/80 z-20 font-mono tracking-widest">
                CAM_FEED_01 [LIVE] :: ISO 3200
            </div>
        </div>
    )
}

export default VisualPanel
