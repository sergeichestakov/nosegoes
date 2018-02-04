from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

class Browser:

    new_tabs = ["https://developer.mozilla.org/en-US/", "https://stackoverflow.com/", "https://www.reddit.com/", "https://news.ycombinator.com/"]
    default_site = "https://en.wikipedia.org/wiki/Main_Page"
    def __init__(self):
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        self.populate()

    def populate(self):
        main_window = self.browser.current_window_handle
        self.browser.execute_script(f"window.location.href = '{self.default_site}'")

        #Open new tabs
        for tab in Browser.new_tabs:
            javascript = f"window.open('{tab}');"
            self.browser.execute_script(javascript)
            sleep(0.4)

        #Switch back to original tab
        self.browser.switch_to_window(main_window)

    def run(self):
        while(True):
            sleep(2)
            self.switchTabs('right')
            sleep(2)
            self.switchTabs('left')

    #Switch tabs left and right: direction should be 'left' or 'right'
    def openTab(self):
        print("opening a new tab")
        self.browser.execute_script("window.open('https://google.com')")

    def forward(self):
        print("going forward")
        self.browser.execute_script("window.history.forward();")
    
    def back(self):
        print("going back")
        self.browser.execute_script("window.history.back();")

    def openWebsite(self, name):
        self.browser.execute_script("window.location.href = '" + self.getWebsite(name) + "'")

    def switchTabs(self, direction):
        tabs = self.browser.window_handles
        currTab = self.browser.current_window_handle
        currIndex = tabs.index(currTab)

        newIndex = self.getNewIndex(currIndex, direction)
        self.browser.switch_to_window(tabs[newIndex])

    def getNewIndex(self, currIndex, direction):
        maxIndex = len(self.browser.window_handles) - 1
        if(direction == 'left'):
            return currIndex - 1 if currIndex > 0 else maxIndex
        elif(direction == 'right'):
            return currIndex + 1 if currIndex < maxIndex else 0

    def getScroll(self, direction):
        return {
            'up': -500,
            'down': 500
        }[direction]

    def getWebsite(self, name):
        return "https://"+name+".com/"
        if name is "facebook":
            return "https://facebook.com"
        if name is "reddit":
            return "https://reddit.com"
        if name is "twitter":
            return "https://twitter.com"
        if name is "google":
            return "https://google.com"
        return "https://google.com/?q=" + name

    def getScrollKey(self, direction):
        return {
            'up': Keys.ARROW_UP,
            'down': Keys.ARROW_DOWN
        }[direction]
    #Scrolls up and down the page: direction should be 'up' or 'down'
    def scroll(self, direction):
        scrollValue = self.getScroll(direction)
        scrollKey = self.getScrollKey(direction)
        ActionChains(self.browser).key_down(scrollKey).perform()
        #javascript = f"window.scrollBy(0, {str(scrollValue)})"
        #self.browser.execute_script(javascript)

    def close(self):
        self.browser.close()
        self.browser.quit()

def main():
    browser = Browser()
    browser.run()
    #browser.close()

if __name__ == "__main__":
    main()
