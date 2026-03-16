#!/usr/bin/env python3
"""
Simple HTTP server to serve the Snake game locally
Run with: python server.py
Then open http://localhost:8000 in your browser
"""

import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    # Change to the directory containing this script
    root_dir = os.path.dirname(os.path.abspath(__file__))
    # Prefer serving from 'dist' (Vite output) if it exists, otherwise fall back to 'public', then root
    dist_dir = os.path.join(root_dir, 'dist')
    public_dir = os.path.join(root_dir, 'public')
    if os.path.isdir(dist_dir):
        os.chdir(dist_dir)
    elif os.path.isdir(public_dir):
        os.chdir(public_dir)
    else:
        os.chdir(root_dir)
    
    Handler = MyHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"🐍 Snake Game Server starting...")
            print(f"📡 Server running at http://localhost:{PORT}")
            print(f"🌐 Opening browser...")
            print(f"⏹️  Press Ctrl+C to stop the server")
            
            # Open browser automatically
            webbrowser.open(f'http://localhost:{PORT}')
            
            httpd.serve_forever()
    except KeyboardInterrupt:
        print(f"\n🛑 Server stopped")
        sys.exit(0)
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Port {PORT} is already in use. Try a different port or stop the existing server.")
        else:
            print(f"❌ Error starting server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()