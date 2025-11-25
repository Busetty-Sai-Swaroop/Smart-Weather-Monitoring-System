# Smart Weather Monitoring System (ThingSpeak-only, simulated sensors)

## What this repo does
- Simulates temperature & humidity.
- Posts readings to ThingSpeak channel.
- Triggers ThingSpeak email alerts when temperature crosses threshold.

## Files
- simulator_thingspeak_alerts.py : main simulator & alerting script
- .github/workflows/simulate.yml : GitHub Actions to run simulator on schedule

## Setup
1. Create ThingSpeak account and channel (2 fields: temperature, humidity).
2. Copy Channel Write API Key.
3. In ThingSpeak Account → My Profile, generate Alerts API Key.
4. Add keys as GitHub Secrets: THINGSPEAK_WRITE_KEY, THINGSPEAK_ALERTS_API_KEY, optionally TEMP_THRESHOLD.
5. Push repo to GitHub and enable Actions.

## Notes
- Free tier update interval: at least 15 seconds. Do not publish faster. :contentReference[oaicite:13]{index=13}
- Alerts are limited to 2 per 30 minutes. Use cooldown logic. :contentReference[oaicite:14]{index=14}
