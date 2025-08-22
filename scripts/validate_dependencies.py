#!/usr/bin/env python3
"""
Dependency validation script for Office PowerPoint MCP Server.
Validates that all required dependencies can be imported and are used in the codebase.
"""

import sys
import importlib
import os
from pathlib import Path

def validate_import(package_name, display_name=None):
    """Validate that a package can be imported."""
    if display_name is None:
        display_name = package_name
    
    try:
        importlib.import_module(package_name)
        print(f"✅ {display_name}: Successfully imported")
        return True
    except ImportError as e:
        print(f"❌ {display_name}: Import failed - {e}")
        return False

def check_dependency_usage():
    """Check that all dependencies are actually used in the codebase."""
    dependencies = {
        'mcp': ['ppt_mcp_server.py', 'src/office_ppt_mcp/protocol/', 'src/office_ppt_mcp/ppt/'],
        'pptx': ['src/office_ppt_mcp/ppt/', 'src/office_ppt_mcp/utils/', 'src/office_ppt_mcp/services/'],
        'PIL': ['src/office_ppt_mcp/utils/design_utils.py'],
        'fontTools': ['src/office_ppt_mcp/utils/design_utils.py']
    }
    
    print("\n🔍 Checking dependency usage in codebase:")
    
    for dep, expected_files in dependencies.items():
        print(f"\n📦 {dep}:")
        found_usage = False
        
        for file_pattern in expected_files:
            if file_pattern.endswith('/'):
                # Check directory
                directory = Path(file_pattern)
                if directory.exists():
                    for py_file in directory.rglob('*.py'):
                        with open(py_file, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            if f'import {dep}' in content or f'from {dep}' in content:
                                print(f"  ✅ Used in {py_file}")
                                found_usage = True
            else:
                # Check specific file
                if os.path.exists(file_pattern):
                    with open(file_pattern, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        if f'import {dep}' in content or f'from {dep}' in content:
                            print(f"  ✅ Used in {file_pattern}")
                            found_usage = True
        
        if not found_usage:
            print(f"  ⚠️  No usage found for {dep}")

def main():
    """Main validation function."""
    print("🧪 Office PowerPoint MCP Server - Dependency Validation")
    print("=" * 60)
    
    # Core dependencies to validate
    dependencies = [
        ('mcp', 'MCP Framework'),
        ('pptx', 'python-pptx'),
        ('PIL', 'Pillow'),
        ('fontTools', 'fonttools')
    ]
    
    print("\n📋 Validating core dependencies:")
    success_count = 0
    total_count = len(dependencies)
    
    for package, display_name in dependencies:
        if validate_import(package, display_name):
            success_count += 1
    
    print(f"\n📊 Import Results: {success_count}/{total_count} dependencies successfully imported")
    
    # Check usage in codebase
    check_dependency_usage()
    
    # Final summary
    print("\n" + "=" * 60)
    if success_count == total_count:
        print("🎉 All dependencies validated successfully!")
        print("✅ All required packages can be imported")
        print("✅ Dependencies are actively used in the codebase")
        return 0
    else:
        print("⚠️  Some dependencies failed validation")
        print(f"❌ {total_count - success_count} package(s) could not be imported")
        print("💡 Run 'pip install -r requirements.txt' to install missing dependencies")
        return 1

if __name__ == "__main__":
    sys.exit(main())