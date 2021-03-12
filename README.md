# gfw-fire-alerts
Code associated with filtering GFW fire alerts

# Scenario 1: Weekly checks and monitoring
- List of "top 10 places on fire" to share with supervisor
    - Countries, states, and subregions experiencing abnormal fire intensity
- Used for strategic messaging to highlight emerging issues related to wildfire severity and frequency
- Collect many streams of information to yield insights
- Display the output on a dashboard that can be looked at once or twice a week to understand global state of wildfires
- Internal dashboard displays time-series graphs, top-N list based on selectable criteria
    - Risk to society
    - Risk to intact forest landscapes
    - Fire longevity
- Have a global or continental map of severity for the week
    - Join data to GADM boundaries and serve on ArcGIS Online or CartoDB

# Scenario 2: Media requests
### Quickly generate insights about fires in arbitrary places
- When and where did these firest begin?
    - Use start of fire season as reference
- How have these fires progressed since starting?
- Who or what has been affected already?
    - Amount of area burned (kha)
    - Amount of tree cover lost (kha)
    - Amount of carbon dioxide released (tons)
    - Number of people displaced
- Who or what is at risk if fires continue?
    - Amount of tree cover within x km of fire perimeter (kha)
    - Number of people within x km of fire perimeter
- How severe is the fire?
- What is driving the severity of these fires?
- How common/uncommon is this fire season?
- What are the public and societal consequences of these fires?
- How did the fire start?

# Scenario 3: Social media posts
- Identify fire-related tags trending on Twitter
    - @Pierre_Markuse
    - #SimilipalForestFire
    - #OdishaIsBurning
    - #fire
- Identify and download imagery for intense fires
- Send tweet about fire

# Scenario 4: Identify trending fires
- Create a tool to track fire-related hashtags on twitter


# Other Information
For a shapefile:

Historical fire alerts per day
Historical cumulative fire alerts
Trend in annual number of fire alerts
Years with highest/lowest number of fire alerts

Highlight el nino years

Start and end of historical fire season
Trend in fire season duration
Shortest and longest fire season years

Historical burned area
Trend in burned area
Years with the most/least burned area

Historical fire emissions
Trend in fire emissions
Years with highest/lowest fire emissions

Historical days with extreme fire risk
Historical cumulative says with extreme fire risk
Trend in days with extreme fire risk
Years with highest/lowest number of days with extreme fire risk

