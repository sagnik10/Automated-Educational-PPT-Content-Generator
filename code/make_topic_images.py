import os
import math
from PIL import Image, ImageDraw, ImageFont

def font(sz):
    for p in [
        r"C:\Windows\Fonts\seguiemj.ttf",
        r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arial.ttf",
    ]:
        try:
            return ImageFont.truetype(p, sz)
        except Exception:
            pass
    return ImageFont.load_default()

def mk(w=900, h=900, bg=(255,255,255,0)):
    return Image.new("RGBA", (w,h), bg)

def save(img, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, "PNG")

def sticker_base(draw, w, h, pad=40):
    r = 70
    draw.rounded_rectangle([pad, pad, w-pad, h-pad], radius=r, fill=(255,255,255,255), outline=(40,60,90,255), width=10)

def title(draw, w, text):
    f = font(58)
    tw = draw.textlength(text, font=f)
    draw.text(((w-tw)/2, 55), text, font=f, fill=(20,35,55,255))

def unit_rate_tag(out):
    img = mk()
    d = ImageDraw.Draw(img)
    w,h = img.size
    sticker_base(d,w,h)
    title(d,w,"UNIT RATE")
    f = font(52)
    d.rounded_rectangle([170, 230, 730, 360], radius=50, fill=(230,245,255,255), outline=(120,170,210,255), width=8)
    d.text((210,260), "AED", font=f, fill=(20,60,100,255))
    d.text((520,260), " / 1", font=f, fill=(20,60,100,255))
    d.polygon([(250,520),(650,520),(600,650),(300,650)], fill=(255,244,210,255), outline=(190,150,60,255))
    d.text((310,545), "per 1", font=f, fill=(90,60,10,255))
    save(img, out)

def speed_kmh(out):
    img = mk()
    d = ImageDraw.Draw(img)
    w,h = img.size
    sticker_base(d,w,h)
    title(d,w,"km per hour")
    d.ellipse([220,260,680,720], fill=(235,255,240,255), outline=(70,140,80,255), width=10)
    d.arc([260,300,640,680], 200, 340, fill=(30,80,40,255), width=12)
    d.line([450,490,620,420], fill=(210,60,60,255), width=14)
    d.ellipse([435,475,465,505], fill=(30,80,40,255))
    f = font(56)
    d.text((300,740), "km/h", font=f, fill=(30,80,40,255))
    save(img, out)

def liter_day(out):
    img = mk()
    d = ImageDraw.Draw(img)
    w,h = img.size
    sticker_base(d,w,h)
    title(d,w,"liters per day")
    d.rounded_rectangle([320,260,580,720], radius=90, fill=(225,245,255,255), outline=(80,140,190,255), width=10)
    d.rounded_rectangle([355,300,545,690], radius=70, fill=(120,190,240,255))
    d.ellipse([375,360,525,500], fill=(180,230,255,255))
    f = font(54)
    d.text((310,750), "L / day", font=f, fill=(40,90,140,255))
    save(img, out)

def fraction_pizza(out):
    img = mk()
    d = ImageDraw.Draw(img)
    w,h = img.size
    sticker_base(d,w,h)
    title(d,w,"FRACTIONS")
    cx,cy=450,500
    r=220
    d.ellipse([cx-r,cy-r,cx+r,cy+r], fill=(255,235,190,255), outline=(180,120,60,255), width=10)
    for ang in [0,45,90,135,180,225,270,315]:
        x = cx + r*math.cos(math.radians(ang))
        y = cy + r*math.sin(math.radians(ang))
        d.line([cx,cy,x,y], fill=(180,120,60,255), width=8)
    d.pieslice([cx-r,cy-r,cx+r,cy+r], start=315, end=45, fill=(255,170,120,255))
    f = font(60)
    d.text((360,740), "1/8", font=f, fill=(90,50,10,255))
    save(img, out)

def fraction_bar(out):
    img = mk()
    d = ImageDraw.Draw(img)
    w,h = img.size
    sticker_base(d,w,h)
    title(d,w,"fraction bars")
    x0,y0=170,300
    bw,bh=560,70
    for i in range(4):
        y=y0+i*(bh+35)
        d.rounded_rectangle([x0,y,x0+bw,y+bh], radius=35, fill=(245,245,255,255), outline=(120,130,170,255), width=8)
        parts = i+2
        partw = bw/parts
        for p in range(parts):
            xx = x0 + p*partw
            d.line([xx,y,xx,y+bh], fill=(120,130,170,255), width=6)
        d.rounded_rectangle([x0,y,x0+partw*(parts-1),y+bh], radius=35, fill=(180,220,255,255))
    save(img, out)

def percent_grid(out):
    img = mk()
    d = ImageDraw.Draw(img)
    w,h = img.size
    sticker_base(d,w,h)
    title(d,w,"PERCENT (out of 100)")
    gx,gy=210,250
    size=480
    cell=size//10
    d.rounded_rectangle([gx-20,gy-20,gx+size+20,gy+size+20], radius=40, fill=(255,255,255,255), outline=(120,170,210,255), width=8)
    fill_n=37
    k=0
    for r in range(10):
        for c in range(10):
            x=gx+c*cell
            y=gy+r*cell
            col=(230,245,255,255) if k<fill_n else (245,245,245,255)
            d.rectangle([x,y,x+cell-2,y+cell-2], fill=col, outline=(200,210,220,255))
            k+=1
    f=font(64)
    d.text((330,760),"37%", font=f, fill=(40,90,140,255))
    save(img, out)

def percent_proportion(out):
    img = mk()
    d = ImageDraw.Draw(img)
    w,h = img.size
    sticker_base(d,w,h)
    title(d,w,"PERCENT PROPORTION")
    f=font(56)
    d.rounded_rectangle([150,280,750,430], radius=45, fill=(255,244,210,255), outline=(190,150,60,255), width=8)
    d.text((190,320),"part / whole = p / 100", font=f, fill=(90,60,10,255))
    d.rounded_rectangle([220,520,680,690], radius=60, fill=(235,255,240,255), outline=(70,140,80,255), width=8)
    d.text((310,565),"x 100", font=f, fill=(30,80,40,255))
    save(img, out)

def percent_equation(out):
    img = mk()
    d = ImageDraw.Draw(img)
    w,h = img.size
    sticker_base(d,w,h)
    title(d,w,"PERCENT EQUATION")
    f=font(64)
    d.rounded_rectangle([120,330,780,520], radius=60, fill=(225,240,255,255), outline=(120,170,210,255), width=10)
    d.text((140,385),"part = percent × whole", font=f, fill=(20,60,100,255))
    f2=font(50)
    d.rounded_rectangle([190,590,710,720], radius=55, fill=(255,235,245,255), outline=(210,140,170,255), width=8)
    d.text((240,625),"percent as decimal = ÷100", font=f2, fill=(120,40,70,255))
    save(img, out)

def receipt_tax(out):
    img = mk()
    d = ImageDraw.Draw(img)
    w,h = img.size
    sticker_base(d,w,h)
    title(d,w,"TAX / TIP")
    d.rounded_rectangle([260,240,640,720], radius=50, fill=(245,245,245,255), outline=(80,80,80,255), width=10)
    for yy in [320,380,440,500,560]:
        d.line([300,yy,600,yy], fill=(160,160,160,255), width=6)
    d.rounded_rectangle([480,260,720,380], radius=60, fill=(255,244,210,255), outline=(190,150,60,255), width=8)
    f=font(70)
    d.text((545,285),"%", font=f, fill=(90,60,10,255))
    save(img, out)

def commission_house(out):
    img = mk()
    d = ImageDraw.Draw(img)
    w,h = img.size
    sticker_base(d,w,h)
    title(d,w,"COMMISSION")
    d.polygon([(260,480),(450,320),(640,480)], fill=(255,225,210,255), outline=(180,90,70,255))
    d.rectangle([300,480,600,700], fill=(235,255,240,255), outline=(70,140,80,255), width=10)
    d.rectangle([430,560,500,700], fill=(225,240,255,255), outline=(120,170,210,255), width=8)
    d.rounded_rectangle([140,280,300,420], radius=55, fill=(255,244,210,255), outline=(190,150,60,255), width=8)
    f=font(70)
    d.text((200,305),"%", font=f, fill=(90,60,10,255))
    save(img, out)

def shoes_compare(out):
    img = mk()
    d = ImageDraw.Draw(img)
    w,h = img.size
    sticker_base(d,w,h)
    title(d,w,"SHOES")
    d.rounded_rectangle([200,350,420,610], radius=80, fill=(225,240,255,255), outline=(120,170,210,255), width=10)
    d.rounded_rectangle([480,350,700,610], radius=80, fill=(255,235,245,255), outline=(210,140,170,255), width=10)
    f=font(48)
    d.text((235,630),"Pair A", font=f, fill=(20,60,100,255))
    d.text((515,630),"Pair B", font=f, fill=(120,40,70,255))
    sf=font(54)
    d.text((260,290),"★★★★☆", font=sf, fill=(190,150,60,255))
    d.text((540,290),"★★★☆☆", font=sf, fill=(190,150,60,255))
    save(img, out)

def main():
    base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets_topic_images")
    unit = os.path.join(base, "unit_rates")
    frac = os.path.join(base, "fractions")
    perc = os.path.join(base, "percent_proportion")
    peq  = os.path.join(base, "percent_equation")
    real = os.path.join(base, "real_life")
    unit_rate_tag(os.path.join(unit, "unit_rate_tag.png"))
    speed_kmh(os.path.join(unit, "speed_kmh.png"))
    liter_day(os.path.join(unit, "liters_day.png"))
    fraction_pizza(os.path.join(frac, "fraction_pizza.png"))
    fraction_bar(os.path.join(frac, "fraction_bars.png"))
    percent_grid(os.path.join(perc, "percent_100_grid.png"))
    percent_proportion(os.path.join(perc, "percent_proportion_formula.png"))
    percent_equation(os.path.join(peq, "percent_equation_formula.png"))
    receipt_tax(os.path.join(real, "receipt_tax.png"))
    commission_house(os.path.join(real, "commission_house.png"))
    shoes_compare(os.path.join(real, "shoes_compare.png"))
    print(base)

if __name__ == "__main__":
    main()