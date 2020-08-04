from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.RunScriptAction import RunScriptAction #test
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction   # test

import os #delete?



class Extension(Extension):

    def __init__(self):
        super(Extension, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):

    def on_event(self, event, extension): 
        query = event.get_argument() or str()
        if len(query.strip()) == 0: #<--------- in case the extension is called but there is nothing in input
            return RenderResultListAction([ # this is from Ulauncher
                ExtensionResultItem(icon='images/icon.png', #image
                                    name='Open Firefox Profile Manager', # text that appears when there is nothing in input except the keyword
                                    on_enter=RunScriptAction('#!/usr/bin/env bash\nfirefox -ProfileManager\n', None))
                ])
            

if __name__ == '__main__':
    Extension().run()
