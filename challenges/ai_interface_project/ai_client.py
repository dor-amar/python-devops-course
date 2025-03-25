"""
AI Interface Project

Create a Python interface for interacting with a local AI model using GPT4All.
This project will help you learn about:
- Working with AI models locally
- API design patterns
- JSON handling
- Error management
- Type hints

Requirements:
- gpt4all (pip install gpt4all)
- typing
- json

TODO:
1. Implement the AIClient class that will:
   - Initialize a local GPT4All model
   - Handle model queries
   - Manage responses
   - Implement proper error handling

2. The interface should support:
   - Text generation
   - Model configuration
   - Response formatting
"""

from typing import Dict, Any, Optional
import json


class AIClient:
    """Interface for local AI model interactions."""
    
    def __init__(self, model_name: str = "ggml-gpt4all-j-v1.3-groovy"):
        """
        TODO: Initialize the AI client with a local model
        - Download and load the specified model
        - Set up default parameters
        - Initialize any necessary configurations
        """
        pass

    def generate_text(self, prompt: str, max_tokens: int = 100) -> Dict[str, Any]:
        """
        TODO: Generate text using the local AI model
        
        Args:
            prompt: The input prompt for the AI
            max_tokens: Maximum number of tokens in the response
            
        Returns:
            Dict containing:
            - generated_text: str
            - model_name: str
            - tokens_used: int
            - generation_time: float
            
        Raises:
            ValueError: If the prompt is invalid
            RuntimeError: If model generation fails
        """
        pass

    def configure_model(self, 
                       temperature: float = 0.7,
                       top_p: float = 0.9,
                       repeat_penalty: float = 1.1) -> None:
        """
        TODO: Configure model parameters
        
        Args:
            temperature: Controls randomness (0.0 to 1.0)
            top_p: Controls diversity (0.0 to 1.0)
            repeat_penalty: Prevents repetition (> 1.0)
            
        Raises:
            ValueError: If parameters are out of valid ranges
        """
        pass

    def save_conversation(self, 
                         conversation_id: str,
                         messages: list) -> None:
        """
        TODO: Save conversation history to a JSON file
        
        Args:
            conversation_id: Unique identifier for the conversation
            messages: List of message dictionaries
            
        Raises:
            IOError: If saving fails
        """
        pass

    def load_conversation(self, conversation_id: str) -> list:
        """
        TODO: Load conversation history from a JSON file
        
        Args:
            conversation_id: Unique identifier for the conversation
            
        Returns:
            List of message dictionaries
            
        Raises:
            FileNotFoundError: If conversation doesn't exist
        """
        pass


def main():
    """
    TODO: Implement example usage of the AIClient class
    - Create different types of prompts
    - Test error handling
    - Demonstrate conversation saving/loading
    - Show model configuration
    """
    pass


if __name__ == "__main__":
    main() 