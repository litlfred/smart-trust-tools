---
# smart-trust-tools-oi29
title: 'OI-29: $generate-vhl sends the passcode in a GET query string'
status: todo
type: bug
parent: smart-trust-tools-oiep
priority: normal
tags:
    - open-issue
    - upstream
created_at: 2026-10-20T00:00:00Z
updated_at: 2026-11-01T10:00:00Z
---

ITI-YY3's $generate-vhl is a GET with passcode as a query parameter, so the passcode lands in server and proxy logs. Host concern, not the library's; noted for the policy track.

## Reported

Reported 2026-10-24 to IHE as point 6 of a comment on IHE/ITI.VHL#48, the July 2026 update PR (https://github.com/IHE/ITI.VHL/pull/48#issuecomment-6385626316). That PR does not yet address it.

## Requirements affected

- req:stt-vhl-005

## Sources

- library/ihe-iti-vhl-iti-yy3/sections/s010-2-3-yy3-4-1-3-expected-actions

## Status 2026-11-01

No change upstream: IHE/ITI.VHL main is still 4820147 (2026-06-14), and the July update, IHE/ITI.VHL#48, is still open.

## Done when

- [ ] the upstream source is corrected, or the requirement no longer depends on it
