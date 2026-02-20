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

            {/* Main Image (Placeholder Implementation) */}
            <div className="w-full h-full flex items-center justify-center bg-[#050505] p-8 border border-cyber-dark">
                {imageData.url ? (
                    // In a real app, this would be an <img src={imageData.url} />
                    // For prototype without actual image generation, we use a stylized text description
                    <div className="w-full h-full flex flex-col items-center justify-center p-8 border border-cyber-glitch/20 bg-black/90 backdrop-blur-sm shadow-[inset_0_0_50px_rgba(0,0,0,0.8)]">
                        <div className="text-6xl mb-6 text-cyber-primary opacity-50 animate-pulse mix-blend-screen filter blur-[1px]">
                            <i className="fas fa-eye"></i> 👁️
                        </div>
                        <div className="text-4xl mb-4 font-bold tracking-[0.2em] text-cyber-primary/80 border-b border-cyber-primary/30 pb-2">
                            VISUAL SIGNAL
                        </div>
                        <p className="text-lg text-gray-300 leading-relaxed font-serif italic text-center max-w-2xl py-8 drop-shadow-md">
                            "{imageData.content}"
                        </p>
                        <div className="mt-8 text-[10px] text-cyber-primary/40 uppercase tracking-[0.3em]">
                            SOURCE: {imageData.agent} || FEED_ID: 0x92A
                        </div>
                    </div>
                ) : (
                    <div className="text-cyber-danger">DATA CORRUPTED</div>
                )}
            </div>

            {/* Helper text */}
            <div className="absolute top-2 left-2 text-xs bg-black/80 px-2 py-1 border border-cyber-primary/50 text-cyber-primary/80">
                CAM_FEED_01 [LIVE]
            </div>
        </div>
    )
}

export default VisualPanel
