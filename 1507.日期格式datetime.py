class Solution:
    def reformatDate(self, date: str) -> str:
        from datetime import datetime
        import re
        return datetime.strptime(re.sub('st|nd|rd|th','',date),'%d %b %Y').strftime('%Y-%m-%d')

