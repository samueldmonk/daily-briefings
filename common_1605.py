# -*- coding: utf-8 -*-
"""Shared summaries + helpers for the 2026-09-11 1605 edition."""

S_CY = ("CISA has given federal agencies until tomorrow to patch a maximum-severity Cisco firewall-management flaw that "
        "ransomware crews and state-linked clusters are already exploiting, one of three edge-device bugs sharing a "
        "12 September deadline.")

S_WS = ("Wall Street is on course to snap a four-day losing streak, with all three major indexes up around 1.1% on reads "
        "through 2:18 PM ET after crude settled sharply lower and an in-line August CPI left a Fed hike next Wednesday "
        "all but priced.")

S_MMA = ("Noche UFC lands in Glendale on Saturday with Jean Silva a heavy &minus;430 favourite over Jose Miguel Delgado, "
         "a short-notice replacement who took the fight on twenty-four days&rsquo; notice and has never faced a ranked "
         "opponent.")


def tldr(label, text):
    return '<div class="tldr"><b>%s</b> <span>%s</span></div>' % (label, text)


FRESH = '<div class="freshline" id="freshline">&nbsp;</div>'


def srcblock(items):
    return "".join('<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u)
                   for t, u in items)
