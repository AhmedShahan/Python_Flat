# import the flet 
import flet as flt 


# প্রথমেই আমাদের একটা Flet এর Main function বানাতে হবে 
# def main()
# এই ফাংশনের কী কী আর্গুমেন্ট থাকবে? 
# Flet এর সকল পেইজ আসলে Page আকারেই থাকে। তাই আমরা বলে দিলাম যে
# Flet এর পেইজ গুলোতে যখন আমরা কিছু করতে চাইব তখন Page দিয়েই যেন Access করতে পারি। 
# এক কথায় একটা ভ্যারিয়েবল। 
# def main(Page: flt.Page)

# এখন আমরা Page word টা ব্যবহার করেই সকল কমান্ড পেয়ে যাবো। বার বার flt.Page লিখার দরকার নেই। 
# এখন আমরা তো বার বারই পেইজ এ কিছু করব। তখন উপডেট হতে হবে। তাই Flet এর পেইজ কে উপডেট করি 
'''
def main(Page: flt.Page):

    Page.update()
'''

# আমাদের ফেইন ফাংশন করা শেষ। এবার আমরা চাচ্ছি আমাদের যা করে সেটা রান কর। 
# রান করার জন্য আমাদের ব্যবহার করতে হবে flt.app()
# আমরা কাকে রান করব। সেটা বলে দিতে হবে Target দিয়ে। flt.app(target=main)
# অর্থাৎ আমরা main ফাংশন টাকেই রান করতে চাচ্ছি। 
''' 
def main(Page:flt.Page):
    Page.update()

flt.app(target=main)
'''

# এই টুকুই রান করলে আমরা একটা সুন্দর Blank window দেখতে পারব। 
def main(Page:flt.Page):
    Page.update()

flt.app(target=main)