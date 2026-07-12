class Site:

    def __init__(self, url = None):
        self.url = url
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.homepage = Site(homepage)
        self.current = self.homepage

    def visit(self, url: str) -> None:
        newSite = Site(url)
        curr = self.current
        newSite.prev = curr
        curr.next = newSite
        self.current = newSite

    def back(self, steps: int) -> str:
        curr = self.current
        while curr.prev:
            if steps == 0:
                self.current = curr
                return curr.url
            curr = curr.prev
            steps -= 1
        self.current = self.homepage
        return curr.url

    def forward(self, steps: int) -> str:
        curr = self.current
        while curr.next:
            if steps == 0:
                self.current = curr
                return curr.url
            curr = curr.next
            steps -= 1
        self.current = curr
        return curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)