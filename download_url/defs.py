import requests
import tempfile
from django.core import files

from .models import Post, Channel

# token = '945735692:AAGRmd7V6ENtP2SGuDsQg-aQVgoRUkr5tgQ'
# bot = telebot.TeleBot(token)


def insert():
    f = Post(chat_title="this is chat title", chat_username="chat username", text="1st text test", is_retail=True)
    f.save()
    return


def download_images():
    print("in download image def")

    url = "http://bayanbox.ir/view/2001315563847741354/%D8%B9%DA%A9%D8%B3-%D9%86%D9%88%D8%B4%D8%AA%D9%87-good-morning-2.jpg"
    url1 = "http://files.namnak.com/users/lm/aup/201804/22_pics/%D8%B9%DA%A9%D8%B3-%D9%87%D8%A7%DB%8C-%D8%AE%D9%86%D8%AF%D9%87-%D8%AF%D8%A7%D8%B1.jpg"
    url2 = "http://delbaraneh.com/wp-content/uploads/2019/04/%D8%B9%DA%A9%D8%B3-%D8%AF%D8%AE%D8%AA%D8%B1-%D8%B2%DB%8C%D8%A8%D8%A7-%D8%A8%D8%B1%D8%A7%DB%8C-%D9%BE%D8%B1%D9%88%D9%81%D8%A7%DB%8C%D9%84-1.jpg"

    # List of images to download
    image_urls = [
        url2,
    ]

    for image_url in image_urls:
        # Steam the image from the url
        print("in first for")
        request = requests.get(image_url, stream=True)
        print("after steaming")

        # Was the request OK?
        if request.status_code != requests.codes.ok:
            print("error handling")
            # Nope, error handling, skip file etc etc etc
            continue

        # Get the filename from the url, used for saving later
        file_name = image_url.split('/')[-1]

        # Create a temporary file
        lf = tempfile.NamedTemporaryFile()

        # Read the streamed image in sections
        for block in request.iter_content(1024 * 8):
            # If no more file then stop
            if not block:
                break

            # Write image block to temporary file
            lf.write(block)


        # Save the temporary image to the model#
        # This saves the model so be sure that is it valid
        c = Channel.objects.get(chat_title="channel45")

        post = Post(channel=c)
        '''
        defining channel within post like below is not effective 
        post.channel.ad_user = 'aduser1'
        '''
        post.image.save(file_name, files.File(lf))
        print("after save")

    return post.pk


def send_photo(chat_id, message_id, id):
    record = Post.objects.get(pk=id)
    id1chattitle = record.chat_title
    path = record.image.url

    # bot.send_photo(chat_id, photo=open(path, 'rb'))
    return


def get_cahnnel_with_sprcific_saletype_senf():
    for channel in Channel.objects.filter(saletype__name="wholesale"):
        print(channel)