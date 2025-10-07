import google.generativeai as genai

    # --- List Models Script ---
    # PASTE YOUR NEWEST "GOLDEN" API KEY DIRECTLY INTO THE QUOTES BELOW
MY_API_KEY = "..................................."

print("--- Listing Available Models for Your API Key ---")

try:
        # Configure the API directly with the key
        genai.configure(api_key=MY_API_KEY)
        
        print("\nSupported Models for 'generateContent':")
        
        count = 0
        # List all available models
        for m in genai.list_models():
            # Check if the model supports the 'generateContent' method (i.e., chat)
            if 'generateContent' in m.supported_generation_methods:
                print(f"  - {m.name}")
                count += 1

        if count == 0:
            print("\n--- CRITICAL ERROR ---")
            print("Your API key did not return any models that support 'generateContent'.")
            print("This indicates a potential issue with your Google Cloud project or account permissions.")
        else:
            print("\n--- SCRIPT SUCCEEDED ---")
            print("Please use one of the model names listed above in your chatbot.py file.")


except Exception as e:
        print("\n--- SCRIPT FAILED ---")
        print("An error occurred. This is likely an API key or authentication issue.")
        print("Error details:")
        print(e)
import google.generativeai as genai

# --- List Models Script ---
# PASTE YOUR NEWEST "GOLDEN" API KEY DIRECTLY INTO THE QUOTES BELOW
MY_API_KEY = "PASTE_YOUR_NEWEST_KEY_HERE"

print("--- Listing Available Models for Your API Key ---")

try:
    # Configure the API directly with the key
    genai.configure(api_key=MY_API_KEY)
    
    print("\nSupported Models for 'generateContent':")
    
    count = 0
    # List all available models
    for m in genai.list_models():
        # Check if the model supports the 'generateContent' method (i.e., chat)
        if 'generateContent' in m.supported_generation_methods:
            print(f"  - {m.name}")
            count += 1

    if count == 0:
        print("\n--- CRITICAL ERROR ---")
        print("Your API key did not return any models that support 'generateContent'.")
        print("This indicates a potential issue with your Google Cloud project or account permissions.")
    else:
        print("\n--- SCRIPT SUCCEEDED ---")
        print("Please use one of the model names listed above in your chatbot.py file.")


except Exception as e:
    print("\n--- SCRIPT FAILED ---")
    print("An error occurred. This is likely an API key or authentication issue.")
    print("Error details:")
    print(e)
