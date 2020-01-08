import urllib.request
# import telebot
import os
import time

from .models import Post

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
    url3 = ""
    url4 = ""
    url5 = ""
    import requests
    import tempfile

    from django.core import files

    # List of images to download
    image_urls = [
        url,
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
        print("after lf")
        # Read the streamed image in sections
        for block in request.iter_content(1024 * 8):
            print("in block for")
            # If no more file then stop
            if not block:
                print("break for")
                break

            # Write image block to temporary file
            lf.write(block)
            print("after lf.write")

        # Create the model you want to save the image to
        image = Post()
        print("after image")

        # Save the temporary image to the model#
        # This saves the model so be sure that is it valid
        image.image.save(file_name, files.File(lf))
        print("after save")
    print("before return")
    #
    # print("time to sleep")
    # time.sleep(2)
    #
    # print("ready to delete")
    # channel = Channels.objects.all()
    # for pk in channel:
    #     try:
    #         print("in for")
    #         print("i = " + str(pk.))
    #         channel.objects.get(id=pk).image.delete(save=True)
    #     except:
    #         print("except run")
    # print("after for before render")

    return image.pk


def send_photo(chat_id, message_id, id):
    print("id = " + str(id))
    print("in send_photo")

    record = Post.objects.get(pk=id)
    print("id1")
    print(record)
    id1chattitle = record.chat_title
    print("id1chattitle = " + id1chattitle)
    path = record.image.url
    print("path = " + path)

    # bot.send_photo(chat_id, photo=open(path, 'rb'))
    print("after send")
    return
