import streamlit as st 
import pandas as pd 
import pickle



data = pickle.load(open(r'notebook\Cars_Prediction.sav', 'rb'))

st.title('Car Price Prediction')

st.sidebar.header('Feature Selecting')
st.sidebar.info('Application For Predicting car price')

st.image('data/images/The-Top-5-Luxury-Cars-imagem-de-capa-1400x700.png')



CarsModelsName = ['LEXUS', 'CHEVROLET', 'HONDA','FORD','HYUNDAI', 'TOYOTA', 'MERCEDES-BENZ', 'OPEL',
       'PORSCHE',           'BMW',          'JEEP',    'VOLKSWAGEN',
          'AUDI',       'RENAULT',        'NISSAN',        'SUBARU',
        'DAEWOO',           'KIA',    'MITSUBISHI',     'SSANGYONG',
         'MAZDA',           'GMC',          'FIAT',      'INFINITI',
    'ALFA ROMEO',        'SUZUKI',         'ACURA',       'LINCOLN',
           'VAZ',           'GAZ',       'CITROEN',    'LAND ROVER',
          'MINI',         'DODGE',      'CHRYSLER',        'JAGUAR',
         'ISUZU',         'SKODA',      'DAIHATSU',         'BUICK',
         'TESLA',      'CADILLAC',       'PEUGEOT',       'BENTLEY',
         'VOLVO',          'სხვა',         'HAVAL',        'HUMMER',
         'SCION',           'UAZ',       'MERCURY',           'ZAZ',
         'ROVER',          'SEAT',        'LANCIA',      'MOSKVICH',
      'MASERATI',       'FERRARI',          'SAAB',   'LAMBORGHINI',
   'ROLLS-ROYCE',       'PONTIAC',        'SATURN',  'ASTON MARTIN',
     'GREATWALL']
ModelNumbers= [16, 12, 17, 43, 27, 45, 35, 31,  6, 41,  9,  3, 21, 30, 40, 26, 14,
       11, 42, 24, 32,  2,  8, 29, 10, 20,  0, 44, 19, 39,  7, 25,  4, 33,
       47, 15, 23,  5, 38, 18, 34, 22, 28, 36, 46,  1, 37, 13]


Cars= dict(zip(CarsModelsName,ModelNumbers))
SelectBox1 = st.selectbox('Manufacturer', CarsModelsName)
CarName = Cars[SelectBox1]

#-------------------------------------------------------------------------------------------------------------------------------

CarsCategory = [ 'Jeep',   'Hatchback',       'Sedan',    'Microbus', 'Goods wagon',
   'Universal',       'Coupe',     'Minivan',   'Cabriolet',   'Limousine',
      'Pickup']
CategoryNumber = [3, 4, 8, 9, 6, 0, 1, 5, 2, 7]


CategoryDict = dict(zip(CarsCategory, CategoryNumber))
SelectBox2 = st.selectbox('Category', CarsCategory)
CarCategory = CategoryDict[SelectBox2]

#-------------------------------------------------------------------------------------------------------------------------------

LeatherInterior = ['Yes', 'No']
LeatherInteriorNum = [0, 1]


LeatherInteriorDict = dict(zip(LeatherInterior, LeatherInteriorNum))
SelectBox3 = st.selectbox('Leather Interior', LeatherInterior)
Leather = LeatherInteriorDict[SelectBox3]

#-------------------------------------------------------------------------------------------------------------------------------

FuelType = ['Hybrid', 'Petrol', 'Diesel', 'CNG', 'Plug-in Hybrid', 'LPG', 'Hydrogen']
FuelTypeNum = [4, 2, 1, 5, 3, 0, 6 ]

FuelTypeDict = dict(zip(FuelType, FuelTypeNum))
SelectBox4 = st.selectbox('Fuel Type',FuelType)
Fuel = FuelTypeDict[SelectBox4]

#-------------------------------------------------------------------------------------------------------------------------------

GearBoxType = ['Automatic', 'Tiptronic', 'Variator', 'Manual']
GearBoxNum = [3, 0, 2, 1]

GearBoxTypeDict = dict(zip(GearBoxType, GearBoxNum))
SelectBox5 = st.selectbox('Gear Box Type', GearBoxType)
GearBox = GearBoxTypeDict[SelectBox5]

#-------------------------------------------------------------------------------------------------------------------------------

DriveWheels = ['4x4', 'Front', 'Rear']
DriveWheelsNum = [1, 0, 2]

DriveWheelsDict = dict(zip(DriveWheels, DriveWheelsNum))
SelectBox6 = st.selectbox('Drive Wheels', DriveWheels)
DriveWheelsNumber = DriveWheelsDict[SelectBox6]
#-------------------------------------------------------------------------------------------------------------------------------

Wheel = ['Left wheel', 'Right-hand drive']
WheelNum = [1, 0]

WheelDict = dict(zip(Wheel, WheelNum))
SelectBox7 = st.selectbox('Wheel', Wheel)
WheelLoc = WheelDict[SelectBox7]

#-------------------------------------------------------------------------------------------------------------------------------

Color = [       'Silver',         'Black',         'White',          'Grey',
          'Blue',         'Green',           'Red',      'Sky blue',
        'Orange',        'Yellow',         'Brown',        'Golden',
         'Beige', 'Carnelian red',        'Purple',          'Pink']

ColorNum= [ 1, 14, 12,  7,  2, 13, 11,  6, 15,  3,  5,  0,  8,  4, 10,  9]

ColorDict = dict(zip(Color, ColorNum))
SelectBox8 = st.selectbox('Color', Color)
ColorType = ColorDict[SelectBox8]

#-------------------------------------------------------------------------------------------------------------------------------

CarsModel = unique_models = [
    "09-Mar", "100", "100 NX", "1000", "1111", "114", "116", "118", "118 2,0", "118 M-sport LCI", 
    "120", "128", "128 M tech", "130", "1300", "135", "147", "1500", "1500,1600 Schtufenheck", "159", 
    "166", "190", "20", "200", "206", "206 CC", "207", "208", "21", "21 3.0", 
    "2101 01", "2103 03", "2105", "2106", "2107", "2107 07", "2109", "2111", "2121 (Niva)", "2140", 
    "216", "220", "225", "230", "230 W153", "24", "24 10", "240", "250", "270", 
    "280", "290", "3.18E+38", "3.20E+38", "3.25E+48", "300", "300 LIMITED", "3008", "3008 2.0", "307", 
    "311", "3110", "31105", "31514", "31514 UAZ", "316", "316 1995", "316 i", "318", "318 318", 
    "318 m", "318 რესტაილინგი", "318 სასწრაფოდ", "320", "320 2.0", "320 2.2", "320 320", "320 DIESEL", "320 Diesel", "320 Gran Turismo", 
    "320 I", "320 M", "320 i", "32214", "322173", "323", "323 F", "325", "325 CI", "325 XI", 
    "325 i", "328", "328 DIZEL", "328 DRIFT CAR", "328 Xdrive", "328 i", "328 sulev", "330", "335", "335 335i", 
    "335 D", "335 M paket", "335 ტურბო", "340", "370Z", "3796", "400", "400X", "401", "406", 
    "407", "416", "420", "428", "428 Sport Line", "428 i", "435", "435 CUPE", "456", "4Runner", 
    "4Runner LIMITED", "5.30E+62", "50", "500", "500 46 ml", "500 Abarth", "500 Abarth ტურბო", "500 Lounge", "500 SPORT", "500 Sport", 
    "500 s", "500 sport", "500 sport panorama", "500 turbo", "500C", "500C Lounge", "500L", "500L LONG", "500X", "500X Lounge", 
    "508", "520", "520 I", "520 Vanos", "520 d xDrive Luxury", "523", "525", "525 ///M", "525 525", "525 TDI", 
    "525 Vanos", "525 i", "528", "528 3.0", "528 i", "530", "530 525i", "530 G30", "530 GT", "530 I", 
    "530 M", "530 i", "535", "535 535", "535 Diesel", "535 I", "535 M", "535 M PAKET", "535 Twinturbo", "535 XI", 
    "535 comfort-sport", "535 i", "535 i xDrive", "540 I", "545", "550", "550 F10", "550 GT", "550 M Packet", "607", 
    "616", "626", "630", "635", "640", "640 GRAN-COUPE", "640 M", "645", "645 CI", "650", 
    "650 450 HP", "7.30E+34", "730", "730 3.0", "735", "740", "740 i", "745", "745 i", "750", 
    "750 4.8", "807", "911", "911 meqanika", "940", "960", "969 968m", "969 luaz", "A 140", "A 140 140", 
    "A 160", "A 170", "A 170 Avangard", "A 170 CDI", "A 190", "A 200", "A3", "A3 4X4", "A3 PREMIUM", "A4", 
    "A4 B5", "A4 B6", "A4 B7", "A4 S line", "A4 S4", "A4 Sline", "A4 premium", "A4 premium plius", "A5", "A5 Sportback", 
    "A6", "A6 C7", "A6 QUATTRO", "A6 UNIVERSAL", "A6 evropuli", "A6 premium plus", "A6 С6", "A7", "A7 Prestige", "A8", 
    "AMG GT S", "ATS", "Acadia", "Accent", "Accent GS", "Accent SE", "Accord", "Accord CL9 type S", "Actyon", "Aerio SX", 
    "Agila", "Airtrek", "Airtrek turbo", "Allante", "Allroad", "Allroad Allroad", "Almera", "Almera dci", "Alphard", "Altezza", 
    "Altima", "Alto Lapin", "Aqua", "Aqua G", "Aqua G klas", "Aqua HIBRID", "Aqua L paketi", "Aqua S", "Aqua g soft leather sele", "Aqua s", 
    "Aqua sport", "Aqua სასწრაფოდ", "Armada", "Astra", "Astra 1600", "Astra A.H", "Astra BERTONE", "Astra CNG", "Astra G", "Astra GE", 
    "Astra GTC 1.9 turbo dies", "Astra H", "Astra astra", "Astra g", "Astra gi", "Astra j", "Astra suzuki mr wagon", "Astra td", "Atenza", "Auris", 
    "Avalanche", "Avalon", "Avalon LIMITED", "Avalon Limited", "Avalon limited", "Avella", "Avenger", "Avensis", "Aveo", "Axela", 
    "Azera", "B 170", "B 170 B Class", "B 170 Edition One", "B 180", "B 200", "B 200 Turbo", "B 220", "B-MAX", "B9 Tribeca", 
    "BB", "BRZ", "Belta", "Berlingo", "Bluebird", "Bora", "C 180", "C 180 2.0", "C 180 komp", "C 200", 
    "C 200 2.0", "C 200 7G-TRONIC", "C 200 KOMPRESSOR", "C 200 Kompressor", "C 220", "C 220 CDI", "C 230", "C 230 2.0 kompresor", "C 230 2.5", "C 230 kompresor", 
    "C 240", "C 240 W 203", "C 240 w203", "C 250", "C 250 1,8 turbo", "C 250 1.8", "C 250 1.8 ტურბო", "C 250 A.M.G", "C 250 AMG", "C 250 AMG-PAKET-1,8", 
    "C 250 luxury", "C 270", "C 280", "C 300", "C 300 4matic", "C 300 6.3 AMG Package", "C 300 sport", "C 32 AMG", "C 320", "C 320 AMG", 
    "C 320 CDI", "C 350", "C 36 AMG", "C 400", "C 43 AMG", "C 63 AMG", "C-MAX", "C-MAX C-MAX", "C-MAX HYBRID", "C-MAX PREMIUM", 
    "C-MAX SE", "C-MAX SEL", "C1", "C1 C", "C30", "C30 2010", "C4", "C5", "C70", "C8", 
    "CC", "CC 2.0 T", "CC R line", "CC sport", "CERVO", "CHR", "CHR Limited", "CL 500", "CL 55 AMG KOMPRESSOR", "CL 550", 
    "CL 600", "CL550 AMG", "CLA 250", "CLA 250 AMG", "CLA 45 AMG", "CLK 200", "CLK 200 200", "CLK 200 208", "CLK 200 Kompressor", "CLK 200 kompresor", 
    "CLK 230", "CLK 230 .", "CLK 240", "CLK 270", "CLK 280", "CLK 320", "CLK 320 AMG", "CLK 320 avangarde", "CLK 350", "CLK 430", 
    "CLK 55 AMG", "CLS 350", "CLS 350 AMG", "CLS 350 JAPAN", "CLS 450 CLS 400", "CLS 500", "CLS 55 AMG", "CLS 550", "CLS 550 550", "CLS 63 AMG", 
    "CR-Z", "CR-Z ჰიბრიდი", "CRX", "CT 200h", "CT 200h 1.8", "CT 200h F SPORT", "CT 200h F sport", "CT 200h F-sport", "CTS", "CX-3", 
    "CX-5", "CX-5 Touring", "CX-7", "CX-9", "Caddy", "Caddy cadi", "Cadenza", "Caldina", "Caliber", "Caliber journey", 
    "Caliber sxt", "Camaro", "Camaro LS", "Camaro RS", "Cami", "Camry", "Camry HYBRID", "Camry Hybrid", "Camry LE", "Camry Le", 
    "Camry S", "Camry SE", "Camry SE HIBRYD", "Camry SPORT", "Camry SPORT PAKET", "Camry Se", "Camry XLE", "Camry XLEi", "Camry XSE", "Camry XV50", 
    "Camry se", "Camry sel", "Camry sport", "Camry sport se", "Camry sporti", "Camry ჰიბრიდი", "Captiva", "Captur QM3 Samsung", "Caravan", "Caravan tradesman", 
    "Carens", "Carisma", "Carnival", "Carnival grand", "Catera", "Cayenne", "Cayenne S", "Cayenne s", "Cayman", "Ceed", 
    "Cefiro", "Celica", "Century", "Cerato", "Cerato K3", "Challenger", "Charger RT", "Chariot", "Cherokee", "Cinquecento", 
    "Citan", "Civic", "Civic EX", "Civic Ferio", "Civic Hybrid", "Clio", "Colorado", "Colt", "Colt Lancer", "ColtPlus", 
    "ColtPlus Plus", "Combo", "Combo 1700", "Combo 2001", "Combo TDI", "Compass", "Continental", "Continental GT", "Cooper", "Cooper CLUBMAN", 
    "Cooper F-56", "Cooper S", "Cooper S Cabrio", "Cooper S Cabrio R56", "Cooper r50", "Corolla", "Corolla 04", "Corolla 140", "Corolla ECO", "Corolla IM", 
    "Corolla Im", "Corolla LE", "Corolla S", "Corolla se", "Corolla spacio", "Corolla verso", "Corsa", "Corsa Corsa", "Corvette", "Cougar", 
    "Countryman", "Countryman S", "Countryman S turbo", "Countryman s", "Countryman sport", "Courier", "Cr-v", "Cr-v Cr-v", "Cr-v LX", "Crafter", 
    "Crafter 2,5TDI", "Crafter 2.5 TDI", "Crossfire", "Crossland X", "Crossroad", "Crosstour", "Crosstrek", "Cruze", "Cruze Cruze", "Cruze L T", 
    "Cruze LS", "Cruze LT", "Cruze LT RS", "Cruze LTZ", "Cruze PREMIER", "Cruze Premier", "Cruze RS", "Cruze S", "Cruze ltz", "Cruze sonic", 
    "Cruze strocna", "DS 4", "DTS", "Daimler", "Dart", "Dart GT 2.4", "Dart Limited", "Defender 90 Cabrio", "Delica", "Delica 5", 
    "Demio", "Demio 12", "Demio Sport", "Demio evropuli", "Demio mazda2", "Discovery", "Discovery IV", "Discovery LR3", "Doblo", "Durango", 
    "Duster", "E 200", "E 200 2000", "E 200 CGI", "E 200 w210", "E 220", "E 220 211", "E 220 CDI", "E 220 ELEGANCE", "E 220 W210...CDI", 
    "E 220 cdi", "E 230", "E 230 124", "E 240", "E 240 E 240", "E 250", "E 260", "E 270", "E 270 4", "E 270 AVANGARDI", 
    "E 270 CDI", "E 280", "E 280 3.0", "E 280 CDI", "E 290", "E 300", "E 300 AVANTGARDE-LTD", "E 320", "E 320 4matic", "E 320 4×4", 
    "E 320 bluetec", "E 350", "E 350 212", "E 350 4 MATIC", "E 350 4 Matic AMG Packag", "E 350 4 matic", "E 350 AMG", "E 350 w211", "E 350 ამგ", "E 36 AMG", 
    "E 400", "E 420", "E 430", "E 50", "E 500", "E 500 AMG", "E 500 AVG", "E 55", "E 550", "E-pace", 
    "E-pace p200", "ES 300", "ES 300 hybrid", "ES 350", "EX35", "EX37", "Eclipse", "Eclipse ES", "EcoSport", "EcoSport SE", 
    "Edge", "Edix", "Edix FR-v", "Elantra", "Elantra 2014", "Elantra 2016", "Elantra GLS / LIMITED", "Elantra GS", "Elantra GT", "Elantra Gt", 
    "Elantra LIMITED", "Elantra LIMITEDI", "Elantra Limited", "Elantra SE", "Elantra Se", "Elantra gt", "Elantra i30", "Elantra limited", "Elantra se", "Elantra sport limited", 
    "Element", "Elgrand", "Elysion", "Elysion 3.0", "Enclave", "Encore", "Envoy", "Eos", "Equinox", "Equinox LT", 
    "Escalade", "Escape", "Escape 3.0", "Escape HYBRID", "Escape Hybrid", "Escape SE", "Escape Titanium", "Escape escape", "Escape მერკური მერინერი", "Escape სასწრაფოდ", 
    "Escort", "Escudo", "Estima", "Eunos 500", "Every Landy NISSAN SEREN", "Expedition", "Explorer", "Explorer Turbo japan", "Explorer XLT", "F-pace", 
    "F-type", "F-type R", "F150", "F50", "FIT", "FIT \"S\"- PAKETI.", "FIT GP-5", "FIT GP-6", "FIT HIBRID", "FIT HYBRYD", 
    "FIT Hbrid", "FIT Hybrid", "FIT LX", "FIT Modulo", "FIT NAVI PREMIUM", "FIT PREMIUM PAKETI", "FIT PREMIUMI", "FIT Premiym", "FIT RS", "FIT RS MODELI", 
    "FIT RS MUGEN", "FIT S", "FIT SPORT", "FIT Sport", "FIT ex", "FIT fit", "FJ Cruiser", "FX35", "FX45", "Fabia", 
    "Feroza", "Fiesta", "Fiesta 1.6", "Fiesta SE", "Fit Aria", "Focus", "Focus Flexfuel", "Focus Fokusi", "Focus SE", "Focus SEL", 
    "Focus ST", "Focus TITANIUM", "Focus Titanium", "Focus se", "Forester", "Forester 4x4", "Forester CrossSport", "Forester L.L.BEAN", "Forester SH", "Forester XT", 
    "Forester cross sport", "Forester stb", "Forte", "Fortuner", "Fred", "Fred HIBRIDI", "Freelander", "Frontera", "Frontera A B", "Frontier", 
    "Fuga", "Fun Cargo", "Fusion", "Fusion 1.6", "Fusion 2015", "Fusion Bybrid", "Fusion HIBRID", "Fusion HYBRID", "Fusion HYBRID SE", "Fusion Hybrid", 
    "Fusion SE", "Fusion TITANIUM", "Fusion Titanium", "Fusion hybrid", "Fusion phev", "G 230 2.2cdi", "G 300", "G 320", "G 350", "G 55 AMG", 
    "G 550", "G 63 AMG", "G 65 AMG 63AMG", "G 65 AMG G63 AMG", "G20", "G35 x", "G37", "G6", "GL 320", 
    "GL 320 bluetec", "GL 350", "GL 350 BLUETEC", "GL 350 BLUTEC", "GL 350 Bluetec", "GL 350 დიზელი", "GL 450", "GL 450 3.0", "GL 500", "GL 550", 
    "GL 63 AMG", "GLA 200", "GLA 250", "GLC 250", "GLC 300", "GLC 300 GLC coupe", "GLE 350", "GLE 400", "GLE 400 A M G", "GLE 400 Coupe, AMG Kit", 
    "GLE 43 AMG", "GLE 450", "GLE 63 AMG", "GLK 250", "GLK 300", "GLK 350", "GLS 450", "GLS 63 AMG", "GONOW", "GS 300", 
    "GS 350", "GS 450", "GTI", "GX 460", "GX 470", "GX 470 470", "GX 470 SUV 4D (4.7L V8 S", "Galant", "Galant GTS", "Galaxy", 
    "Galloper", "Genesis", "Gentra", "Getz", "Ghibli", "Giulietta", "Gloria", "Golf", "Golf 1.8", "Golf 2", 
    "Golf 3", "Golf 4", "Golf 6", "Golf GOLF 5", "Golf GTI", "Golf Gti", "Golf TDI", "Grand Cherokee", "Grand Cherokee LAREDO", "Grand Cherokee Saiubileo", 
    "Grand Cherokee special e", "Grand HIACE", "Grand Vitara", "Grandeur", "Grandis", "H1", "H1 GRAND STAREX", "H1 grandstarex", "H1 starixs", "H2", 
    "H3", "H6", "HHR", "HS 250h", "HS 250h Hybrid", "HUSTLER", "Harrier", "Hiace", "Highlander", "Highlander 2,4", 
    "Highlander 2.4 lit", "Highlander LIMITED", "Highlander XLE", "Highlander limited", "Highlander sport", "Hilux", "Hilux Surf", "Hr-v", "Hr-v EX", "Hr-v EXL", 
    "I", "I30", "INSIGNIA", "IS 200", "IS 250", "IS 250 TURBO", "IS 250 რესტაილინგი", "IS 300", "IS 350", "IS 350 C", 
    "IS-F", "ISIS", "IVECO DAYLY", "IX35", "IX35 2.0", "Ibiza", "Ignis", "Impala", "Impreza", "Impreza G4", 
    "Impreza Sport", "Impreza WRX/STI LIMITED", "Insight", "Insight EX", "Insight LX", "Inspire", "Integra", "Intrepid", "Ioniq", "Ipsum", 
    "Ipsum S", "Ist", "Ist 1.5", "JX35", "Jetta", "Jetta 1.4 TURBO", "Jetta 2", "Jetta 2.0", "Jetta GLI", "Jetta Hybrid", 
    "Jetta SE", "Jetta SEL", "Jetta SPORT", "Jetta TDI", "Jetta s", "Jetta se", "Jetta sei", "Jetta sel", "Jetta sport", "Jetta სასწაფოდ", 
    "Jetta სპორტ", "Jimny", "Jimny GLX", "Journey", "Juke", "Juke Juke", "Juke NISMO", "Juke Nismo", "Juke Nismo RS", "Juke Turbo", 
    "Juke juke", "Juke nismo", "KA", "Kalos", "Kangoo", "Kangoo Waggon", "Kicks", "Kicks SR", "Kizashi", "Kizashi sporti", 
    "Korando", "Kyron", "L 200", "LAFESTA", "LATIO", "LS 460", "LX 470", "LX 570", "Lacetti", "Laguna", 
    "Lancer", "Lancer GT", "Lancer GTS", "Land Cruiser", "Land Cruiser 100", "Land Cruiser 105", "Land Cruiser 11", "Land Cruiser 200", "Land Cruiser 80", "Land Cruiser PRADO", 
    "Land Cruiser Prado", "Land Cruiser Prado RX", "Land Rover Sport", "Lantra", "Lantra LIMITED", "Leaf", "Legacy", "Legacy B4", "Legacy B4 twin turbo", "Legacy Bl5", 
    "Legacy Outback", "Legacy b4", "Legacy bl5", "Legend FULL", "Leon", "Liana", "Liberty", "Lupo", "Lupo iaponuri", "M3", 
    "M37", "M4", "M4 Competition", "M5", "M5 Japan", "M5 Машина в максимально", "M550", "M6", "M6 Gran cupe", "MDX", 
    "MKZ", "MKZ hybrid", "ML 250", "ML 270", "ML 270 CDI", "ML 280", "ML 280 სასწრაფოდ", "ML 300", "ML 320", "ML 320 AMG", 
    "ML 320 cdi", "ML 350", "ML 350 3.7", "ML 350 370", "ML 350 4 MATIC", "ML 350 4matic", "ML 350 BLUETEC", "ML 350 ML350", "ML 350 SPECIAL EDITION", "ML 350 sport", 
    "ML 500", "ML 500 AMG", "ML 55 AMG", "ML 550", "ML 550 4.7", "ML 63 AMG", "MPV", "MPV LX", "Malibu", "Malibu Hybrid", 
    "Malibu LT", "Malibu eco", "March", "March 231212", "March Rafeet", "Mariner", "Mariner Hybrid", "Mark X", "Mark X Zio", "Matiz", 
    "Matrix XR", "Maverick", "Maxima", "Mazda 2", "Mazda 3", "Mazda 3 SPORT", "Mazda 5", "Mazda 6", "Mazda 6 Grand Touring", "Mazda 6 Grand touring", 
    "Mazda 6 TOURING", "Megane", "Megane 1.5CDI", "Megane 1.9 CDI", "Megane 1.9CDI", "Megane 19", "Megane 5", "Megane GT Line", "Meriva", "Micra", 
    "Micra <DIESEL>", "Millenia", "Minica", "Mira", "Mirage", "Moco", "Model X", "Mondeo", "Monterey", "Montero", 
    "Montero Sport", "Move", "Mulsanne", "Murano", "Musa", "Mustang", "Mustang cabrio", "Mustang ecoboost", "Mx-5", "NEW Beetle", 
    "NX 200", "NX 300", "Navara", "Navigator", "Neon", "Niro", "Niva", "Noah", "Note", "Nubira", 
    "Octavia", "Octavia SCOUT", "Octavia Scout", "Odyssey", "Omega", "Omega 1", "Omega B", "Omega b", "Omega c", "One", 
    "Optima", "Optima ECO", "Optima EX", "Optima HYBRID", "Optima Hybrid", "Optima SXL", "Optima X", "Optima ex", "Optima hybid", "Optima hybrid", 
    "Optima k5", "Orlando", "Outback", "Outback 2007", "Outback 3.0", "Outback Limited", "Outlander", "Outlander 2.0", "Outlander SE", "Outlander SPORT", 
    "Outlander Sport", "Outlander sport", "Outlander xl", "Outlander სპორტ", "PT Cruiser", "PT Cruiser pt cruiser", "Paceman", "Pacifica", "Pajero", "Pajero 2.5diezel", 
    "Pajero IO", "Pajero MONTERO", "Pajero Mini", "Pajero Mini 2008 წლიანი", "Pajero Mini 2010 წლიანი", "Pajero Sport", "Panamera", "Panamera 4", "Panamera GTS", "Panamera S", 
    "Panda", "Passat", "Passat 2.0 tfsi", "Passat B5", "Passat B7", "Passat R-line", "Passat RLAINI", "Passat SE", "Passat SEL", "Passat Se", 
    "Passat pasat", "Passat se", "Passat sel", "Passat sport", "Passat tdi sel", "Passat tsi-se", "Passo", "Passport", "Pathfinder", "Pathfinder SE", 
    "Patriot", "Patriot 70th anniversary", "Patriot Latitude", "Patrol", "Patrol Y60", "Phaeton", "Phantom", "Picanto", "Pilot", "Polo", 
    "Polo GTI 16V", "Premacy", "Presage", "Presage RIDER", "Primera", "Prius", "Prius 1.5I", "Prius 1.8", "Prius 11", "Prius 2014", 
    "Prius 3", "Prius 9", "Prius BLUG-IN", "Prius C", "Prius C 1.5I", "Prius C 2013", "Prius C 80 original", "Prius C Hybrid", "Prius C Navigation", "Prius C YARIS IA", 
    "Prius C aqua", "Prius C hybrid", "Prius C ჰიბრიდი", "Prius Plug IN", "Prius Plug in", "Prius S", "Prius TSS LIMITED", "Prius V", "Prius V ALPINA", "Prius V HIBRID", 
    "Prius V HYBRID", "Prius personna", "Prius plagin", "Prius plug-in", "Prius plugin", "Prius prius", "Prius s", "Prius ფლაგინი", "Prius ჰიბრიდი", "Protege", 
    "Punto", "Q3", "Q45", "Q5", "Q5 Prestige", "Q5 S-line", "Q50 S Red", "Q7", "Q7 sport", "QX56", 
    "QX60", "QX80", "Qashqai Advance CVT", "Qashqai SPORT", "Quattroporte", "Quest", "Quest 2016", "R 320", "R 350", "R 350 BLUETEC", 
    "R2", "RAM", "RAM 1500", "RAV 4", "RAV 4 Dizel", "RAV 4 L", "RAV 4 LIMITED", "RAV 4 Le", "RAV 4 SPORT", "RAV 4 SUPER!!!", 
    "RAV 4 XLE", "RAV 4 XLE Sport", "RAV 4 s p o r t", "RAV 4 se", "RC F", "RC F F SPORT", "RDX", "REXTON", "REXTON SUPER", "RIO", 
    "RIO lX", "RIO lx", "RS6", "RS7", "RVR", "RX 300", "RX 350", "RX 350 F sport", "RX 400", "RX 400 H", 
    "RX 400 HYBRID", "RX 400 RESTAILING", "RX 400 hybrid", "RX 450", "RX 450 F SPORT", "RX 450 H", "RX 450 HYBRID", "Ractis", "Ramcharger", "Range Rover", 
    "Range Rover Evoque", "Range Rover Evoque 2.0", "Range Rover Evoque რესტა", "Range Rover VOGUE", "Range Rover Velar", "Range Rover Vogue", "Ranger", "Ranger Wildtrak", "Rasheen", "Regal", 
    "Renegade", "Ridgeline", "Rodeo", "Rogue", "Rogue SL", "Rogue SPORT", "Rogue Sport", "Routan SEL", "Rx-8", "S 320", 
    "S 350", "S 350 CDI 320", "S 350 Longia", "S 350 W2222", "S 400", "S 420", "S 430", "S 430 4.3", "S 500", "S 500 67", 
    "S 500 long", "S 55 5.5", "S 550", "S 550 LONG", "S 550 ჰიბრიდი", "S 600", "S 63 AMG", "S-max", "S-type", "S3", 
    "S40", "S6", "S60", "S70", "S80", "SJ 413 Samurai", "SL 55 AMG", "SLK 230", "SLK 32 AMG", "SLK 350 300", 
    "SOUL", "SRX", "SX4", "Sai", "Sambar", "Samurai", "Santa FE", "Santa FE Ultimate", "Santa FE long", "Santa FE sport", 
    "Scenic", "Scirocco", "Scorpio", "Sebring", "Seicento fiat 600", "Sentra", "Sequoia", "Serena", "Serena Serea", "Sharan", 
    "Shuttle", "Sienna", "Sienta", "Sienta LE", "Sierra", "Sierra DIZEL", "Silverado", "Silvia", "Sintra", "Sirion", 
    "Skyline", "Skyline 4WD", "Skyline GT250", "Smart", "Smart Fortwo", "Sonata", "Sonata 2.0t", "Sonata 2.4L", "Sonata HYBRID", "Sonata Hibrid", 
    "Sonata Hybrid", "Sonata LIMITED", "Sonata LPG", "Sonata Limited", "Sonata S", "Sonata SE", "Sonata SE LIMITED", "Sonata SPORT", "Sonata Sport", "Sonata blue edition", 
    "Sonata hybrid", "Sonata sport", "Sonata სასწრაფოდ", "Sonic", "Sonic LT", "Sorento", "Sorento EX", "Sorento SX", "Space Runner", "Spark", 
    "Sportage", "Sportage EX", "Sportage PRESTIGE", "Sportage SX", "Sprinter", "Sprinter 308 CDI", "Sprinter 311", "Sprinter 313", "Sprinter 313CDI", "Sprinter 314", 
    "Sprinter 315CDI", "Sprinter 315CDI-XL", "Sprinter 316", "Sprinter 316 CDI", "Sprinter 411", "Sprinter 516", "Sprinter EURO4", "Sprinter MAX", "Sprinter Maxi-ს Max", "Sprinter VAN", 
    "Sprinter VIP CLASS", "Sprinter სატვირთო", "Stella", "Step Wagon", "Step Wagon Pada", "Step Wagon RG2 SPADA", "Stream", "Suburban", "Superb", "Swift", 
    "Swift Sport", "T3", "T3 0000", "T5", "TERRAIN", "TL", "TL saber", "TLX", "TSX", "TT", 
    "Tacoma", "Tacoma TRD Off Road", "Taurus", "Taurus X", "Taurus interceptor", "Teana", "Terios", "Terrano", "Tigra", "Tiguan", 
    "Tiguan SE", "Tiida", "Tiida 15 M", "Tiida 2008", "Tiida AXIS", "Tiida Latio", "Touareg", "Touran", "Tourneo Connect", "Town Car", 
    "Town and Country", "Trailblazer", "Transit", "Transit 100LD", "Transit 135", "Transit 2.4", "Transit 350T", "Transit CL", "Transit Connect", "Transit Connect Prastoi", 
    "Transit Connect ბენზინი", "Transit Custom", "Transit Fff", "Transit S", "Transit T330", "Transit Tourneo", "Transit ford", "Transit პერეგაროტკა", "Transporter", "Traverse", 
    "Trax", "Tribute", "Tribute სასწრაფოდ", "Tucson", "Tucson Limited", "Tucson SE", "Tucson Se", "Tucson TURBO", "Tundra", "Twingo", 
    "UP", "Urus", "V 230", "V50", "VOXY", "VOXY 2003", "Vaneo", "Vanette", "Vectra", "Vectra 1.6", "Vectra B", "Vectra C", 
    "Vectra H", "Vectra b", "Vectra c", "Vectra ბ", "VehiCross", "Veloster", "Veloster R-spec", "Veloster TURBO", "Veloster Turbo", "Veloster remix", 
    "Vento", "Venza", "Veracruz", "Verisa", "Verisa 2007", "Versa", "Versa SE", "Versa s", "Verso", "Vesta", 
    "Viano", "Viano Ambiente", "Virage", "Vitara", "Vitara GL+", "Vito", "Vito 110d", "Vito 111", "Vito 111 CDI", "Vito 113", 
    "Vito 115", "Vito 115 CDI", "Vito 2.2", "Vito Exstralong", "Vito Extra Long", "Vito Extralong", "Vito long115", "Vitz", "Vitz RS", 
    "Vitz funkargo", "Vitz i.ll", "Volt", "Volt Full Packet", "Volt PREMIER", "Volt Premier", "Volt premier", "Vue", "Will Chypa", "Will Vs", 
    "Wingroad", "Wish", "Wizard", "Wrangler", "Wrangler ARB", "Wrangler sport", "X 250", "X 250 ევროპული", "X-Terra", "X-Trail", 
    "X-Trail NISMO", "X-Trail NISSAN X TRAIL R", "X-Trail X-trail", "X-Trail gt", "X-type", "X1", "X1 28Xdrive", "X1 4X4", "X1 X-Drive", "X3", 
    "X3 3.5i", "X3 SDRIVE", "X4", "X5", "X5 3.0", "X5 3.0i", "X5 3.5", "X5 35d", "X5 4,4i", "X5 4.8is", 
    "X5 DIESEL", "X5 E70", "X5 Japan", "X5 M", "X5 M packet", "X5 Sport", "X5 X-Drive", "X5 XDRIVE", "X5 XDRIVE 35D", "X5 e53", 
    "X5 rest", "X5 restilling", "X5 x5", "X6", "X6 40D", "X6 GERMANY", "X6 Limited", "X6 M", "XC90", "XC90 2.5turbo", 
    "XC90 3.2 AWD", "XE", "XF", "XJ", "XK", "XL7", "XL7 limited", "XV", "XV HYBRID", "XV LIMITED", 
    "YRV", "Yaris", "Yaris IA", "Yaris RS", "Yaris SE", "Yaris iA", "Yukon", "Z4", "Z4 3,0 SI", "Zafira", 
    "Zafira B", "i20", "i3", "i40", "iA isti", "kona", "macan", "macan S", "tC", "xD"
]
CarsModelNum = [346, 333, 681, 614, 695, 167, 312, 194, 294, 428, 467, 621,  99,
       335, 226, 543, 300, 482, 273, 395, 773,  66, 767, 213, 554, 833,
       269, 575, 382, 502,  37, 414, 723, 376, 609,  94, 497,  63, 687,
       650, 809, 740, 443,  40, 327,  67, 658, 217,   2, 145, 807, 755,
       775, 343, 445, 425, 175, 781, 655, 692, 593, 119, 223, 184, 112,
       245, 670, 409, 689, 748, 152,  91, 674, 652, 303, 263, 118, 521,
       232, 579, 199, 523, 459,  98, 795, 412, 231, 153, 656, 405, 124,
       104, 569, 690, 507, 331, 805,  80, 495,  30, 328, 158, 818, 659,
       109, 249, 171, 370, 239, 235,  74, 254, 647, 568, 499, 460, 373,
       532, 535, 684,  25, 557, 718, 527, 435, 707, 322, 117, 307, 678,
        51, 279, 258, 246, 671,  83, 646,  86, 426, 442, 285, 185,  89,
       404, 466, 238, 758, 830, 105, 547, 634, 715,   3, 305, 719, 789,
       365, 216, 734, 284, 736, 741,  73, 843, 448, 275, 450,   8, 757,
       580, 610, 743, 224, 838,  16, 829, 207, 498, 565, 536, 464, 452,
       750, 686, 392, 694,  69, 479, 251,  36, 828, 760, 325, 198, 364,
       465, 243, 555, 265,  65, 188, 696, 137, 704, 127, 222, 510, 587,
       709, 139, 732, 777, 227, 393, 793, 519, 281, 259, 751, 738, 813,
       434, 179, 576, 116, 746, 203, 352, 792, 420,   7, 515, 590,  97,
       233,  77, 710, 221, 418, 427, 363, 786, 662, 832, 611, 252, 286,
       469, 563, 182, 141, 292, 744, 407,  42, 168,  12,  81, 538, 389,
       337, 451, 201, 454, 455, 441, 277, 230, 582,  53, 667,  11, 350,
       432, 165, 541, 190, 142,  28, 415, 164, 135, 679,   9,  45, 423,
       209, 437, 289, 825, 332, 581, 596, 204, 341,  82,  95, 391, 583,
       688, 522, 242, 762, 154, 329, 756, 186, 189, 106, 319, 114, 556,
       546, 821, 317, 278, 520, 163, 626, 255, 698, 635, 661, 472, 121,
       379,  85, 388,  90,  49, 742, 103, 682, 725, 584, 801,  62, 123,
       699, 642, 660, 620, 613, 834,  59, 548, 416,  50, 330, 542, 351,
       323, 378, 211, 713, 272, 195, 180, 504, 197,  61, 177, 503, 321,
       675, 657,  26,  31, 456, 367, 598, 842, 315, 120, 753, 256, 778,
       817, 298, 261, 287,  41, 816, 806,  43,  93, 463, 268, 280, 564,
       125, 685,  71, 669, 411, 271, 157, 101, 403,  33, 717, 250, 491,
        92, 552, 439, 702, 196, 496, 822, 525, 375, 447, 845, 643, 183,
       310, 782, 761, 839, 615, 228, 474, 570,  60, 700, 787, 493, 824,
       837, 374, 100, 739, 606, 291,  17, 754, 759, 368, 788, 210, 440,
       170, 206, 763, 644, 336, 237, 102, 339, 844, 560, 653, 780, 172,
       526,  23, 309, 359, 512, 433, 633, 244, 162, 318,  72,   1, 380,
       632, 808, 654, 553, 605, 151, 601, 301, 476,  52, 823,  14, 381,
       361, 147, 623, 160, 815, 494, 192,  39, 663, 220, 173, 155, 386,
       591, 270, 768, 453, 248, 218, 749, 283, 290,  75, 567, 529,  47,
       471, 360,  46, 161, 143, 424,   0, 436, 225, 234, 597, 302, 586,
       260, 637, 524, 208, 313, 136, 764, 766, 126, 156, 340, 288, 449,
       181, 810, 390, 383, 486, 505,  84, 619, 528,  24, 485, 345, 508,
       826, 362, 384, 578, 174, 148, 571, 299, 387, 149, 122, 514, 138,
       835,   4, 722, 820, 641, 666, 703, 770, 727, 214, 594, 473, 394,
       697, 558, 501, 166, 617, 344, 398, 517,   5, 819, 509, 784, 811,
       800, 604, 708, 533, 612, 677, 534, 311,  10, 640, 651, 115,  70,
       369, 638, 676, 419,  58, 397, 720, 559, 733, 355, 417, 664, 111,
       629, 562, 540, 716, 202, 745, 399, 729, 551, 348, 422, 492, 511,
       219,  21,  27,  54, 771, 714, 769, 430, 721, 737, 550, 545, 478,
       257, 410, 730, 276, 585, 347, 371, 429, 752, 264, 680,  55, 648,
        88, 262, 726,  29, 481, 306, 366, 530, 804, 774, 798, 600, 665,
       814, 308, 396, 765, 215, 314, 267, 783,  78, 108, 785,  76, 489,
       794, 334,  56, 797, 846, 595, 831, 320,  32, 144, 649, 113,  34,
       480, 159,  20, 131, 779, 169, 438, 588,  64, 624, 461, 607, 193,
       296, 728, 349, 566, 477, 132, 324, 776, 630, 282, 304,  57, 539,
       518, 444, 531,  18, 107,  96, 457, 827, 406, 796,  15, 724, 731,
       836,   6,  19, 176, 236, 602, 130, 683, 573, 711, 799, 706, 616,
       431,  87, 253, 537, 150, 561, 128, 133,  13, 693, 516, 295, 701,
       146, 544, 500, 297, 672, 668, 628, 488, 353, 483, 413, 772, 191,
        35, 205,  48, 129, 400, 266, 812, 358, 316, 599, 402, 603, 187,
       589, 673, 549, 840, 639, 645, 618, 134, 212, 200,  38, 487, 841,
       791, 631, 357, 506, 691, 484, 475, 240, 293, 421, 462, 458, 247,
       241, 274, 110, 735, 513, 470, 356, 229, 468, 385, 705, 372, 446,
       338,  22, 625, 712, 747,  44, 627,  68, 178, 592, 622, 408, 608,
       490,  79, 636, 140, 377, 574, 577, 326, 401, 790, 802, 803, 354,
       342, 572]

ModelDict = dict(zip(CarsModel, CarsModelNum))
SelectBox9 = st.selectbox('Model', CarsModel)
Model = ModelDict[SelectBox9]
#-------------------------------------------------------------------------------------------------------------------------------

EngineVolume = st.selectbox('Engine Volume', [1.3, 2.5, 2. , 1.8, 2.4, 1.6, 2.2, 1.5, 1.4, 2.3, 1.2, 1.7, 2.9,
       1.9, 3.5, 2.1, 2.7, 1. , 0.8, 3. , 3.3, 2.8, 3.2, 1.1])

#-------------------------------------------------------------------------------------------------------------------------------

Airbags = st.selectbox('Airbags', [ 2,  0,  4, 12,  8, 10,  6,  1, 16,  7,  9,  5, 11,  3, 14, 15, 13])

Cylinders = st.selectbox('Cylinders', [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 12.0, 14.0, 16.0])

#-------------------------------------------------------------------------------------------------------------------------------

Age = st.number_input('Age')

Mileage = st.number_input('Mileage')

Levy = st.number_input('Levy')

#-------------------------------------------------------------------------------------------------------------------------------

input_data = {
    'Levy': [Levy],
    'Manufacturer': [CarName],
    'Model': [Model],
    'Category': [CarCategory],
    'Leather interior': [Leather],
    'Fuel type': [Fuel],
    'Gear box type': [GearBox],
    'Drive wheels': [DriveWheelsNumber],
    'Wheel': [WheelLoc],
    'Color': [ColorType],
    'Engine volume': [EngineVolume],
    'Mileage': [Mileage],
    'Cylinders': [Cylinders],
    'Airbags': [Airbags],
    'Car Age': [Age]
}

df = pd.DataFrame(input_data)

st.markdown("---")
if st.button('Predict Car Price', type='primary'):
    try:
        PredictedValue = data.predict(df)
        
        st.success(f'Estimated Car Price is: ${PredictedValue[0]:,.2f}')
        
    except Exception as e:
        st.error(f"Prediction Erro : {e}")





    


#-------------------------------------------------------------------------------------------------------------------------------


# df = pd.DataFrame({'Manufacturer': CarName, 'Category':CarCategory, 'Leather interior': Leather, 'Fuel type': Fuel, 'Gear box type': GearBox, 'Drive wheels': DriveWheelsNumber,
#               'Wheel': WheelLoc, 'Color': ColorType, 'Mileage':Mileage, 'Car Age': Age,
#                 'Levy' : Levy, 'Engine volume': EngineVolume, 'Airbags': Airbags, 'Model': Model, 'Cylinders': Cylinders }, index=[0])

# #-------------------------------------------------------------------------------------------------------------------------------

# MyButton = st.sidebar.button('Predict')

# if MyButton:
#     PredictedValue = data.predict(df)
#     st.sidebar.write('The Price Is : ', PredictedValue)

