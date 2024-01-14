# inport flet

import flet as ft

'''
def main(Page:ft.Page):
    Page.update()
ft.app(main)
'''

######################### Title Change #######################

# আমাদের সকল পরিবর্তন হবে Page.update() এর উপরে। 
# প্রথমেই আসা যাক আমরা চাচ্ছি আমাদের পেইজ এর টাইটেল দিতে। সেটা কীভাবে দিতে হয় 
# Page.title="This is Title"

# def main(Page:ft.Page):
#     Page.title="This is Title"
#     Page.update()
# ft.app(main)

# তাহলেই শেখা যাবে যে আমাদের পেইজ এর Title Change হয়ে গিয়েছে। মূলত HTML এ এটা হল Header এর টাইটেল এর মতো 


###################### Output #########################

# এবার আসা যাক আমরা কোনো Text আউটপুট দেখাবো 
def main(Page:ft.Page):
    Page.title="This is Title"

    # আচ্ছা আমরা টেক্সট লিখতে চাচ্ছি। এটা কী পেইজ এর কিছু। পেইজ এর ডকুএন্টেশন বা কিছু না
    # তাই পেইজ এর ভিতরে কিছু করার জন্য আমাদের ft ব্যবহার করা লাগবে। 
    # যেহেতু আমরা টেক্সট লিখতে চাঁচ্ছি তাই flet.Text() ভিতরে ভ্যালু হিসেবে থাকবে আমাদের টেক্সট flet.text(value="Hello Wrold")
    # এবার আমাদের কাজ হলও এই লিখা পেইজ এ উপস্থাপন করা। আমরা লিখাটাকে একটা ভ্যারিয়েবল এ নিয়ে যাই যাতে ঐ ভ্যারিয়েবল অনুজায়ই কাজ করা যায়
    text=ft.Text(value="Hello World")

    # এবার আমরা পেইজ এর কন্ট্রোল থেকে বলও যে আগে যা ছিল (আগে কিছুই তো ছিল না) তার সাথে বারাও আমাদের লিখা 
    Page.controls.append(text)

    Page.update()
ft.app(main)