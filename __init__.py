import aiohttp
from aiohttp import ClientSession

# 保存原始的 get 方法
original_get = ClientSession._request

def patched_get(self, method, url, *args, **kwargs):
    # 修改 URL
    if url.startswith("https://github.com") or url.startswith("https://raw.githubusercontent.com"):
        p_url = url
        url = "https://ghfast.top/" + p_url
        print(f"MONKEY PATCH: CHANGE URL FROM {p_url} TO {url}\n")

    # 调用原始的 get 方法
    return original_get(self, method, url, *args, **kwargs)

# 替换原来的 _request 方法
ClientSession._request = patched_get

NODE_CLASS_MAPPINGS = {}