#import flet
import flet as ft 


def main(Page:ft.Page):

    Page.update()
ft.app(main,view=ft.WEB_BROWSER)

## এটা তো এখন একটা Desktop app/ App হিসেবে রান হচ্ছে। ধরা যাক আমরা চাচ্ছি যে একটা Web App হিসেবে রান হবে
## তাহলে আমাদের পুরো ফাংশন টাকে রান করা হয়েছে জেহকাহেন সেখানে Change করতে হবে। 
# কী চেঞ্জ করতে হবে। আমরা কী চাচ্ছি। আমরা চাচ্ছি View করতে একটা Web Browwser হিসেবে
# তাহলে এটাই লিখে দেই। ft.app(main,view=ft.WEB_BROWSER)
# তাহলে আমাদের আগের Blank একটা ওয়েব পেইজ খুলবে। 