from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlunparse,urlencode
from urllib.request import urlopen

import requests
from PIL import Image
from django.utils import timezone
from social_core.exceptions import AuthForbidden
from users.models import UserProfile

def save_user_profile(backend,user,response,*args,**kwargs):
    if backend.name != 'vk-oauth2':
        return

    api_url = urlunparse(('https',
                          'api.vk.com',
                          '/method/users.get',
                          None,
                          urlencode(OrderedDict(fields=','.join(('bdate', 'sex', 'about', 'personal', 'domain','photo_max')),
                                                access_token=response['access_token'],
                                                v='5.131')),
                          None
                          ))
    resp = requests.get(api_url)
    if resp.status_code != 200:
        return

    data = resp.json()['response'][0]

    if data['sex']:
        user.userprofile.gender = UserProfile.MALE if data['sex'] == 2 else UserProfile.FEMALE

    if data['about']:
        user.userprofile.about_me = data['about']

    bdate = datetime.strptime(data['bdate'], '%d.%m.%Y').date()

    age = timezone.now().date().year - bdate.year
    user.age = age
    if age < 18:
        user.delete()
        raise AuthForbidden('social_core.backends.vk.VKOAuth2')

    if data['personal']:
        if 'langs' in data['personal']:
            user.userprofile.langs = ', '.join(data['personal']['langs'])
        else:
            user.userprofile.langs =''

    if data['domain']:
        user.userprofile.vk_id = f"vk.com/{data['domain']}"

    if data['photo_max']:
        img_data = requests.get(data['photo_max']).content
        with open(f"media/users_image/{user.username}{user.id}.jpg", 'wb') as handler:
            handler.write(img_data)
        user.image = f"users_image/{user.username}{user.id}.jpg"
    user.save()