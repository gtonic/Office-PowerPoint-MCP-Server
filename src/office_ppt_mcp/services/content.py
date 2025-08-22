"""
Content Service for managing PowerPoint content operations.

Handles slide content management, text operations, and media handling.
"""
from typing import Any, Dict, List, Optional


class ContentService:
    """Service for managing PowerPoint content operations."""
    
    def __init__(self):
        pass
    
    def validate_slide_index(self, presentation: Any, slide_index: int) -> bool:
        """
        Validate that a slide index is valid for the given presentation.
        
        Args:
            presentation: The PowerPoint presentation object
            slide_index: The slide index to validate (0-based)
            
        Returns:
            True if valid, False otherwise
        """
        if presentation is None:
            return False
        
        try:
            slide_count = len(presentation.slides)
            return 0 <= slide_index < slide_count
        except:
            return False
    
    def get_slide_info(self, presentation: Any, slide_index: int) -> Dict[str, Any]:
        """
        Get information about a specific slide.
        
        Args:
            presentation: The PowerPoint presentation object
            slide_index: The slide index (0-based)
            
        Returns:
            Dictionary containing slide information
        """
        if not self.validate_slide_index(presentation, slide_index):
            raise ValueError(f"Invalid slide index: {slide_index}")
        
        slide = presentation.slides[slide_index]
        
        info = {
            "slide_index": slide_index,
            "layout_name": slide.slide_layout.name if slide.slide_layout else "Unknown",
            "shape_count": len(slide.shapes),
            "has_title": hasattr(slide, 'shapes') and slide.shapes.title is not None,
            "shapes": []
        }
        
        # Get information about shapes on the slide
        for i, shape in enumerate(slide.shapes):
            shape_info = {
                "index": i,
                "name": shape.name if hasattr(shape, 'name') else f"Shape {i}",
                "shape_type": str(shape.shape_type) if hasattr(shape, 'shape_type') else "Unknown",
                "has_text": hasattr(shape, 'text_frame') and shape.text_frame is not None
            }
            info["shapes"].append(shape_info)
        
        return info
    
    def validate_content_parameters(self, **kwargs) -> Dict[str, Any]:
        """
        Validate content-related parameters.
        
        Returns:
            Dictionary of validated parameters
        """
        validated = {}
        
        # Add validation logic for content parameters as needed
        for key, value in kwargs.items():
            validated[key] = value
        
        return validated