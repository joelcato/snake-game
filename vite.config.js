import { defineConfig } from 'vite'

// Use `src/` as canonical source root and output production files to `dist/` at repo root
export default defineConfig({
  root: 'src',
  build: {
    outDir: '../dist'
  }
})
