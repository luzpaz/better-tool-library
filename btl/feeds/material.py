from .const import Operation
from . import const

# TODO: Load materials from resource files.

# Notes:
# - *_chipload_divisor attributes are defined as chipload = DIAMETER/divisor
# - The power factor originally taken from "Machinery's Handbook 29" (2012) pp1083-1084,
#   originally specified the "width of a chip that 1 HP can make".
#   I converted this to metric. In other words, the original factor was "in³ * fac = HP",
#   which equals "mm³*0.0610237 * fac * 0.745699872 = KW". So below, I multiplied all
#   factors by 0.000061024*0.745699872=0.00004550260618944 to simplify their use in
#   a metric context.
METRIC_POWER_FACTOR=0.04550260618944

class Aluminium6061(object):
    name = 'Aluminium Alloy (e.g. 6061)'
    power_factor = 0.33*METRIC_POWER_FACTOR

    hss_chipload_divisor = 160  # chipload = DIAMETER/divisor
    hss_speeds = {
        Operation.MILLING: (152, 182), # https://littlemachineshop.com/reference/cuttingspeeds.php
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (106, 122), # https://littlemachineshop.com/reference/cuttingspeeds.php
    }

    carbide_chipload_divisor = 80
    carbide_speeds = { # Source: https://www.machiningdoctor.com/mds/?matId=3850
        Operation.MILLING: (640, 865),
        Operation.SLOTTING: (425, 575),
        Operation.DRILLING: (215, 290),
        #Operation.TURNING: (510, 690),
        #Operation.PARTING: (340, 460),
    }

class Aluminium7075(object):
    name = 'Aluminium Alloy (7075)'
    power_factor = 0.33*METRIC_POWER_FACTOR

    hss_chipload_divisor = 160
    hss_speeds = {
        Operation.MILLING: (60, 300), # https://bekas.sk/files/pdfs/44.pdf
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (106, 122), # https://littlemachineshop.com/reference/cuttingspeeds.php
    }

    carbide_chipload_divisor = 80
    carbide_speeds = { # Source: https://www.machiningdoctor.com/mds/?matId=3970
        Operation.MILLING: (400, 545),
        Operation.SLOTTING: (270, 360),
        Operation.DRILLING: (135, 180),
        #Operation.TURNING: (320, 435),
        #Operation.PARTING: (215, 290),
    }

class CopperAlloy(object):
    name = 'Copper Alloy'
    power_factor = 0.80*METRIC_POWER_FACTOR

    hss_chipload_divisor = 160
    hss_speeds = {
        Operation.MILLING: (60, 300), # https://bekas.sk/files/pdfs/44.pdf
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (24, 60), # https://www.easyspeedsandfeeds.com/
        #Operation.PARTING: (120, 250), # https://www.heinrich-meier.de/upload/shoppictures_29/SchnittgeschwindigkeitNutex.pdf
    }

    carbide_chipload_divisor = 80
    carbide_speeds = { # Source: https://www.machiningdoctor.com/mds/?matId=7210
        Operation.MILLING: (280, 555),
        Operation.SLOTTING: (185, 370),
        Operation.DRILLING: (95, 185),
        #Operation.TURNING: (220, 445),
        #Operation.PARTING: (150, 295),
    }

class Iron(object):
    name = 'Iron'
    power_factor = 0.85*METRIC_POWER_FACTOR

    hss_chipload_divisor = 200
    hss_speeds = {
        Operation.MILLING: (60, 250), # https://bekas.sk/files/pdfs/44.pdf
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (15, 30), # https://www.easyspeedsandfeeds.com/
        #Operation.PARTING: (15, 45), # https://www.heinrich-meier.de/upload/shoppictures_29/SchnittgeschwindigkeitNutex.pdf
    }

    carbide_chipload_divisor = 100
    carbide_speeds = { # Source: https://www.machiningdoctor.com/mds/?matId=3230
        Operation.MILLING: (225, 305),
        Operation.SLOTTING: (230, 315),
        Operation.DRILLING: (190, 255),
        #Operation.PARTING: (165, 225),
        #Operation.TURNING: (330, 450),
    }

class ToolSteel(object):
    name = 'Tool Steel (640-670N/mm²)'
    power_factor = 1.0*METRIC_POWER_FACTOR

    hss_chipload_divisor = 250
    hss_speeds = {
        Operation.MILLING: (60, 100), # https://bekas.sk/files/pdfs/44.pdf
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (7, 15), # https://www.easyspeedsandfeeds.com/
        #Operation.PARTING: (30, 45), # https://www.heinrich-meier.de/upload/shoppictures_29/SchnittgeschwindigkeitNutex.pdf
    }

    carbide_chipload_divisor = 300
    carbide_speeds = { # Source: https://www.machiningdoctor.com/mds/?matId=1610
        Operation.MILLING: (95, 130),
        Operation.SLOTTING: (90, 120),
        Operation.DRILLING: (65, 85),
        #Operation.TURNING: (155, 210),
        #Operation.PARTING: (75, 100),
    }

class LowCarbonSteel(object):
    name = 'Low Carbon Steel (340-690N/mm²)'
    power_factor = 1.0*METRIC_POWER_FACTOR

    hss_chipload_divisor = 250
    hss_speeds = {
        Operation.MILLING: (60, 100), # https://bekas.sk/files/pdfs/44.pdf
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (6, 18), # https://www.easyspeedsandfeeds.com/
        #Operation.PARTING: (40, 60), # https://www.heinrich-meier.de/upload/shoppictures_29/SchnittgeschwindigkeitNutex.pdf
    }

    carbide_chipload_divisor = 300
    carbide_speeds = { # Source: https://www.machiningdoctor.com/mds/?matId=960
        Operation.MILLING: (125, 170),
        Operation.SLOTTING: (115, 155),
        Operation.DRILLING: (80, 110),
        #Operation.TURNING: (205, 275),
        #Operation.PARTING: (100, 135),
    }

class Stainless(object):
    name = 'Stainless Steel'
    power_factor = 0.80*METRIC_POWER_FACTOR

    hss_chipload_divisor = 200
    hss_speeds = {
        Operation.MILLING: (60, 80), # https://bekas.sk/files/pdfs/44.pdf
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (7, 15), # https://www.easyspeedsandfeeds.com/
        #Operation.PARTING: (15, 35), # https://www.heinrich-meier.de/upload/shoppictures_29/SchnittgeschwindigkeitNutex.pdf
    }

    carbide_chipload_divisor = 200
    carbide_speeds = { # Source: https://www.machiningdoctor.com/mds/?matId=1750
        Operation.MILLING: (100, 135),
        Operation.SLOTTING: (95, 130),
        Operation.DRILLING: (45, 60),
        #Operation.TURNING: (160, 215),
        #Operation.PARTING: (65, 85),
    }

class Titanium(object):
    name = 'Titanium (900-1200N/mm²)'
    power_factor = 0.80*METRIC_POWER_FACTOR

    hss_chipload_divisor = 200
    hss_speeds = {
        Operation.MILLING: (5, 7), # https://mae.ufl.edu/designlab/Advanced%20Manufacturing/Speeds%20and%20Feeds/Speeds%20and%20Feeds.htm
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (6, 15), # https://www.easyspeedsandfeeds.com/
        #Operation.PARTING: (10, 15), # https://www.heinrich-meier.de/upload/shoppictures_29/SchnittgeschwindigkeitNutex.pdf
    }

    carbide_chipload_divisor = 250
    carbide_speeds = { # Source: https://www.machiningdoctor.com/mds/?matId=6640
        Operation.MILLING: (45, 60),
        Operation.SLOTTING: (50, 70),
        Operation.DRILLING: (50, 70),
        #Operation.TURNING: (60, 80),
        #Operation.PARTING: (35, 50),
    }

class Plastic(object):
    name = 'Plastic'
    power_factor = 0.20*METRIC_POWER_FACTOR
    hss_chipload_divisor = 125

    hss_speeds = {
        Operation.MILLING: (200, 300), # https://bekas.sk/files/pdfs/44.pdf
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (100, 300), # TODO. guesses for now
        #Operation.PARTING: (100, 150), # https://www.heinrich-meier.de/upload/shoppictures_29/SchnittgeschwindigkeitNutex.pdf
    }

    carbide_chipload_divisor = 40
    carbide_speeds = {
        Operation.MILLING: (100, 1000), # TODO. guesses for now
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (100, 1000), # TODO. guesses for now
        #Operation.PARTING: (150, 300), # https://www.heinrich-meier.de/upload/shoppictures_29/SchnittgeschwindigkeitNutex.pdf
    }

class Softwood(object):
    name = 'Wood (soft)'
    power_factor = 0.20*METRIC_POWER_FACTOR

    hss_chipload_divisor = 100
    hss_speeds = {
        Operation.MILLING: (100, 1300), # TODO. guesses for now
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (100, 1000), # TODO. guesses for now
    }

    carbide_chipload_divisor = 80
    carbide_speeds = {
        Operation.MILLING: (100, 1300), # TODO. guesses for now
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (100, 1300), # TODO. guesses for now
    }

class Hardwood(object):
    name = 'Hardwood'
    power_factor = 0.30*METRIC_POWER_FACTOR # Guess based on softwood

    hss_chipload_divisor = 100 # Guess based on softwood
    hss_speeds = {
        Operation.MILLING: (100, 1300), # TODO. guesses for now
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (100, 1300), # TODO. guesses for now
    }

    carbide_chipload_divisor = 80 # Guess based on softwood
    carbide_speeds = {
        Operation.MILLING: (100, 1300), # TODO. guesses for now
        Operation.SLOTTING: (None, None), # will be auto-estimated from milling
        Operation.DRILLING: (100, 1300), # TODO. guesses for now
    }
