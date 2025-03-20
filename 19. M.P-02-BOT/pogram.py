import pyautogui
import pyperclip
import time

# Function to click on an chrome icon at the specified coordinates
def click_icon(x, y):
    pyautogui.moveTo(x, y)
    pyautogui.click()

# Function to select text by dragging the mouse
def drag_and_select_text(start_x, start_y, end_x, end_y):
    pyautogui.moveTo(start_x, start_y)
    pyautogui.dragTo(end_x, end_y, duration=0.5, button='left')

# Function to copy selected text to the clipboard
def copy_to_clipboard():
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)  # Wait for a moment to ensure the text is copied

# Function to retrieve the text from the clipboard
def get_copied_text():
    return pyperclip.paste()

# Main script
if __name__ == "__main__":
    # Coordinates to click on the icon
    icon_x, icon_y = 560, 746
    # Coordinates to start and end the drag action
    drag_start_x, drag_start_y = 440, 109
    drag_end_x, drag_end_y = 1345, 651

    # Click on the icon
    click_icon(icon_x, icon_y)
    time.sleep(1)  # Wait for a moment before the next action

    # Drag to select text
    drag_and_select_text(drag_start_x, drag_start_y, drag_end_x, drag_end_y)
    time.sleep(0.5)  # Wait for a moment before the next action

    # Copy the selected text to the clipboard
    copy_to_clipboard()

    # Get the copied text from the clipboard
    copied_text = get_copied_text()
    print(f"Copied Text: {copied_text}")
