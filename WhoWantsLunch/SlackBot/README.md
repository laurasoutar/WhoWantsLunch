# Improvements
Channel input for lunch command (limit the users to a specific channel, not whole team)

Browser Redirect for yes ( or popup if easier )

Better for Yes => Popup in Slack
Better for No => Selection of phases



# Refactors
Why are commands required to be within a package?
Can we extract our own client to prevent repetition in accessing and connecting to rtm?
Should we be using Observer pattern to map slack events to internal events?
Event API vs RTM?
Interactive Messages?