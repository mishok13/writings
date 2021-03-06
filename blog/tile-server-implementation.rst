It's been almost 2 years as CloudMade has ditched mod_tile and renderd as main
rendering solution in favour of in-house solution. As the principle designer
of the said alternative, I must say that this decision led to higher
development pace. This article will try to cover the general architecture
approach, reasons of decisions made and short comparison to other rendering
alternatives.

Before The Switch
=================

As some of you might know, CloudMade has its roots in OpenStreetMap and it was
quite natural to adopt OSM's software stack to have something to start with.
But as CloudMade grew, the needs and requirements changed rapidly and the task
of supporting and developing mod_tile became more of a burden, the decision to
switch to more high-level language as the main was made. The language of choice
was Python, due to its generous set of already existing spatial libraries
(e.g. Shapely, GeoAlchemy, Mapnik bindings, etc), ease of deployment and its
simpler support for cross-platform development. And, well, I knew it better
than Scala, Ruby or Perl at that moment. Here goes a list of our tasks with
mod_tile and renderd that we found easier to implement with Python:

Variable priorities
   mod_tile has the notion of "dirty" and "general" requests, with dirty
   requests having lower priority and thus having the property of being
   rendered when there's little-to-none on-demand rendering required.
   While this seems enough for most applications, it does has its warts,
   as it makes the priority system overall less general. What this means
   in practice, is that every time we need to add some special priority
   (i.e. in case we need to health-check system by forcing rendering)
   we get into adding quite a lot of code, rather than changing the
   "priority" property of the request. It might seem silly, but off the
   top of my head I can remember that we have at least 6 different
   priorities now

Replicating cache
   When it comes to scaling rendering and serving of tiles, the simplest
   solution that comes to mind is adding more servers. It's as simple, as
   pushing several links in web interface or even using automated process and
   Amazon Web Services API. But when you add new server with rendering stack
   installed you lose all the cache that has been on other servers and
   furthermore all the instances don't share cache, which makes the cacheto use
   system less effective. There're several solutions to this issue, each
   of them making use networking or database libraries, programming against
   which is tedious task in C (and C++).

Being tied to Apache
   mod_tile is an Apache module, which makes it less interesting if you look at
   it from "commodity server" perspective. Having to program against a monster
   that is Apache, using its APR library is one giant leap into full-blown
   programmer depression. The autogenerated documentation make the matters even
   worse. And two last things about Apache are its comparatively slow serving of
   static files and complicated configuration scheme. One might say that Apache
   might be winning in other parts of comparison, but the things that have been
   mentioned were essential to our rendering services.

These were the main reasons to switch, as mod_tile and renderd didn't seem like
the right thing for CloudMade. Of course, there were a lot of others, more and
less subjective reasons, but having even before mentioned ones, it was enough
to seriously consider a switch.

The Switch
==========

With all the warts of the existing system and requirements for the future in
mind, we decided to move on with the new approach. There were several things
to consider in our system:

Decoupling
   This was our main goal -- thoroughly decoupled system, where every part
   does one thing and does it good. This makes scaling much easier, but also
   incurs additional penalty on the amount of code, because of the
   need to write communication utilities. This also makes the system as a
   whole seem much more stable, as every other part of the system can work as
   a replacement in case of failure. Of course, the price is having network
   overhead and supervising system parts.

Handling styles
   One of the main CloudMade web-services is the style editor, which gives
   ability to edit map styles using WYSIWYG technique. Handling thousands of
   Mapnik styles wasn't something any existing system was prepared for, so
   unique way of doing exactly this had to be devised. Of course, this meant
   that style state in every part of the system had to be consistent at any
   given moment of time, making this even harder to accomplish.

Cache expiry
   To minimize load on the system, as much cache as possible has to be
   available. But for rapidly changing OpenStreetMap data, having all tiles
   cached for month wouldn't work and at the same time rendering all images
   on the fly would be an enormously heavy goal to accomplish. Whatever cache
   update approach is taken, unless there's a hardware possibility to render
   maps on the fly, someone will be unhappy about cache expiry scheme.

Health monitoring and high availability
   In order to meet requirement of having usable web services, one of the most
   important things to consider is having as high service uptime as possible.
   Without having health monitoring which knows about state of every part of
   the system the said objective is almost unreachable. Of course, the ideal
   can not achieved, but having a setup that covers at least 80% of the nodes
   would satisfy our needs.

The system that's currently in use at CloudMade has been developed with exactly
these goals in mind, with minor additions and subtractions along the way.
To summarize, the goal was the system where every part has a maximum level
of independency from every other while succumbing to the general goal of having
fast and easily-deployed rendering stack.

To Be Continued
===============

I'll continue the talk about moving from mod_tile to our in-house system in
follow-ups, where I'll try to get into technical details, explain our
shortcomings and issues that arised while developing.

Stay tuned.
