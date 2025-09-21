#!/usr/bin/env python3
"""
Entry point for the country data pipeline
"""

if __name__ == "__main__":
    from src.main import main
    success = main()
    import sys
    sys.exit(0 if success else 1)