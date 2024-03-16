

import UI.UI as UI
import Tests.Tests as Tests

def main():
    Tests.test_tick_functionality()
    print("Test passed!")
    ui = UI.UI()
    ui.run()


if __name__ == '__main__':
    main()

