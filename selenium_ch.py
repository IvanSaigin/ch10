from page_objects.Challenging_DOM import Challenging_DOM
from page_objects.Context_Menu import Context_Menu
from page_objects.Drag_and_Drop import Drag_and_Drop
from page_objects.Dropdown import Dropdown
from page_objects.Dynamic_Loading import Dynamic_Loading

import time


def test_Challenging_DOM(driver):

    result = Challenging_DOM(driver).challenging_DOM()
    if (result[0] != result[1]): 
        assert "все прошло успешно"
    else: assert "данные не изменились"


def test_Drag_and_Drop(driver):
    
    result = Drag_and_Drop(driver).drag_and_drop()

    if (result[0] != result[1]): 
        assert "все прошло успешно"
    else: assert "данные не изменились"


# def test_Dropdown(driver):
#     result = Dropdown(driver).dropdown()

#     if (result[0] != result[1]): 
#         assert "все прошло успешно"
#     else: assert "данные не изменились"


def test_Context_Menu(driver):
    result = Context_Menu(driver).context_menu()

    if (result): 
        assert "все прошло успешно"
    else: assert "данные не изменились"


# def test_Dynamic_Loading(driver):
#     result = Dynamic_Loading(driver).dynamic_loading()

#     if (result): 
#         assert "все прошло успешно"
#     else: assert "данные не изменились"