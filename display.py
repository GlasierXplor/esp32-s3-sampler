import adafruit_displayio_ssd1306 as ssd1306
import board
import busio
import displayio
import global_vars as gv
import time

from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label
from adafruit_displayio_layout.layouts.grid_layout import GridLayout
from adafruit_displayio_layout.layouts.page_layout import PageLayout

from displayio import I2CDisplay

display_font = bitmap_font.load_font("/lib/tom-thumb.pcf")
kit_name_text = "Default Kit"

def init_display():
    displayio.release_displays()

    scl = board.GPIO42
    sda = board.GPIO41

    i2c = busio.I2C(scl, sda)
    display_bus = I2CDisplay(i2c, device_address=0x3C)

    global display
    display = ssd1306.SSD1306(display_bus, width=128, height=64)

    splash_group = displayio.Group()
    splash_abc = label.Label(font=display_font, \
                                text="abcdefghijklmnopqrstuvwxyz", \
                                x=0, y=5)
    splash_ABC = label.Label(font=display_font, \
                                text="ABCDEFGHIJKLMNOPQRSTUVWXYZ", \
                                x=0, y=12)
    splash_123 = label.Label(font=display_font, \
                                text="0123456789<>?,./:\";'[]\{\}-=_+", \
                                x=0, y=19)
    splash_text = label.Label(font=display_font, text="TD-Sampler", \
                                x=20, y=28, scale=2)
    splash_text_sub = label.Label(font=display_font, text="Loading...", \
                                x=45, y=40)

    splash_group.append(splash_abc)
    splash_group.append(splash_ABC)
    splash_group.append(splash_123)
    splash_group.append(splash_text)
    splash_group.append(splash_text_sub)

    display.root_group = splash_group

    init_main_menu_pages()
    show_main_menu(1)


def set_kit_name(kit_name_text):
    pass


def init_main_menu_pages():
    banner_grid = GridLayout(x=0, y=0, width=128, height=9, \
                            grid_size=(4,1), cell_padding=2, \
                            divider_lines=True)
    kit_name_label = label.Label(font=display_font, text=kit_name_text)
    icons_banner_label = label.Label(font=display_font, text="icons")

    banner_grid.add_content(kit_name_label, grid_position=(0,0), \
                                cell_size=(3,1))
    banner_grid.add_content(icons_banner_label, grid_position=(3,0), \
                                cell_size=(1,1))

    global banner_group
    banner_group = displayio.Group()
    banner_group.append(banner_grid)

    global main_menu_layout
    main_menu_layout = PageLayout(0,9)

    main_menu_page_1 = GridLayout(x=0, y=0, width=128, height=55, \
                                    grid_size=(4,2), cell_padding=2, \
                                    divider_lines=True)

    page1_cell1 = label.Label(font=display_font, text="Edit\nStep")
    page1_cell2 = label.Label(font=display_font, \
                                text="Seq\n " + str(gv.sequence))
    page1_cell3 = label.Label(font=display_font, \
                                text="BPM\n" + str(gv.bpm))
    page1_cell4 = label.Label(font=display_font, \
                                text="Volume\n  " + str(gv.volume))
    page1_cell5 = label.Label(font=display_font, text="Play/\nStop")
    page1_cell6 = label.Label(font=display_font, text="Change\nSounds")
    page1_cell7 = label.Label(font=display_font, \
                                text="Set\n " + str(gv._set))
    page1_cell8 = label.Label(font=display_font, \
                                text="Page\n1/2")

    main_menu_page_1.add_content(page1_cell1, grid_position=(0,0), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_1.add_content(page1_cell2, grid_position=(1,0), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_1.add_content(page1_cell3, grid_position=(2,0), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_1.add_content(page1_cell4, grid_position=(3,0), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_1.add_content(page1_cell5, grid_position=(0,1), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_1.add_content(page1_cell6, grid_position=(1,1), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_1.add_content(page1_cell7, grid_position=(2,1), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_1.add_content(page1_cell8, grid_position=(3,1), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))

    main_menu_layout.add_content(main_menu_page_1, "page1")

    main_menu_page_2 = GridLayout(x=0, y=0, width=128, height=55, \
                                    grid_size=(4,2), cell_padding=2, \
                                    divider_lines=True)

    page2_cell1 = label.Label(font=display_font, text="Save\n Kit")
    page2_cell2 = label.Label(font=display_font, \
                                text="Save\n Seq")
    page2_cell3 = label.Label(font=display_font, \
                                text="SFX")
    page2_cell4 = label.Label(font=display_font, \
                                text="Files/\nSystem")
    page2_cell5 = label.Label(font=display_font, text="Load\n Kit")
    page2_cell6 = label.Label(font=display_font, text="Load\n Seq")
    page2_cell7 = label.Label(font=display_font, \
                                text="Empty")
    page2_cell8 = label.Label(font=display_font, \
                                text="Page\n2/2")

    main_menu_page_2.add_content(page2_cell1, grid_position=(0,0), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_2.add_content(page2_cell2, grid_position=(1,0), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_2.add_content(page2_cell3, grid_position=(2,0), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_2.add_content(page2_cell4, grid_position=(3,0), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_2.add_content(page2_cell5, grid_position=(0,1), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_2.add_content(page2_cell6, grid_position=(1,1), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_2.add_content(page2_cell7, grid_position=(2,1), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))
    main_menu_page_2.add_content(page2_cell8, grid_position=(3,1), \
                                    cell_size=(1,1), \
                                    cell_anchor_point=(0.5,0.5))

    main_menu_layout.add_content(main_menu_page_2, "page2")

    global main_menu_group
    main_menu_group = displayio.Group()
    main_menu_group.append(main_menu_layout)

    main_menu_full = displayio.Group()
    main_menu_full.append(banner_group)
    main_menu_full.append(main_menu_group)
    display.root_group = main_menu_full


def show_main_menu(page):
    if isinstance(page, int):
        if page == 1:
            main_menu_layout.show_page("page1")
        elif page == 2:
            main_menu_layout.show_page("page2")
    elif isinstance(page, str):
        if page == "next":
            main_menu_layout.next_page(loop=True)
        elif page == "prev":
            main_menu_layout.previous_page(loop=True)
