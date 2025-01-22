import fontforge

font = fontforge.open("JetBrainsMono-Regular.ttf")

# unicode A
default_width = font[0x0041].width

glyph_mappings = {
    0x1F50A: "icons/speaker.svg",
    0x1F507: "icons/speaker-muted.svg",
    0x1F50B: "icons/batfull.svg",
    0xE001: "icons/bat1.svg",
    0xE002: "icons/bat2.svg",
    0xE003: "icons/batcharge.svg",
    0x231A: "icons/clock.svg",
    0xE004: "icons/list.svg",
    0x1F4F6: "icons/wifi.svg",
    0xE005: "icons/ram.svg",
    0xE006: "icons/cpu.svg",
    0xE007: "icons/disk.svg",
    0xE008: "icons/ethernet.svg",
}

for code_point, svg_path in glyph_mappings.items():
    glyph = font.createChar(code_point)
    glyph.importOutlines(svg_path)
    glyph.width = default_width
    bearing = abs(int(glyph.width - glyph.boundingBox()[2]) //2 ))
    glyph.left_side_bearing = bearing
    glyph.right_side_bearing = bearing 

font.fontname = "JetBrainsMonoRegularBar"
font.familyname = "JetBrainsMono"
font.fullname = "JetBrainsMonoRegularBar"

font.generate("JetBrainsMonoRegularBar.ttf")
font.close()

