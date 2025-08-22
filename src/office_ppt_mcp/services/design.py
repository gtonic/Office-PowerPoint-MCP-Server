"""
Design Service for managing PowerPoint design operations.

Handles themes, colors, fonts, and visual styling operations.
"""
from typing import Any, Dict, List, Tuple, Optional


class DesignService:
    """Service for managing PowerPoint design operations."""
    
    def __init__(self):
        self._color_schemes = self._initialize_color_schemes()
    
    def _initialize_color_schemes(self) -> Dict[str, Dict[str, Tuple[int, int, int]]]:
        """Initialize predefined color schemes."""
        return {
            "professional_blue": {
                "primary": (31, 73, 125),
                "secondary": (68, 84, 106),
                "accent": (91, 155, 213),
                "background": (255, 255, 255),
                "text": (0, 0, 0)
            },
            "modern_green": {
                "primary": (70, 130, 76),
                "secondary": (112, 173, 71),
                "accent": (146, 208, 80),
                "background": (255, 255, 255),
                "text": (0, 0, 0)
            },
            "elegant_purple": {
                "primary": (91, 50, 147),
                "secondary": (142, 86, 173),
                "accent": (177, 133, 201),
                "background": (255, 255, 255),
                "text": (0, 0, 0)
            }
        }
    
    def get_color_schemes(self) -> Dict[str, Dict[str, Tuple[int, int, int]]]:
        """Get available color schemes."""
        return self._color_schemes
    
    def get_professional_color(self, scheme_name: str, color_type: str) -> Tuple[int, int, int]:
        """
        Get a professional color from a color scheme.
        
        Args:
            scheme_name: Name of the color scheme
            color_type: Type of color (primary, secondary, accent, background, text)
            
        Returns:
            RGB tuple
        """
        if scheme_name not in self._color_schemes:
            raise ValueError(f"Unknown color scheme: {scheme_name}")
        
        scheme = self._color_schemes[scheme_name]
        if color_type not in scheme:
            raise ValueError(f"Unknown color type: {color_type}")
        
        return scheme[color_type]
    
    def validate_rgb_color(self, color: Tuple[int, int, int]) -> bool:
        """
        Validate an RGB color tuple.
        
        Args:
            color: RGB color tuple
            
        Returns:
            True if valid, False otherwise
        """
        if not isinstance(color, (list, tuple)) or len(color) != 3:
            return False
        return all(isinstance(c, int) and 0 <= c <= 255 for c in color)
    
    def get_font_recommendations(self, use_case: str = "general") -> List[str]:
        """
        Get font recommendations for different use cases.
        
        Args:
            use_case: The use case for the fonts (general, presentation, professional, etc.)
            
        Returns:
            List of recommended font names
        """
        recommendations = {
            "general": ["Calibri", "Arial", "Segoe UI", "Helvetica"],
            "presentation": ["Calibri", "Segoe UI", "Arial", "Tahoma"],
            "professional": ["Calibri", "Times New Roman", "Arial", "Cambria"],
            "modern": ["Segoe UI", "Arial", "Calibri", "Lato"],
            "creative": ["Arial", "Calibri", "Segoe UI", "Georgia"]
        }
        
        return recommendations.get(use_case, recommendations["general"])