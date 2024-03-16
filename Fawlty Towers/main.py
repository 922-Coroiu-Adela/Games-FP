# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import UI.UI as UI
import Tests.Tests as Tests

def main():
    tests = Tests.test_functionalities()
    ui = UI.UI()
    ui.run()

main()