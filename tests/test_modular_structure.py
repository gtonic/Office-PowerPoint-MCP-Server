"""
Basic smoke tests for the Office PowerPoint MCP Server.

Tests that the modular structure is working correctly and basic imports succeed.
"""
import unittest
import sys
import os

# Add src to path for testing
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))


class TestModularStructure(unittest.TestCase):
    """Test that the new modular structure works correctly."""
    
    def test_protocol_imports(self):
        """Test that protocol module imports correctly."""
        try:
            from src.office_ppt_mcp.protocol import mcp_server
            self.assertTrue(hasattr(mcp_server, 'main'))
        except ImportError as e:
            self.fail(f"Protocol module import failed: {e}")
    
    def test_services_imports(self):
        """Test that service modules import correctly."""
        try:
            from src.office_ppt_mcp.services.presentation import PresentationService
            from src.office_ppt_mcp.services.template import TemplateService
            from src.office_ppt_mcp.services.content import ContentService
            from src.office_ppt_mcp.services.design import DesignService
            
            # Test that services can be instantiated
            ps = PresentationService()
            ts = TemplateService()
            cs = ContentService()
            ds = DesignService()
            
            self.assertIsNotNone(ps)
            self.assertIsNotNone(ts)
            self.assertIsNotNone(cs)
            self.assertIsNotNone(ds)
        except ImportError as e:
            self.fail(f"Services module import failed: {e}")
    
    def test_ppt_tools_imports(self):
        """Test that PPT tools import correctly."""
        try:
            from src.office_ppt_mcp.ppt import (
                register_presentation_tools,
                register_content_tools,
                register_structural_tools,
                register_professional_tools,
                register_template_tools
            )
            
            # Check that functions are callable
            self.assertTrue(callable(register_presentation_tools))
            self.assertTrue(callable(register_content_tools))
            self.assertTrue(callable(register_structural_tools))
            self.assertTrue(callable(register_professional_tools))
            self.assertTrue(callable(register_template_tools))
        except ImportError as e:
            self.fail(f"PPT tools import failed: {e}")
    
    def test_utils_imports(self):
        """Test that utils modules import correctly."""
        try:
            # Import some key utility functions
            from src.office_ppt_mcp.utils.core_utils import safe_operation
            from src.office_ppt_mcp.utils.presentation_utils import create_presentation
            from src.office_ppt_mcp.utils.design_utils import get_professional_color
            
            # Check that functions are callable
            self.assertTrue(callable(safe_operation))
            self.assertTrue(callable(create_presentation))
            self.assertTrue(callable(get_professional_color))
        except ImportError as e:
            self.fail(f"Utils import failed: {e}")
    
    def test_adapters_imports(self):
        """Test that adapter modules import correctly."""
        try:
            from src.office_ppt_mcp.adapters.template_adapter import get_template_search_directories
            from src.office_ppt_mcp.adapters.file_adapter import FileAdapter
            
            # Check that functions/classes are available
            self.assertTrue(callable(get_template_search_directories))
            self.assertTrue(FileAdapter)
        except ImportError as e:
            self.fail(f"Adapters import failed: {e}")
    
    def test_main_entry_point(self):
        """Test that the main entry point works."""
        try:
            from src.office_ppt_mcp.protocol.mcp_server import main
            self.assertTrue(callable(main))
        except ImportError as e:
            self.fail(f"Main entry point import failed: {e}")
    
    def test_services_functionality(self):
        """Test basic service functionality."""
        from src.office_ppt_mcp.services.design import DesignService
        from src.office_ppt_mcp.services.template import TemplateService
        
        # Test design service
        ds = DesignService()
        color_schemes = ds.get_color_schemes()
        self.assertIsInstance(color_schemes, dict)
        self.assertGreater(len(color_schemes), 0)
        
        # Test template service
        ts = TemplateService()
        search_dirs = ts.get_template_search_directories()
        self.assertIsInstance(search_dirs, list)
        self.assertGreater(len(search_dirs), 0)


if __name__ == '__main__':
    unittest.main()