# -*- coding: utf-8 -*-
"""Shared summaries + helpers for the 2026-09-11 1635 edition (POST-CLOSE)."""

S_CY = ("GitLab is urging emergency upgrades after attackers began probing a maximum-severity flaw that lets an "
        "unauthenticated user read any file off the server, hours before a federal deadline expires on three "
        "already-exploited edge-device bugs.")

S_WS = ("Stocks snapped a four-day losing streak at the bell, with the Dow up 509 points and all three major indexes "
        "closing higher as crude settled back and an in-line August CPI left a Fed hike next Wednesday near fully "
        "priced.")

S_MMA = ("Noche UFC lands in Glendale on Saturday with all 26 fighters on weight and Jean Silva a heavy favourite at "
         "&minus;450 over short-notice replacement Jose Miguel Delgado.")


def tldr(label, text):
    return '<div class="tldr"><b>%s</b> <span>%s</span></div>' % (label, text)


FRESH = '<div class="freshline" id="freshline">&nbsp;</div>'


def srcblock(items):
    return "".join('<div style="margin-bottom:7px">%s &mdash; <a href="%s">%s</a></div>' % (t, u, u)
                   for t, u in items)
