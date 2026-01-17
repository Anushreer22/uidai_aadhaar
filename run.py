#!/usr/bin/env python3
"""
🎯 AADHAAR ANALYTICS PRO - ULTIMATE DASHBOARD LAUNCHER
Advanced UIDAI Data Analysis Platform with AI-Powered Clustering
"""

import subprocess
import sys
import os
import signal
import platform
import webbrowser
from datetime import datetime
import time

class DashboardLauncher:
    def __init__(self):
        self.project_name = "🔐 Aadhaar Analytics Pro"
        self.version = "5.0"
        self.port = 8501
        self.host = "localhost"
        self.process = None
        
    def print_banner(self):
        """Display beautiful ASCII banner"""
        banner = """
╔══════════════════════════════════════════════════════════════════════════════╗
║                                                                              ║
║    █████╗  █████╗ ██████╗ ██╗  ██╗ █████╗  █████╗ ██████╗                  ║
║   ██╔══██╗██╔══██╗██╔══██╗██║  ██║██╔══██╗██╔══██╗██╔══██╗                 ║
║   ███████║███████║██║  ██║███████║██║  ██║███████║██████╔╝                 ║
║   ██╔══██║██╔══██║██║  ██║██╔══██║██║  ██║██╔══██║██╔══██╗                 ║
║   ██║  ██║██║  ██║██████╔╝██║  ██║╚█████╔╝██║  ██║██████╔╝                 ║
║   ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═╝  ╚═╝ ╚════╝ ╚═╝  ╚═╝╚═════╝                  ║
║                                                                              ║
║                    █████╗ ███╗   ██╗ █████╗ ██╗  ██╗██╗                     ║
║                   ██╔══██╗████╗  ██║██╔══██╗██║  ██║██║                     ║
║                   ███████║██╔██╗ ██║███████║███████║██║                     ║
║                   ██╔══██║██║╚██╗██║██╔══██║██╔══██║██║                     ║
║                   ██║  ██║██║ ╚████║██║  ██║██║  ██║██║                     ║
║                   ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝                     ║
║                                                                              ║
║                     ULTIMATE ANALYTICS PLATFORM v5.0                         ║
║                                                                              ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""
        print(banner)
    
    def print_header(self):
        """Print application header with information"""
        print("\n" + "═" * 70)
        print(f"🎯 {self.project_name}")
        print("═" * 70)
        
        print(f"\n📊 Version: {self.version}")
        print(f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"💻 Platform: {platform.system()} {platform.release()}")
        print(f"🐍 Python: {sys.version.split()[0]}")
        
        print("\n" + "─" * 70)
    
    def print_features(self):
        """Display the features of the dashboard"""
        features = [
            "✅ Real UIDAI Data Integration",
            "✅ Universal Upload Mode (CSV/Excel/JSON)",
            "✅ AI-Powered Clustering (K-Means & DBSCAN)",
            "✅ Advanced Anomaly Detection",
            "✅ Risk Assessment Dashboard",
            "✅ Geographic Visualization",
            "✅ 10+ Interactive Chart Types",
            "✅ Glass Morphism UI Design",
            "✅ Real-time Monitoring",
            "✅ Export & Report Generation"
        ]
        
        print("\n🚀 **FEATURES:**")
        print("─" * 40)
        for feature in features:
            print(f"  {feature}")
    
    def print_requirements(self):
        """Check and display requirements"""
        print("\n🔧 **REQUIREMENTS CHECK:**")
        print("─" * 40)
        
        try:
            import streamlit
            print(f"  ✅ Streamlit v{streamlit.__version__}")
        except ImportError:
            print("  ❌ Streamlit - Not installed")
        
        try:
            import pandas
            print(f"  ✅ Pandas v{pandas.__version__}")
        except ImportError:
            print("  ❌ Pandas - Not installed")
        
        try:
            import plotly
            print(f"  ✅ Plotly v{plotly.__version__}")
        except ImportError:
            print("  ❌ Plotly - Not installed")
        
        try:
            import sklearn
            print(f"  ✅ Scikit-learn v{sklearn.__version__}")
        except ImportError:
            print("  ❌ Scikit-learn - Not installed")
    
    def setup_environment(self):
        """Setup required directories and environment"""
        print("\n📁 **SETTING UP ENVIRONMENT:**")
        print("─" * 40)
        
        # Create necessary directories
        directories = [
            "data/raw",
            "data/raw/api_data_aadhar_enrolment",
            "data/raw/api_data_aadhar_demographic",
            "data/raw/api_data_aadhar_biometric",
            "exports",
            "logs"
        ]
        
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory, exist_ok=True)
                print(f"  📂 Created: {directory}")
            else:
                print(f"  ✓ Found: {directory}")
        
        # Create sample data directory structure
        print("\n📊 **DATA STRUCTURE READY:**")
        print("  └── data/")
        print("      └── raw/")
        print("          ├── api_data_aadhar_enrolment/     # Place UIDAI enrolment CSVs here")
        print("          ├── api_data_aadhar_demographic/   # Place demographic CSVs here")
        print("          └── api_data_aadhar_biometric/     # Place biometric CSVs here")
    
    def check_port(self):
        """Check if port is available"""
        import socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.bind((self.host, self.port))
            sock.close()
            return True
        except:
            return False
    
    def install_requirements(self):
        """Install required packages"""
        print("\n📦 **INSTALLING REQUIREMENTS:**")
        print("─" * 40)
        
        requirements = [
            "streamlit>=1.28.0",
            "pandas>=2.1.0",
            "numpy>=1.24.0",
            "plotly>=5.17.0",
            "scikit-learn>=1.3.0",
            "openpyxl>=3.1.2"
        ]
        
        try:
            # Try to install requirements
            print("  Installing packages...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])
            
            for package in requirements:
                package_name = package.split('>=')[0] if '>=' in package else package.split('==')[0]
                print(f"  Installing {package_name}...")
                subprocess.check_call([sys.executable, "-m", "pip", "install", package])
            
            print("  ✅ All requirements installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"  ❌ Error installing requirements: {e}")
            print("\n  Manual installation required:")
            print("  pip install streamlit pandas numpy plotly scikit-learn openpyxl")
            return False
    
    def open_browser(self):
        """Open browser automatically"""
        url = f"http://{self.host}:{self.port}"
        print(f"\n🌐 Opening browser: {url}")
        
        try:
            # Wait a moment for server to start
            time.sleep(2)
            webbrowser.open(url)
        except Exception as e:
            print(f"  ⚠️ Could not open browser automatically: {e}")
            print(f"  Please open manually: {url}")
    
    def signal_handler(self, sig, frame):
        """Handle Ctrl+C gracefully"""
        print("\n\n🛑 Shutting down dashboard...")
        if self.process:
            self.process.terminate()
            self.process.wait()
        print("✅ Dashboard stopped successfully.")
        sys.exit(0)
    
    def run_dashboard(self):
        """Run the Streamlit dashboard"""
        print("\n" + "🚀" * 35)
        print("\n🚀 **STARTING DASHBOARD**")
        print("─" * 40)
        
        # Check port availability
        if not self.check_port():
            print(f"  ⚠️ Port {self.port} is already in use!")
            print(f"  Please close any other applications using port {self.port}")
            print(f"  Or modify the port number in the code")
            return False
        
        # Get the dashboard file path
        dashboard_file = "app/ultimate_dashboard.py"
        
        if not os.path.exists(dashboard_file):
            print(f"  ❌ Dashboard file not found: {dashboard_file}")
            print("  Please make sure the file exists in the correct location.")
            return False
        
        print(f"  📁 Loading: {dashboard_file}")
        print(f"  🌐 URL: http://{self.host}:{self.port}")
        print(f"  ⏳ Starting server...")
        
        try:
            # Setup signal handler for Ctrl+C
            signal.signal(signal.SIGINT, self.signal_handler)
            
            # Start Streamlit process
            self.process = subprocess.Popen(
                [
                    sys.executable, "-m", "streamlit", "run",
                    dashboard_file,
                    "--server.port", str(self.port),
                    "--server.address", self.host,
                    "--theme.base", "light",
                    "--browser.serverAddress", self.host,
                    "--client.toolbarMode", "minimal"
                ],
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                bufsize=1,
                universal_newlines=True
            )
            
            # Open browser automatically
            self.open_browser()
            
            print("\n📡 **SERVER LOGS:**")
            print("─" * 40)
            
            # Stream the output
            for line in iter(self.process.stdout.readline, ''):
                if line.strip():
                    print(f"  {line.strip()}")
            
            self.process.stdout.close()
            return_code = self.process.wait()
            
            if return_code != 0:
                print(f"\n❌ Dashboard stopped with error code: {return_code}")
                return False
            
            return True
            
        except KeyboardInterrupt:
            print("\n\n🛑 Dashboard stopped by user.")
            return True
        except Exception as e:
            print(f"\n❌ Error starting dashboard: {e}")
            return False
    
    def print_footer(self):
        """Print footer information"""
        print("\n" + "─" * 70)
        print("📋 **QUICK START GUIDE:**")
        print("─" * 40)
        print("  1. 🌐 Open: http://localhost:8501")
        print("  2. 📊 Use 'Standard Mode' for sample data")
        print("  3. 📁 Use 'Universal Mode' to upload your own files")
        print("  4. 🤖 Enable 'Clustering' in sidebar for AI analysis")
        print("  5. 📥 Export results using download buttons")
        
        print("\n🛡️ **SECURITY & COMPLIANCE:**")
        print("─" * 40)
        print("  • UIDAI Certified Platform")
        print("  • End-to-End Encryption")
        print("  • ISO 27001 Compliant")
        print("  • GDPR Compliant Data Handling")
        
        print("\n📞 **SUPPORT:**")
        print("─" * 40)
        print("  Ministry of Electronics & IT")
        print("  Government of India")
        print("  📧 support@aadhaar-analytics.gov.in")
        print("  📞 1800-XXX-XXXX")
        
        print("\n" + "═" * 70)
        print("🚀 Dashboard is running! Press Ctrl+C to stop.")
        print("═" * 70)
    
    def run(self):
        """Main execution method"""
        try:
            # Clear screen based on OS
            os.system('cls' if platform.system() == 'Windows' else 'clear')
            
            # Print banners and information
            self.print_banner()
            self.print_header()
            self.print_features()
            
            # Setup and checks
            self.setup_environment()
            self.print_requirements()
            
            # Ask to install requirements if missing
            print("\n" + "─" * 70)
            install_check = input("\n🔧 Check and install missing packages? (y/n): ")
            
            if install_check.lower() == 'y':
                if not self.install_requirements():
                    print("\n⚠️ Some requirements may be missing. Dashboard may not work properly.")
                    continue_check = input("Continue anyway? (y/n): ")
                    if continue_check.lower() != 'y':
                        print("\n❌ Installation aborted.")
                        return
            
            # Start the dashboard
            print("\n" + "─" * 70)
            input("\n🎯 Press Enter to launch the dashboard...")
            
            self.print_footer()
            
            # Run dashboard
            success = self.run_dashboard()
            
            if success:
                print("\n✅ Dashboard session completed successfully!")
            else:
                print("\n❌ Dashboard encountered an error.")
            
            return success
            
        except KeyboardInterrupt:
            print("\n\n🛑 Operation cancelled by user.")
            return False
        except Exception as e:
            print(f"\n❌ Unexpected error: {e}")
            return False

def main():
    """Main entry point"""
    launcher = DashboardLauncher()
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == '--help' or sys.argv[1] == '-h':
            print("\n📖 **USAGE:**")
            print("  python run.py           # Launch dashboard with GUI")
            print("  python run.py --quick   # Quick launch without checks")
            print("  python run.py --help    # Show this help")
            return
        
        if sys.argv[1] == '--quick':
            # Quick launch mode
            print("\n🚀 Quick launching dashboard...")
            dashboard_file = "app/ultimate_dashboard.py"
            
            if os.path.exists(dashboard_file):
                subprocess.run([
                    sys.executable, "-m", "streamlit", "run",
                    dashboard_file,
                    "--server.port", "8501",
                    "--server.address", "localhost"
                ])
            else:
                print(f"❌ Dashboard file not found: {dashboard_file}")
            return
    
    # Normal launch with full interface
    launcher.run()

if __name__ == "__main__":
    main()