"""
Makernote (proprietary) tag definitions for Reconyx.

http://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/Reconyx.html

These vary in length, and there's really no indicator in the file to tell what the lengths are,
so it's included here as the second value in TAGS.
This also needs a way to recognize the value type (hex, string, unit16, date)
"""

TAGS = {
    0: ('MakerNoteVersion', 'uint16', 2, ),
    2: ('FirmwareVersion', 'uint16', 6, ),
    8: ('FirmwareDate', 'uint16', 4, ),  # I can't figure out how this is actually meant to be read
    12: ('TriggerMode', 'uint16', 2, {
        0x4d: 'Motion Detection',
        0x54: 'Time Lapse'
    }),
    14: ('SequencePosition', 'uint16', 2, ),
    16: ('ImagesInSequence', 'uint16', 2, ),
    22: ('DateTimeOriginal', 'date', 12, ),
    36: ('MoonPhase', 'uint16', 2, {
        0x0: 'New',
        0x1: 'New Crescent',
        0x2: 'First Quarter',
        0x3: 'Waxing Gibbous',
        0x4: 'Full',
        0x5: 'Waning Gibbous',
        0x6: 'Last Quarter',
        0x7: 'Old Crescent'
    }),
    38: ('AmbientTemperatureF', 'uint16', 2, ),
    40: ('AmbientTemperatureC', 'uint16', 2, ),
    42: ('SerialNumber', 'string16', 28, ),
    72: ('Contrast', 'uint16', 2, ),
    74: ('Brightness', 'uint16', 2, ),
    76: ('Sharpness', 'uint16', 2, ),
    78: ('Saturation', 'uint16', 2, ),
    80: ('InfraredIlluminator', 'uint16', 2, {
        0x0: 'Off',
        0x1: 'On'
    }),
    82: ('MotionSensitivity', 'uint16', 2, ),
    84: ('BatteryVoltage', 'uint16', 2, ),
    86: ('UserLabel', 'string', 32, )
}
