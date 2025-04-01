import json
import jmespath
import requests

from sqlalchemy.ext.asyncio import AsyncSession
from core.crud import create_posts


async def parse_new_post(db: AsyncSession):
    data = {
        'av': '17841401925677520',
        '__d': 'www',
        '__user': '0',
        '__a': '1',
        '__req': '8',
        '__hs': '20178.HYP:instagram_web_pkg.2.1...1',
        'dpr': '2',
        '__ccg': 'EXCELLENT',
        '__rev': '1021407836',
        '__s': '9ox5fi:ejfrh4:2014lt',
        '__hsi': '7487976170473803137',
        '__dyn': '7xe5WwlEnwn8K2Wmm1twpUnwgU7S6EdF8aUco38w5ux609vCwjE1EE2Cw8G11wBw5Zx62G3i1ywOwa90Fw4Hw9O0Lbwae4UaEW2G0AEco5G0zEnwhE0Caazo7u1xwIwbS1LwTwKG0hq1Iwqo5q1IQp1yU426V8aUuwm8jxK2K0P8Km5o',
        '__csr': 'h475PMVlhIDkYhFsCzubFF4KSAiAbQFCXqVUDUZ2d6AAmnVdngaaz8hG8WgzqyRpbCJ7Byau6bgig-ubCS6Uiopzu368zEmg8VUGH8Ea8vwAxC9wxzVEy2OcG2y2q25004NIyp60pam0bNwoofFk0pO06yE1vE0gLBAwNoOrg0Su0ne0lYM6x1-19wjokw3T82mScgSkj801Ilw3sE',
        '__hsdp': 'l2292GkkkjkN7ai4papBlaQoBFRKqhamTnlb8fjF0GwwoWq2O5obfQ253shcm1oaC3O0w8566EqwyzAaxx2E8E34wu82HDxq686-05j86W0hG3a48y0nS581W8fE',
        '__hblp': '09a19wwwdG1zwoEbo46cwIU42m6Eqxy9xG22UG5Udoig3bwDwaK3ai1Lga87mU1d83Hgx04tw5uwrEnxe0FE4uawDwqU9U2ygG7odEkw5XyoiwjUfE',
        '__comet_req': '7',
        'fb_dtsg': 'NAcPJHTTUGamOWYfEh0eMcPEL7e98BHGfgQEP3oLoJl7ORl_N0QuXJw:17865379441060568:1733938433',
        'jazoest': '26082',
        'lsd': 'R7xHu8f2dYcFo0STSD5yiW',
        '__spin_r': '1021407836',
        '__spin_b': 'trunk',
        '__spin_t': '1743430311',
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'PolarisProfilePostsQuery',
        'variables': '{"data":{"count":10,"include_reel_media_seen_timestamp":true,"include_relationship_info":true,"latest_besties_reel_media":true,"latest_reel_media":true},"username":"nasa","__relay_internal__pv__PolarisIsLoggedInrelayprovider":true,"__relay_internal__pv__PolarisShareSheetV3relayprovider":true}',
        'server_timestamps': 'true',
        'doc_id': '9750506811647048',
    }

    response = requests.post('https://www.instagram.com/graphql/query', data=data)
    post_data = json.loads(response.text)
    posts = jmespath.search('data.xdt_api__v1__feed__user_timeline_graphql_connection.edges', post_data)
    new_posts = await create_posts(db, posts)
    return new_posts
