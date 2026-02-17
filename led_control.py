import tkinter as tk  # Import the tkinter library for creating the GUI, aliased as 'tk'
from gpiozero import LED  # Import the LED class from gpiozero to control GPIO pins on the Raspberry Pi

# Set up LED on GPIO pin 17
led = LED(17)  # Create an LED object connected to GPIO pin 17

# Create the main window
root = tk.Tk()  # Initialize the main application window
root.geometry("400x300")  # Set the window size to 400 pixels wide by 300 pixels tall
root.title("LED Control")  # Set the title bar text to "LED Control"
root.configure(bg='black')  # Set the window background color to black

# Track whether LED is on or off
led_on = False  # Boolean variable to track the current state of the LED (starts off)


def toggle_led():  # Define function to toggle the LED on and off
    """Toggle the LED on/off and update the button appearance."""
    global led_on  # Use the global led_on variable so we can modify it inside this function
    if led_on:  # If the LED is currently on...
        led.off()  # Turn the LED off
        button.config(text="Turn LED ON", bg='green')  # Update button text and color to green (indicating it can be turned on)
        led_on = False  # Update the state variable to reflect LED is now off
    else:  # If the LED is currently off...
        led.on()  # Turn the LED on
        button.config(text="Turn LED OFF", bg='red')  # Update button text and color to red (indicating it can be turned off)
        led_on = True  # Update the state variable to reflect LED is now on


def toggle_fullscreen(event):  # Define function to toggle fullscreen, 'event' is passed by the key binding
    """Toggle fullscreen mode on/off."""
    is_fullscreen = root.attributes('-fullscreen')  # Get the current fullscreen state (True or False)
    root.attributes('-fullscreen', not is_fullscreen)  # Set fullscreen to the opposite of its current state


def exit_fullscreen(event):  # Define function to exit fullscreen mode, 'event' is passed by the key binding
    """Exit fullscreen mode."""
    root.attributes('-fullscreen', False)  # Disable fullscreen by setting it to False


# Create large touch-friendly button
button = tk.Button(  # Create a Button widget
    root,  # Place the button inside the main window
    text="Turn LED ON",  # Set the initial button text
    font=("Arial", 42),  # Set the font to Arial at size 42 (large for touch screens)
    bg='green',  # Set the button background color to green
    fg='white',  # Set the button text color to white
    command=toggle_led,  # Call the toggle_led function when the button is clicked
    height=7,  # Set the button height to 7 text units
    width=15  # Set the button width to 15 text units
)
button.pack(expand=True, fill='both', padx=20, pady=20)  # Add the button to the window, expanding to fill available space with 20px padding

# Bind keyboard shortcuts
root.bind('<F11>', toggle_fullscreen)  # Bind the F11 key to call the toggle_fullscreen function
root.bind('<Escape>', exit_fullscreen)  # Bind the Escape key to call the exit_fullscreen function

# Quit button at the bottom
quit_button = tk.Button(  # Create a second Button widget for quitting
    root,  # Place the button inside the main window
    text="QUIT",  # Set the button text to "QUIT"
    font=("Arial", 16),  # Set the font to Arial at size 16
    bg='darkred',  # Set the button background color to dark red
    fg='white',  # Set the button text color to white
    command=root.destroy  # Call root.destroy to close the application when clicked
)
quit_button.pack(side='bottom', pady=10)  # Place the quit button at the bottom of the window with 10px vertical padding

# Start the app
root.mainloop()  # Start the tkinter event loop, which keeps the window open and responsive to user input
