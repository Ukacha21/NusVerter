from kivymd.app import MDApp
from tkinter import *
from tkinter import filedialog
from kivymd.uix.screen import MDScreen
from PIL import Image as PILImage
from kivymd.uix.button import MDRectangleFlatIconButton, MDIconButton
from kivy.uix.image import Image as kimage
from kivymd.uix.label import MDLabel
from kivy.resources import resource_add_path, resource_find
import os, sys

rtk = Tk()
rtk.geometry("1x1")
rtk.overrideredirect(1)


class NusVerter(MDApp):

    state = 0

    def browsePic(*args):
        try:
            global image
            image = filedialog.askopenfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("icon files", "*.ico")])
            global nextPic
            nextPic = PILImage.open(image)

            homeLabel.text="File open.\nSave it now using the save Button"

            root.add_widget(saveButton)
    

            
        except AttributeError:
            homeLabel.text="Sorry, we couldn't open it\nwould you like to try it again?"
    

    def invert_colors(self, *args):
        if self.state == 0:
            self.theme_cls.theme_style = "Dark"
            self.state = 1
        elif self.state == 1:
            self.theme_cls.theme_style = "Light"
            self.state = 0

    def savePic(*args):
        #del setOne
        #del setTwo
        try:
            #print(newPic)

            nextPic.save(filedialog.asksaveasfilename(filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("icon files", "*.ico")]))
            homeLabel.text="Saved Successfully!"
        except NameError:
            homeLabel.text="Please make sure you followed the steps above"

    def build(self):
        self.icon = "logo.png"
        self.theme_cls.theme_style = "Light"
        #['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue', 'LightBlue', 'Cyan', 'Teal', 
        #'Green', 'LightGreen', 'Lime', 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 
        # 'BlueGray']
        self.theme_cls.primary_palette = "Purple"


        global root
        root = MDScreen()

        root.add_widget(
            kimage(
                source="logo.png"
            )
        )

        hometext = "Please start by uploding your file\nusing the upload botton below"
        global homeLabel
        homeLabel = MDLabel(
            text = hometext,
            font_style="H5",
            pos_hint = {"center_x": .5, "center_y": .8},
            halign="center",
            font_size="100sp"
            )

        root.add_widget(homeLabel)

        colorButton = MDIconButton(
            icon="invert-colors",
            pos_hint = {"center_x": .9, "center_y": .9},
            on_press = self.invert_colors
        )

        root.add_widget(colorButton)

        global saveButton
        saveButton = MDRectangleFlatIconButton(
            icon = "floppy",
            text="save",
            pos_hint = {"center_x": .5, "center_y": .5},
            on_press = self.savePic

        )

        

        openButton = MDRectangleFlatIconButton(
            icon="upload",
            text="upload",
            pos_hint = {"center_x": .5, "center_y": .6},
            on_press = self.browsePic
            )

        root.add_widget(openButton)

        return root

if __name__ == '__main__':
    try:
        if hasattr(sys, '_MEIPASS'):
            resource_add_path(os.path.join(sys._MEIPASS))
        app = NusVerter()
        app.run()
    except Exception as e:
        print(e)
        input("Press enter.")