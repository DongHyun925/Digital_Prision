import { useState, useEffect, useRef } from 'react'
import Terminal from './components/Terminal'
import VisualPanel from './components/VisualPanel'
import StatusPanel from './components/StatusPanel'

function App() {
  const [logs, setLogs] = useState([])
  const [image, setImage] = useState(null)
  const [status, setStatus] = useState("SYSTEM OFFLINE")
  const [inventory, setInventory] = useState([])
  const [loading, setLoading] = useState(false)

  const addLog = (newLogs) => {
    setLogs(prev => [...prev, ...newLogs])

    // Process side effects from logs (images, status updates)
    newLogs.forEach(log => {
      if (log.type === 'image') {
        setImage(log)
      }
      if (log.type === 'ui_update') {
        setStatus(log.status)
        setInventory(log.inventory)
      }
    })
  }

  const startGame = async () => {
    setLoading(true)
    try {
      const res = await fetch('http://localhost:5000/api/init', { method: 'POST' })
      const data = await res.json()
      addLog(data.logs)
    } catch (err) {
      console.error("Failed to start game:", err)
      addLog([{ agent: "SYSTEM", text: "ERROR: Failed to connect to server.", type: "error" }])
    }
    setLoading(false)
  }

  const sendCommand = async (text) => {
    if (!text.trim()) return
    setLoading(true)
    try {
      const res = await fetch('http://localhost:5000/api/action', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ command: text })
      })
      const data = await res.json()
      addLog(data.logs)
    } catch (err) {
      console.error("Failed to send command:", err)
      addLog([{ agent: "SYSTEM", text: "ERROR: Connection lost.", type: "error" }])
    }
    setLoading(false)
  }

  useEffect(() => {
    startGame()
  }, [])

  return (
    <div className="flex h-screen w-screen bg-cyber-bg text-cyber-primary font-mono overflow-hidden relative">
      <div className="scanline"></div>
      <div className="mystery-overlay"></div>
      <div className="noise"></div>

      {/* Main Grid Layout */}
      <div className="grid grid-cols-12 grid-rows-12 gap-4 p-6 w-full h-full z-50 relative">

        {/* Header (Top) */}
        <header className="col-span-12 row-span-1 border-b border-cyber-primary/30 flex items-center justify-between px-4 bg-cyber-dark/90 backdrop-blur shadow-lg">
          <h1 className="text-3xl font-bold tracking-[0.5em] text-cyber-primary/80 uppercase">The Digital Prison</h1>
          <div className="flex gap-4 text-sm">
            <span className="animate-pulse">NET: ONLINE</span>
            <span>SEC: 00</span>
          </div>
        </header>

        {/* Visual Panel (Main Center-Left) */}
        <div className="col-span-12 md:col-span-8 row-span-7 border border-cyber-dark bg-black relative">
          <VisualPanel imageData={image} />
        </div>

        {/* Status Panel (Right Sidebar) */}
        <div className="col-span-12 md:col-span-4 row-span-11 border border-cyber-primary bg-cyber-dark/50 p-4">
          <StatusPanel status={status} inventory={inventory} />
        </div>

        {/* Terminal (Bottom Center-Left) */}
        <div className="col-span-12 md:col-span-8 row-span-4 border-t border-cyber-primary bg-cyber-dark/90 text-sm">
          <Terminal logs={logs} onSend={sendCommand} loading={loading} />
        </div>

      </div>
    </div>
  )
}

export default App
