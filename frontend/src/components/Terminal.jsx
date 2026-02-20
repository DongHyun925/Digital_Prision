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
        <div className="flex flex-col h-full w-full">
            {/* Log Output */}
            <div className="flex-1 overflow-y-auto p-4 space-y-2 font-mono scrollbar-custom">
                {logs.map((log, i) => (
                    <div key={i} className={`
            ${log.type === 'user_input' ? 'text-cyber-glitch text-right' : ''}
            ${log.type === 'error' ? 'text-cyber-danger' : ''}
            ${log.agent === 'SYSTEM' ? 'text-cyber-warning' : ''}
            ${log.agent === '시나리오 마스터' ? 'text-white font-bold' : ''}
          `}>
                        {log.type !== 'user_input' && <span className="opacity-50 text-xs mr-2">[{log.agent}]</span>}
                        <span>{log.text}</span>
                    </div>
                ))}
                {loading && <div className="text-cyber-glitch animate-pulse">Processing...</div>}
                <div ref={bottomRef} />
            </div>

            {/* Input Area */}
            <form onSubmit={handleSubmit} className="flex border-t border-cyber-primary">
                <span className="p-3 bg-cyber-dark text-cyber-primary font-bold">{'>'}</span>
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    className="flex-1 bg-transparent border-none outline-none text-cyber-primary p-3 focus:bg-white/5 transition-colors"
                    placeholder="Enter command..."
                    autoFocus
                    disabled={loading}
                />
                <button
                    type="submit"
                    disabled={loading}
                    className="px-6 bg-cyber-primary text-black font-bold hover:bg-cyber-glitch transition-colors disabled:opacity-50"
                >
                    SEND
                </button>
            </form>
        </div>
    )
}

export default Terminal
