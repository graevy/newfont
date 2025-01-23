import fontforge

font = fontforge.open("JetBrainsMono-Regular.ttf")

# unicode A
default_width = font[0x0041].width

# kindof a hack: not using the following unicode codepoints:
#    0x1F50A: "icons/speaker.svg",
#    0x1F507: "icons/speaker-muted.svg",
#    0x1F50B: "icons/batfull.svg",
#    0x231A: "icons/clock.svg",
#    0x1F4F6: "icons/wifi.svg"
# while these map neatly to the unicode codepoints for these symbols,
# some are emoji codepoints, so system preferred emoji fonts will render over these
# preferring this font would similarly collide in other applications,
# so using those points would necessitate a declarative fontconfig dependency.
# best to just use the unicode private use codepoint range
glyph_mappings = {
    0xE001: "icons/speaker.svg",
    0xE002: "icons/speaker-muted.svg",
    0xE003: "icons/batfull.svg",
    0xE004: "icons/bat1.svg",
    0xE005: "icons/bat2.svg",
    0xE006: "icons/batcharge.svg",
    0xE007: "icons/clock.svg",
    0xE008: "icons/list.svg",
    0xE009: "icons/wifi.svg",
    0xE00A: "icons/ram.svg",
    0xE00B: "icons/cpu.svg",
    0xE00C: "icons/disk.svg",
    0xE00D: "icons/ethernet.svg",
    0xE00E: "icons/brightness.svg",
}

for code_point, svg_path in glyph_mappings.items():
    glyph = font.createChar(code_point)
    glyph.importOutlines(svg_path)
    glyph.width = default_width
    bearing = abs(int(glyph.width - glyph.boundingBox()[2]) //2 )
    glyph.left_side_bearing = bearing
    glyph.right_side_bearing = bearing 

font.fontname = "JetBrainsMonoRegularBar"
font.familyname = "JetBrainsMono"
font.fullname = "JetBrainsMonoRegularBar"

font.generate("JetBrainsMonoRegularBar.ttf")
font.close()

