"""
Makernote (proprietary) tag definitions for Reconyx.

http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/Reconyx.html

These vary in length, and there's really no indicator in the file to tell what the lengths are,
so it's included here as the second value in TAGS.
This also needs a way to recognize the value type (hex, string, unit16, date)
"""

TAGS = {
    0: ('MakerNoteVersion', 2, ),
    2: ('FirmwareVersion', 6, ),
    8: ('FirmwareDate', 4, ),
    12: ('TriggerMode', 2, {
        0x4d: 'Motion Detection',
        0x54: 'Time Lapse'
    }),
    14: ('SequencePosition', 2, ),
    16: ('ImagesInSequence', 2, ),
    22: ('DateTimeOriginal', 12, ),
    36: ('MoonPhase', 2, {
        0x0: 'New',
        0x1: 'New Crescent',
        0x2: 'First Quarter',
        0x3: 'Waxing Gibbous',
        0x4: 'Full',
        0x5: 'Waning Gibbous',
        0x6: 'Last Quarter',
        0x7: 'Old Crescent'
    }),
    38: ('AmbientTemperatureF', 2, ),
    40: ('AmbientTemperatureC', 2, ),
    42: ('SerialNumber', 30, ),
    72: ('Contrast', 2, ),
    74: ('Brightness', 2, ),
    76: ('Sharpness', 2, ),
    78: ('Saturation', 2, ),
    80: ('InfraredIlluminator', 2, {
        0x0: 'Off',
        0x1: 'On'
    }),
    82: ('MotionSensitivity', 2, ),
    84: ('BatteryVoltage', 2, ),
    86: ('UserLabel ', 32, )
}
