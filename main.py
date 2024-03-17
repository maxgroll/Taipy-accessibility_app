from taipy.gui import Gui

logo = "static/online-marketing-agentur-berlin-digitalagenten-logo-orange-mobil-40.svg"
mode = False
static_header = """
<|layout|columns=1fr auto 1fr
<|{logo}|image|width=80px|>
# **Web Accessibility Checker**
#<|{mode}|toggle|theme=switch_mode|class_name=nolabel|>
|>
#"""
# Define a function to handle theme switching
def switch_mode(value):
    # Toggle the theme state
    if value == False:
        return True
    else:
        return False
# This area will be updated dynamically based on user interactions
dynamic_area = "<div id='dynamic_area'></div>"

# Define the complete page layout by combining the static header and the dynamic area
page = static_header + dynamic_area

# Function to update the dynamic area of the UI
def update_dynamic_area(gui, content):
    gui.get_element_by_id('dynamic_area').markdown = content

# Run the app
if __name__ == "__main__":
    #switch_mode(mode)
    Gui(page).run(title="Web Accessibility Checker", debug=True, use_reloader=True, favicon="static/online-marketing-agentur-berlin-digitalagenten-logo-orange-mobil-40.svg", dark_mode=mode) 
