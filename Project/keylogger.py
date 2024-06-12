from pynput import keyboard

# A buffer to keep the last 10 characters
key_buffer = []

# Function to handle key press events
def on_press(key):
    global key_buffer
    
    try:
        # Convert the key press to a character
        char = key.char
    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.space:
            char = ' '
        elif key == keyboard.Key.enter:
            char = '\n'
        elif key == keyboard.Key.tab:
            char = '\t'
        elif key == keyboard.Key.backspace:
            char = '<BACKSPACE>'
        else:
            char = ''  # Ignore other special keys

    if char:
        # Append the character to the buffer
        key_buffer.append(char)
        if len(key_buffer) > 10:
            key_buffer.pop(0)
        
        # Check if the buffer contains 10 spaces
        if ''.join(key_buffer) == ' ' * 10:
            # Execute the function to add two numbers
            add_two_numbers()
            # Clear the buffer
            key_buffer = []

# Function to handle key release events (optional)
def on_release(key):
    pass

# Function to add two numbers (example function)
def add_two_numbers():
    num1 = 10
    num2 = 20
    result = num1 + num2
    print(f'The result of {num1} + {num2} is {result}')

# Start listening to keyboard events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
