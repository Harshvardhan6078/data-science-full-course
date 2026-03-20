import os
import sys

try:
    import google.generativeai as genai
except ImportError:
    print("Required library not found. Please install it using:")
    print("pip install google-generativeai")
    sys.exit(1)

# Configure the API Key
# The key you provided earlier is saved here:
API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyBERN50M_R_fxFJhSCb-d84--gcwG7GNNs")
genai.configure(api_key=API_KEY)

# The system prompt sets the behavior of the AI
SYSTEM_INSTRUCTION = """
You are a highly capable, professional, fast, and responsive personal assistant. 
Your primary roles are:
1. To help the user solve day-to-day problems quickly, offering practical and concise solutions.
2. To be an excellent conversational partner to help the user practice their English communication. 
   - Proactively but politely correct any grammatical errors or awkward phrasing in their English.
   - Suggest better vocabulary where appropriate.
   - Keep responses natural, engaging, and highly professional.
"""

def main():
    print("=" * 65)
    print(" 🤖 Personal Assistant Chatbot Initialized (Text Only)")
    print(" - Fast, responsive, and ready to help.")
    print(" - Type 'quit', 'exit', or 'q' to end the conversation.")
    print("=" * 65)
    
    try:
        # Initializing the model. 
        # `gemini-2.5-flash` is used here because it is exceptionally fast and responsive.
        model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            system_instruction=SYSTEM_INSTRUCTION
        )
        
        # Start a chat session, which automatically keeps track of conversation history
        chat = model.start_chat(history=[])
        
    except Exception as e:
        print(f"Error initializing model: {e}")
        return

    while True:
        try:
            user_input = input("\nYou: ")
            
            if user_input.strip().lower() in ['quit', 'exit', 'q']:
                print("\nChatbot: Goodbye! Have a productive day.")
                break
                
            if not user_input.strip():
                continue
                
            print("Chatbot: ", end="", flush=True)
            
            # Using stream=True gives the bot a fast, typewriter-like responsive feel 
            # rather than waiting for the entire response to generate.
            response = chat.send_message(user_input, stream=True)
            
            for chunk in response:
                print(chunk.text, end="", flush=True)
            print() # Add a newline when the response is complete
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\nChatbot: Goodbye!")
            break
        except Exception as e:
            # Handle API errors or network issues
            print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    main()
