"""
Centralized configuration management for PowerPoint MCP Server.

This module provides a centralized configuration system using pydantic BaseSettings
with support for environment variables, .env files, and default values.

Loading precedence (highest to lowest):
1. Environment variables
2. .env file
3. Default values
"""

import os
from typing import List, Optional
from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class PowerPointMCPConfig(BaseSettings):
    """Configuration settings for PowerPoint MCP Server."""
    
    # Server Configuration
    default_port: int = Field(default=8000, alias='PPT_MCP_PORT', description="Default port for HTTP/SSE transport")
    default_transport: str = Field(default="stdio", alias='PPT_MCP_TRANSPORT', description="Default transport method")
    
    # Slide Dimensions (in EMU - English Metric Units)
    slide_width_emu: int = Field(default=10 * 914400, alias='PPT_SLIDE_WIDTH_EMU', description="Standard slide width in EMU (10 inches)")
    slide_height_emu: int = Field(default=int(7.5 * 914400), alias='PPT_SLIDE_HEIGHT_EMU', description="Standard slide height in EMU (7.5 inches)")
    
    # EMU Conversion Constants
    inch_to_emu: int = Field(default=914400, description="Conversion factor from inches to EMU")
    point_to_emu: int = Field(default=12700, description="Conversion factor from points to EMU")
    
    # Spacing and Layout
    min_shape_spacing_emu: int = Field(default=int(0.1 * 914400), alias='PPT_MIN_SPACING_EMU', description="Minimum spacing between shapes in EMU (0.1 inches)")
    
    # Font Size Defaults
    min_font_size: int = Field(default=8, alias='PPT_MIN_FONT_SIZE', description="Minimum allowed font size in points")
    max_font_size: int = Field(default=72, alias='PPT_MAX_FONT_SIZE', description="Maximum allowed font size in points")
    template_min_font_size: int = Field(default=8, description="Minimum font size for templates")
    template_max_font_size: int = Field(default=36, description="Maximum font size for templates")
    header_font_size: int = Field(default=12, description="Default header font size")
    body_font_size: int = Field(default=10, description="Default body font size")
    default_font_size: int = Field(default=14, description="Default font size assumption")
    
    # Template Configuration
    template_search_paths: List[str] = Field(
        default=['.', './templates', './assets', './resources'],
        description="Default directories to search for templates"
    )
    ppt_template_path: Optional[str] = Field(
        default=None,
        alias='PPT_TEMPLATE_PATH',
        description="Environment variable for custom template paths (colon/semicolon separated)"
    )
    
    # Validation Thresholds
    max_text_length_warning: int = Field(default=500, description="Text length threshold for warnings")
    max_empty_paragraphs: int = Field(default=2, description="Maximum empty paragraphs before warning")
    
    # File and Performance Limits
    max_concurrent_presentations: int = Field(default=10, description="Maximum number of concurrent presentations")
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )

    def get_template_search_directories(self) -> List[str]:
        """
        Get list of directories to search for templates.
        Uses ppt_template_path if set, otherwise uses default directories.
        
        Returns:
            List of directories to search for templates
        """
        if self.ppt_template_path:
            # Support multiple paths separated by colon (Unix) or semicolon (Windows)
            import platform
            separator = ';' if platform.system() == "Windows" else ':'
            env_dirs = [path.strip() for path in self.ppt_template_path.split(separator) if path.strip()]
            
            # Verify that the directories exist
            valid_env_dirs = []
            for dir_path in env_dirs:
                expanded_path = os.path.expanduser(dir_path)
                if os.path.exists(expanded_path) and os.path.isdir(expanded_path):
                    valid_env_dirs.append(expanded_path)
            
            if valid_env_dirs:
                # Add default fallback directories
                return valid_env_dirs + self.template_search_paths
            else:
                print(f"Warning: PPT_TEMPLATE_PATH directories not found: {self.ppt_template_path}")
        
        # Default search directories when no environment variable or invalid paths
        return self.template_search_paths

    def inches_to_emu(self, inches: float) -> int:
        """Convert inches to EMU."""
        return int(inches * self.inch_to_emu)
    
    def points_to_emu(self, points: float) -> int:
        """Convert points to EMU."""
        return int(points * self.point_to_emu)
    
    def emu_to_inches(self, emu: int) -> float:
        """Convert EMU to inches."""
        return emu / self.inch_to_emu
    
    def emu_to_points(self, emu: int) -> float:
        """Convert EMU to points."""
        return emu / self.point_to_emu


# Global configuration instance
config = PowerPointMCPConfig()