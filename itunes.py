# -*- coding: utf-8 -*-

from Foundation import *
from ScriptingBridge import *

class iTunes(object):
    """
    A helper class for interacting with iTunes on Mac OS X via Scripting 
    Bridge framework.

    To use this, launch iTunes and make sure a playlist or an album is ready.

    Usage:

    >>> player = iTunes()
    >>> player.status
    'playing'
    >>> player.current_track
    u'Maison Rilax'
    >>> player.current_album
    u'Maison Rilax'
    >>> player.current_artist
    u'Lemonator'
    >>> player.pause()
    >>> player.status
    'paused'
    >>> player.play()
    >>> player.next()
    >>> player.current_track
    u'Not Your Game'

    """

    def __init__(self):
        self.app = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")

    def _get_status(self):
        if self.app.playerState() == 1800426320:
            return "playing"
        elif self.app.playerState() == 1800426352:
            return "paused"
        else:
            return "unknown"
    status = property(_get_status)

    def _get_current_track(self):
        return self.app.currentTrack().name()
    current_track = property(_get_current_track)

    def _get_current_artist(self):
        return self.app.currentTrack().artist()
    current_artist = property(_get_current_artist)

    def _get_current_album(self):
        return self.app.currentTrack().album()
    current_album = property(_get_current_album)

    def _set_volume(self, level):
        """
        level should be an integer between 0-100.
        """
        self.app.setSoundVolume_(level)

    def _get_volume(self):
        return self.app.soundVolume()
    volume = property(_get_volume, _set_volume)

    def run(self):
        self.app.run()

    def play(self):
        """
        There is no built-in play() method,
        so we create it :)
        """
        if self.status == "paused":
            self.app.playpause()

    def playpause(self):
        self.app.playpause()

    def pause(self):
        self.app.pause()

    def next(self):
        self.app.nextTrack()

    def previous(self):
        self.app.previousTrack()
