import { useState, useEffect, useRef } from 'react'

function Terminal({ logs, onSend, loading }) {
    const [input, setInput] = useState('')
    const bottomRef = useRef(null)

    useEffect(() => {
        bottomRef.current?.scrollIntoView({ behavior: 'smooth' })
    }, [logs])

    const handleSubmit = (e) => {
        e.preventDefault()
        onSend(input)
        setInput('')
    }

    return (
        <div className="flex flex-col h-full w-full bg-black/90 border-t border-cyber-primary/20 backdrop-blur-sm">
            {/* Log Output */}
            <div className="flex-1 overflow-y-auto p-4 space-y-3 font-mono scrollbar-custom text-sm">
                {logs.map((log, i) => (
                    <div key={i} className={`
            flex gap-3
            ${log.type === 'user_input' ? 'flex-row-reverse text-cyber-primary/80 italic' : ''}
            ${log.type === 'error' ? 'text-cyber-danger' : ''}
            ${log.agent === 'SYSTEM' ? 'text-cyber-warning' : ''}
            ${log.agent === '시나리오 마스터' ? 'text-gray-200 font-bold tracking-wide' : ''}
          `}>
                        {log.type !== 'user_input' && (
                            <span className="text-[10px] uppercase opacity-40 mt-1 min-w-[80px] text-right border-r border-gray-700 pr-2 h-fit">
                                [{log.agent}]
                            </span>
                        )}
                        <span className={`leading-relaxed ${log.type !== 'user_input' ? 'flex-1' : 'bg-cyber-primary/10 px-3 py-1 rounded-sm border-l-2 border-cyber-primary/50'}`}>
                            {log.text}
                        </span>
                    </div>
                ))}
                {loading && <div className="text-cyber-glitch animate-pulse text-xs ml-24">Processing Data Stream...</div>}
                <div ref={bottomRef} />
            </div>

            {/* Input Area */}
            <form onSubmit={handleSubmit} className="flex border-t border-cyber-primary/20 bg-black">
                <span className="p-4 bg-cyber-dark text-cyber-primary font-bold border-r border-cyber-primary/10 text-lg">{'>'}</span>
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    className="flex-1 bg-transparent border-none outline-none text-cyber-primary p-4 focus:bg-white/5 transition-colors font-mono tracking-wider"
                    placeholder="Enter command protocol..."
                    autoFocus
                    disabled={loading}
                />
                <button
                    type="submit"
                    disabled={loading}
                    className="px-8 bg-cyber-primary/10 text-cyber-primary font-bold hover:bg-cyber-primary hover:text-black transition-all duration-300 disabled:opacity-30 border-l border-cyber-primary/20 tracking-widest text-xs"
                >
                    SEND
                </button>
            </form>
        </div>
    )
}

export default Terminal
