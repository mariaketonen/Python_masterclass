from datetime import datetime, timezone
from zoneinfo import available_timezones

try: # conditional import
    import zoneinfo
except ImportError:
    from backports import zoneinfo

utc_now = datetime.now(timezone.utc)

france_tz = zoneinfo.ZoneInfo('Europe/Paris')
france_now = utc_now.astimezone(france_tz)
print('Time now in Paris')
print(france_now)

uk_tz = zoneinfo.ZoneInfo('Europe/London')
uk_now = utc_now.astimezone(uk_tz)
print('Time now in London')
print(uk_now)

hongkong_tz = zoneinfo.ZoneInfo('Asia/Hong_Kong')
hongkong_now = utc_now.astimezone(hongkong_tz)
print('Time now in Hong Kong')
print(hongkong_now)

nairobi_tz = zoneinfo.ZoneInfo('Africa/Nairobi')
nairobi_now = utc_now.astimezone(nairobi_tz)
print('Time now in Nairobi')
print(nairobi_now)