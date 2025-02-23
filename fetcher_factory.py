from fetch_content import FetchContent, PlaywrightFetchContent, SeleniumFetchContent

class FetcherFactory:
    def __init__(self):
        self.fatchers = {}
        self._register_fatcher("playwright", PlaywrightFetchContent)
        self._register_fatcher("selenium", SeleniumFetchContent)

    def _register_fatcher(self, fatcher_name, fatcher: FetchContent):
        self.fatchers[fatcher_name] = fatcher

    def get_fatcher(self, fatcher_name,base_url)->FetchContent:
        fatcher = self.fatchers.get(fatcher_name)
        if fatcher:
            return fatcher(base_url)
        raise ValueError(f"Invalid fatcher name {fatcher_name}")