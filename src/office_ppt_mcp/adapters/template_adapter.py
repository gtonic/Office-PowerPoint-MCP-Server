"""
Template Adapter for file system template operations.

Handles template file discovery, validation, and loading from the file system.
"""
import os
import platform
from typing import List


def get_template_search_directories() -> List[str]:
    """
    Get list of directories to search for templates.
    Uses environment variable PPT_TEMPLATE_PATH if set, otherwise uses default directories.
    
    Returns:
        List of directories to search for templates
    """
    template_env_path = os.environ.get('PPT_TEMPLATE_PATH')
    
    if template_env_path:
        # If environment variable is set, use it as the primary template directory
        # Support multiple paths separated by colon (Unix) or semicolon (Windows)
        separator = ';' if platform.system() == "Windows" else ':'
        env_dirs = [path.strip() for path in template_env_path.split(separator) if path.strip()]
        
        # Verify that the directories exist
        valid_env_dirs = []
        for dir_path in env_dirs:
            expanded_path = os.path.expanduser(dir_path)
            if os.path.exists(expanded_path) and os.path.isdir(expanded_path):
                valid_env_dirs.append(expanded_path)
        
        if valid_env_dirs:
            # Add default fallback directories
            return valid_env_dirs + ['.', './templates', './assets', './resources']
        else:
            print(f"Warning: PPT_TEMPLATE_PATH directories not found: {template_env_path}")
    
    # Default search directories when no environment variable or invalid paths
    return ['.', './templates', './assets', './resources']


def find_template_file(template_name: str) -> str:
    """
    Find a template file in the search directories.
    
    Args:
        template_name: Name of the template file
        
    Returns:
        Full path to the template file
        
    Raises:
        FileNotFoundError: If template is not found
    """
    search_dirs = get_template_search_directories()
    
    for directory in search_dirs:
        template_path = os.path.join(directory, template_name)
        if os.path.exists(template_path):
            return template_path
    
    raise FileNotFoundError(f"Template '{template_name}' not found in search directories: {search_dirs}")


def validate_template_file(template_path: str) -> bool:
    """
    Validate that a template file exists and is a valid PowerPoint file.
    
    Args:
        template_path: Path to the template file
        
    Returns:
        True if valid, False otherwise
    """
    if not os.path.exists(template_path):
        return False
    
    # Check file extension
    valid_extensions = ['.pptx', '.potx']
    _, ext = os.path.splitext(template_path)
    return ext.lower() in valid_extensions