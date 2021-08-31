import json
from urllib.parse import quote, urlencode

BASE_URL = "https://m.tiktok.com/"

def __add_url_params__(self) -> str:
        api_url = (
            BASE_URL + "api/post/item_list/?{}&count={}&id={}&type=1&secUid={}"
            "&cursor={}&sourceType=8&appId=1233&region={}&language={}".format(
                self.__add_url_params__(),
                page_size,
                str(userID),
                str(secUID),
                cursor,
                region,
                language,
            )
        )

        query = {
            "aid": 1988,
            "app_name": "tiktok_web",
            "device_platform": "web_mobile",
            "region": self.region or "US",
            "priority_region": "",
            "os": "ios",
            "referer": "",
            "root_referer": "",
            "cookie_enabled": "true",
            "screen_width": self.width,
            "screen_height": self.height,
            "browser_language": self.browser_language.lower() or "en-us",
            "browser_platform": "iPhone",
            "browser_name": "Mozilla",
            "browser_version": self.__format_new_params__(self.userAgent),
            "browser_online": "true",
            "timezone_name": self.timezone_name or "America/Chicago",
            "is_page_visible": "true",
            "focus_state": "true",
            "is_fullscreen": "false",
            "history_len": random.randint(0, 30),
            "language": self.language or "en"
        }
        return urlencode(query)