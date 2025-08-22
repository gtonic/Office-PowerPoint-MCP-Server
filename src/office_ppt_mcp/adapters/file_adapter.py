"""
File Adapter for file system operations.

Handles file I/O operations, path management, and file validation.
"""
import os
import shutil
from typing import List, Optional


class FileAdapter:
    """Adapter for file system operations."""
    
    @staticmethod
    def exists(path: str) -> bool:
        """Check if a file or directory exists."""
        return os.path.exists(path)
    
    @staticmethod
    def is_file(path: str) -> bool:
        """Check if path is a file."""
        return os.path.isfile(path)
    
    @staticmethod
    def is_directory(path: str) -> bool:
        """Check if path is a directory."""
        return os.path.isdir(path)
    
    @staticmethod
    def get_file_extension(path: str) -> str:
        """Get the file extension."""
        _, ext = os.path.splitext(path)
        return ext.lower()
    
    @staticmethod
    def get_file_size(path: str) -> int:
        """Get file size in bytes."""
        return os.path.getsize(path)
    
    @staticmethod
    def create_directory(path: str, exist_ok: bool = True) -> None:
        """Create a directory."""
        os.makedirs(path, exist_ok=exist_ok)
    
    @staticmethod
    def list_files(directory: str, pattern: Optional[str] = None) -> List[str]:
        """List files in a directory, optionally filtered by pattern."""
        if not os.path.isdir(directory):
            return []
        
        files = []
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                if pattern is None or pattern.lower() in item.lower():
                    files.append(item)
        
        return sorted(files)
    
    @staticmethod
    def copy_file(src: str, dst: str) -> None:
        """Copy a file from source to destination."""
        shutil.copy2(src, dst)
    
    @staticmethod
    def move_file(src: str, dst: str) -> None:
        """Move a file from source to destination."""
        shutil.move(src, dst)
    
    @staticmethod
    def delete_file(path: str) -> None:
        """Delete a file."""
        if os.path.exists(path):
            os.remove(path)
    
    @staticmethod
    def get_absolute_path(path: str) -> str:
        """Get absolute path."""
        return os.path.abspath(path)
    
    @staticmethod
    def join_paths(*paths: str) -> str:
        """Join multiple path components."""
        return os.path.join(*paths)
    
    @staticmethod
    def expand_user(path: str) -> str:
        """Expand user home directory in path."""
        return os.path.expanduser(path)