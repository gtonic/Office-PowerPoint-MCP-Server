"""
Presentation Service for managing PowerPoint presentations.

Handles presentation lifecycle, state management, and coordination.
"""
from typing import Dict, Optional, Any


class PresentationService:
    """Service for managing PowerPoint presentations."""
    
    def __init__(self):
        self.presentations: Dict[str, Any] = {}
        self._current_presentation_id: Optional[str] = None
    
    def get_current_presentation(self):
        """Get the current presentation object or raise an error if none is loaded."""
        if self._current_presentation_id is None or self._current_presentation_id not in self.presentations:
            raise ValueError("No presentation is currently loaded. Please create or open a presentation first.")
        return self.presentations[self._current_presentation_id]
    
    def get_current_presentation_id(self):
        """Get the current presentation ID."""
        return self._current_presentation_id
    
    def set_current_presentation_id(self, pres_id: str):
        """Set the current presentation ID."""
        self._current_presentation_id = pres_id
    
    def store_presentation(self, pres: Any, pres_id: str):
        """Store a presentation and set it as current."""
        self.presentations[pres_id] = pres
        self.set_current_presentation_id(pres_id)
    
    def get_presentation(self, pres_id: str):
        """Get a specific presentation by ID."""
        if pres_id not in self.presentations:
            raise ValueError(f"Presentation with ID '{pres_id}' not found.")
        return self.presentations[pres_id]
    
    def remove_presentation(self, pres_id: str):
        """Remove a presentation from memory."""
        if pres_id in self.presentations:
            del self.presentations[pres_id]
            if self._current_presentation_id == pres_id:
                self._current_presentation_id = None
    
    def list_presentations(self):
        """List all loaded presentations."""
        return list(self.presentations.keys())


class PresentationManager:
    """Wrapper to handle presentation state updates (legacy compatibility)."""
    
    def __init__(self, presentations_dict):
        self.presentations = presentations_dict
    
    def store_presentation(self, pres, pres_id):
        """Store a presentation and set it as current."""
        self.presentations[pres_id] = pres