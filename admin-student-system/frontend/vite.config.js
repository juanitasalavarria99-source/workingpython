import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    host: true,
    port: 3000,
    strictPort: true,
    // Forzar polling para Docker
    watch: {
      usePolling: true
    }
  },
  // Configurar cache directory
  cacheDir: '/tmp/.vite'
})