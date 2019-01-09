import errno
import os
import sys
import tempfile
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import requests, json
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URIAction,
    PostbackAction, DatetimePickerAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent,
    FlexSendMessage, BubbleContainer, ImageComponent, BoxComponent,
    TextComponent, SpacerComponent, IconComponent, ButtonComponent,
    SeparatorComponent,
)
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('f2ZAIRDhyaMMmmhPB1G8BQDZjzFc2aTM2g1Y5J9jWliY0M4+gMhYzzTrDm9Os1aUv7oKIetsvYetYwlmuiGj4deDwfKFQOeKcnMlhMkubwpUmZCfojqzQS10+vVZC89KRA3uLIuz/ObEFaXWf0UaUgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('ed773ebfcd44875532c32f39ff494158')
#-------------{ Credit by @Basyir? }-------------#

notes = {}



# Post Request

@app.route("/callback", methods=['POST'])

def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'
    
@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Type /help for command :D')) 

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text
 
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    text = event.message.text #simplify for receove message
    sender = event.source.user_id #get user_id
    gid = event.source.sender_id #get group_id
#-------------{ Credit by @Basyir? }-------------#
    if text == '/me':
        if isinstance(event.source, SourceGroup):
            profile = line_bot_api.get_profile(event.source.user_id)
            line_bot_api.reply_message(
                event.reply_token, [
                    TextSendMessage(text='Display name: ' + profile.display_name),
                    TextSendMessage(text='Status message: ' + profile.status_message)
                ]
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't use profile in group chat"))

    if text == '/bsybye':
        if isinstance(event.source, SourceGroup):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Pamit dulu bye-bye'))
            line_bot_api.leave_group(event.source.group_id)
        elif isinstance(event.source, SourceRoom):
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text='Pamit dulu bye-bye'))
            line_bot_api.leave_room(event.source.room_id)
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="Bot can't leave from 1:1 chat"))
#-------------{ Credit by @Basyir? }-------------#
    if text == "redtube on":
    	r = request.get_data('https://api.eater.pw/redtube?page=1')
    	data=r.text
    	data=json.loads(data)
    	for anu in data["result"]:
        	line_bot_api.reply_message(event.reply_token,VideoMessage(original_content_url=anu["dl"], preview_image_url=anu["img"]))
        
    elif text == "xvideos on":
    	r = request.get_data('https://api.eater.pw/xvideos?page=1')
    	data=r.text
    	data=json.loads(data)
    	for anu in data["result"]:
    		line_bot_api.reply_message(event.reply_token,VideoMessage(original_content_url=anu["dl"], preview_image_url=anu["img"]))
#-------------{ Credit by @Basyir? }-------------#
    elif text == 'confirm':
        confirm_template = ConfirmTemplate(text='Bot nya bagus?', actions=[
            MessageTemplateAction(label='Yes', text='Yes!'),
            MessageTemplateAction(label='No', text='No!'),
        ])
        template_message = TemplateSendMessage(
            alt_text='Confirm alt text', template=confirm_template)
        line_bot_api.reply_message(event.reply_token, template_message)

    elif "/idline: " in event.message.text:
        skss = event.message.text.replace('/idline: ', '')
        sasa = "http://line.me/R/ti/p/~" + skss
        text_message = TextSendMessage(text=sasa)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
        
    elif "/fs1: " in event.message.text:
        skss = event.message.text.replace('/fs1: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=rambu&text=' + skss,
        preview_image_url='https://rest.farzain.com/api/special/fansign/indo/viloid.php?apikey=rambu&text=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/fs2: " in event.message.text:
        skss = event.message.text.replace('/fs2: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=rambu&text=' + skss,
        preview_image_url='https://rest.farzain.com/api/special/fansign/cosplay/cosplay.php?apikey=rambu&text=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0
    elif "/graffiti: " in event.message.text:
        skss = event.message.text.replace('/graffiti: ', '')
        message = ImageSendMessage(
        original_content_url='https://rest.farzain.com/api/photofunia/graffiti_wall.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&text2=Gans&text1=' + skss,
        preview_image_url='https://rest.farzain.com/api/photofunia/graffiti_wall.php?&apikey=3w92e8nR5eWuDWQShRlh6C1ye&text2=Gans&text1=' + skss
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    elif "/apakah " in event.message.text:
        quo = ('Iya','Tidak','Gak tau','Bisa jadi','Mungkin iya','Mungkin tidak')
        jwb = random.choice(quo)
        text_message = TextSendMessage(text=jwb)
        line_bot_api.reply_message(event.reply_token, text_message)
        return 0
        
    if text == '/tiktok':
        url = requests.get("https://rest.farzain.com/api/tiktok.php?country=jp&apikey=3w92e8nR5eWuDWQShRlh6C1ye&type=json")
        data = url.json()
        message = VideoSendMessage(
        original_content_url=data["first_video"],
        preview_image_url='https://i.ibb.co/Tr1mjYH/1545946474474.jpg'
        )
        line_bot_api.reply_message(event.reply_token, message)
        return 0

    elif (text == 'Bot') or (text == 'bot'):
        message = TextSendMessage(text='Siapa bot? ke bot an lu')
        line_bot_api.reply_message(event.reply_token, message)
    if text == '/info bmkg':
        url = request.get("https://triopekokbots026.herokuapp.com/bmkg")
        data = url.json()
        message = TextSendMessage(text=data["info"])
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ Credit by @Basyir? }-------------#

    elif text == '/tools':
        buttons_template = TemplateSendMessage(
            alt_text='Tools message',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.ibb.co/Tr1mjYH/1545946474474.jpg',
                title='TOOLS MESSAGE',
                text= '>Tap the Button<',
                align= 'center',
                actions=[
                    MessageTemplateAction(
                        label='More App',
                        text='/app'
                    ),
                    MessageTemplateAction(
                        label='Cek idline',
                        text='/idline: savegenerasimicin'
                    ),
                    MessageTemplateAction(
                        label='Your profile',
                        text='/me'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)

    elif (text == '/help') or (text == 'help') or (text == 'Help'):
        buttons_template = TemplateSendMessage(
            alt_text='Help message',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.ibb.co/Tr1mjYH/1545946474474.jpg',
                title='HELP MESSAGE',
                text= '>Tap the Button<',
                align= 'center',
                actions=[
                    MessageTemplateAction(
                        label='My Creator',
                        text='/creator'
                    ),
                    MessageTemplateAction(
                        label='List bot',
                        text='/bsy bots'
                    ),
                    MessageTemplateAction(
                        label='Aplikasi',
                        text='/app'
                    ),
                    MessageTemplateAction(
                        label='Bot bye',
                        text='/bsybye'
                    )
                ]
            )
        )
        
        line_bot_api.reply_message(event.reply_token, buttons_template)

#-------------{ Credit by @Basyir? }-------------#

    elif text == '/bsy bots':
        message = TemplateSendMessage(
            alt_text='List Bot',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.ibb.co/Tr1mjYH/1545946474474.jpg',
                        title='PUBLIC BOT',
                        text='TRIO PEKOK BOTS',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='http://line.me/ti/p/~triopekokbots'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.ibb.co/Tr1mjYH/1545946474474.jpg',
                        title='OA FAMS',
                        text='TRIO PEKOK BOTS',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='http://line.me/ti/p/%40nhz7119a'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.ibb.co/Tr1mjYH/1545946474474.jpg',
                        title='BOT OFFICIAL',
                        text='BASYIR INI MAH',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='http://line.me/ti/p/%40swv6521a'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == '/creator') or (text == 'About'):
        message = TemplateSendMessage(
            alt_text='My creator',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.ibb.co/Tr1mjYH/1545946474474.jpg',
                        title='CREATOR BOT',
                        text='This is my creator',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='https://line.me/ti/p/~savegenerasimicin'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.ibb.co/Tr1mjYH/1545946474474.jpg',
                        title='OA CREATOR',
                        text='This is my creator',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='http://line.me/ti/p/%40swv6521a'
                            )
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.ibb.co/Tr1mjYH/1545946474474.jpg',
                        title='OA FAMS',
                        text='This is my Fams',
                        align= 'center',
                        actions=[
                            URITemplateAction(
                                label='>Tap the Button<',
                                uri='http://line.me/ti/p/%40tmu9418f'
                            )
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    if event.message.text == "/app":
        buttons_template = TemplateSendMessage(
            alt_text='More App',
            template=ButtonsTemplate(
                title='More Aplikasi',
                text='Klik salah satu menu dibawah ini.',
                align= 'center',
                thumbnail_image_url='https://i.ibb.co/Tr1mjYH/1545946474474.jpg',
                actions=[
                    URITemplateAction(
                        label='Line',
                        uri='https://drive.google.com/file/d/1C9HApH1D-f60KRFVsTBhAXspFQg25ZZ8/view?usp=drivesdk'
                    ),
                    URITemplateAction(
                        label='Create Fancyname',
                        uri='https://drive.google.com/file/d/1bLA28as0LztPNO1x28TeK1Xm3jnKXn5q/view?usp=drivesdk'
                    ),
                    URITemplateAction(
                        label='Es File Explorer Pro',
                        uri='http://rexdlfile.com/index.php?id=es-file-explorer-pro-apk'
                    ),
                    URITemplateAction(
                        label='Multi Pro',
                        uri='https://m.apkpure.com/id/multiple-account-pro/workersdesign.dualaccountpro'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, buttons_template)
        return 0

#-------------{ Credit by @Basyir? }-------------#
    elif (text == 'makasih') or (text == 'Makasih'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/21831487/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Matamu') or (text == 'Matane'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/7111997/IOS/sticker.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hoax') or (text == 'Hoaxx'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/11221543/IOS/sticker.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'nyimak') or (text == 'Nyimak'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/9756022/IOS/sticker.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'ga') or (text == 'gak') or (text == 'gamau') or (text == 'Gamau') or (text == 'Ga') or (text == 'Gak'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/8683557/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Keren') or (text == 'Mantap') or (text == 'Kerenn') or (text == 'Mantapp') or (text == 'Bagus') or (text == 'Hebat'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12860202/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sepi'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200512/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Malem') or (text == 'Met malem'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/18282481/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Hai') or (text == 'Halo'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186953/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/~savegenerasimicin')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'sabar') or (text == 'Sabar'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22499899/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/~savegenerasimicin')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Ngantuk'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691708/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/~savegenerasimicin')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Haha') or (text == 'Wkwk'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200499/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/~savegenerasimicin')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Kzl') or (text == 'Kezel'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24464008/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/~savegenerasimicin')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Go') or (text == 'Siap'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186952/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif text == 'Bingung':
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/34751035/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Tolong') or (text == 'Please'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/11825345/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)

    elif (text == 'Okee') or (text == 'Okay') or (text == 'Ok') or (text == 'Oke'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22482252/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Baper') or (text == 'Karepmu'):
        message = TemplateSendMessage(
            alt_text='TRIO PEKOK PROTECTION',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16365505/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kamm') or (text == 'Kam') or (text == 'Wc') or (text == 'Welcome'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24862265/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bye') or (text == 'Minggat'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200514/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Ngopi') or (text == 'Ngopii') or (text == 'Ngopi cok') or (text == 'Ngopi woy'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691714/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Opo') or (text == 'Opoo') or (text == 'Naon'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691705/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Jancik') or (text == 'Jancok') or (text == 'Jancuk') or (text == 'Ancik'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547155/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sider on') or (text == 'Cctv on') or (text == 'Lurking on') or (text == '.sider on'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200507/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Mandi') or (text == 'Adus') or (text == 'Mandi dulu') or (text == 'Adus sik'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691709/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Juhh') or (text == 'Johh') or (text == 'Juoh'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12521487/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hbd') or (text == 'Met ultah') or (text == 'Selamat hari jadi') or (text == 'Happy Birthday'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/7670129/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Salken') or (text == 'Salam kenal'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24464015/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'O') or (text == 'O aja') or (text == 'Oo') or (text == 'Ooo'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/17530681/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Gift') or (text == 'Gift aku') or (text == 'Gift me') or (text == 'Gift dul'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/22220762/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Dih'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12842266/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Yank') or (text == 'Syg') or (text == 'Jo'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/78960399/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'No') or (text == 'Tidak Boleh') or (text == 'Moh') or (text == 'Giah'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12842265/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Galau') or (text == 'Galon') or (text == 'Lagi galon') or (text == 'Lagi galau'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/55737941/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kenyang') or (text == 'Wareg'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12842261/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == '$me') or (text == 'Me') or (text == '.me') or (text == '!me'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/16673425/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Maaf') or (text == 'Sorry'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/18282476/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Muleh'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/20217667/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Mbalik'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547168/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Jembut') or (text == 'Asw') or (text == 'Jiembut') or (text == 'Asu'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200497/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Otw') or (text == 'Otww') or (text == 'Gas'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/20217665/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sue') or (text == 'Suee') or (text == 'Suek') or (text == 'Sueek'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/19002665/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == '@?????????Rizal??????? ') or (text == 'Rizal') or (text == 'Zal') or (text == 'Mbot'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/14038591/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == '@??????????ARDEWI)????? ') or (text == 'Botak') or (text == 'Ari') or (text == 'Tak'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/17354215/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == '@??????????????????? ') or (text == 'Manyun') or (text == 'Nyun'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/14038579/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == '@(???????????????????)') or (text == 'Syir') or (text == 'Sir') or (text == 'Basyir'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186955/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Pm') or (text == 'Pc') or (text == 'Cek pm') or (text == 'Buka pm'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/17241274/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kuy') or (text == 'Kuyy') or (text == 'Kuy ah') or (text == 'Kuyy ah'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200506/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bubug') or (text == 'Bobog') or (text == 'Tidur') or (text == 'Merem'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/26538903/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Apes') or (text == 'Apes aku'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200515/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Pekok') or (text == 'Gemblung') or (text == 'Koplok') or (text == 'Gendeng'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/12521475/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Sepi') or (text == 'Sepii'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200512/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Makan') or (text == 'Mangan') or (text == 'Maem'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/14038588/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    
    elif (text == 'Jones') or (text == 'Jomblo') or (text == 'Mblo'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186956/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Pagi') or (text == 'Met pagi') or (text == 'Morning'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/15666186/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bangun') or (text == 'Tangi'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547152/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Terserah') or (text == 'Serah'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691717/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Call') or (text == 'Kojom') or (text == 'Ayo kojom'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24200511/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Wekkk') or (text == 'Wekk') or (text == 'Wek'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547171/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Kangen') or (text == 'Angen') or (text == 'Kangenn'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/11866860/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Muach') or (text == 'Muachh') or (text == 'Muachhh'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89691710/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Hihi') or (text == 'Hihihi') or (text == 'Hihihihi'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/24186955/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Typo') or (text == 'Asem typo') or (text == 'Typoo'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/89547158/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
        
    elif (text == 'Bacot') or (text == 'Omong ae') or (text == 'Padon ae'):
        message = TemplateSendMessage(
            alt_text='BASYIR INI MAH',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://stickershop.line-scdn.net/stickershop/v1/sticker/23581910/IOS/sticker_animation@2x.png',
                        action=URIAction(uri='http://line.me/ti/p/%40swv6521a')
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
#-------------{ Credit by @Basyir? }-------------#

import os

if __name__ == "__main__":

    port = int(os.environ.get('PORT', 5000))

    app.run(host='0.0.0.0', port=port)
