"""
Felera, Nathaniel Philip D.
9-Balingkilat
08-13-2026
"""

chinesezodiac = int(input("Enter your birth year: "))

if chinesezodiac < 1900:
    print(f"\nInvalid Year. It should not be earlier than 1900")

elif chinesezodiac%12 == 4:
    print(f"\nYour Chinese Zodiac Sign is : Rat (鼠 / Shǔ)")
elif chinesezodiac%12 == 5:
    print(f"\nYour Chinese Zodiac Sign is : Ox (牛 / Niú)")
elif chinesezodiac%12 == 6:
    print(f"\nYour Chinese Zodiac Sign is : Tiger (虎 / Hǔ)")
elif chinesezodiac%12 == 7:
    print(f"\nYour Chinese Zodiac Sign is : Rabbit (兔 / Tù)")
elif chinesezodiac%12 == 8:
    print(f"\nYour Chinese Zodiac Sign is : Dragon (龙 / Lóng)")
elif chinesezodiac%12 == 9:
    print(f"\nYour Chinese Zodiac Sign is : Snake (蛇 / Shé)")
elif chinesezodiac%12 == 10:
    print(f"\nYour Chinese Zodiac Sign is : Horse (马 / Mǎ)")
elif chinesezodiac%12 == 11:
    print(f"\nYour Chinese Zodiac Sign is : Goat (羊 / Yáng)")
elif chinesezodiac%12 == 0:
    print(f"\nYour Chinese Zodiac Sign is : Monkey (猴 / Hóu)")
elif chinesezodiac%12 == 1:
    print(f"\nYour Chinese Zodiac Sign is : Rooster (鸡 / Jī)")
elif chinesezodiac%12 == 2:
    print(f"\nYour Chinese Zodiac Sign is : Dog (狗 / Gǒu)")
elif chinesezodiac%12 == 3:
    print(f"\nYour Chinese Zodiac Sign is : Pig (猪 / Zhū)")
    
