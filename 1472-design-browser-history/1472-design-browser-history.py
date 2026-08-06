class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current = 0

    def visit(self, url: str) -> None:
        # Remove forward history
        self.history = self.history[:self.current + 1]
        
        # Add new page
        self.history.append(url)
        self.current += 1

    def back(self, steps: int) -> str:
        # Move back safely
        self.current = max(0, self.current - steps)
        return self.history[self.current]

    def forward(self, steps: int) -> str:
        # Move forward safely
        self.current = min(len(self.history) - 1, self.current + steps)
        return self.history[self.current]
        
# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)