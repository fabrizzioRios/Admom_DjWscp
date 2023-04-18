import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main_async():
    img_list = []
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, 'https://www.casasyterrenos.com/jalisco/zapopan/terrenos/venta')
        split_html = html.split('"')
        for element in range(len(split_html)):
            if split_html[element] == "photoPreview":
                img_list.append(split_html[element + 2])
    return img_list

